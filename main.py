import os
import time

from src.fetch.health_check import HealthCheck
from src.fetch.report import Report
from src.utils.load_endpoints import load_endpoints_from_yaml
from dotenv import load_dotenv

if __name__ == "__main__":
  
  load_dotenv()
  
  file_name = os.getenv('API_ENDPOINT_FILE')
  endpoints = load_endpoints_from_yaml(file_name)

  # Create HealthCheck object
  health_check = HealthCheck()
  
  # Create the Report object with the healthCheck reference
  report = Report(health_check)

  while True:
    for endpoint in endpoints:
      health_check.request(endpoint)
    
    report.display_domain_availability()
    time.sleep(15)
