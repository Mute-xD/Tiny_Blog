from django.shortcuts import render, reverse
from django.http import HttpResponseRedirect, Http404
from .models import Topic
from .forms import TopicForm, EntryForm, Entry
from django.contrib.auth.decorators import login_required
from django.db.models import Q


def index(request):
    return render(request, 'learning_log/index.html')


@login_required
def topics(request):
    get_topics = Topic.objects.filter(Q(owner=request.user) | Q(isPublic=True)).order_by('createDate')
    context = {'topics': get_topics}
    return render(request, 'learning_log/topics.html', context)


@login_required
def topic(request, topic_id):
    get_topic = Topic.objects.get(id=topic_id)
    if get_topic.owner != request.user and not get_topic.isPublic:
        raise Http404
    entries = get_topic.entry_set.filter(Q(owner=request.user) | Q(isPublic=True)).order_by('-createDate')
    context = {'topic': get_topic, 'entries': entries}
    return render(request, 'learning_log/topic.html', context)


@login_required
def new_topic(request):
    if request.method != 'POST':
        form = TopicForm()
    else:
        form = TopicForm(request.POST)
        if form.is_valid():
            form.instance.owner = request.user
            form.save()
            return HttpResponseRedirect(reverse('learning_log:topics'))
    context = {'form': form}
    return render(request, 'learning_log/new_topic.html', context)


@login_required
def new_entry(request, topic_id):
    topic1 = Topic.objects.get(id=topic_id)
    if request.method != 'POST':
        form = EntryForm()
    else:
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry1 = form.save(commit=False)
            new_entry1.owner = request.user
            new_entry1.topic = topic1
            new_entry1.save()
            return HttpResponseRedirect(reverse('learning_log:topic', args=[topic_id]))
    context = {'topic': topic1, 'form': form}
    return render(request, 'learning_log/new_entry.html', context)


@login_required()
def edit_entry(request, entry_id):
    entry = Entry.objects.get(id=entry_id)
    topic1 = entry.topic
    if topic1.owner != request.user:
        raise Http404
    if request.method != 'POST':
        form = EntryForm(instance=entry)
    else:
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('learning_log:topic', args=[topic1.id]))
    context = {'entry': entry, 'topic': topic1, 'form': form}
    return render(request, 'learning_log/edit_entry.html', context)
