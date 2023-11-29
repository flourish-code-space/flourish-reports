from django.conf import settings
from edc_model_wrapper.wrappers import ModelWrapper
from edc_visit_schedule import site_visit_schedules
from edc_metadata.constants import REQUIRED
from django.apps import apps as django_apps
from dateutil.relativedelta import relativedelta


class CaregiverAppointmentModelWrapper(ModelWrapper):
    model = 'edc_appointment.appointment'
    next_url_name = settings.DASHBOARD_URL_NAMES.get('subject_dashboard_url')
    next_url_attrs = ['subject_identifier', 'appointment']

    crf_metadata_model = 'edc_metadata.crfmetadata'

    @property
    def crf_metadata_cls(self):
        return django_apps.get_model(self.crf_metadata_model)

    @property
    def missing_crf(self):
        crf_metadata = self.crf_metadata_cls.objects.filter(
            subject_identifier=self.object.subject_identifier,
            visit_code=self.object.visit_code,
            visit_code_sequence=self.object.visit_code_sequence,
            entry_status=REQUIRED
        )

        return crf_metadata.count()
