#!/usr/bin/env python

# Copyright 2016 Google, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import argparse
import base64
import datetime
import decimal
import json
import logging
import time

from google.cloud import spanner
from google.protobuf import field_mask_pb2  # type: ignore

# [START spanner_insert_data]
def insert_data(instance_id, database_id):
    """Inserts sample data into the given database.

    The database and table must already exist and can be created using
    `create_database`.
    """
    spanner_client = spanner.Client()
    instance = spanner_client.instance(instance_id)
    database = instance.database(database_id)

    with database.batch() as batch:
        batch.insert(
            table="carros",
            columns=("ID", "NOME", "ANO"),
            values=[
                (1, "VW Gol", "1983"),
                (2, "Ford Fiesta", "2008"),
                (3, "BMW X3", "2021"),
            ],
        )

    print("Inserted data.")


# [END spanner_insert_data]

insert_data("destrinchando-spanner","modelos-carros")