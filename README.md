# drf-nested-field-multipart
Parser for nested params in multipart file upload


# Usage
```python
from drf_nested_field_multipart import NestedMultipartParser
from rest_framework import viewsets

class YourViewSet(viewsets.ViewSet):
	parser_classes = (NestedMultipartParser,)
```
To enable JSON and multipart

```python
from drf_nested_field_multipart import NestedMultipartParser
from rest_framework.parsers import JSONParser
from rest_framework import viewsets

class YourViewSet(viewsets.ViewSet):
	parser_classes = (JSONParser, NestedMultipartParser)
```

# Installation
`pip install drf-nested-field-multipart`