#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright: (c) 2021, Ansible Project
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
# template: header.j2
# This module is autogenerated by vmware_rest_code_generator.
# See: https://github.com/ansible-collections/vmware_rest_code_generator
from __future__ import absolute_import, division, print_function

__metaclass__ = type


DOCUMENTATION = r"""
module: vcenter_ovf_libraryitem
short_description: Creates a library item in content library from a virtual machine
  or virtual appliance
description: Creates a library item in content library from a virtual machine or virtual
  appliance. <p> This {@term operation} creates a library item in content library
  whose content is an OVF package derived from a source virtual machine or virtual
  appliance, using the supplied create specification. The OVF package may be stored
  as in a newly created library item or in an in an existing library item. For an
  existing library item whose content is updated by this {@term operation}, the original
  content is overwritten. Meta data such as name and description is not updated for
  the exisitng library item. </p>
options:
  client_token:
    description:
    - Client-generated token used to retry a request if the client fails to get a
      response from the server. If the original request succeeded, the result of that
      request will be returned, otherwise the operation will be retried.
    type: str
  create_spec:
    description:
    - Information used to create the OVF package from the source virtual machine or
      virtual appliance. Required with I(state=['present'])
    - 'Valid attributes are:'
    - ' - C(name) (str): Name to use in the OVF descriptor stored in the library item.
      ([''present''])'
    - ' - C(description) (str): Description to use in the OVF descriptor stored in
      the library item. ([''present''])'
    - ' - C(flags) (list): Flags to use for OVF package creation. The supported flags
      can be obtained using {@link ExportFlag#list}. ([''present''])'
    type: dict
  deployment_spec:
    description:
    - Specification of how the OVF package should be deployed to the target. Required
      with I(state=['deploy'])
    - 'Valid attributes are:'
    - ' - C(name) (str): Name assigned to the deployed target virtual machine or virtual
      appliance. ([''deploy''])'
    - ' - C(annotation) (str): Annotation assigned to the deployed target virtual
      machine or virtual appliance. ([''deploy''])'
    - ' - C(accept_all_EULA) (bool): Whether to accept all End User License Agreements.
      ([''deploy''])'
    - '   This key is required with [''deploy''].'
    - ' - C(network_mappings) (dict): Specification of the target network to use for
      sections of type ovf:NetworkSection in the OVF descriptor. The key in the {@term
      map} is the section identifier of the ovf:NetworkSection section in the OVF
      descriptor and the value is the target network to be used for deployment. ([''deploy''])'
    - ' - C(storage_mappings) (dict): Specification of the target storage to use for
      sections of type vmw:StorageGroupSection in the OVF descriptor. The key in the
      {@term map} is the section identifier of the ovf:StorageGroupSection section
      in the OVF descriptor and the value is the target storage specification to be
      used for deployment. ([''deploy''])'
    - ' - C(storage_provisioning) (str): The C(disk_provisioning_type) defines the
      virtual disk provisioning types that can be set for a disk on the target platform.
      ([''deploy''])'
    - '   - Accepted values:'
    - '     - eagerZeroedThick'
    - '     - thick'
    - '     - thin'
    - ' - C(storage_profile_id) (str): Default storage profile to use for all sections
      of type vmw:StorageSection in the OVF descriptor. ([''deploy''])'
    - ' - C(locale) (str): The locale to use for parsing the OVF descriptor. ([''deploy''])'
    - ' - C(flags) (list): Flags to be use for deployment. The supported flag values
      can be obtained using {@link ImportFlag#list}. ([''deploy''])'
    - ' - C(additional_parameters) (list): Additional OVF parameters that may be needed
      for the deployment. Additional OVF parameters may be required by the OVF descriptor
      of the OVF package in the library item. Examples of OVF parameters that can
      be specified through this field include, but are not limited to: <ul> <li>{@link
      DeploymentOptionParams}</li> <li>{@link ExtraConfigParams}</li> <li>{@link IpAllocationParams}</li>
      <li>{@link PropertyParams}</li> <li>{@link ScaleOutParams}</li> <li>{@link VcenterExtensionParams}</li>
      </ul> ([''deploy''])'
    - ' - C(default_datastore_id) (str): Default datastore to use for all sections
      of type vmw:StorageSection in the OVF descriptor. ([''deploy''])'
    type: dict
  ovf_library_item_id:
    description:
    - Identifier of the content library item containing the OVF package to be deployed.
      Required with I(state=['deploy', 'filter'])
    type: str
  session_timeout:
    description:
    - 'Timeout settings for client session. '
    - 'The maximal number of seconds for the whole operation including connection
      establishment, request sending and response. '
    - The default value is 300s.
    type: float
    version_added: 2.1.0
  source:
    description:
    - Identifier of the virtual machine or virtual appliance to use as the source.
      Required with I(state=['present'])
    - 'Valid attributes are:'
    - ' - C(type) (str): Type of the deployable resource. ([''present''])'
    - '   This key is required with [''present''].'
    - ' - C(id) (str): Identifier of the deployable resource. ([''present''])'
    - '   This key is required with [''present''].'
    type: dict
  state:
    choices:
    - deploy
    - filter
    - present
    default: present
    description: []
    type: str
  target:
    description:
    - Specification of the target content library and library item. This parameter
      is mandatory.
    - 'Valid attributes are:'
    - ' - C(library_id) (str): Identifier of the library in which a new library item
      should be created. This field is not used if the C(#library_item_id) field is
      specified. ([''present''])'
    - ' - C(library_item_id) (str): Identifier of the library item that should be
      should be updated. ([''present''])'
    - ' - C(resource_pool_id) (str): Identifier of the resource pool to which the
      virtual machine or virtual appliance should be attached. ([''deploy'', ''filter''])'
    - '   This key is required with [''deploy'', ''filter''].'
    - ' - C(host_id) (str): Identifier of the target host on which the virtual machine
      or virtual appliance will run. The target host must be a member of the cluster
      that contains the resource pool identified by {@link #resourcePoolId}. ([''deploy'',
      ''filter''])'
    - ' - C(folder_id) (str): Identifier of the vCenter folder that should contain
      the virtual machine or virtual appliance. The folder must be virtual machine
      folder. ([''deploy'', ''filter''])'
    required: true
    type: dict
  vcenter_hostname:
    description:
    - The hostname or IP address of the vSphere vCenter
    - If the value is not specified in the task, the value of environment variable
      C(VMWARE_HOST) will be used instead.
    required: true
    type: str
  vcenter_password:
    description:
    - The vSphere vCenter password
    - If the value is not specified in the task, the value of environment variable
      C(VMWARE_PASSWORD) will be used instead.
    required: true
    type: str
  vcenter_rest_log_file:
    description:
    - 'You can use this optional parameter to set the location of a log file. '
    - 'This file will be used to record the HTTP REST interaction. '
    - 'The file will be stored on the host that run the module. '
    - 'If the value is not specified in the task, the value of '
    - environment variable C(VMWARE_REST_LOG_FILE) will be used instead.
    type: str
  vcenter_username:
    description:
    - The vSphere vCenter username
    - If the value is not specified in the task, the value of environment variable
      C(VMWARE_USER) will be used instead.
    required: true
    type: str
  vcenter_validate_certs:
    default: true
    description:
    - Allows connection when SSL certificates are not valid. Set to C(false) when
      certificates are not trusted.
    - If the value is not specified in the task, the value of environment variable
      C(VMWARE_VALIDATE_CERTS) will be used instead.
    type: bool
author:
- Ansible Cloud Team (@ansible-collections)
version_added: 2.0.0
requirements:
- vSphere 7.0.2 or greater
- python >= 3.6
- aiohttp
notes:
- Tested on vSphere 7.0.2
"""

