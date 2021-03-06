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

from msrest.serialization import Model


class VolumePropertiesExportPolicy(Model):
    """exportPolicy.

    Set of export policy rules.

    :param rules: Export policy rule. Export policy rule
    :type rules: list[~azure.mgmt.netapp.models.ExportPolicyRule]
    """

    _attribute_map = {
        'rules': {'key': 'rules', 'type': '[ExportPolicyRule]'},
    }

    def __init__(self, **kwargs):
        super(VolumePropertiesExportPolicy, self).__init__(**kwargs)
        self.rules = kwargs.get('rules', None)
