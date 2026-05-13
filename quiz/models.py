from django.db import models

class QuizData(models.Model):
    title = models.CharField(max_length=200, default="Mening Savollarim", verbose_name="To'plam nomi")
    raw_content = models.TextField(verbose_name="JS formatidagi savollarni shu yerga qo'shing")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Savollar bazasi"
        verbose_name_plural = "Savollar bazalari"