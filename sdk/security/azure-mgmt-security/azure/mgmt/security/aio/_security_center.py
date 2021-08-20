# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from typing import Any, Optional, TYPE_CHECKING

from azure.core.pipeline.transport import AsyncHttpResponse, HttpRequest
from azure.mgmt.core import AsyncARMPipelineClient
from msrest import Deserializer, Serializer

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from azure.core.credentials_async import AsyncTokenCredential

from ._configuration import SecurityCenterConfiguration
from .operations import ComplianceResultsOperations
from .operations import PricingsOperations
from .operations import AdvancedThreatProtectionOperations
from .operations import DeviceSecurityGroupsOperations
from .operations import IotSecuritySolutionOperations
from .operations import IotSecuritySolutionAnalyticsOperations
from .operations import IotSecuritySolutionsAnalyticsAggregatedAlertOperations
from .operations import IotSecuritySolutionsAnalyticsRecommendationOperations
from .operations import LocationsOperations
from .operations import Operations
from .operations import TasksOperations
from .operations import AutoProvisioningSettingsOperations
from .operations import CompliancesOperations
from .operations import InformationProtectionPoliciesOperations
from .operations import SecurityContactsOperations
from .operations import WorkspaceSettingsOperations
from .operations import RegulatoryComplianceStandardsOperations
from .operations import RegulatoryComplianceControlsOperations
from .operations import RegulatoryComplianceAssessmentsOperations
from .operations import SubAssessmentsOperations
from .operations import AutomationsOperations
from .operations import AlertsSuppressionRulesOperations
from .operations import ServerVulnerabilityAssessmentOperations
from .operations import AssessmentsMetadataOperations
from .operations import AssessmentsOperations
from .operations import AdaptiveApplicationControlsOperations
from .operations import AdaptiveNetworkHardeningsOperations
from .operations import AllowedConnectionsOperations
from .operations import TopologyOperations
from .operations import JitNetworkAccessPoliciesOperations
from .operations import DiscoveredSecuritySolutionsOperations
from .operations import SecuritySolutionsReferenceDataOperations
from .operations import ExternalSecuritySolutionsOperations
from .operations import SecureScoresOperations
from .operations import SecureScoreControlsOperations
from .operations import SecureScoreControlDefinitionsOperations
from .operations import SecuritySolutionsOperations
from .operations import ConnectorsOperations
from .operations import SqlVulnerabilityAssessmentScansOperations
from .operations import SqlVulnerabilityAssessmentScanResultsOperations
from .operations import SqlVulnerabilityAssessmentBaselineRulesOperations
from .operations import AlertsOperations
from .operations import SettingsOperations
from .operations import IngestionSettingsOperations
from .operations import SoftwareInventoriesOperations
from .. import models


