from django.db import models
from django.utils.translation import gettext_lazy as _


class Subject(models.Model):
    """Model definition for Subject."""

    name = models.CharField(max_length=200)

    class Meta:
        """Meta definition for Subject."""

        ordering = ("name",)
        verbose_name = "Subject"
        verbose_name_plural = "Subjects"

    def __str__(self):
        return self.name


class Meeting(models.Model):
    """Model definition for Meeting."""

    host_id = models.CharField(_("host_id"), max_length=255)
    host_email = models.EmailField(_("host_email"))
    topic = models.CharField(_("topic"), max_length=255)
    type = models.IntegerField(_("type"))
    occurence_status = models.CharField(_("occurence_status"), max_length=64)
    start_time = models.DateTimeField(_("start_time"))
    password = models.CharField(_("password"), max_length=255)
    created_at = models.DateTimeField(_("createdAt"))
    agenda = models.CharField(_("agenda"), max_length=255)
    duration = models.DurationField(_("duration"))
    course = models.ForeignKey(
        "courses.Course",
        verbose_name=_("course"),
        related_name="meetings",
        on_delete=models.CASCADE,
    )
    subject = models.ForeignKey(
        Subject,
        verbose_name=_("subject"),
        related_name="classes",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )

    def __str__(self):
        return f"{self.topic}_{self.id} - {self.start_time}"

    class Meta:
        verbose_name = "Meeting"
        verbose_name_plural = "Meetings"
