# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.service_client import SDKClient
from msrest import Serializer, Deserializer

from ._configuration import DataBoxEdgeManagementClientConfiguration
from .operations import Operations
from .operations import DevicesOperations
from .operations import AlertsOperations
from .operations import BandwidthSchedulesOperations
from .operations import JobsOperations
from .operations import NodesOperations
from .operations import OperationsStatusOperations
from .operations import OrdersOperations
from .operations import RolesOperations
from .operations import SharesOperations
from .operations import StorageAccountCredentialsOperations
from .operations import StorageAccountsOperations
from .operations import ContainersOperations
from .operations import TriggersOperations
from .operations import UsersOperations
from .operations import SkusOperations
from . import models


class DataBoxEdgeManagementClient(SDKClient):
    """DataBoxEdgeManagementClient

    :ivar config: Configuration for client.
    :vartype config: DataBoxEdgeManagementClientConfiguration

    :ivar operations: Operations operations
    :vartype operations: azure.mgmt.databoxedge.operations.Operations
    :ivar devices: Devices operations
    :vartype devices: azure.mgmt.databoxedge.operations.DevicesOperations
    :ivar alerts: Alerts operations
    :vartype alerts: azure.mgmt.databoxedge.operations.AlertsOperations
    :ivar bandwidth_schedules: BandwidthSchedules operations
    :vartype bandwidth_schedules: azure.mgmt.databoxedge.operations.BandwidthSchedulesOperations
    :ivar jobs: Jobs operations
    :vartype jobs: azure.mgmt.databoxedge.operations.JobsOperations
    :ivar nodes: Nodes operations
    :vartype nodes: azure.mgmt.databoxedge.operations.NodesOperations
    :ivar operations_status: OperationsStatus operations
    :vartype operations_status: azure.mgmt.databoxedge.operations.OperationsStatusOperations
    :ivar orders: Orders operations
    :vartype orders: azure.mgmt.databoxedge.operations.OrdersOperations
    :ivar roles: Roles operations
    :vartype roles: azure.mgmt.databoxedge.operations.RolesOperations
    :ivar shares: Shares operations
    :vartype shares: azure.mgmt.databoxedge.operations.SharesOperations
    :ivar storage_account_credentials: StorageAccountCredentials operations
    :vartype storage_account_credentials: azure.mgmt.databoxedge.operations.StorageAccountCredentialsOperations
    :ivar storage_accounts: StorageAccounts operations
    :vartype storage_accounts: azure.mgmt.databoxedge.operations.StorageAccountsOperations
    :ivar containers: Containers operations
    :vartype containers: azure.mgmt.databoxedge.operations.ContainersOperations
    :ivar triggers: Triggers operations
    :vartype triggers: azure.mgmt.databoxedge.operations.TriggersOperations
    :ivar users: Users operations
    :vartype users: azure.mgmt.databoxedge.operations.UsersOperations
    :ivar skus: Skus operations
    :vartype skus: azure.mgmt.databoxedge.operations.SkusOperations

    :param credentials: Credentials needed for the client to connect to Azure.
    :type credentials: :mod:`A msrestazure Credentials
     object<msrestazure.azure_active_directory>`
    :param subscription_id: The subscription ID.
    :type subscription_id: str
    :param str base_url: Service URL
    """

    def __init__(
            self, credentials, subscription_id, base_url=None):

        self.config = DataBoxEdgeManagementClientConfiguration(credentials, subscription_id, base_url)
        super(DataBoxEdgeManagementClient, self).__init__(self.config.credentials, self.config)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self.api_version = '2019-08-01'
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)

        self.operations = Operations(
            self._client, self.config, self._serialize, self._deserialize)
        self.devices = DevicesOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.alerts = AlertsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.bandwidth_schedules = BandwidthSchedulesOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.jobs = JobsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.nodes = NodesOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.operations_status = OperationsStatusOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.orders = OrdersOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.roles = RolesOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.shares = SharesOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.storage_account_credentials = StorageAccountCredentialsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.storage_accounts = StorageAccountsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.containers = ContainersOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.triggers = TriggersOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.users = UsersOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.skus = SkusOperations(
            self._client, self.config, self._serialize, self._deserialize)