class SecurityCenter(object):
    """API spec for Microsoft.Security (Azure Security Center) resource provider.

    :ivar compliance_results: ComplianceResultsOperations operations
    :vartype compliance_results: azure.mgmt.security.aio.operations.ComplianceResultsOperations
    :ivar pricings: PricingsOperations operations
    :vartype pricings: azure.mgmt.security.aio.operations.PricingsOperations
    :ivar advanced_threat_protection: AdvancedThreatProtectionOperations operations
    :vartype advanced_threat_protection: azure.mgmt.security.aio.operations.AdvancedThreatProtectionOperations
    :ivar device_security_groups: DeviceSecurityGroupsOperations operations
    :vartype device_security_groups: azure.mgmt.security.aio.operations.DeviceSecurityGroupsOperations
    :ivar iot_security_solution: IotSecuritySolutionOperations operations
    :vartype iot_security_solution: azure.mgmt.security.aio.operations.IotSecuritySolutionOperations
    :ivar iot_security_solution_analytics: IotSecuritySolutionAnalyticsOperations operations
    :vartype iot_security_solution_analytics: azure.mgmt.security.aio.operations.IotSecuritySolutionAnalyticsOperations
    :ivar iot_security_solutions_analytics_aggregated_alert: IotSecuritySolutionsAnalyticsAggregatedAlertOperations operations
    :vartype iot_security_solutions_analytics_aggregated_alert: azure.mgmt.security.aio.operations.IotSecuritySolutionsAnalyticsAggregatedAlertOperations
    :ivar iot_security_solutions_analytics_recommendation: IotSecuritySolutionsAnalyticsRecommendationOperations operations
    :vartype iot_security_solutions_analytics_recommendation: azure.mgmt.security.aio.operations.IotSecuritySolutionsAnalyticsRecommendationOperations
    :ivar locations: LocationsOperations operations
    :vartype locations: azure.mgmt.security.aio.operations.LocationsOperations
    :ivar operations: Operations operations
    :vartype operations: azure.mgmt.security.aio.operations.Operations
    :ivar tasks: TasksOperations operations
    :vartype tasks: azure.mgmt.security.aio.operations.TasksOperations
    :ivar auto_provisioning_settings: AutoProvisioningSettingsOperations operations
    :vartype auto_provisioning_settings: azure.mgmt.security.aio.operations.AutoProvisioningSettingsOperations
    :ivar compliances: CompliancesOperations operations
    :vartype compliances: azure.mgmt.security.aio.operations.CompliancesOperations
    :ivar information_protection_policies: InformationProtectionPoliciesOperations operations
    :vartype information_protection_policies: azure.mgmt.security.aio.operations.InformationProtectionPoliciesOperations
    :ivar security_contacts: SecurityContactsOperations operations
    :vartype security_contacts: azure.mgmt.security.aio.operations.SecurityContactsOperations
    :ivar workspace_settings: WorkspaceSettingsOperations operations
    :vartype workspace_settings: azure.mgmt.security.aio.operations.WorkspaceSettingsOperations
    :ivar regulatory_compliance_standards: RegulatoryComplianceStandardsOperations operations
    :vartype regulatory_compliance_standards: azure.mgmt.security.aio.operations.RegulatoryComplianceStandardsOperations
    :ivar regulatory_compliance_controls: RegulatoryComplianceControlsOperations operations
    :vartype regulatory_compliance_controls: azure.mgmt.security.aio.operations.RegulatoryComplianceControlsOperations
    :ivar regulatory_compliance_assessments: RegulatoryComplianceAssessmentsOperations operations
    :vartype regulatory_compliance_assessments: azure.mgmt.security.aio.operations.RegulatoryComplianceAssessmentsOperations
    :ivar sub_assessments: SubAssessmentsOperations operations
    :vartype sub_assessments: azure.mgmt.security.aio.operations.SubAssessmentsOperations
    :ivar automations: AutomationsOperations operations
    :vartype automations: azure.mgmt.security.aio.operations.AutomationsOperations
    :ivar alerts_suppression_rules: AlertsSuppressionRulesOperations operations
    :vartype alerts_suppression_rules: azure.mgmt.security.aio.operations.AlertsSuppressionRulesOperations
    :ivar server_vulnerability_assessment: ServerVulnerabilityAssessmentOperations operations
    :vartype server_vulnerability_assessment: azure.mgmt.security.aio.operations.ServerVulnerabilityAssessmentOperations
    :ivar assessments_metadata: AssessmentsMetadataOperations operations
    :vartype assessments_metadata: azure.mgmt.security.aio.operations.AssessmentsMetadataOperations
    :ivar assessments: AssessmentsOperations operations
    :vartype assessments: azure.mgmt.security.aio.operations.AssessmentsOperations
    :ivar adaptive_application_controls: AdaptiveApplicationControlsOperations operations
    :vartype adaptive_application_controls: azure.mgmt.security.aio.operations.AdaptiveApplicationControlsOperations
    :ivar adaptive_network_hardenings: AdaptiveNetworkHardeningsOperations operations
    :vartype adaptive_network_hardenings: azure.mgmt.security.aio.operations.AdaptiveNetworkHardeningsOperations
    :ivar allowed_connections: AllowedConnectionsOperations operations
    :vartype allowed_connections: azure.mgmt.security.aio.operations.AllowedConnectionsOperations
    :ivar topology: TopologyOperations operations
    :vartype topology: azure.mgmt.security.aio.operations.TopologyOperations
    :ivar jit_network_access_policies: JitNetworkAccessPoliciesOperations operations
    :vartype jit_network_access_policies: azure.mgmt.security.aio.operations.JitNetworkAccessPoliciesOperations
    :ivar discovered_security_solutions: DiscoveredSecuritySolutionsOperations operations
    :vartype discovered_security_solutions: azure.mgmt.security.aio.operations.DiscoveredSecuritySolutionsOperations
    :ivar security_solutions_reference_data: SecuritySolutionsReferenceDataOperations operations
    :vartype security_solutions_reference_data: azure.mgmt.security.aio.operations.SecuritySolutionsReferenceDataOperations
    :ivar external_security_solutions: ExternalSecuritySolutionsOperations operations
    :vartype external_security_solutions: azure.mgmt.security.aio.operations.ExternalSecuritySolutionsOperations
    :ivar secure_scores: SecureScoresOperations operations
    :vartype secure_scores: azure.mgmt.security.aio.operations.SecureScoresOperations
    :ivar secure_score_controls: SecureScoreControlsOperations operations
    :vartype secure_score_controls: azure.mgmt.security.aio.operations.SecureScoreControlsOperations
    :ivar secure_score_control_definitions: SecureScoreControlDefinitionsOperations operations
    :vartype secure_score_control_definitions: azure.mgmt.security.aio.operations.SecureScoreControlDefinitionsOperations
    :ivar security_solutions: SecuritySolutionsOperations operations
    :vartype security_solutions: azure.mgmt.security.aio.operations.SecuritySolutionsOperations
    :ivar connectors: ConnectorsOperations operations
    :vartype connectors: azure.mgmt.security.aio.operations.ConnectorsOperations
    :ivar sql_vulnerability_assessment_scans: SqlVulnerabilityAssessmentScansOperations operations
    :vartype sql_vulnerability_assessment_scans: azure.mgmt.security.aio.operations.SqlVulnerabilityAssessmentScansOperations
    :ivar sql_vulnerability_assessment_scan_results: SqlVulnerabilityAssessmentScanResultsOperations operations
    :vartype sql_vulnerability_assessment_scan_results: azure.mgmt.security.aio.operations.SqlVulnerabilityAssessmentScanResultsOperations
    :ivar sql_vulnerability_assessment_baseline_rules: SqlVulnerabilityAssessmentBaselineRulesOperations operations
    :vartype sql_vulnerability_assessment_baseline_rules: azure.mgmt.security.aio.operations.SqlVulnerabilityAssessmentBaselineRulesOperations
    :ivar alerts: AlertsOperations operations
    :vartype alerts: azure.mgmt.security.aio.operations.AlertsOperations
    :ivar settings: SettingsOperations operations
    :vartype settings: azure.mgmt.security.aio.operations.SettingsOperations
    :ivar ingestion_settings: IngestionSettingsOperations operations
    :vartype ingestion_settings: azure.mgmt.security.aio.operations.IngestionSettingsOperations
    :ivar software_inventories: SoftwareInventoriesOperations operations
    :vartype software_inventories: azure.mgmt.security.aio.operations.SoftwareInventoriesOperations
    :param credential: Credential needed for the client to connect to Azure.
    :type credential: ~azure.core.credentials_async.AsyncTokenCredential
    :param subscription_id: Azure subscription ID.
    :type subscription_id: str
    :param asc_location: The location where ASC stores the data of the subscription. can be retrieved from Get locations.
    :type asc_location: str
    :param str base_url: Service URL
    :keyword int polling_interval: Default waiting time between two polls for LRO operations if no Retry-After header is present.
    """

    def __init__(
        self,
        credential: "AsyncTokenCredential",
        subscription_id: str,
        asc_location: str,
        base_url: Optional[str] = None,
        **kwargs: Any
    ) -> None:
        if not base_url:
            base_url = 'https://management.azure.com'
        self._config = SecurityCenterConfiguration(credential, subscription_id, asc_location, **kwargs)
        self._client = AsyncARMPipelineClient(base_url=base_url, config=self._config, **kwargs)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._serialize.client_side_validation = False
        self._deserialize = Deserializer(client_models)

        self.compliance_results = ComplianceResultsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.pricings = PricingsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.advanced_threat_protection = AdvancedThreatProtectionOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.device_security_groups = DeviceSecurityGroupsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.iot_security_solution = IotSecuritySolutionOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.iot_security_solution_analytics = IotSecuritySolutionAnalyticsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.iot_security_solutions_analytics_aggregated_alert = IotSecuritySolutionsAnalyticsAggregatedAlertOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.iot_security_solutions_analytics_recommendation = IotSecuritySolutionsAnalyticsRecommendationOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.locations = LocationsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.operations = Operations(
            self._client, self._config, self._serialize, self._deserialize)
        self.tasks = TasksOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.auto_provisioning_settings = AutoProvisioningSettingsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.compliances = CompliancesOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.information_protection_policies = InformationProtectionPoliciesOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.security_contacts = SecurityContactsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.workspace_settings = WorkspaceSettingsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.regulatory_compliance_standards = RegulatoryComplianceStandardsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.regulatory_compliance_controls = RegulatoryComplianceControlsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.regulatory_compliance_assessments = RegulatoryComplianceAssessmentsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.sub_assessments = SubAssessmentsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.automations = AutomationsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.alerts_suppression_rules = AlertsSuppressionRulesOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.server_vulnerability_assessment = ServerVulnerabilityAssessmentOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.assessments_metadata = AssessmentsMetadataOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.assessments = AssessmentsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.adaptive_application_controls = AdaptiveApplicationControlsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.adaptive_network_hardenings = AdaptiveNetworkHardeningsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.allowed_connections = AllowedConnectionsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.topology = TopologyOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.jit_network_access_policies = JitNetworkAccessPoliciesOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.discovered_security_solutions = DiscoveredSecuritySolutionsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.security_solutions_reference_data = SecuritySolutionsReferenceDataOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.external_security_solutions = ExternalSecuritySolutionsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.secure_scores = SecureScoresOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.secure_score_controls = SecureScoreControlsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.secure_score_control_definitions = SecureScoreControlDefinitionsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.security_solutions = SecuritySolutionsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.connectors = ConnectorsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.sql_vulnerability_assessment_scans = SqlVulnerabilityAssessmentScansOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.sql_vulnerability_assessment_scan_results = SqlVulnerabilityAssessmentScanResultsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.sql_vulnerability_assessment_baseline_rules = SqlVulnerabilityAssessmentBaselineRulesOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.alerts = AlertsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.settings = SettingsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.ingestion_settings = IngestionSettingsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.software_inventories = SoftwareInventoriesOperations(
            self._client, self._config, self._serialize, self._deserialize)

    async def _send_request(self, http_request: HttpRequest, **kwargs: Any) -> AsyncHttpResponse:
        """Runs the network request through the client's chained policies.

        :param http_request: The network request you want to make. Required.
        :type http_request: ~azure.core.pipeline.transport.HttpRequest
        :keyword bool stream: Whether the response payload will be streamed. Defaults to True.
        :return: The response of your network call. Does not do error handling on your response.
        :rtype: ~azure.core.pipeline.transport.AsyncHttpResponse
        """
        path_format_arguments = {
            'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str', pattern=r'^[0-9A-Fa-f]{8}-([0-9A-Fa-f]{4}-){3}[0-9A-Fa-f]{12}$'),
            'ascLocation': self._serialize.url("self._config.asc_location", self._config.asc_location, 'str'),
        }
        http_request.url = self._client.format_url(http_request.url, **path_format_arguments)
        stream = kwargs.pop("stream", True)
        pipeline_response = await self._client._pipeline.run(http_request, stream=stream, **kwargs)
        return pipeline_response.http_response

    async def close(self) -> None:
        await self._client.close()

    async def __aenter__(self) -> "SecurityCenter":
        await self._client.__aenter__()
        return self

    async def __aexit__(self, *exc_details) -> None:
        await self._client.__aexit__(*exc_details)
