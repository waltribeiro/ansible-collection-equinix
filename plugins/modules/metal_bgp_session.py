#!/usr/bin/python
# -*- coding: utf-8 -*-

# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

# DOCUMENTATION, EXAMPLES, and RETURN are generated by
# ansible_specdoc. Do not edit them directly.

DOCUMENTATION = '''
author: Equinix DevRel Team (@equinix) <support@equinix.com>
description: 'Manage the resource kind in Equinix Metal. You can use *id* or *device_id*
  to lookup the resource. '
module: metal_bgp_session
notes: []
options:
  address_family:
    description:
    - (Required) ipv4 or ipv6.
    required: false
    type: str
  default_route:
    description:
    - (Optional) Boolean flag to set the default route policy. False by default.
    required: false
    type: bool
  device_id:
    description:
    - (Required) ID of device.
    required: false
    type: str
  id:
    description:
    - UUID of the BGP session.
    required: false
    type: str
requirements: null
short_description: Manage a particular resource type in Equinix Metal
'''
EXAMPLES = '''
- name: Start first test bgp session
  hosts: localhost
  tasks:
  - equinix.cloud.metal_bgp_session:
      device_id: 8ea9837a-6d19-4607-b166-f7f7bb04b022
      address_family: ipv6
      default_route: true
'''
RETURN = '''
metal_bgp_session:
  description: The module object
  returned: always
  sample:
  - "\n{\n    \"address_family\": \"ipv6\",\n    \"changed\": false,\n    \"device_id\"\
    : \"b068984f-f7d9-43a2-aa45-de04dcf4fe06\",\n    \"id\": \"43cc0fa9-4b73-4629-a60b-2904ca919155\"\
    ,\n}\n"
  type: dict
'''

# End of generated documentation


from ansible.module_utils._text import to_native
from ansible_specdoc.objects import (
    SpecField,
    FieldType,
    SpecReturnValue,
)
import traceback

from ansible_collections.equinix.cloud.plugins.module_utils.equinix import (
    EquinixModule,
    get_diff,
    getSpecDocMeta,
)


module_spec = dict(
    id=SpecField(
        type=FieldType.string,
        description="UUID of the BGP session to look up",
    ),
    device_id=SpecField(
        type=FieldType.string,
        description="(Required) ID of device.",
    ),
    address_family=SpecField(
        type=FieldType.string,
        description="(Required) ipv4 or ipv6.",
        editable=False,
    ),
    default_route=SpecField(
        type=FieldType.bool,
        description="(Optional) Boolean flag to set the default route policy. False by default.",
        editable=False,
    ),
)


specdoc_examples = ['''
- name: Start first test bgp session
  hosts: localhost
  tasks:
  - equinix.cloud.metal_bgp_session:
      device_id: 8ea9837a-6d19-4607-b166-f7f7bb04b022
      address_family: ipv6
      default_route: true
''',
]

result_sample = ['''
{
    "address_family": "ipv6",
    "changed": false,
    "device_id": "b068984f-f7d9-43a2-aa45-de04dcf4fe06",
    "id": "43cc0fa9-4b73-4629-a60b-2904ca919155",
}
''']

MUTABLE_ATTRIBUTES = [
    k for k, v in module_spec.items() if v.editable
]

SPECDOC_META = getSpecDocMeta(
    short_description='Manage BGP sessions in Equinix Metal',
    description=(
        'Manage BGP sessions in Equinix Metal.'
        'You can use *id* or *device_id* to lookup the resource. '
    ),
    examples=specdoc_examples,
    options=module_spec,
    return_values={
        "metal_bgp_session": SpecReturnValue(
            description='The module object',
            type=FieldType.dict,
            sample=result_sample,
        ),
    },
)


def main():
    module = EquinixModule(
        argument_spec=SPECDOC_META.ansible_spec,
        required_one_of=[("id", "address_family"), ("id", "default_route"), ("id", "device_id")],
    )

    state = module.params.get("state")
    changed = False

    fetched = {}
    try:
        module.params_syntax_check()
        if module.params.get("id"):
            tolerate_not_found = state == "absent"
            fetched = module.get_by_id("metal_bgp_session", tolerate_not_found)
        else:
            fetched = module.get_one_from_list(
                "metal_bgp_session",
                ["device_id"],
            )

        if fetched:
            module.params['id'] = fetched['id']
            if state == "present":
                diff = get_diff(module.params, fetched, MUTABLE_ATTRIBUTES)
                if diff:
                    fetched = module.update_by_id(diff, "metal_bgp_session")
                    changed = True

            else:
                module.delete_by_id("metal_bgp_session")
                changed = True
        elif state == "present":
            fetched = module.create("metal_bgp_session")
            if 'id' not in fetched:
                module.fail_json(msg="UUID not found in resource creation response")
            changed = True

    except Exception as e:
        tb = traceback.format_exc()
        module.fail_json(msg="Error in metal_bgp_session: {0}".format(to_native(e)),
                         exception=tb)

    fetched = {} if not fetched else fetched
    fetched.update({'changed': changed})
    module.exit_json(**fetched)


if __name__ == '__main__':
    main()
