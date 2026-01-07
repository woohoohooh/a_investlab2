from django.contrib import admin
from .models import (
    Project002,
    Category,
    Market,
    InvestmentType,
    Tag,
    AIAnalyzeYear,
    ProjectComment,
    Expert,
)


# ================== INLINE ==================

class ProjectCommentInline(admin.TabularInline):
    model = ProjectComment
    extra = 0
    fields = ('author_name', 'comment', 'recommend', 'is_active', 'created_at')
    readonly_fields = ('created_at',)
    show_change_link = True


# ================== PROJECT ==================

@admin.register(Project002)
class ProjectAdmin(admin.ModelAdmin):
    list_display = (
        'project_name',
        'language',
        'published',
        'published_at',
        'expert_author',
        'top',
        'pro',
        'our_project',
    )

    list_filter = (
        'language',
        'published',
        'top',
        'pro',
        'our_project',
        'risk',
        'categories',
        'markets',
        'investment_types',
        'tags',
    )

    search_fields = (
        'project_name',
        'project_subname',
        'slug',
        'ticker',
        'keywords',
    )

    prepopulated_fields = {'slug': ('project_name',)}
    filter_horizontal = (
        'categories',
        'markets',
        'investment_types',
        'tags',
        'ai_analyze_yearly',
        'related_posts',
    )

    date_hierarchy = 'published_at'
    ordering = ('-published_at', '-created_at')

    readonly_fields = ('created_at', 'updated_at')

    inlines = (ProjectCommentInline,)

    fieldsets = (
        ('Основное', {
            'fields': (
                'language',
                'project_name',
                'project_subname',
                'slug',
                'published',
                'published_at',
            )
        }),
        ('Классификация', {
            'fields': (
                'categories',
                'markets',
                'investment_types',
                'tags',
            )
        }),
        ('AI / Аналитика', {
            'fields': (
                'ai_analyze_yearly',
                'ai_summarize',
            )
        }),
        ('Контент', {
            'fields': (
                'description_short',
                'description_full',
                'description_team_short',
                'description_team_full',
            )
        }),
        ('Экспертное мнение', {
            'fields': (
                'expert_author',
                'expert_opinion',
                'expert_recommend',
                'our_rating',
                'our_rating_tooltip',
                'our_advice',
                'our_opinion',
            )
        }),
        ('Финансы и риски', {
            'fields': (
                'pays_or_not',
                'risk',
                'risk_tooltip',
                'min_investment',
                'max_investment',
                'results_percent',
                'average_income_percent',
                'max_income_percent',
                'max_drawdown',
            )
        }),
        ('Ссылки', {
            'classes': ('collapse',),
            'fields': (
                'link_site',
                'link_whitepaper',
                'link_github',
                'link_register',
                'link_plans',
                'link_conditions',
                'link_terms_fees',
                'link_news',
            )
        }),
        ('Соцсети', {
            'classes': ('collapse',),
            'fields': (
                'link_tg_channel',
                'link_tg_group',
                'link_youtube',
                'link_facebook',
                'link_x',
                'link_another',
            )
        }),
        ('Изображения', {
            'classes': ('collapse',),
            'fields': (
                'img_main_page',
                'img_logo',
                'img_cover',
                'img_cover_description',
                'img_cover_filename',
            )
        }),
        ('Флаги', {
            'fields': (
                'top',
                'pro',
                'our_project',
            )
        }),
        ('Связанные проекты', {
            'classes': ('collapse',),
            'fields': ('related_posts',)
        }),
        ('Системное', {
            'classes': ('collapse',),
            'fields': (
                'created_at',
                'updated_at',
            )
        }),
    )


# ================== СПРАВОЧНИКИ ==================

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_active', 'order')
    list_editable = ('is_active', 'order')
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ('name',)


@admin.register(Market)
class MarketAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_active', 'order')
    list_editable = ('is_active', 'order')
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ('name',)


@admin.register(InvestmentType)
class InvestmentTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_active', 'order')
    list_editable = ('is_active', 'order')
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ('name',)


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'popularity')
    search_fields = ('name',)


@admin.register(AIAnalyzeYear)
class AIAnalyzeYearAdmin(admin.ModelAdmin):
    list_display = ('year', 'title', 'created_at')
    search_fields = ('year', 'title')


@admin.register(ProjectComment)
class ProjectCommentAdmin(admin.ModelAdmin):
    list_display = ('author_name', 'project', 'recommend', 'is_active', 'created_at')
    list_filter = ('recommend', 'is_active')
    search_fields = ('author_name', 'comment')
    readonly_fields = ('created_at',)

@admin.register(Expert)
class ExpertAdmin(admin.ModelAdmin):
    list_display = ('name', 'position', 'company', 'is_active')
    search_fields = ('name', 'company')
    prepopulated_fields = {'slug': ('name',)}
