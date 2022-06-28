from django import template
 
register = template.Library()

@register.filter(name='censor')
def censor(value):

    censor_list = ['Говно', 'залупа', 'пенис', 'хер', 'давалка', 'хуй', 'блядина','Головка', 'шлюха', 'жопа', 'член', 'еблан', 'петух','Мудила','Рукоблуд', 'ссанина', 'очко', 'блядун', 'вагина','Сука', 'ебланище', 'влагалище', 'пердун', 'дрочила','Пидор', 'пизда', 'туз', 'малафья','Гомик', 'мудила', 'пилотка', 'манда','Анус', 'вагина', 'путана', 'пидрила','Шалава', 'хуила', 'мошонка', 'елда']

    for word in censor_list:
        value = value.replace(word, '***')
    return value