python -m grpc_tools.protoc -Isrc/protos/python/image_processing=src/protos --python_out=. --pyi_out=. --grpc_python_out=. src/protos/image_processing.proto