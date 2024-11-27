import math


class Report:
  """Report is dedicated to caculate service availability"""
  
  def __init__(self, health_check):
    self.health_check = health_check
    
  def display_domain_availability(self) -> None:
    availability = {}
    for domain, metrics in self.health_check.domain_metrics.items():
      if metrics["total"] == 0:
        availability[domain] = 0
      else:
        availability[domain] = math.floor((metrics["success"] / metrics["total"]) * 100)
          
    # Calculate and print availability for each domain
    for domain, avail in availability.items():
      print(f"{domain} has {avail}% availability percentage", flush=True)
