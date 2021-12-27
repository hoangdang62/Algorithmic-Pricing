#! /usr/bin/python
# coding: UTF-8
import sys
l11lll1_opy_ = sys.version_info [0] == 2
l1lll1l_opy_ = 2048
l1l11l1_opy_ = 7
def l111_opy_ (l1lllll_opy_):
    global l1l1ll_opy_
    l1lll_opy_ = ord (l1lllll_opy_ [-1])
    l1ll1ll_opy_ = l1lllll_opy_ [:-1]
    l11lll_opy_ = l1lll_opy_ % len (l1ll1ll_opy_)
    l11l1l_opy_ = l1ll1ll_opy_ [:l11lll_opy_] + l1ll1ll_opy_ [l11lll_opy_:]
    if l11lll1_opy_:
        l1111l1_opy_ = unicode () .join ([unichr (ord (char) - l1lll1l_opy_ - (l1ll111_opy_ + l1lll_opy_) % l1l11l1_opy_) for l1ll111_opy_, char in enumerate (l11l1l_opy_)])
    else:
        l1111l1_opy_ = str () .join ([chr (ord (char) - l1lll1l_opy_ - (l1ll111_opy_ + l1lll_opy_) % l1l11l1_opy_) for l1ll111_opy_, char in enumerate (l11l1l_opy_)])
    return eval (l1111l1_opy_)
import shutil
import codecs
import random
import importlib
import keyword
import errno
import sys
import os
import re
license = (
    '''Copyright 2014, 2015, 2016, 2017, 2018 Jacques de Hooge, GEATEC engineering, www.geatec.com
Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at
    http://www.apache.org/licenses/LICENSE-2.0
Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.'''
)
# =========== l1ll1l1ll_opy_ constants
l1ll1111_opy_ = sys.version_info[0] == 2
if l1ll1111_opy_:
    import __builtin__ as l1ll1llll_opy_
else:
    import builtins as l1ll1llll_opy_
l1lll1lll_opy_ = l111_opy_ (u"ࠫࡴࡶࡹࠨࠎ")
l111l111_opy_ = l111_opy_ (u"ࠬ࠷࠮࠲࠰࠵࠽ࠬࠏ")
random.seed()
l1l1llll1_opy_ = 2048
l1lll_opy_ = l1l1llll1_opy_
l111ll11_opy_ = 7
print(l111_opy_ (u"࠭ࡻࡾࠢࠫࡘࡒ࠯ࠠࡄࡱࡱࡪ࡮࡭ࡵࡳࡣࡥࡰࡪࠦࡍࡶ࡮ࡷ࡭ࠥࡓ࡯ࡥࡷ࡯ࡩࠥࡖࡹࡵࡪࡲࡲࠥࡕࡢࡧࡷࡶࡧࡦࡺ࡯ࡳ࡙ࠢࡩࡷࡹࡩࡰࡰࠣࡿࢂ࠭ࠐ").format(
    l1lll1lll_opy_.capitalize(), l111l111_opy_))
