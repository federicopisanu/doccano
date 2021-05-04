from django.urls import include, path
from rest_framework.authtoken.views import obtain_auth_token

from . import views

urlpatterns_project = [
    path(
        route='statistics',
        view=views.StatisticsAPI.as_view(),
        name='statistics'),
    path(
        route='labels',
        view=views.LabelList.as_view(),
        name='label_list'
    ),
    path(
        route='label-upload',
        view=views.LabelUploadAPI.as_view(),
        name='label_upload'
    ),
    path(
        route='labels/<int:label_id>',
        view=views.LabelDetail.as_view(),
        name='label_detail'
    ),
    path(
        route='relation_types',
        view=views.RelationTypesList.as_view(),
        name='relation_types_list'
    ),
    path(
        route='relation_type-upload',
        view=views.RelationTypesUploadAPI.as_view(),
        name='relation_type-upload'
    ),
    path(
        route='relation_types/<int:relation_type_id>',
        view=views.RelationTypesDetail.as_view(),
        name='relation_type_detail'
    ),
    path(
        route='annotation_relations',
        view=views.AnnotationRelationsList.as_view(),
        name='relation_types_list'
    ),
    path(
        route='annotation_relation-upload',
        view=views.AnnotationRelationsUploadAPI.as_view(),
        name='annotation_relation-upload'
    ),
    path(
        route='annotation_relations/<int:annotation_relation_id>',
        view=views.AnnotationRelationsDetail.as_view(),
        name='annotation_relation_detail'
    ),
    path(
        route='docs',
        view=views.DocumentList.as_view(),
        name='doc_list'
    ),
    path(
        route='docs/<int:doc_id>',
        view=views.DocumentDetail.as_view(),
        name='doc_detail'
    ),
    path(
        route='docs/<int:doc_id>/approve-labels',
        view=views.ApproveLabelsAPI.as_view(),
        name='approve_labels'
    ),
    path(
        route='docs/<int:doc_id>/annotations',
        view=views.AnnotationList.as_view(),
        name='annotation_list'
    ),
    path(
        route='docs/<int:doc_id>/annotations/<int:annotation_id>',
        view=views.AnnotationDetail.as_view(),
        name='annotation_detail'
    ),
    path(
        route='docs/<int:doc_id>/comments',
        view=views.CommentListDoc.as_view(),
        name='comment_list_doc'
    ),
    path(
        route='comments',
        view=views.CommentListProject.as_view(),
        name='comment_list_project'
    ),
    path(
        route='docs/<int:doc_id>/comments/<int:comment_id>',
        view=views.CommentDetail.as_view(),
        name='comment_detail'
    ),
    path(
        route='docs/upload',
        view=views.TextUploadAPI.as_view(),
        name='doc_uploader'
    ),
    path(
        route='docs/download',
        view=views.TextDownloadAPI.as_view(),
        name='doc_downloader'
    ),
    path(
        route='roles',
        view=views.RoleMappingList.as_view(),
        name='rolemapping_list'
    ),
    path(
        route='roles/<int:rolemapping_id>',
        view=views.RoleMappingDetail.as_view(),
        name='rolemapping_detail'
    ),
    path(
        route='auto-labeling-templates',
        view=views.AutoLabelingTemplateListAPI.as_view(),
        name='auto_labeling_templates'
    ),
    path(
        route='auto-labeling-templates/<str:option_name>',
        view=views.AutoLabelingTemplateDetailAPI.as_view(),
        name='auto_labeling_template'
    ),
    path(
        route='auto-labeling-configs',
        view=views.AutoLabelingConfigList.as_view(),
        name='auto_labeling_configs'
    ),
    path(
        route='auto-labeling-configs/<int:config_id>',
        view=views.AutoLabelingConfigDetail.as_view(),
        name='auto_labeling_config'
    ),
    path(
        route='auto-labeling-config-testing',
        view=views.AutoLabelingConfigTest.as_view(),
        name='auto_labeling_config_test'
    ),
    path(
        route='docs/<int:doc_id>/auto-labeling',
        view=views.AutoLabelingAnnotation.as_view(),
        name='auto_labeling_annotation'
    ),

    path(
        route='auto-labeling-template-testing',
        view=views.AutoLabelingTemplateTest.as_view(),
        name='auto_labeling_template_test'
    ),
    path(
        route='auto-labeling-mapping-testing',
        view=views.AutoLabelingMappingTest.as_view(),
        name='auto_labeling_mapping_test'
    )
]

urlpatterns = [
    path(
        route='health',
        view=views.Health.as_view(),
        name='health'
    ),
    path('auth/', include('dj_rest_auth.urls')),
    path(
        route='me',
        view=views.Me.as_view(),
        name='me'
    ),
    path(
        route='features',
        view=views.Features.as_view(),
        name='features'
    ),
    path(
        route='cloud-upload',
        view=views.CloudUploadAPI.as_view(),
        name='cloud_uploader'
    ),
    path(
        route='projects',
        view=views.ProjectList.as_view(),
        name='project_list'
    ),
    path(
        route='users',
        view=views.Users.as_view(),
        name='user_list'
    ),
    path(
        route='roles',
        view=views.Roles.as_view(),
        name='roles'
    ),
    path(
        route='auto-labeling-parameter-testing',
        view=views.AutoLabelingConfigParameterTest.as_view(),
        name='auto_labeling_parameter_testing'
    ),
    path(
        route='projects/<int:project_id>',
        view=views.ProjectDetail.as_view(),
        name='project_detail'
    ),
    path('projects/<int:project_id>/', include(urlpatterns_project))
]
