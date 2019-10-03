from django.contrib import admin
from .models import Tag, Evenement, ImageEvenement, APropos, AProposSection, ImageAPropos

class AProposSectionInline(admin.StackedInline):
    model = AProposSection
    extra = 1

class ImageAProposInline(admin.TabularInline):
    model = ImageAPropos
    extra = 1

class AProposAdmin(admin.ModelAdmin):
    inlines = [
                AProposSectionInline,
                ImageAProposInline,
              ]

class ImageEvenementInline(admin.TabularInline):
    model = ImageEvenement
    extra = 1

class EvenementAdmin(admin.ModelAdmin):
    inlines = [
                ImageEvenementInline,
              ]

admin.site.register(Tag)
admin.site.register(Evenement, EvenementAdmin)
admin.site.register(APropos, AProposAdmin)