EXAMPLES = r"""
"""

RETURN = r"""
# content generated by the update_return_section callback# task: Create a new VM from the OVF and specify the host and folder
value:
  description: Create a new VM from the OVF and specify the host and folder
  returned: On success
  sample:
    error:
      errors: []
      information: []
      warnings: []
    resource_id:
      id: vm-1343
      type: VirtualMachine
    succeeded: 1
  type: dict
"""

# This structure describes the format of the data expected by the end-points
PAYLOAD_FORMAT = {
    "create": {
        "query": {"client_token": "client_token"},
        "body": {"create_spec": "create_spec", "source": "source", "target": "target"},
        "path": {},
    },
    "deploy": {
        "query": {"client_token": "client_token"},
        "body": {"deployment_spec": "deployment_spec", "target": "target"},
        "path": {"ovf_library_item_id": "ovf_library_item_id"},
    },
    "filter": {
        "query": {},
        "body": {"target": "target"},
        "path": {"ovf_library_item_id": "ovf_library_item_id"},
    },
}  # pylint: disable=line-too-long

import json
import socket
from ansible.module_utils.basic import env_fallback

try:
    from ansible_collections.cloud.common.plugins.module_utils.turbo.exceptions import (
        EmbeddedModuleFailure,
    )
    from ansible_collections.cloud.common.plugins.module_utils.turbo.module import (
        AnsibleTurboModule as AnsibleModule,
    )

    AnsibleModule.collection_name = "vmware.vmware_rest"
