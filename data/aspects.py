"""
Copyright [2022-2023] Victor C Hall

Licensed under the GNU Affero General Public License;
You may not use this code except in compliance with the License.
You may obtain a copy of the License at

    https://www.gnu.org/licenses/agpl-3.0.en.html

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""
from typing import Tuple

"""
Notes:
this is generated from an excel sheet and actual ratios are hand picked to 
spread out the ratios evenly to avoid having super-finely defined buckets
Too many buckets means more "runt" steps with repeated images to fill batch than necessary
ex. we do not need both 1.0:1 and 1.125:1, they're almost identical ratios
Try to keep around <20 ratio buckets per resolution, should be plenty coverage everything between 1:1 and 4:1
More finely defined buckets will reduce cropping at the expense of more runt steps
"""

ASPECTS_1536 = [[1536,1536],   # 2359296 1:1
    [1728,1344],[1344,1728],   # 2322432 1.286:1
    [1792,1280],[1280,1792],   # 2293760 1.4:1
    [2048,1152],[1152,2048],   # 2359296 1.778:1
    [2304,1024],[1024,2304],   # 2359296 2.25:1
    [2432,960],[960,2432],     # 2334720 2.53:1
    [2624,896],[896,2624],     # 2351104 2.929:1
    [2816,832],[832,2816],     # 2342912 3.385:1
    [3072,768],[768,3072],     # 2359296 4:1
]

ASPECTS_1408 = [[1408,1408],   # 1982464 1:1
    [1536,1280],[1280,1536],   # 1966080 1.2:1
    [1664,1152],[1152,1664],   # 1916928 1.444:1
    [1920,1024],[1024,1920],   # 1966080 1.875:1
    [2048,960],[960,2048],     # 1966080 2.133:1
    [2368,832],[832,2368],     # 1970176 2.846:1
    [2560,768],[768,2560],     # 1966080 3.333:1
    [2816,704],[704,3072],     # 1982464 4:1
]

ASPECTS_1280 = [[1280,1280],   # 1638400 1:1
    [1408,1152],[1408,1344],   # 1622016 1.222:1
    [1600,1024],[1024,1600],   # 1638400 1.563:1
    [1792,896],[896,1792],   # 1605632 2:1
    [1920,832],[832,1920],   # 1597440 2.308:1
    [2112,768],[768,2112],   # 1585152 2.75:1
    [2304,704],[704,2304],   # 1622016 3.27:1
    [2560,640],[640,2560],   # 1638400 4:1
]

ASPECTS_1152 = [[1152,1152],    # 1327104 1:1
    #[1216,1088],[1088,1216], # 1323008 1.118:1
    [1280,1024],[1024,1280], # 1310720 1.25:1
    [1344,960],[960,1344],   # 1290240 1.4:1
    [1472,896],[896,1472],   # 1318912 1.64:1
    [1536,832],[832,1536],   # 1277952 1.846:1
    [1728,768],[768,1728],   # 1327104 2.25:1
    [1856,704],[704,1856],   # 1306624 2.64:1
    [2048,640],[640,2048],   # 1310720 3.2:1
    [2304,576],[576,2304],   # 1327104 4:1
]

ASPECTS_1088 = [[1088,1088],    # 1183744 1:1
    [1152,1024],[1024,1152], # 1167360 1.267:1
    [1216,896],[896,1216],   # 1146880 1.429:1
    [1408,832],[832,1408],   # 1171456 1.692:1
    [1536,768],[768,1536],   # 1179648 2:1
    [1664,704],[704,1664],   # 1171456 2.36:1
    [1792,640],[640,1792],   # 1146880 2.8:1
    [2048,576],[576,2048],   # 1179648 3.556:1
    [2304,512],[512,2304],   # 1179648 4.5:1
]

ASPECTS_1024 = [[1024,1024],   # 1048576 1:1
    #[1088,960],[960,1088], # 1044480 1.125:1
    [1152,896],[896,1152], # 1032192 1.286:1
    [1216,832],[832,1216], # 1011712 1.462:1
    [1344,768],[768,1344], # 1032192 1.75:1
    [1472,704],[704,1472], # 1036288 2.09:1
    [1600,640],[640,1600], # 1024000 2.5:1
    [1792,576],[576,1792], # 1032192 3.111:1
    [2048,512],[512,2048], # 1048576 4:1
]

ASPECTS_960 = [[960,960],     # 921600 1:1
    #[1024,896],[896,1024], # 917504 1.143:1
    [1088,832],[832,1088], # 905216 1.308:1
    [1152,768],[768,1152], # 884736 1.5:1
    [1280,704],[704,1280], # 901120 1.818:1
    [1408,640],[640,1408], # 901120 2.2:1
    [1680,576],[576,1680], # 921600 2.778:1
    #[1728,512],[512,1728], # 884736 3.375:1
    [1792,512],[512,1792], # 917504 3.5:1
    [2048,448],[448,2048], # 917504 4.57:1
]

ASPECTS_896 = [[896,896],     # 802816 1:1
    #[960,832],[832,960],   # 798720 1.153:1
    [1024,768],[768,1024], # 786432 1.333:1
    [1088,704],[704,1088], # 765952 1.545:1
    [1216,640],[640,1216], # 778240 1.9:1
    [1344,576],[576,1344], # 774144 2.333:1
    [1536,512],[512,1536], # 786432 3:1
    [1792,448],[448,1792], # 802816 4:1
]

ASPECTS_832 = [[832,832],     # 692224 1:1
    [896,768],[768,896],   # 688128 1.167:1
    [960,704],[704,960],   # 675840 1.364:1
    #[960,640],[640,960],   # 614400 1.5:1
    [1024,640],[640,1024], # 655360 1.6:1
    [1152,576],[576,1152], # 663552 2:1
    [1216,512],[512,1216], # 622080 2.375:1
    #[1280,512],[512,1280], # 655360 2.5:1
    [1344,512],[512,1344], # 688128 2.625:1
    [1536,448],[448,1536], # 688128 3.429:1
    [1600,384],[384,1600], # 614400 4.167:1
]

ASPECTS_768 = [[768,768],     # 589824 1:1
    [832,704],[704,832],   # 585728 1.181:1
    [896,640],[640,896],   # 573440 1.4:1
    [960,576],[576,960],   # 552960 1.6:1
    [1024,576],[576,1024], # 524288 1.778:1
    #[1088,512],[512,1088], # 497664 2.125:1
    [1152,512],[512,1152], # 589824 2.25:1
    #[1216,448],[448,1216], # 552960 2.714:1
    [1280,448],[448,1280], # 573440 2.857:1
    #[1344,384],[384,1344], # 518400 3.5:1
    [1408,384],[384,1408], # 540672 3.667:1
    [1472,320],[320,1472], # 470400 4.6:1
]

ASPECTS_704 = [[704,704],     # 501,376 1:1
    [768,640],[640,768],   # 491,520 1.2:1
    [832,576],[576,832],   # 458,752 1.444:1
    #[896,512],[512,896],   # 458,752 1.75:1
    [960,512],[512,960],   # 491,520 1.875:1
    #[1024,448],[448,1024], # 458,752 2.286:1
    [1088,448],[448,1088], # 487,424 2.429:1
    [1152,384],[384,1152], # 442,368 3:1
    #[1216,384],[384,1216], # 466,944 3.125:1
    [1280,384],[384,1280], # 491,520 3.333:1
    [1280,320],[320,1280], # 409,600 4:1
]

ASPECTS_640 = [[640,640],     # 409600 1:1 
    [704,576],[576,704],   # 405504 1.25:1
    [768,512],[512,768],   # 393216 1.5:1
    [832,448],[448,832],   # 372736 1.857:1
    [896,448],[448,896],   # 401408 2:1    
    [1024,384],[384,1024], # 393216 2.667:1
    [1152,320],[320,1152], # 368640 3.6:1
    [1280,320],[320,1280], # 409600 4:1
]

ASPECTS_576 = [[576,576],     # 331776 1:1
    [640,512],[512,640],   # 327680 1.25:1
    #[640,448],[448,640],   # 286720 1.4286:1
    [704,448],[448,704],   # 314928 1.5625:1
    [832,384],[384,832],   # 317440 2.1667:1
    [960,320],[320,960],   # 307200 3:1
    #[1024,320],[320,1024], # 327680 3.2:1
    [1152,256],[256,1152], # 327680 4.5:1
    #[1280,256],[256,1280], # 327680 5:1
]

ASPECTS_512 = [
    [512,512],      # 262144 1:1
    [384,640],   # 245760 1.667:1
]

ASPECTS_448 = [[448,448],      # 200704 1:1
    [512,384],[384,512],   # 196608 1.333:1
    [640,320],[320,640],   # 204800 2:1
    [768,256],[256,768],   # 196608 3:1
]

ASPECTS_384 = [[384,384],      # 147456 1:1
    [448,320],[320,448],   # 143360 1.4:1
    [512,256],[256,512],   # 131072 2:1
    [704,192],[192,704],   # 135168 3.667:1
]

ASPECTS_320 = [[320,320],      # 102400 1:1
    [384,256],[256,384],   # 98304 1.5:1
    [448,192],[192,448],   # 86016 2.333:1
    [576,128],[576,640],   # 73728 4.5:1
]

ASPECTS_256 = [[256,256],  # 65536 1:1
    [384,192],[192,384],   # 73728 2:1
    [512,128],[128,512],   # 65536 4:1
]

def get_aspect_buckets(resolution, square_only=False, reduced_buckets=False):
    if resolution < 256:
        raise ValueError("Resolution must be at least 512")
    try: 
        rounded_resolution = int(resolution / 64) * 64
        if square_only:
            return [[rounded_resolution, rounded_resolution]]
        all_image_sizes = __get_all_aspects()
        aspects = next(filter(lambda sizes: sizes[0][0]==rounded_resolution, all_image_sizes), None)
        if reduced_buckets:
            return aspects[0:2]
        return aspects
    except Exception as e:
        print(f" *** Unsupported resolution of {resolution}, check your resolution config")
        print(f" *** Value must be between 512 and 1024")
        raise e
    
def get_supported_resolutions():
    all_image_sizes = __get_all_aspects()
    return list(map(lambda sizes: sizes[0][0], all_image_sizes))

def __get_all_aspects():
    return [ASPECTS_256,
            ASPECTS_320,
            ASPECTS_384,
            ASPECTS_448,
            ASPECTS_512,
            ASPECTS_576,
            ASPECTS_640,
            ASPECTS_704,
            ASPECTS_768,
            ASPECTS_832,
            ASPECTS_896,
            ASPECTS_960,
            ASPECTS_1024,
            ASPECTS_1088,
            ASPECTS_1152,
            ASPECTS_1280,
            ASPECTS_1536,
           ]


def get_rational_aspect_ratio(bucket_wh: Tuple[int, int]) -> Tuple[int]:
    def farey_aspect_ratio_pair(x: float, max_denominator_value: int):
        if x <= 1:
            return farey_aspect_ratio_pair_lt1(x, max_denominator_value)
        else:
            b,a = farey_aspect_ratio_pair_lt1(1/x, max_denominator_value)
            return a,b

    # adapted from https://www.johndcook.com/blog/2010/10/20/best-rational-approximation/
    def farey_aspect_ratio_pair_lt1(x: float, max_denominator_value: int):
        if x > 1:
            raise ValueError("x must be <1")
        a, b = 0, 1
        c, d = 1, 1
        while (b <= max_denominator_value and d <= max_denominator_value):
            mediant = float(a+c)/(b+d)
            if x == mediant:
                if b + d <= max_denominator_value:
                    return a+c, b+d
                elif d > b:
                    return c, d
                else:
                    return a, b
            elif x > mediant:
                a, b = a+c, b+d
            else:
                c, d = a+c, b+d

        if (b > max_denominator_value):
            return c, d
        else:
            return a, b

    return farey_aspect_ratio_pair(bucket_wh[0]/bucket_wh[1], 32)
