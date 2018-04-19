from django.contrib import admin

# Register your models here.
from .models import Project
from .models import Status
from .models import Milestone
from .models import IssueType
from .models import Priority
from .models import Issue
from .models import Commit
from .models import Comment

admin.site.register(Project)
admin.site.register(Status)
admin.site.register(Milestone)
admin.site.register(IssueType)
admin.site.register(Priority)
admin.site.register(Issue)
admin.site.register(Commit)
admin.site.register(Comment)