except ImportError:
    from ansible.module_utils.basic import AnsibleModule
from ansible_collections.vmware.vmware_rest.plugins.module_utils.vmware_rest import (
    build_full_device_list,
    exists,
    gen_args,
    get_device_info,
    get_subdevice_type,
    list_devices,
    open_session,
    prepare_payload,
    update_changed_flag,
    session_timeout,
)


def prepare_argument_spec():
    argument_spec = {
        "vcenter_hostname": dict(
            type="str", required=True, fallback=(env_fallback, ["VMWARE_HOST"]),
        ),
        "vcenter_username": dict(
            type="str", required=True, fallback=(env_fallback, ["VMWARE_USER"]),
        ),
        "vcenter_password": dict(
            type="str",
            required=True,
            no_log=True,
            fallback=(env_fallback, ["VMWARE_PASSWORD"]),
        ),
        "vcenter_validate_certs": dict(
            type="bool",
            required=False,
            default=True,
            fallback=(env_fallback, ["VMWARE_VALIDATE_CERTS"]),
        ),
        "vcenter_rest_log_file": dict(
            type="str",
            required=False,
            fallback=(env_fallback, ["VMWARE_REST_LOG_FILE"]),
        ),
        "session_timeout": dict(
            type="float",
            required=False,
            fallback=(env_fallback, ["VMWARE_SESSION_TIMEOUT"]),
        ),
    }

    argument_spec["client_token"] = {"no_log": True, "type": "str"}
    argument_spec["create_spec"] = {"type": "dict"}
    argument_spec["deployment_spec"] = {"type": "dict"}
    argument_spec["ovf_library_item_id"] = {"type": "str"}
    argument_spec["source"] = {"type": "dict"}
    argument_spec["state"] = {
        "type": "str",
        "choices": ["deploy", "filter", "present"],
        "default": "present",
    }
    argument_spec["target"] = {"required": True, "type": "dict"}

    return argument_spec


async def main():
    required_if = list([])

    module_args = prepare_argument_spec()
    module = AnsibleModule(
        argument_spec=module_args, required_if=required_if, supports_check_mode=True
    )
    if not module.params["vcenter_hostname"]:
        module.fail_json("vcenter_hostname cannot be empty")
    if not module.params["vcenter_username"]:
        module.fail_json("vcenter_username cannot be empty")
    if not module.params["vcenter_password"]:
        module.fail_json("vcenter_password cannot be empty")
    try:
        session = await open_session(
            vcenter_hostname=module.params["vcenter_hostname"],
            vcenter_username=module.params["vcenter_username"],
            vcenter_password=module.params["vcenter_password"],
            validate_certs=module.params["vcenter_validate_certs"],
            log_file=module.params["vcenter_rest_log_file"],
        )
    except EmbeddedModuleFailure as err:
        module.fail_json(err.get_message())
    result = await entry_point(module, session)
    module.exit_json(**result)


