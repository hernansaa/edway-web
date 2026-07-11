from django.db import models


class DemoRequest(models.Model):
    """
    Demo request submissions from the marketing website.
    """

    name = models.CharField(max_length=200)
    email = models.EmailField()
    company = models.CharField(max_length=200, blank=True)
    phone = models.CharField(max_length=50, blank=True)
    message = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "demo request"
        verbose_name_plural = "demo requests"

    def __str__(self):
        return f"{self.name} ({self.company}) — {self.email}"