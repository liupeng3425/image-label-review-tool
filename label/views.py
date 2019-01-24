import os
import random
# Create your views here.
from glob import glob

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from label import models

IMAGE_PATH = 'static/sample'
FILE_EXTENSION = '.jpg'
STATISTICS_PATH = os.path.join('./', 'statics.csv')

# train = glob(os.path.join(IMAGE_PATH, 'train/*.jpeg'))
# test = glob(os.path.join(IMAGE_PATH, 'test/*.jpeg'))
# validate = glob(os.path.join(IMAGE_PATH, 'validate/*.jpeg'))

# data_set = glob(os.path.join(IMAGE_PATH,'*'+FILE_EXTENSION))
data_set = ['sample/gh_26b9a2949f46_258.jpg', 'sample/qrcode_for_gh_51a28b3d099b_258.jpg']
total = len(data_set)
pending = []
done = []

wright = []
wrong = []
unknown = []


def getLabel(path):
    # you may need to custom how to get the label
    return 'wechat app code'


def index(request):
    if len(data_set) == 0:
        return statistics(request)
    target = random.randint(0, len(data_set) - 1)
    pending.append(data_set[target])
    target = data_set[target]
    target = {'path': target, 'filename': os.path.basename(target), 'label': getLabel(target)}
    context = {
        'img': target,
        'progress': '{}/{}'.format(len(done), total),
    }
    return render(request, 'label.html', context)


def commit(request, filename):
    print(filename)
    if 'wrong' in request.POST:
        wrong.append(filename)
        done.append({'filename': filename, 'wrong': 1})
    elif 'right' in request.POST:
        wright.append(filename)
        done.append({'filename': filename, 'wrong': 0})
    elif 'unknown' in request.POST:
        unknown.append(filename)
        done.append({'filename': filename, 'wrong': -1})
    find = ''
    for item in pending:
        if filename in item:
            find = item
            break
    print('find:{}'.format(find))
    pending.remove(find)
    print(pending)
    data_set.remove(find)

    return HttpResponseRedirect(reverse('label:label'))


def statistics(request):
    csv = open(STATISTICS_PATH, 'w')
    csv.write('filename,wrong\n')
    for item in done:
        csv.writelines('{},{}\n'.format(item['filename'], item['wrong']))
    csv.close()
    return HttpResponse('total:{}<br/>'
                        'train:{}<br/>'
                        'pending:{}<br/>'
                        'done:{}<br/>'
                        'wrong:{}<br/>'
                        'right:{}<br/>'
                        'unknown:{}<br/>'.format(total, len(data_set), len(pending), len(done), len(wrong),
                                                 len(wright),
                                                 len(unknown)))