# template: default_module.j2
def build_url(params):
    return ("https://{vcenter_hostname}" "/api/vcenter/ovf/library-item").format(
        **params
    )


async def entry_point(module, session):

    if module.params["state"] == "present":
        if "_create" in globals():
            operation = "create"
        else:
            operation = "update"
    elif module.params["state"] == "absent":
        operation = "delete"
    else:
        operation = module.params["state"]

    func = globals()["_" + operation]

    return await func(module.params, session)


async def _create(params, session):

    payload = prepare_payload(params, PAYLOAD_FORMAT["create"])
    _url = ("https://{vcenter_hostname}" "/api/vcenter/ovf/library-item").format(
        **params
    )
    async with session.post(_url, json=payload, **session_timeout(params)) as resp:
        if resp.status == 500:
            text = await resp.text()
            raise EmbeddedModuleFailure(
                f"Request has failed: status={resp.status}, {text}"
            )
        try:
            if resp.headers["Content-Type"] == "application/json":
                _json = await resp.json()
        except KeyError:
            _json = {}

        if (resp.status in [200, 201]) and "error" not in _json:
            if isinstance(_json, str):  # 7.0.2 and greater
                _id = _json  # TODO: fetch the object
            elif isinstance(_json, dict) and "value" not in _json:
                _id = list(_json["value"].values())[0]
            elif isinstance(_json, dict) and "value" in _json:
                _id = _json["value"]
            _json_device_info = await get_device_info(session, _url, _id)
            if _json_device_info:
                _json = _json_device_info

        return await update_changed_flag(_json, resp.status, "create")


async def _deploy(params, session):
    _in_query_parameters = PAYLOAD_FORMAT["deploy"]["query"].keys()
    payload = prepare_payload(params, PAYLOAD_FORMAT["deploy"])
    subdevice_type = get_subdevice_type(
        "/api/vcenter/ovf/library-item/{ovf_library_item_id}?action=deploy"
    )
    if subdevice_type and not params[subdevice_type]:
        _json = await exists(params, session, build_url(params))
        if _json:
            params[subdevice_type] = _json["id"]
    _url = (
        "https://{vcenter_hostname}"
        # aa
        "/api/vcenter/ovf/library-item/{ovf_library_item_id}?action=deploy"
    ).format(**params) + gen_args(params, _in_query_parameters)
    async with session.post(_url, json=payload, **session_timeout(params)) as resp:
        try:
            if resp.headers["Content-Type"] == "application/json":
                _json = await resp.json()
        except KeyError:
            _json = {}
        if "value" not in _json:  # 7.0.2
            _json = {"value": _json}

        return await update_changed_flag(_json, resp.status, "deploy")


async def _filter(params, session):
    _in_query_parameters = PAYLOAD_FORMAT["filter"]["query"].keys()
    payload = prepare_payload(params, PAYLOAD_FORMAT["filter"])
    subdevice_type = get_subdevice_type(
        "/api/vcenter/ovf/library-item/{ovf_library_item_id}?action=filter"
    )
    if subdevice_type and not params[subdevice_type]:
        _json = await exists(params, session, build_url(params))
        if _json:
            params[subdevice_type] = _json["id"]
    _url = (
        "https://{vcenter_hostname}"
        # aa
        "/api/vcenter/ovf/library-item/{ovf_library_item_id}?action=filter"
    ).format(**params) + gen_args(params, _in_query_parameters)
    async with session.post(_url, json=payload, **session_timeout(params)) as resp:
        try:
            if resp.headers["Content-Type"] == "application/json":
                _json = await resp.json()
        except KeyError:
            _json = {}
        if "value" not in _json:  # 7.0.2
            _json = {"value": _json}

        return await update_changed_flag(_json, resp.status, "filter")


if __name__ == "__main__":
    import asyncio

    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
