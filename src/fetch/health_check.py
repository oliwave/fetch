import time
import requests

from collections import defaultdict

from src.utils.endpoint import Endpoint

LATENCY_THRESHOLD_MS = 500

class HealthCheck:
  """HealthCheck holds the information of totol and successful request for futher availability caculation"""
  
  def __init__(self):
    self.__domain_metrics = defaultdict(lambda: {"total": 0, "success": 0})

  def request(self, endpoint: Endpoint):
    self.__domain_metrics[endpoint.domain]["total"] += 1  # Increment total requests for the domain

    start_time = time.time()

    try:
      response = requests.request(
        method=endpoint.method, 
        url=endpoint.url,
        headers=endpoint.headers,
        data=endpoint.body
      )
      end_time = time.time()
      latency_ms = (end_time - start_time) * 1000

      # Only view the request as success if the reponse is 200-299 and latency is lower than threshold
      if response.status_code >= 200 and response.status_code <= 299 and latency_ms <= LATENCY_THRESHOLD_MS:
        self.__domain_metrics[endpoint.domain]["success"] += 1

    except Exception as e:
      print(f"Error: {endpoint.url}, Error: {str(e)}")

  @property
  def domain_metrics(self):
      return self.__domain_metrics
