import yaml
from src.utils.endpoint import Endpoint

# Read YAML and parse into Endpoint objects
def load_endpoints_from_yaml(file_path: str) -> list[Endpoint]:
  with open(file_path, 'r') as f:
    data = yaml.safe_load(f)

  endpoints = []
  
  for item in data:
    # Don't add the invalid endpoint format to the endpoints so it won't affect the availability metrics
    try:
      endpoint = Endpoint(name=item.get("name"), url=item.get("url"))
      endpoint.method = item.get('method', 'GET'),
      endpoint.headers = item.get("headers"),
      endpoint.body = item.get("body"),
      endpoints.append(endpoint)
    except Exception as e:  
      print(f"Endpoint name: {endpoint.name}, Error: {str(e)}")

  return endpoints
