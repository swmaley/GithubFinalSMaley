from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from .models import Choice, Question
from .services import RainbowSixSiegeService


class IndexView(generic.ListView):
    template_name = "polls/index.html"
    context_object_name = "latest_question_list"

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by("-pub_date")[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = "polls/detail.html"


class ResultsView(generic.DetailView):
    model = Question
    template_name = "polls/results.html"


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(
            request,
            "polls/detail.html",
            {
                "question": question,
                "error_message": "You didn't select a choice.",
            },
        )
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))


class RainbowSixSiegeStatsView(generic.View):
    def get(self, request, *args, **kwargs):
        username = request.GET.get('username')

        if not username:
            return JsonResponse({'error': 'Username parameter is required'}, status=400)

        ubisoft_email = 'email'
        ubisoft_password = 'password'
        siege_service = RainbowSixSiegeService(ubisoft_email, ubisoft_password)

        try:
            player_stats = siege_service.get_player_stats(username)
            return JsonResponse({'player_stats': player_stats}, status=200)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)


