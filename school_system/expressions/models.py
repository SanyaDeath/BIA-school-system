import operator
from django.db import models

from users.models import Student


def parse(expr):
    operators = set('+-*/')
    op_out = []
    num_out = []
    buff = []

    for c in expr:
        if c in operators:
            num_out.append(''.join(buff))
            buff = []
            op_out.append(c)
        else:
            buff.append(c)
    num_out.append(''.join(buff))
    return num_out, op_out


def my_eval(numbers, operators):
    numbers = list(numbers)
    operators = list(operators)
    operator_order = ('*/', '+-')

    op_dict = {'*': operator.mul,
               '/': operator.floordiv,
               '+': operator.add,
               '-': operator.sub}

    for op in operator_order:
        while any(o in operators for o in op):
            idx, oo = next((i, o) for i, o in enumerate(operators) if o in op)
            operators.pop(idx)
            values = map(float, numbers[idx:idx + 2])
            value = op_dict[oo](*values)
            numbers[idx:idx + 2] = [value]
    return numbers[0]


class Expression(models.Model):
    user = models.ForeignKey(Student,
                             on_delete=models.CASCADE,
                             verbose_name='Ученик',
                             related_name='expressions')
    expr = models.CharField(max_length=255,
                            help_text='Введите выражение',
                            verbose_name='Выражение')

    result = models.FloatField(help_text='Введите ожидаемый результат',
                               verbose_name='Результат')
    actual_result = models.FloatField(blank=True,
                                      verbose_name='Истинный результат')
    is_valid = models.BooleanField(blank=True, default=False,
                                   verbose_name='Ответ правильный')

    class Meta:
        verbose_name = 'Выражение'
        verbose_name_plural = 'Выражения'

    def save(self, *args, **kwargs):
        self.actual_result = my_eval(*parse(self.expr))
        self.is_valid = self.actual_result == self.result
        return super(Expression, self).save(*args, **kwargs)
