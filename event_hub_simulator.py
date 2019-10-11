#!/usr/bin/env python

"""
An Azure Event Hub event simulator
"""

# pylint: disable=C0111

import argparse
import sys
import logging
import datetime
import time
import os
import random
import pandas as pd
import json

from azure.eventhub import EventHubClient, Sender, EventData

def run_event_hub_simulation(conn_str, batch_size, sample_data=None):
  def data_generator(batch_size):
    if not batch_size:
      batch_size = random.randint(1,50)

    logger.info("Generating {} data points".format(batch_size))

    if sample_data:
      for i in range(batch_size):
        data_json = random.sample(sample_data, 1)
        yield str.encode(json.dumps(data_json))

    else:
      for i in range(batch_size):
        yield str.encode(json.dumps({'Hello': 'World'}))

  try:
    client = EventHubClient.from_connection_string(conn_str)
    sender = client.add_sender(partition="1")
    client.run()
    try:
      start_time = time.time()
      while True:
        # print([x for x in data_generator(batch_size=batch_size)])

        data = EventData(batch=data_generator(batch_size=batch_size))
        sender.send(data)

        # Sleep for 0.5 - 2 seconds between each batch
        time.sleep(random.randint(500, 2001)/1000)

    except:
      raise

    finally:
      end_time = time.time()
      client.stop()
      run_time = end_time - start_time
      logger.info("Runtime: {} seconds".format(run_time))

  except KeyboardInterrupt:
    pass

if __name__ == '__main__':
  logger = logging.getLogger()
  logging.basicConfig(level=logging.INFO)

  parser = argparse.ArgumentParser()
  parser.add_argument("--batch", help="Number of events to send and wait", type=int)
  # Connection string can be in either of these formats:
  # "Endpoint=sb://<mynamespace>.servicebus.windows.net/<myeventhub>;SharedAccessKeyName=<sharedaccesskeyname>;SharedAccessKey=<sharedaccesskey>"
  parser.add_argument("--conn-str", help="EventHub connection string", required=True)
  parser.add_argument("--data-path", help="File path of input data to sample from")
  parser.add_argument("--data-format", help="Format of input data", choices=['csv']) # Currently only supports CSV file

  args, _ = parser.parse_known_args()

  data = None
  if args.data_path:
    data = pd.read_csv(args.data_path)
    data = data.to_json(orient='records')
    data = json.loads(data)

  run_event_hub_simulation(conn_str=args.conn_str, batch_size=args.batch, sample_data=data)