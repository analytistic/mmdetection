# Copyright (c) OpenMMLab. All rights reserved.
from .bbox_head import BBoxHead
from .convfc_bbox_head import (ConvFCBBoxHead, Shared2FCBBoxHead,
                               Shared4Conv1FCBBoxHead,
                               Shared3FCBBoxHead_with_BboxEncoding)
from .dii_head import DIIHead
from .double_bbox_head import DoubleConvFCBBoxHead
from .multi_instance_bbox_head import MultiInstanceBBoxHead
from .sabl_head import SABLHead
from .scnet_bbox_head import SCNetBBoxHead

__all__ = [
    'BBoxHead', 'ConvFCBBoxHead', 'Shared2FCBBoxHead',
    'Shared4Conv1FCBBoxHead', 'DoubleConvFCBBoxHead', 'SABLHead', 'DIIHead',
<<<<<<< HEAD
    'SCNetBBoxHead', 'MultiInstanceBBoxHead'
=======
    'SCNetBBoxHead', 'Shared3FCBBoxHead_with_BboxEncoding'
>>>>>>> feature/chartdete
]
