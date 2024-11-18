from datacenter.models import Schoolkid, Mark, Chastisement, Lesson, Commendation, Subject
import random


def search_kid(child_name):
    try:
        child = Schoolkid.objects.get(full_name__contains=child_name)
        return child
    except Schoolkid.DoesNotExist:
        print('Не найдено ни одного ученика с таким именем')
    except Schoolkid.MultipleObjectsReturned:
        print('Найдено несколько учеников, укажите более точные данные')


def fix_marks(child):
    marks = Mark.objects.filter(schoolkid=child)
    marks.filter(points__in=[2, 3]).update(points=5)


def remove_chastisements(child):
    bad_remarks = Chastisement.objects.filter(schoolkid=child)
    bad_remarks.delete()


def create_commendation(child, subject):
    good_phrases = ['Молодец!', 'Отлично!', 'Хорошо!',
                    'Хорошая работа на уроке', 'Отлично отвечал', 'Хвалю!',
                    'Лучше всех', 'Замечательно!']
    good_phrase = random.choice(good_phrases)
    year_of_study = child.year_of_study
    group_letter = child.group_letter
    if Subject.objects.filter(title=subject).exists():
        lessons = Lesson.objects.filter(year_of_study=year_of_study,
                                        group_letter=group_letter,
                                        subject__title=subject)
        lesson = lessons.order_by('date').last()
        Commendation.objects.create(text=good_phrase, created=lesson.date,
                                    schoolkid=child, teacher=lesson.teacher,
                                    subject=lesson.subject)
    else:
        print('Перепроверьте название предмета')
