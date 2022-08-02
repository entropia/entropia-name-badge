import nvs
import sys
from display import *

nickname = nvs.nvs_getstr("owner","nickname")
APP_PATH = "/".join(__file__.split("/")[:-1])
sys.path.append(APP_PATH)
teebeutel = "teebeutel.png"

drawFill(0xFFFFFF)
drawPng(0,0,"%s/%s"% (APP_PATH, teebeutel))

nick_w = getTextWidth(nickname)
nick_h = getTextHeight(nickname)

scaling = 1.15 * width() // nick_w

translate( width() // 2 , height() // 2 - 20)
rotate(0.15)
scale(scaling,scaling)
drawText( -nick_w // 2, -nick_h // 2, nickname)

flush()
