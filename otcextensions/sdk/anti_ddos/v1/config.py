# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.
from openstack import resource

from otcextensions.sdk import sdk_resource


class Config(sdk_resource.Resource):

    base_path = '/antiddos/query_config_list'

    # capabilities
    allow_list = True

    # Properties
    #: A list of traffic limited.
    #: *Type: list*
    traffic_limited_list = resource.Body('traffic_limited_list', type=list)
    #: Http limit list
    #: *Type: list*
    http_limited_list = resource.Body('http_limited_list', type=list)
    #: Connection limit list
    #: *Type: list*
    connection_limited_list = resource.Body('connection_limited_list',
                                            type=list)
    #: Extended configuration
    #: *Type: list*
    extend_ddos_config = resource.Body('extend_ddos_config',
                                       type=list)
