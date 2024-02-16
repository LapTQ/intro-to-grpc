from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class FrameImg(_message.Message):
    __slots__ = ("img_pkl",)
    IMG_PKL_FIELD_NUMBER: _ClassVar[int]
    img_pkl: bytes
    def __init__(self, img_pkl: _Optional[bytes] = ...) -> None: ...

class FrameData(_message.Message):
    __slots__ = ("img_pkl", "window_name")
    IMG_PKL_FIELD_NUMBER: _ClassVar[int]
    WINDOW_NAME_FIELD_NUMBER: _ClassVar[int]
    img_pkl: bytes
    window_name: str
    def __init__(self, img_pkl: _Optional[bytes] = ..., window_name: _Optional[str] = ...) -> None: ...

class ImgSize(_message.Message):
    __slots__ = ("width", "height")
    WIDTH_FIELD_NUMBER: _ClassVar[int]
    HEIGHT_FIELD_NUMBER: _ClassVar[int]
    width: int
    height: int
    def __init__(self, width: _Optional[int] = ..., height: _Optional[int] = ...) -> None: ...

class EmptyResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ResizeRequest(_message.Message):
    __slots__ = ("img_pkl", "target_size")
    IMG_PKL_FIELD_NUMBER: _ClassVar[int]
    TARGET_SIZE_FIELD_NUMBER: _ClassVar[int]
    img_pkl: bytes
    target_size: ImgSize
    def __init__(self, img_pkl: _Optional[bytes] = ..., target_size: _Optional[_Union[ImgSize, _Mapping]] = ...) -> None: ...
