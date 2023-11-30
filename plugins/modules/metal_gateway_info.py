#!/usr/bin/python
# -*- coding: utf-8 -*-

# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

# DOCUMENTATION, EXAMPLES, and RETURN are generated by
# ansible_specdoc. Do not edit them directly.

DOCUMENTATION = '''
author: Equinix DevRel Team (@equinix) <support@equinix.com>
description: Gather information about Metal Gateways
module: metal_gateway_info
notes: []
options:
  project_id:
    description:
    - UUID of parent project the gateway is scoped to.
    required: false
    type: str
requirements: null
short_description: Gather information about Metal Gateways
'''
EXAMPLES = '''
- name: Gather information about all gateways in a project
  hosts: localhost
  tasks:
  - equinix.cloud.metal_gateway_info:
      project_id: 2a5122b9-c323-4d5c-b53c-9ad3f54273e7
'''
RETURN = '''
resources:
  description: Found Metal Gateways
  returned: always
  sample:
  - "\n[\n    {\n        \"id\": \"771c9418-7c60-4a45-8fa6-3a002132331d\",\n     \
    \   \"ip_reservation_id\": \"d45c9629-3aab-4a7b-af5d-4ca50041e311\",\n       \
    \ \"metal_state\": \"ready\",\n        \"private_ipv4_subnet_size\": 8,\n    \
    \    \"project_id\": \"f7a35065-2e41-4747-b3d1-400af0a3e0e8\",\n        \"virtual_network_id\"\
    : \"898972b3-7eb9-4ca2-b803-7b5d339bbea7\"\n    },\n    {\n        \"id\": \"\
    b66eb02d-c4bb-4ae8-a22e-0f7934da971e\",\n        \"ip_reservation_id\": \"6282982a-e6de-4f4d-b230-2ae27e90778c\"\
    ,\n        \"metal_state\": \"ready\",\n        \"private_ipv4_subnet_size\":\
    \ 8,\n        \"project_id\": \"f7a35065-2e41-4747-b3d1-400af0a3e0e8\",\n    \
    \    \"virtual_network_id\": \"898972b3-7eb9-4ca2-b803-7b5d339bbea7\"\n    }\n\
    ]"
  type: dict
'''

# End

from ansible.module_utils._text import to_native
from ansible_specdoc.objects import SpecField, FieldType, SpecReturnValue
import traceback

from ansible_collections.equinix.cloud.plugins.module_utils.equinix import (
    EquinixModule,
    getSpecDocMeta,
)

module_spec = dict(
    project_id=SpecField(
        type=FieldType.string,
        description=['UUID of parent project the gateway is scoped to.'],
    ),
)

specdoc_examples = ['''
- name: Gather information about all gateways in a project
  hosts: localhost
  tasks:
      - equinix.cloud.metal_gateway_info:
          project_id: 2a5122b9-c323-4d5c-b53c-9ad3f54273e7
''',
]

result_sample = ['''
[
    {
        "id": "771c9418-7c60-4a45-8fa6-3a002132331d",
        "ip_reservation_id": "d45c9629-3aab-4a7b-af5d-4ca50041e311",
        "metal_state": "ready",
        "private_ipv4_subnet_size": 8,
        "project_id": "f7a35065-2e41-4747-b3d1-400af0a3e0e8",
        "virtual_network_id": "898972b3-7eb9-4ca2-b803-7b5d339bbea7"
    },
    {
        "id": "b66eb02d-c4bb-4ae8-a22e-0f7934da971e",
        "ip_reservation_id": "6282982a-e6de-4f4d-b230-2ae27e90778c",
        "metal_state": "ready",
        "private_ipv4_subnet_size": 8,
        "project_id": "f7a35065-2e41-4747-b3d1-400af0a3e0e8",
        "virtual_network_id": "898972b3-7eb9-4ca2-b803-7b5d339bbea7"
    }
]''',
]

SPECDOC_META = getSpecDocMeta(
    short_description="Gather information about Metal Gateways",
    description=(
        'Gather information about Metal Gateways'
    ),
    examples=specdoc_examples,
    options=module_spec,
    return_values={
        "resources": SpecReturnValue(
            description='Found Metal Gateways',
            type=FieldType.dict,
            sample=result_sample,
        ),
    },
)


def main():
    module = EquinixModule(
        argument_spec=SPECDOC_META.ansible_spec,
        is_info=True,
    )
    try:
        module.params_syntax_check()
        return_value = {'resources': module.get_list("metal_gateway")}
    except Exception as e:
        tr = traceback.format_exc()
        module.fail_json(msg=to_native(e), exception=tr)
    module.exit_json(**return_value)


if __name__ == '__main__':
    main()