print(l111_opy_ (u"ࠧࡄࡱࡳࡽࡷ࡯ࡧࡩࡶࠣࠬࡈ࠯ࠠࡈࡧࡤࡸࡪࡩࠠࡆࡰࡪ࡭ࡳ࡫ࡥࡳ࡫ࡱ࡫࠳ࠦࡌࡪࡥࡨࡲࡸ࡫࠺ࠡࡃࡳࡥࡨ࡮ࡥࠡ࠴࠱࠴ࠥࡧࡴࠡࠢ࡫ࡸࡹࡶ࠺࠰࠱ࡺࡻࡼ࠴ࡡࡱࡣࡦ࡬ࡪ࠴࡯ࡳࡩ࠲ࡰ࡮ࡩࡥ࡯ࡵࡨࡷ࠴ࡒࡉࡄࡇࡑࡗࡊ࠳࠲࠯࠲࡟ࡲࠬࠑ"))
def main():
    global l1l1l111_opy_
    global l1lll_opy_
    global l1l11111_opy_
    global l111l1l1_opy_
    def l1111l11_opy_(l111l1ll_opy_, open=False):
        try:
            os.makedirs(l111l1ll_opy_.rsplit(l111_opy_ (u"ࠨ࠱ࠪࠒ"), 1)[0])
        except OSError as exception:
            if exception.errno != errno.EEXIST:
                raise
        if open:
            return codecs.open(l111l1ll_opy_, encoding=l111_opy_ (u"ࠩࡸࡸ࡫࠳࠸ࠨࠓ"), mode=l111_opy_ (u"ࠪࡻࠬࠔ"))
    def l11ll1ll_opy_(l11ll1l1_opy_, name):
        return l111_opy_ (u"ࠫࢀ࠶ࡽࡼ࠳ࢀࡿ࠷ࢃࠧࠕ").format(
            l111_opy_ (u"ࠬࡥ࡟ࠨࠖ") if name.startswith(
                l111_opy_ (u"࠭࡟ࡠࠩࠗ")) else l111_opy_ (u"ࠧࡠࠩ࠘") if name.startswith(l111_opy_ (u"ࠨࡡࠪ࠙")) else l111_opy_ (u"ࠩ࡯ࠫࠚ"),
            bin(l11ll1l1_opy_)[2:] .replace(l111_opy_ (u"ࠪ࠴ࠬࠛ"), l111_opy_ (u"ࠫࡱ࠭ࠜ")),
            l111l11l_opy_
        )
    def scramble(l1111l1_opy_):
        global l1lll_opy_
        if l1ll1111_opy_:
            l11l1l_opy_ = unicode() .join([unichr(l1l1llll1_opy_ + ord(char) + (
                l1ll111_opy_ + l1lll_opy_) % l111ll11_opy_) for l1ll111_opy_, char in enumerate(l1111l1_opy_)])
            l1lll11ll_opy_ = unichr(l1lll_opy_)
        else:
            l11l1l_opy_ = str() .join([chr(l1l1llll1_opy_ + ord(char) + (
                l1ll111_opy_ + l1lll_opy_) % l111ll11_opy_) for l1ll111_opy_, char in enumerate(l1111l1_opy_)])
            l1lll11ll_opy_ = chr(l1lll_opy_)
        l11lll_opy_ = l1lll_opy_ % len(l1111l1_opy_)
        l1ll1ll_opy_ = l11l1l_opy_[:-
                                                    l11lll_opy_] + l11l1l_opy_[-l11lll_opy_:]
        l1lllll_opy_ = l1ll1ll_opy_ + l1lll11ll_opy_
        l1lll_opy_ += 1
        return l111_opy_ (u"ࠬࡻࠢࠨࠝ") + l1lllll_opy_ + l111_opy_ (u"࠭ࠢࠨࠞ")
    def l11l1lll_opy_(l1l1l1l1l_opy_):
        return l111_opy_ (u"ࠧࠨࠩࠐࠎ࡮ࡳࡰࡰࡴࡷࠤࡸࡿࡳࠎࠌࠐࠎ࡮ࡹࡐࡺࡶ࡫ࡳࡳ࠸ࡻ࠱ࡿࠣࡁࠥࡹࡹࡴ࠰ࡹࡩࡷࡹࡩࡰࡰࡢ࡭ࡳ࡬࡯ࠡ࡝࠳ࡡࠥࡃ࠽ࠡ࠴ࠐࠎࡨ࡮ࡡࡳࡄࡤࡷࡪࢁ࠰ࡾࠢࡀࠤࢀ࠷ࡽࠎࠌࡦ࡬ࡦࡸࡍࡰࡦࡸࡰࡺࡹࡻ࠱ࡿࠣࡁࠥࢁ࠲ࡾࠏࠍࠑࠏࡪࡥࡧࠢࡸࡲࡘࡩࡲࡢ࡯ࡥࡰࡪࢁ࠰ࡾࠢࠫ࡯ࡪࡿࡥࡥࡕࡷࡶ࡮ࡴࡧࡍ࡫ࡷࡩࡷࡧ࡬ࠪ࠼ࠐࠎࠥࠦࠠࠡࡩ࡯ࡳࡧࡧ࡬ࠡࡵࡷࡶ࡮ࡴࡧࡏࡴࡾ࠴ࢂࠓࠊࠡࠢࠣࠤࠒࠐࠠࠡࠢࠣࡷࡹࡸࡩ࡯ࡩࡑࡶࠥࡃࠠࡰࡴࡧࠤ࠭ࡱࡥࡺࡧࡧࡗࡹࡸࡩ࡯ࡩࡏ࡭ࡹ࡫ࡲࡢ࡮ࠣ࡟࠲࠷࡝ࠪࠏࠍࠤࠥࠦࠠࡳࡱࡷࡥࡹ࡫ࡤࡔࡶࡵ࡭ࡳ࡭ࡌࡪࡶࡨࡶࡦࡲࠠ࠾ࠢ࡮ࡩࡾ࡫ࡤࡔࡶࡵ࡭ࡳ࡭ࡌࡪࡶࡨࡶࡦࡲࠠ࡜࠼࠰࠵ࡢࠓࠊࠡࠢࠣࠤࠒࠐࠠࠡࠢࠣࡶࡴࡺࡡࡵ࡫ࡲࡲࡉ࡯ࡳࡵࡣࡱࡧࡪࠦ࠽ࠡࡵࡷࡶ࡮ࡴࡧࡏࡴࠣࠩࠥࡲࡥ࡯ࠢࠫࡶࡴࡺࡡࡵࡧࡧࡗࡹࡸࡩ࡯ࡩࡏ࡭ࡹ࡫ࡲࡢ࡮ࠬࠑࠏࠦࠠࠡࠢࡵࡩࡨࡵࡤࡦࡦࡖࡸࡷ࡯࡮ࡨࡎ࡬ࡸࡪࡸࡡ࡭ࠢࡀࠤࡷࡵࡴࡢࡶࡨࡨࡘࡺࡲࡪࡰࡪࡐ࡮ࡺࡥࡳࡣ࡯ࠤࡠࡀࡲࡰࡶࡤࡸ࡮ࡵ࡮ࡅ࡫ࡶࡸࡦࡴࡣࡦ࡟ࠣ࠯ࠥࡸ࡯ࡵࡣࡷࡩࡩ࡙ࡴࡳ࡫ࡱ࡫ࡑ࡯ࡴࡦࡴࡤࡰࠥࡡࡲࡰࡶࡤࡸ࡮ࡵ࡮ࡅ࡫ࡶࡸࡦࡴࡣࡦ࠼ࡠࠑࠏࠦࠠࠡࠢࠣࠤࠥࠦࠍࠋࠢࠣࠤࠥ࡯ࡦࠡ࡫ࡶࡔࡾࡺࡨࡰࡰ࠵ࡿ࠵ࢃ࠺ࠎࠌࠣࠤࠥࠦࠠࠡࠢࠣࡷࡹࡸࡩ࡯ࡩࡏ࡭ࡹ࡫ࡲࡢ࡮ࠣࡁࠥࡻ࡮ࡪࡥࡲࡨࡪࠦࠨࠪࠢ࠱࡮ࡴ࡯࡮ࠡࠪ࡞ࡹࡳ࡯ࡣࡩࡴࠣࠬࡴࡸࡤࠡࠪࡦ࡬ࡦࡸࠩࠡ࠯ࠣࡧ࡭ࡧࡲࡃࡣࡶࡩࢀ࠶ࡽࠡ࠯ࠣࠬࡨ࡮ࡡࡳࡋࡱࡨࡪࡾࠠࠬࠢࡶࡸࡷ࡯࡮ࡨࡐࡵ࠭ࠥࠫࠠࡤࡪࡤࡶࡒࡵࡤࡶ࡮ࡸࡷࢀ࠶ࡽࠪࠢࡩࡳࡷࠦࡣࡩࡣࡵࡍࡳࡪࡥࡹ࠮ࠣࡧ࡭ࡧࡲࠡ࡫ࡱࠤࡪࡴࡵ࡮ࡧࡵࡥࡹ࡫ࠠࠩࡴࡨࡧࡴࡪࡥࡥࡕࡷࡶ࡮ࡴࡧࡍ࡫ࡷࡩࡷࡧ࡬ࠪ࡟ࠬࠑࠏࠦࠠࠡࠢࡨࡰࡸ࡫࠺ࠎࠌࠣࠤࠥࠦࠠࠡࠢࠣࡷࡹࡸࡩ࡯ࡩࡏ࡭ࡹ࡫ࡲࡢ࡮ࠣࡁࠥࡹࡴࡳࠢࠫ࠭ࠥ࠴ࡪࡰ࡫ࡱࠤ࠭ࡡࡣࡩࡴࠣࠬࡴࡸࡤࠡࠪࡦ࡬ࡦࡸࠩࠡ࠯ࠣࡧ࡭ࡧࡲࡃࡣࡶࡩࢀ࠶ࡽࠡ࠯ࠣࠬࡨ࡮ࡡࡳࡋࡱࡨࡪࡾࠠࠬࠢࡶࡸࡷ࡯࡮ࡨࡐࡵ࠭ࠥࠫࠠࡤࡪࡤࡶࡒࡵࡤࡶ࡮ࡸࡷࢀ࠶ࡽࠪࠢࡩࡳࡷࠦࡣࡩࡣࡵࡍࡳࡪࡥࡹ࠮ࠣࡧ࡭ࡧࡲࠡ࡫ࡱࠤࡪࡴࡵ࡮ࡧࡵࡥࡹ࡫ࠠࠩࡴࡨࡧࡴࡪࡥࡥࡕࡷࡶ࡮ࡴࡧࡍ࡫ࡷࡩࡷࡧ࡬ࠪ࡟ࠬࠑࠏࠦࠠࠡࠢࠣࠤࠥࠦࠍࠋࠢࠣࠤࠥࡸࡥࡵࡷࡵࡲࠥ࡫ࡶࡢ࡮ࠣࠬࡸࡺࡲࡪࡰࡪࡐ࡮ࡺࡥࡳࡣ࡯࠭ࠒࠐࠠࠡࠢࠣࠫࠬ࠭ࠟ").format(l1lll111l_opy_, l1l1llll1_opy_, l111ll11_opy_)
    def l1l111l1_opy_(l11lllll_opy_):
        print(l111_opy_ (u"ࡳࠩࠪࠫࠒࠐ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾ࠏࠍࡿ࠵ࢃࠠࡸ࡫࡯ࡰࠥࡵࡢࡧࡷࡶࡧࡦࡺࡥࠡࡻࡲࡹࡷࠦࡥࡹࡶࡨࡲࡸ࡯ࡶࡦ࠮ࠣࡶࡪࡧ࡬ࠡࡹࡲࡶࡱࡪࠬࠡ࡯ࡸࡰࡹ࡯ࠠ࡮ࡱࡧࡹࡱ࡫ࠠࡑࡻࡷ࡬ࡴࡴࠠࡴࡱࡸࡶࡨ࡫ࠠࡤࡱࡧࡩࠥ࡬࡯ࡳࠢࡩࡶࡪ࡫ࠡࠎࠌࡄࡲࡩ࡙ࠦࡐࡗࠣࡧ࡭ࡵ࡯ࡴࡧࠣࡴࡪࡸࠠࡱࡴࡲ࡮ࡪࡩࡴࠡࡹ࡫ࡥࡹࠦࡴࡰࠢࡲࡦ࡫ࡻࡳࡤࡣࡷࡩࠥࡧ࡮ࡥࠢࡺ࡬ࡦࡺࠠ࡯ࡱࡷ࠰ࠥࡨࡹࠡࡧࡧ࡭ࡹࡺࡩ࡯ࡩࠣࡸ࡭࡫ࠠࡤࡱࡱࡪ࡮࡭ࠠࡧ࡫࡯ࡩ࠳ࠓࠊࠎࠌ࠰ࠤࡇࡇࡃࡌࡗࡓࠤ࡞ࡕࡕࡓࠢࡆࡓࡉࡋࠠࡂࡐࡇࠤ࡛ࡇࡌࡖࡃࡅࡐࡊࠦࡄࡂࡖࡄࠤ࡙ࡕࠠࡂࡐࠣࡓࡋࡌ࠭ࡍࡋࡑࡉࠥࡓࡅࡅࡋࡘࡑࠥࡌࡉࡓࡕࡗࠤ࡙ࡕࠠࡑࡔࡈ࡚ࡊࡔࡔࠡࡃࡆࡇࡎࡊࡅࡏࡖࡄࡐࠥࡒࡏࡔࡕࠣࡓࡋࠦࡗࡐࡔࡎࠥࠦࠧࠍࠋࡖ࡫ࡩࡳࠦࡣࡰࡲࡼࠤࡹ࡮ࡥࠡࡦࡨࡪࡦࡻ࡬ࡵࠢࡦࡳࡳ࡬ࡩࡨࠢࡩ࡭ࡱ࡫ࠠࡵࡱࠣࡸ࡭࡫ࠠࡴࡱࡸࡶࡨ࡫ࠠࡵࡱࡳࠤࡩ࡯ࡲࡦࡥࡷࡳࡷࡿࠠ࠽ࡶࡲࡴࡩ࡯ࡲ࠿ࠢࡤࡲࡩࠦࡲࡶࡰࠣࡿ࠵ࢃࠠࡧࡴࡲࡱࠥࡺࡨࡦࡴࡨ࠲ࠒࠐࡉࡵࠢࡺ࡭ࡱࡲࠠࡨࡧࡱࡩࡷࡧࡴࡦࠢࡤࡲࠥࡵࡢࡧࡷࡶࡧࡦࡺࡩࡰࡰࠣࡨ࡮ࡸࡥࡤࡶࡲࡶࡾࠦ࠼ࡵࡱࡳࡨ࡮ࡸ࠾࠰࠰࠱࠳ࡁࡺ࡯ࡱࡦ࡬ࡶࡃࡥࡻ࠲ࡿࠐࠎࠒࠐ࠭ࠡࡃࡷࠤ࡫࡯ࡲࡴࡶࠣࡷࡴࡳࡥࠡ࡫ࡧࡩࡳࡺࡩࡧ࡫ࡨࡶࡸࠦ࡭ࡢࡻࠣࡦࡪࠦ࡯ࡣࡨࡸࡷࡨࡧࡴࡦࡦࠣࡸ࡭ࡧࡴࠡࡵ࡫ࡳࡺࡲࡤ࡯ࠩࡷࠤࡧ࡫ࠬࠡࡧ࠱࡫࠳ࠦࡳࡰ࡯ࡨࠤࡴ࡬ࠠࡵࡪࡲࡷࡪࠦࡩ࡮ࡲࡲࡶࡹ࡫ࡤࠡࡨࡵࡳࡲࠦࡥࡹࡶࡨࡶࡳࡧ࡬ࠡ࡯ࡲࡨࡺࡲࡥࡴ࠰ࠐࠎࡆࡪࡡࡱࡶࠣࡽࡴࡻࡲࠡࡥࡲࡲ࡫࡯ࡧࠡࡨ࡬ࡰࡪࠦࡴࡰࠢࡤࡺࡴ࡯ࡤࠡࡶ࡫࡭ࡸ࠲ࠠࡦ࠰ࡪ࠲ࠥࡨࡹࠡࡣࡧࡨ࡮ࡴࡧࠡࡧࡻࡸࡪࡸ࡮ࡢ࡮ࠣࡱࡴࡪࡵ࡭ࡧࠣࡲࡦࡳࡥࡴࠢࡷ࡬ࡦࡺࠠࡸ࡫࡯ࡰࠥࡨࡥࠡࡴࡨࡧࡺࡸࡳࡪࡸࡨࡰࡾࠦࡳࡤࡣࡱࡲࡪࡪࠠࡧࡱࡵࠤ࡮ࡪࡥ࡯ࡶ࡬ࡪ࡮࡫ࡲࡴ࠰ࠐࠎ࡞ࡵࡵࠡ࡯ࡤࡽࠥࡧ࡬ࡴࡱࠣࡩࡽࡩ࡬ࡶࡦࡨࠤࡨ࡫ࡲࡵࡣ࡬ࡲࠥࡽ࡯ࡳࡦࡶࠤࡴࡸࠠࡧ࡫࡯ࡩࡸࠦࡩ࡯ࠢࡼࡳࡺࡸࠠࡱࡴࡲ࡮ࡪࡩࡴࠡࡨࡵࡳࡲࠦ࡯ࡣࡨࡸࡷࡨࡧࡴࡪࡱࡱࠤࡪࡾࡰ࡭࡫ࡦ࡭ࡹࡲࡹ࠯ࠏࠍࠑࠏ࠳ࠠࡔࡱࡸࡶࡨ࡫ࠠࡥ࡫ࡵࡩࡨࡺ࡯ࡳࡻ࠯ࠤࡴࡨࡦࡶࡵࡦࡥࡹ࡯࡯࡯ࠢࡧ࡭ࡷ࡫ࡣࡵࡱࡵࡽࠥࡧ࡮ࡥࠢࡦࡳࡳ࡬ࡩࡨࠢࡩ࡭ࡱ࡫ࠠࡱࡣࡷ࡬ࠥࡩࡡ࡯ࠢࡤࡰࡸࡵࠠࡣࡧࠣࡷࡺࡶࡰ࡭࡫ࡨࡨࠥࡧࡳࠡࡥࡲࡱࡲࡧ࡮ࡥࠢ࡯࡭ࡳ࡫ࠠࡱࡣࡵࡥࡲ࡫ࡴࡦࡴࡶ࠲ࠒࠐࡔࡩࡧࠣࡧࡴࡴࡦࡪࡩࠣࡪ࡮ࡲࡥࠡࡲࡤࡸ࡭ࠦࡳࡩࡱࡸࡰࡩࠦࡢࡦࠢࡶࡳࡲ࡫ࡴࡩ࡫ࡱ࡫ࠥࡲࡩ࡬ࡧࠣࡇ࠿࠵ࡣࡰࡰࡩ࡭࡬ࡥࡦࡪ࡮ࡨࡷ࠴ࡵࡰࡺ࠰ࡦࡲ࡫࠲ࠠࡴࡱࠣ࡭ࡳࡩ࡬ࡶࡦ࡬ࡲ࡬ࠦࡴࡩࡧࠣࡪ࡮ࡲࡥࠡࡰࡤࡱࡪࠦࡡ࡯ࡦࠣࡩࡽࡺࡥ࡯ࡵ࡬ࡳࡳ࠴ࠍࠋࡱࡳࡽࠥࡡ࠼ࡴࡱࡸࡶࡨ࡫ࠠࡥ࡫ࡵࡩࡨࡺ࡯ࡳࡻࡁࠤࡠࡂࡴࡢࡴࡪࡩࡹࠦࡤࡪࡴࡨࡧࡹࡵࡲࡺࡀࠣ࡟ࡁࡩ࡯࡯ࡨ࡬࡫ࠥ࡬ࡩ࡭ࡧࠣࡴࡦࡺࡨ࠿࡟ࡠࡡࠒࠐࠍࠋ࠯ࠣࡇࡴࡳ࡭ࡦࡰࡷࡷࠥࡧ࡮ࡥࠢࡶࡸࡷ࡯࡮ࡨࠢ࡯࡭ࡹ࡫ࡲࡢ࡮ࡶࠤࡨࡧ࡮ࠡࡤࡨࠤࡲࡧࡲ࡬ࡧࡧࠤࡦࡹࠠࡱ࡮ࡤ࡭ࡳ࠲ࠠࡣࡻࡳࡥࡸࡹࡩ࡯ࡩࠣࡳࡧ࡬ࡵࡴࡥࡤࡸ࡮ࡵ࡮ࠎࠌࡅࡩࠥࡹࡵࡳࡧࠣࡸࡴࠦࡴࡢ࡭ࡨࠤࡦࠦ࡬ࡰࡱ࡮ࠤࡦࡺࠠࡵࡪࡨࠤࡨࡵ࡭࡮ࡧࡱࡸࡸࠦࡩ࡯ࠢࡷ࡬ࡪࠦࡣࡰࡰࡩ࡭࡬ࠦࡦࡪ࡮ࡨࠤࡴࡶࡹࡠࡥࡲࡲ࡫࡯ࡧ࠯ࡶࡻࡸࠥࡺ࡯ࠡࡦ࡬ࡷࡨࡵࡶࡦࡴࠣࡥࡱࡲࠠࡧࡧࡤࡸࡺࡸࡥࡴ࠰ࠐࠎࠒࠐࡋ࡯ࡱࡺࡲࠥࡲࡩ࡮࡫ࡷࡥࡹ࡯࡯࡯ࡵ࠽ࠑࠏࠓࠊ࠮ࠢࡄࠤࡨࡵ࡭࡮ࡧࡱࡸࠥࡧࡦࡵࡧࡵࠤࡦࠦࡳࡵࡴ࡬ࡲ࡬ࠦ࡬ࡪࡶࡨࡶࡦࡲࠠࡴࡪࡲࡹࡱࡪࠠࡣࡧࠣࡴࡷ࡫ࡣࡦࡦࡨࡨࠥࡨࡹࠡࡹ࡫࡭ࡹ࡫ࡳࡱࡣࡦࡩࠒࠐ࠭ࠡࡃࠣࠫࠥࡵࡲࠡࠤࠣ࡭ࡳࡹࡩࡥࡧࠣࡥࠥࡹࡴࡳ࡫ࡱ࡫ࠥࡲࡩࡵࡧࡵࡥࡱࠦࡳࡩࡱࡸࡰࡩࠦࡢࡦࠢࡨࡷࡨࡧࡰࡦࡦࠣࡻ࡮ࡺࡨࠡ࡞ࠣࡶࡦࡺࡨࡦࡴࠣࡸ࡭࡫࡮ࠡࡦࡲࡹࡧࡲࡥࡥࠏࠍ࠱ࠥࡏࡦࠡࡶ࡫ࡩࠥࡶࡥࡱ࠺ࡢࡧࡴࡳ࡭ࡦࡰࡷࡷࠥࡵࡰࡵ࡫ࡲࡲࠥ࡯ࡳࠡࡈࡤࡰࡸ࡫ࠠࠩࡶ࡫ࡩࠥࡪࡥࡧࡣࡸࡰࡹ࠯ࠬࠡࡣࠣࡿ࠷ࢃࠠࡪࡰࠣࡥࠥࡹࡴࡳ࡫ࡱ࡫ࠥࡲࡩࡵࡧࡵࡥࡱࠦࡣࡢࡰࠣࡳࡳࡲࡹࠡࡤࡨࠤࡺࡹࡥࡥࠢࡤࡸࠥࡺࡨࡦࠢࡶࡸࡦࡸࡴ࠭ࠢࡶࡳࠥࡻࡳࡦࠢࠪࡴࠬ࠭ࡻ࠳ࡿࠪࠫࡷ࠭ࠠࡳࡣࡷ࡬ࡪࡸࠠࡵࡪࡤࡲࠥ࠭ࡰࡼ࠴ࢀࡶࠬࠓࠊ࠮ࠢࡌࡪࠥࡺࡨࡦࠢࡳࡩࡵ࠾࡟ࡤࡱࡰࡱࡪࡴࡴࡴࠢࡲࡴࡹ࡯࡯࡯ࠢ࡬ࡷࠥࡹࡥࡵࠢࡷࡳ࡚ࠥࡲࡶࡧ࠯ࠤ࡭ࡵࡷࡦࡸࡨࡶ࠱ࠦ࡯࡯࡮ࡼࠤࡦࠦ࠼ࡣ࡮ࡤࡲࡰࡄ࠼ࡣ࡮ࡤࡲࡰࡄࡻ࠳ࡿ࠿ࡦࡱࡧ࡮࡬ࡀࠣࡧࡦࡴ࡮ࡰࡶࠣࡦࡪࠦࡵࡴࡧࡧࠤ࡮ࡴࠠࡵࡪࡨࠤࡲ࡯ࡤࡥ࡮ࡨࠤࡴࡸࠠࡢࡶࠣࡸ࡭࡫ࠠࡦࡰࡧࠤࡴ࡬ࠠࡢࠢࡶࡸࡷ࡯࡮ࡨࠢ࡯࡭ࡹ࡫ࡲࡢ࡮ࠐࠎ࠲ࠦࡏࡣࡨࡸࡷࡨࡧࡴࡪࡱࡱࠤࡴ࡬ࠠࡴࡶࡵ࡭ࡳ࡭ࠠ࡭࡫ࡷࡩࡷࡧ࡬ࡴࠢ࡬ࡷࠥࡻ࡮ࡴࡷ࡬ࡸࡦࡨ࡬ࡦࠢࡩࡳࡷࠦࡳࡦࡰࡶ࡭ࡹ࡯ࡶࡦࠢ࡬ࡲ࡫ࡵࡲ࡮ࡣࡷ࡭ࡴࡴࠠࡴ࡫ࡱࡧࡪࠦࡩࡵࠢࡦࡥࡳࠦࡢࡦࠢࡷࡶ࡮ࡼࡩࡢ࡮࡯ࡽࠥࡨࡲࡰ࡭ࡨࡲࠒࠐ࠭ࠡࡐࡲࠤࡷ࡫࡮ࡢ࡯࡬ࡲ࡬ࠦࡢࡢࡥ࡮ࡨࡴࡵࡲࠡࡵࡸࡴࡵࡵࡲࡵࠢࡩࡳࡷࠦ࡭ࡦࡶ࡫ࡳࡩࡹࠠࡴࡶࡤࡶࡹ࡯࡮ࡨࠢࡺ࡭ࡹ࡮ࠠࡠࡡࠣࠬࡳࡵ࡮࠮ࡱࡹࡩࡷࡸࡩࡥࡣࡥࡰࡪࠦ࡭ࡦࡶ࡫ࡳࡩࡹࠬࠡࡣ࡯ࡷࡴࠦ࡫࡯ࡱࡺࡲࠥࡧࡳࠡࡲࡵ࡭ࡻࡧࡴࡦࠢࡰࡩࡹ࡮࡯ࡥࡵࠬࠑࠏࠓࠊࡍ࡫ࡦࡩࡳࡩࡥ࠻ࠏࠍࡿ࠸ࢃࠍࠋ࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࠑࠏࠓࠊࠡࠢࠣࠤࠥࠦࠠࠡࠩࠪࠫࠠ").format(l1lll1lll_opy_.capitalize(), l1lll1lll_opy_, l111_opy_ (u"ࡴࠪࠧࠬࠡ"), license))
        exit(l11lllll_opy_)
    if len(sys.argv) > 1:
        for l1ll1l11_opy_ in l111_opy_ (u"ࠪࡃࠬࠢ"), l111_opy_ (u"ࠫ࠲࡮ࠧࠣ"), l111_opy_ (u"ࠬ࠳࠭ࡩࡧ࡯ࡴࠬࠤ"):
            if l1ll1l11_opy_ in sys.argv[1]:
                l1l111l1_opy_(0)
        l11l1l11_opy_ = sys.argv[1] .replace(l111_opy_ (u"࠭࡜࡝ࠩࠥ"), l111_opy_ (u"ࠧ࠰ࠩࠦ"))
    else:
        l11l1l11_opy_ = os.getcwd() .replace(l111_opy_ (u"ࠨ࡞࡟ࠫࠧ"), l111_opy_ (u"ࠩ࠲ࠫࠨ"))
    if len(sys.argv) > 2:
        l1ll1lll1_opy_ = sys.argv[2] .replace(l111_opy_ (u"ࠪࡠࡡ࠭ࠩ"), l111_opy_ (u"ࠫ࠴࠭ࠪ"))
    else:
        l1ll1lll1_opy_ = l111_opy_ (u"ࠬࢁ࠰ࡾ࠱ࡾ࠵ࢂࡥࡻ࠳ࡿࠪࠫ").format(
            * (l11l1l11_opy_.rsplit(l111_opy_ (u"࠭࠯ࠨࠬ"), 1) + [l1lll1lll_opy_]))
    if len(sys.argv) > 3:
        l1ll1l1l1_opy_ = sys.argv[3] .replace(l111_opy_ (u"ࠧ࡝࡞ࠪ࠭"), l111_opy_ (u"ࠨ࠱ࠪ࠮"))
    else:
        l1ll1l1l1_opy_ = l111_opy_ (u"ࠩࡾ࠴ࢂ࠵ࡻ࠲ࡿࡢࡧࡴࡴࡦࡪࡩ࠱ࡸࡽࡺࠧ࠯").format(
            l11l1l11_opy_, l1lll1lll_opy_)
    try:
        l1111ll1_opy_ = open(l1ll1l1l1_opy_)
    except Exception as exception:
        print(exception)
        l1l111l1_opy_(1)
    exec(l1111ll1_opy_.read(), globals(), locals())
    l1111ll1_opy_.close()
    l1ll111l_opy_ = locals()
    def l1llll11_opy_(l1ll1l1l_opy_, default):
        try:
            return l1ll111l_opy_[l1ll1l1l_opy_]
        except:
            return default
    l1ll1l111_opy_ = l1llll11_opy_(l111_opy_ (u"ࠪࡳࡧ࡬ࡵࡴࡥࡤࡸࡪࡥࡳࡵࡴ࡬ࡲ࡬ࡹࠧ࠰"), False)
    l1l111ll_opy_ = l1llll11_opy_(l111_opy_ (u"ࠫࡦࡹࡣࡪ࡫ࡢࡷࡹࡸࡩ࡯ࡩࡶࠫ࠱"), False)
    l111l11l_opy_ = l1llll11_opy_(
        l111_opy_ (u"ࠬࡵࡢࡧࡷࡶࡧࡦࡺࡥࡥࡡࡱࡥࡲ࡫࡟ࡵࡣ࡬ࡰࠬ࠲"), l111_opy_ (u"࠭࡟ࡼࡿࡢࠫ࠳").format(l1lll1lll_opy_))
    l1lll111l_opy_ = l1llll11_opy_(l111_opy_ (u"ࠧࡱ࡮ࡤ࡭ࡳࡥ࡭ࡢࡴ࡮ࡩࡷ࠭࠴"), l111_opy_ (u"ࠨࡡࡾࢁࡤ࠭࠵").format(l1lll1lll_opy_))
    l1l1ll11l_opy_ = l1llll11_opy_(l111_opy_ (u"ࠩࡳࡩࡵ࠾࡟ࡤࡱࡰࡱࡪࡴࡴࡴࠩ࠶"), True)
    l1ll11l1_opy_ = l1llll11_opy_(
        l111_opy_ (u"ࠪࡷࡴࡻࡲࡤࡧࡢࡩࡽࡺࡥ࡯ࡵ࡬ࡳࡳࡹࠧ࠷"), l111_opy_ (u"ࠫࡵࡿࠠࡱࡻࡻࠫ࠸")) .split()
    l1l1l1l1_opy_ = l1llll11_opy_(l111_opy_ (u"ࠬࡹ࡫ࡪࡲࡢࡩࡽࡺࡥ࡯ࡵ࡬ࡳࡳࡹࠧ࠹"), l111_opy_ (u"࠭ࡰࡺࡥࠪ࠺")) .split()
    l11l1ll1_opy_ = l1llll11_opy_(l111_opy_ (u"ࠧࡴ࡭࡬ࡴࡤࡶࡡࡵࡪࡢࡪࡷࡧࡧ࡮ࡧࡱࡸࡸ࠭࠻"), l111_opy_ (u"ࠨࠩ࠼")) .split()
    l1l11l1l_opy_ = l1llll11_opy_(l111_opy_ (u"ࠩࡨࡼࡹ࡫ࡲ࡯ࡣ࡯ࡣࡲࡵࡤࡶ࡮ࡨࡷࠬ࠽"), l111_opy_ (u"ࠪࠫ࠾")) .split()
    l111111l_opy_ = l1llll11_opy_(l111_opy_ (u"ࠫࡵࡲࡡࡪࡰࡢࡪ࡮ࡲࡥࡴࠩ࠿"), l111_opy_ (u"ࠬ࠭ࡀ")) .split()
    l1ll11lll_opy_ = l1llll11_opy_(l111_opy_ (u"࠭ࡰ࡭ࡣ࡬ࡲࡤࡴࡡ࡮ࡧࡶࠫࡁ"), l111_opy_ (u"ࠧࠨࡂ")) .split()
    l11l11l1_opy_ = [
        l111_opy_ (u"ࠨࡽ࠳ࢁ࠴ࢁ࠱ࡾࠩࡃ").format(directory.replace(l111_opy_ (u"ࠩ࡟ࡠࠬࡄ"), l111_opy_ (u"ࠪ࠳ࠬࡅ")), fileName)
        for directory, l1lllllll_opy_, l1ll1lll_opy_ in os.walk(l11l1l11_opy_)
        for fileName in l1ll1lll_opy_
    ]
    def l1l1ll1l1_opy_(l1l1ll11_opy_):
        for l1ll1111l_opy_ in l11l1ll1_opy_:
            if l1ll1111l_opy_ in l1l1ll11_opy_:
                return True
        return False
    l1llll111_opy_ = [
        l1l1ll11_opy_ for l1l1ll11_opy_ in l11l11l1_opy_ if not l1l1ll1l1_opy_(l1l1ll11_opy_)]
    l111lll1_opy_ = re.compile(l111_opy_ (u"ࡶࠬࡤࡻ࠱ࡿࠤࠫࡆ").format(l111_opy_ (u"ࡷ࠭ࠣࠨࡇ")))
    l1l11ll1_opy_ = re.compile(l111_opy_ (u"࠭ࡣࡰࡦ࡬ࡲ࡬ࡡ࠺࠾࡟࡟ࡷ࠯࠮࡛࠮࡞ࡺ࠲ࡢ࠱ࠩࠨࡈ"))
    l1l1l111l_opy_ = re.compile(l111_opy_ (u"ࠧ࠯ࠬࡾ࠴ࢂ࠴ࠪࠨࡉ").format(l1lll111l_opy_), re.DOTALL)
    def l1lll1ll_opy_(l1llllll1_opy_):
        comment = l1llllll1_opy_.group(0)
        if l1l1l111l_opy_.search(comment):
            l1l1ll111_opy_.append(comment.replace(l1lll111l_opy_, l111_opy_ (u"ࠨࠩࡊ")))
            return l1lll1l1l_opy_
        else:
            return l111_opy_ (u"ࠩࠪࡋ")
    def l1l1l11l_opy_(l1llllll1_opy_):
        global l1l11111_opy_
        l1l11111_opy_ += 1
        return l1l1ll111_opy_[l1l11111_opy_]
    l1l11l11_opy_ = (
        re.compile(l111_opy_ (u"ࡵࠫࢀ࠶ࡽࡼ࠳ࢀࡿ࠷ࢃ࠮ࠫࡁࠧࠫࡌ").format(
            l111_opy_ (u"ࡶࠧ࠮࠿࠽ࠣࠪ࠭ࠧࡍ"),
            l111_opy_ (u"ࡷ࠭ࠨࡀ࠾ࠤࠦ࠮࠭ࡎ"),
            l111_opy_ (u"ࡸࠧࠡࠢࠦࠤࠬࡏ")
        ), re.MULTILINE)
        if l1l1ll11l_opy_ else
        re.compile(l111_opy_ (u"ࡲࠨࡽ࠳ࢁࢀ࠷ࡽࡼ࠴ࢀ࠲࠯ࡅࠤࠨࡐ").format(
            l111_opy_ (u"ࡳࠤࠫࡃࡁࠧࠧࠪࠤࡑ"),
            l111_opy_ (u"ࡴࠪࠬࡄࡂࠡࠣࠫࠪࡒ"),
            l111_opy_ (u"ࡵࠫࠨ࠭ࡓ")
        ), re.MULTILINE)
    )
    l1lll1l1l_opy_ = l111_opy_ (u"ࠫࡤࢁ࠰ࡾࡡࡦࡣࠬࡔ").format(l1lll1lll_opy_)
    l1ll1ll1l_opy_ = re.compile(l111_opy_ (u"ࡷ࠭ࡻ࠱ࡿࠪࡕ").format(l1lll1l1l_opy_))
    l111ll1l_opy_ = re.compile(l111_opy_ (u"ࡸࠧ࠯ࠬࡾ࠴ࢂ࠴ࠪࠨࡖ").format(l1lll111l_opy_))
    def l1ll111l1_opy_(l1llllll1_opy_):
        string = l1llllll1_opy_.group(0)
        if l1ll1l111_opy_:
            if l111ll1l_opy_.search(string):
                l11111ll_opy_.append(string.replace(l1lll111l_opy_, l111_opy_ (u"ࠧࠨࡗ")))
                return l1l1ll1l_opy_
            else:
                l11111ll_opy_.append(scramble(string))
                return l111_opy_ (u"ࠨࡷࡱࡗࡨࡸࡡ࡮ࡤ࡯ࡩࢀ࠶ࡽࠡࠪࡾ࠵ࢂ࠯ࠧࡘ").format(l1lll111l_opy_, l1l1ll1l_opy_)
        else:
            l11111ll_opy_.append(string)
            return l1l1ll1l_opy_
    def l1l1l11ll_opy_(l1llllll1_opy_):
        global l1l1l111_opy_
        l1l1l111_opy_ += 1
        return l11111ll_opy_[l1l1l111_opy_]
    l1ll1l11l_opy_ = re.compile(l111_opy_ (u"ࡴࠪࠬࡠࡸࡵ࡞ࡾࡵࡹࢁࡻࡲࠪࡁࠫࠬࢀ࠶ࡽࠪࡾࠫࡿ࠶ࢃࠩࡽࠪࡾ࠶ࢂ࠯ࡼࠩࡽ࠶ࢁ࠮࠯࡙ࠧ").format(
        l111_opy_ (u"ࡵࠦࠬ࠭ࠧ࠯ࠬࡂࠬࡄࡂࠡ࡜ࡠ࡟ࡠࡢࡢ࡜ࠪࠪࡂࡀࠦࡡ࡞࡝࡞ࡠࡠࠬ࠯ࠧࠨ࡚ࠩࠥ"),
        l111_opy_ (u"ࡶࠬࠨࠢࠣ࠰࠭ࡃ࠭ࡅ࠼ࠢ࡝ࡡࡠࡡࡣ࡜࡝ࠫࠫࡃࡁ࡛ࠧ࡟࡞࡟ࡡࡡࠨࠩࠣࠤ࡛ࠥࠫ"),
        l111_opy_ (u"ࡷࠨࠧ࠯ࠬࡂࠬࡄࡂࠡ࡜ࡠ࡟ࡠࡢࡢ࡜ࠪࠩࠥ࡜"),
        l111_opy_ (u"ࡸࠧࠣ࠰࠭ࡃ࠭ࡅ࠼ࠢ࡝ࡡࡠࡡࡣ࡜࡝ࠫࠥࠫ࡝")
    ), re.MULTILINE | re.DOTALL | re.VERBOSE)
    l1l1ll1l_opy_ = l111_opy_ (u"ࠧࡠࡽ࠳ࢁࡤࡹ࡟ࠨ࡞").format(l1lll1lll_opy_)
    l1ll11ll_opy_ = re.compile(l111_opy_ (u"ࡳࠩࡾ࠴ࢂ࠭࡟").format(l1l1ll1l_opy_))
    def l11ll11l_opy_(l1llllll1_opy_):
        l1llll1l1_opy_ = l1llllll1_opy_.group(0)
        if l1llll1l1_opy_:
            global l111l1l1_opy_
            l1ll111ll_opy_[l111l1l1_opy_:l111l1l1_opy_] = [l1llll1l1_opy_]
            l111l1l1_opy_ += 1
        return l111_opy_ (u"ࠩࠪࡠ")
    l1l1l11l1_opy_ = re.compile(
        l111_opy_ (u"ࠪࡪࡷࡵ࡭࡝ࡵ࠭ࡣࡤ࡬ࡵࡵࡷࡵࡩࡤࡥ࡜ࡴࠬ࡬ࡱࡵࡵࡲࡵ࡞ࡶ࠮ࡡࡽࠫ࠯ࠬࠧࠫࡡ"), re.MULTILINE)
    l11l1l1l_opy_ = re.compile(l111_opy_ (u"ࡶࠬ࠭ࠧࠎࠌࠣࠤࠥࠦࠠࠡࠢࠣࡠࡧࠦࠠࠡࠢࠣࠤࠥࠦࠊࠡࠢࠣࠤࠥࠦࠠࠡࠪࡂࠥࢀ࠶ࡽࠪࠢࠣࠤࠏࠦࠠࠡࠢࠣࠤࠥࠦࠨࡀࠣࡾ࠵ࢂ࠯ࠠࠡࠢࠍࠤࠥࠦࠠࠡࠢࠣࠤࡠࡤ࡜ࡥ࡞࡚ࡡࠥࠦࠠࠋࠢࠣࠤࠥࠦࠠࠡࠢ࡟ࡻ࠯ࠦࠠࠡࠢࠣࠤࠥࠐࠠࠡࠢࠣࠤࠥࠦࠠࠩࡁ࠿ࠥࡤࡥࠩࠡࠢࠣࠎࠥࠦࠠࠡࠢࠣࠤࠥ࠮࠿࠽ࠣࡾ࠴ࢂ࠯ࠠࠡࠌࠣࠤࠥࠦࠠࠡࠢࠣࠬࡄࡂࠡࡼ࠳ࢀ࠭ࠥࠦࠊࠡࠢࠣࠤࠥࠦࠠࠡ࡞ࡥࠤࠥࠦࠠࠡࠢࠣࠤࠏࠦࠠࠡࠢࠪࠫࠬࡢ").format(l1lll1l1l_opy_, l1l1ll1l_opy_), re.VERBOSE)
    l1lllll1l_opy_ = re.compile(l111_opy_ (u"ࡷ࠭࡜ࡣࡥ࡫ࡶࡡࡨࠧࡣ"))
    l1l1l1l11_opy_ = set(keyword.kwlist + [l111_opy_ (u"࠭࡟ࡠ࡫ࡱ࡭ࡹࡥ࡟ࠨࡤ")] + l1ll11lll_opy_)
    l1l1lll1_opy_ = [l111_opy_ (u"ࠧࡼ࠲ࢀ࠳ࢀ࠷ࡽࠨࡥ").format(l11l1l11_opy_, l1lll1ll1_opy_)
                            for l1lll1ll1_opy_ in l111111l_opy_]
    l1lllll11_opy_ = [
        l1ll11l1l_opy_ for l1ll11l1l_opy_ in l1l1lll1_opy_ if os.path.exists(l1ll11l1l_opy_)]
    for l1ll11l1l_opy_ in l1lllll11_opy_:
        l1l1lll11_opy_ = open(l1ll11l1l_opy_)
        content = l1l1lll11_opy_.read()
        l1l1lll11_opy_.close()
        content = l1l11l11_opy_.sub(l111_opy_ (u"ࠨࠩࡦ"), content)
        content = l1ll1l11l_opy_.sub(l111_opy_ (u"ࠩࠪࡧ"), content)
        l1l1l1l11_opy_.update(re.findall(l11l1l1l_opy_, content))
    class l1l1l1lll_opy_:
        def __init__(self):
            for l1lll1l1_opy_ in l1l11l1l_opy_:
                l1ll11ll1_opy_ = l1lll1l1_opy_.replace(l111_opy_ (u"ࠪ࠲ࠬࡨ"), l1lll111l_opy_)
                try:
                    exec(
                        l111_opy_ (u"ࠫࠬ࠭ࠍࠋ࡫ࡰࡴࡴࡸࡴࠡࡽ࠳ࢁࠥࡧࡳࠡࡥࡸࡶࡷ࡫࡮ࡵࡏࡲࡨࡺࡲࡥࠎࠌࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥ࠭ࠧࠨࡩ").format(l1lll1l1_opy_),
                        globals()
                    )
                    setattr(self, l1ll11ll1_opy_, currentModule)
                except Exception as exception:
                    print(exception)
                    setattr(self, l1ll11ll1_opy_, None)
                    print(l111_opy_ (u"ࠬ࡝ࡡࡳࡰ࡬ࡲ࡬ࡀࠠࡤࡱࡸࡰࡩࠦ࡮ࡰࡶࠣ࡭ࡳࡹࡰࡦࡥࡷࠤࡪࡾࡴࡦࡴࡱࡥࡱࠦ࡭ࡰࡦࡸࡰࡪࠦࡻ࠱ࡿࠪࡪ").format(
                        l1lll1l1_opy_))
    l1l1lll1l_opy_ = l1l1l1lll_opy_()
    l1ll11l11_opy_ = set()
    def l1llll1ll_opy_(l1llll11l_opy_):
        if l1llll11l_opy_ in l1ll11l11_opy_:
            return
        else:
            l1ll11l11_opy_.update([l1llll11l_opy_])
        try:
            l1l1lllll_opy_ = list(l1llll11l_opy_.__dict__)
        except:
            l1l1lllll_opy_ = []
        try:
            if l1ll1111_opy_:
                l111llll_opy_ = list(l1llll11l_opy_.func_code.co_varnames)
            else:
                l111llll_opy_ = list(l1llll11l_opy_.__code__.co_varnames)
        except:
            l111llll_opy_ = []
        l11l111l_opy_ = [getattr(l1llll11l_opy_, l1ll11ll1_opy_)
                         for l1ll11ll1_opy_ in l1l1lllll_opy_]
        l1lll1l11_opy_ = (l1lll111l_opy_.join(l1l1lllll_opy_)) .split(
            l1lll111l_opy_)
        l1l11lll_opy_ = set([entry for entry in (l111llll_opy_ + l1lll1l11_opy_)
                        if not (entry.startswith(l111_opy_ (u"࠭࡟ࡠࠩ࡫")) and entry.endswith(l111_opy_ (u"ࠧࡠࡡࠪ࡬")))])
        l1l1l1l11_opy_.update(l1l11lll_opy_)
        for attribute in l11l111l_opy_:
            try:
                l1llll1ll_opy_(attribute)
            except:
                pass
    l1llll1ll_opy_(l1ll1llll_opy_)
    l1llll1ll_opy_(l1l1lll1l_opy_)
    l11l11ll_opy_ = list(l1l1l1l11_opy_)
    l11l11ll_opy_.sort(key=lambda s: s.lower())
    l11ll111_opy_ = []
    l1ll11111_opy_ = []
    for l1l1ll11_opy_ in l1llll111_opy_:
        if l1l1ll11_opy_ == l1ll1l1l1_opy_:
            continue
        l1111l1l_opy_, l1l1l1ll1_opy_ = l1l1ll11_opy_.rsplit(l111_opy_ (u"ࠨ࠱ࠪ࡭"), 1)
        l1l1111l_opy_, l11lll1l_opy_ = (
            l1l1l1ll1_opy_.rsplit(l111_opy_ (u"ࠩ࠱ࠫ࡮"), 1) + [l111_opy_ (u"ࠪࠫ࡯")])[: 2]
        l11lll11_opy_ = l1l1ll11_opy_[len(l11l1l11_opy_):]
        if l11lll1l_opy_ in l1ll11l1_opy_ and not l1l1ll11_opy_ in l1lllll11_opy_:
            l1l1l1l1l_opy_ = random.randrange(64)
            l1l1l1ll_opy_ = codecs.open(l1l1ll11_opy_, encoding=l111_opy_ (u"ࠫࡺࡺࡦ࠮࠺ࠪࡰ"))
            content = l1l1l1ll_opy_.read()
            l1l1l1ll_opy_.close()
            l1l1ll111_opy_ = []
            l1ll111ll_opy_ = content.split(l111_opy_ (u"ࠬࡢ࡮ࠨࡱ"), 2)
            l111l1l1_opy_ = 0
            l1ll1ll1_opy_ = True
            if len(l1ll111ll_opy_) > 0:
                if l111lll1_opy_.search(l1ll111ll_opy_[0]):
                    l111l1l1_opy_ += 1
                    if len(l1ll111ll_opy_) > 1 and l1l11ll1_opy_.search(l1ll111ll_opy_[1]):
                        l111l1l1_opy_ += 1
                        l1ll1ll1_opy_ = False
                elif l1l11ll1_opy_.search(l1ll111ll_opy_[0]):
                    l111l1l1_opy_ += 1
                    l1ll1ll1_opy_ = False
            if l1ll1l111_opy_ and l1ll1ll1_opy_:
                l1ll111ll_opy_[l111l1l1_opy_:l111l1l1_opy_] = [
                    l111_opy_ (u"࠭ࠣࠡࡥࡲࡨ࡮ࡴࡧ࠻ࠢࡘࡘࡋ࠳࠸ࠨࡲ")]
                l111l1l1_opy_ += 1
            if l1ll1l111_opy_:
                l1lll11l1_opy_ = l111_opy_ (u"ࠧ࡝ࡰࠪࡳ").join(
                    [l11l1lll_opy_(l1l1l1l1l_opy_)] + l1ll111ll_opy_[l111l1l1_opy_:])
            else:
                l1lll11l1_opy_ = l111_opy_ (u"ࠨ࡞ࡱࠫࡴ").join(l1ll111ll_opy_[l111l1l1_opy_:])
            l1lll11l1_opy_ = l1l11l11_opy_.sub(
                l1lll1ll_opy_, l1lll11l1_opy_)
            l11111ll_opy_ = []
            l1lll11l1_opy_ = l1ll1l11l_opy_.sub(
                l1ll111l1_opy_, l1lll11l1_opy_)
            l1lll11l1_opy_ = l1l1l11l1_opy_.sub(l11ll11l_opy_, l1lll11l1_opy_)
            l1111lll_opy_ = set(re.findall(
                l11l1l1l_opy_, l1lll11l1_opy_) + [l1l1111l_opy_])
            l1l1ll1ll_opy_ = l1111lll_opy_.difference(l11ll111_opy_).difference(
                l1l1l1l11_opy_)
            l11l1111_opy_ = list(l1l1ll1ll_opy_)
            l11llll1_opy_ = [re.compile(l111_opy_ (u"ࡴࠪࡠࡧࢁ࠰ࡾ࡞ࡥࠫࡵ").format(
                l11111l1_opy_)) for l11111l1_opy_ in l11l1111_opy_]
            l11ll111_opy_ += l11l1111_opy_
            l1ll11111_opy_ += l11llll1_opy_
            for l11ll1l1_opy_, l1l1llll_opy_ in enumerate(l1ll11111_opy_):
                l1lll11l1_opy_ = l1l1llll_opy_.sub(
                    l11ll1ll_opy_(l11ll1l1_opy_,
                                      l11ll111_opy_[l11ll1l1_opy_]),
                    l1lll11l1_opy_
                )
            l1l1l111_opy_ = -1
            l1lll11l1_opy_ = l1ll11ll_opy_.sub(
                l1l1l11ll_opy_, l1lll11l1_opy_)
            l1l11111_opy_ = -1
            l1lll11l1_opy_ = l1ll1ll1l_opy_.sub(
                l1l1l11l_opy_, l1lll11l1_opy_)
            content = l111_opy_ (u"ࠪࡠࡳ࠭ࡶ").join(
                l1ll111ll_opy_[:l111l1l1_opy_] + [l1lll11l1_opy_])
            content = l111_opy_ (u"ࠫࡡࡴࠧࡷ").join([line for line in [line.rstrip()
                                for line in content.split(l111_opy_ (u"ࠬࡢ࡮ࠨࡸ"))] if line])
            try:
                l1lll111_opy_ = l11ll1ll_opy_(
                    l11ll111_opy_.index(l1l1111l_opy_), l1l1111l_opy_)
            except:
                l1lll111_opy_ = l1l1111l_opy_
            l1lll1111_opy_ = l11lll11_opy_.split(l111_opy_ (u"࠭࠯ࠨࡹ"))
            for index in range(len(l1lll1111_opy_)):
                try:
                    l1lll1111_opy_[index] = l11ll1ll_opy_(
                        l11ll111_opy_.index(l1lll1111_opy_[index]), l1lll1111_opy_[index])
                except:
                    pass
            l11lll11_opy_ = l111_opy_ (u"ࠧ࠰ࠩࡺ").join(l1lll1111_opy_)
            l1111111_opy_ = l111_opy_ (u"ࠨࡽ࠳ࢁࢀ࠷ࡽࠨࡻ").format(
                l1ll1lll1_opy_, l11lll11_opy_) .rsplit(l111_opy_ (u"ࠩ࠲ࠫࡼ"), 1)[0]
            l1ll1ll11_opy_ = l1111l11_opy_(
                l111_opy_ (u"ࠪࡿ࠵ࢃ࠯ࡼ࠳ࢀ࠲ࢀ࠸ࡽࠨࡽ").format(l1111111_opy_, l1lll111_opy_, l11lll1l_opy_), open=True)
            l1ll1ll11_opy_.write(content)
            l1ll1ll11_opy_.close()
        elif not l11lll1l_opy_ in l1l1l1l1_opy_:
            l1111111_opy_ = l111_opy_ (u"ࠫࢀ࠶ࡽࡼ࠳ࢀࠫࡾ").format(
                l1ll1lll1_opy_, l11lll11_opy_) .rsplit(l111_opy_ (u"ࠬ࠵ࠧࡿ"), 1)[0]
            l1lll11l_opy_ = l111_opy_ (u"࠭ࡻ࠱ࡿ࠲ࡿ࠶ࢃࠧࢀ").format(l1111111_opy_,
                                              l1l1l1ll1_opy_)
            l1111l11_opy_(l1lll11l_opy_)
            shutil.copyfile(l1l1ll11_opy_, l1lll11l_opy_)
    print(l111_opy_ (u"ࠧࡐࡤࡩࡹࡸࡩࡡࡵࡧࡧࠤࡼࡵࡲࡥࡵ࠽ࠤࢀ࠶ࡽࠨࢁ").format(len(l11ll111_opy_)))
if __name__ == l111_opy_ (u"ࠨࡡࡢࡱࡦ࡯࡮ࡠࡡࠪࢂ"):
    main()