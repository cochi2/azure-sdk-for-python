# coding=utf-8
# ------------------------------------
# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.
# ------------------------------------

import pytest
import uuid
import functools
from azure.ai.formrecognizer.aio import DocumentModelAdministrationClient
from azure.ai.formrecognizer import DocumentModel
from azure.ai.formrecognizer._generated.v2021_09_30_preview.models import GetOperationResponse, ModelInfo
from preparers import FormRecognizerPreparer
from preparers import GlobalClientPreparer as _GlobalClientPreparer
from asynctestcase import AsyncFormRecognizerTest

DocumentModelAdministrationClientPreparer = functools.partial(_GlobalClientPreparer, DocumentModelAdministrationClient)


class TestTrainingAsync(AsyncFormRecognizerTest):

    @FormRecognizerPreparer()
    @DocumentModelAdministrationClientPreparer()
    async def test_compose_model(self, client, formrecognizer_storage_container_sas_url):
        model_id_1 = str(uuid.uuid4())
        model_id_2 = str(uuid.uuid4())
        composed_id = str(uuid.uuid4())
        async with client:
            poller = await client.begin_build_model(formrecognizer_storage_container_sas_url, model_id=model_id_1, description="model1")
            model_1 = await poller.result()

            poller = await client.begin_build_model(formrecognizer_storage_container_sas_url, model_id=model_id_2, description="model2")
            model_2 = await poller.result()

            poller = await client.begin_create_composed_model([model_1.model_id, model_2.model_id], model_id=composed_id, description="my composed model")

            composed_model = await poller.result()
            if self.is_live:
                assert composed_model.model_id == composed_id

            assert composed_model.model_id
            assert composed_model.description == "my composed model"
            assert composed_model.created_on
            for name, doc_type in composed_model.doc_types.items():
                assert name
                for key, field in doc_type.field_schema.items():
                    assert key
                    assert field["type"]
                    assert doc_type.field_confidence[key] is not None

    @FormRecognizerPreparer()
    @DocumentModelAdministrationClientPreparer()
    async def test_compose_model_transform(self, client, formrecognizer_storage_container_sas_url):
        raw_response = []

        def callback(response, _, headers):
            op_response = client._deserialize(GetOperationResponse, response)
            model_info = client._deserialize(ModelInfo, op_response.result)
            document_model = DocumentModel._from_generated(model_info)
            raw_response.append(model_info)
            raw_response.append(document_model)

        async with client:
            poller = await client.begin_build_model(formrecognizer_storage_container_sas_url, description="model1")
            model_1 = await poller.result()

            poller = await client.begin_build_model(formrecognizer_storage_container_sas_url, description="model2")
            model_2 = await poller.result()

            poller = await client.begin_create_composed_model([model_1.model_id, model_2.model_id], description="my composed model", cls=callback)
            model = await poller.result()

        generated = raw_response[0]
        document_model = raw_response[1]
        self.assertModelTransformCorrect(document_model, generated)

        document_model_dict = document_model.to_dict()
        document_model_from_dict = DocumentModel.from_dict(document_model_dict)
        self.assertModelTransformCorrect(document_model_from_dict, generated)

    @pytest.mark.live_test_only
    @FormRecognizerPreparer()
    @DocumentModelAdministrationClientPreparer()
    async def test_compose_continuation_token(self, client, formrecognizer_storage_container_sas_url):

        async with client:
            poller = await client.begin_build_model(formrecognizer_storage_container_sas_url)
            model_1 = await poller.result()

            poller = await client.begin_build_model(formrecognizer_storage_container_sas_url)
            model_2 = await poller.result()

            initial_poller = await client.begin_create_composed_model([model_1.model_id, model_2.model_id])
            cont_token = initial_poller.continuation_token()

            poller = await client.begin_create_composed_model(None, continuation_token=cont_token)
            result = await poller.result()
            assert result

            await initial_poller.wait()  # necessary so azure-devtools doesn't throw assertion error

    @FormRecognizerPreparer()
    @DocumentModelAdministrationClientPreparer()
    async def test_poller_metadata(self, client, formrecognizer_storage_container_sas_url):
        async with client:
            poller = await client.begin_build_model(formrecognizer_storage_container_sas_url)
            model_1 = await poller.result()

            poller = await client.begin_build_model(formrecognizer_storage_container_sas_url)
            model_2 = await poller.result()

            poller = await client.begin_create_composed_model([model_1.model_id, model_2.model_id])
            assert poller.operation_id
            assert poller.percent_completed is not None
            await poller.result()
            assert poller.operation_kind == "documentModelCompose"
            assert poller.percent_completed == 100
            assert poller.resource_location_url
            assert poller.created_on
            assert poller.last_updated_on
