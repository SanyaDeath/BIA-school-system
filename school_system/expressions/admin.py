from django.contrib import admin

from .models import Expression


@admin.register(Expression)
class ExpressionAdmin(admin.ModelAdmin):
    model = Expression
    list_display = ('user', 'expr',
                    'result', 'actual_result',
                    'is_valid', 'positive_amount', 'negative_amount')
    readonly_fields = ('is_valid', 'actual_result',
                       'positive_amount', 'negative_amount')
