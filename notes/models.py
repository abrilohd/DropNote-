from django.db import models


class Note(models.Model):
    CATEGORY_CHOICES = [  # noqa: RUF012
        ("Python", "Python"),
        ("AI", "AI"),
        ("Security", "Security"),
        ("Web", "Web"),
        ("Cloud", "Cloud"),
        ("Ideas", "Ideas"),
    ]

    title = models.CharField(max_length=120)
    content = models.TextField()
    category = models.CharField(
        max_length=30,
        choices=CATEGORY_CHOICES,
        default="Ideas",
    )
    link = models.URLField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]  # noqa: RUF012
        indexes = [  # noqa: RUF012
            models.Index(fields=["category"], name="note_category_idx"),
            models.Index(fields=["-created_at"], name="note_created_idx"),
        ]
        verbose_name = "note"
        verbose_name_plural = "notes"

    def __str__(self):
        return self.title
