#!/usr/bin/env python3
"""
周易占卜起卦器

功能：
- 支持金钱卦（三枚铜钱摇六次）
- 支持时间起卦
- 支持数字起卦
- 自动起卦（随机模拟摇卦）
- 计算主卦、变卦、动爻
- 输出卦象、卦名、卦辞、爻辞
- 输出 JSON 格式结果

用法：
    # 自动摇卦
    python zhouyi_divination.py --question "问事业" --method coins --auto
    # 数字起卦
    python zhouyi_divination.py --question "问事业" --method numbers --numbers 3,8
    # 时间起卦
    python zhouyi_divination.py --question "问事业" --method time
"""

import argparse
import json
import random
from datetime import datetime

# 八卦
BAGUA = {
    1: {'name': '乾', 'symbol': '☰', 'lines': [1,1,1], 'wuxing': '金', 'nature': '天'},
    2: {'name': '兑', 'symbol': '☱', 'lines': [0,1,1], 'wuxing': '金', 'nature': '泽'},
    3: {'name': '离', 'symbol': '☲', 'lines': [0,1,0], 'wuxing': '火', 'nature': '火'},
    4: {'name': '震', 'symbol': '☳', 'lines': [0,0,1], 'wuxing': '木', 'nature': '雷'},
    5: {'name': '巽', 'symbol': '☴', 'lines': [1,0,0], 'wuxing': '木', 'nature': '风'},
    6: {'name': '坎', 'symbol': '☵', 'lines': [0,1,0], 'wuxing': '水', 'nature': '水'},
    7: {'name': '艮', 'symbol': '☶', 'lines': [1,0,0], 'wuxing': '土', 'nature': '山'},
    8: {'name': '坤', 'symbol': '☷', 'lines': [0,0,0], 'wuxing': '土', 'nature': '地'},
}

# 先天八卦数: 乾1 兑2 离3 震4 巽5 坎6 艮7 坤8
XIANTIAN_NUM = {'乾':1, '兑':2, '离':3, '震':4, '巽':5, '坎':6, '艮':7, '坤':8}
NUM_XIANTIAN = {v:k for k,v in XIANTIAN_NUM.items()}

# 六十四卦表 (上卦×下卦)
# 索引: 上卦先天数 × 下卦先天数
HEXAGRAM_NAMES = {
    ('乾','乾'): '乾为天', ('乾','兑'): '天泽履', ('乾','离'): '天火同人', ('乾','震'): '天雷无妄',
    ('乾','巽'): '天风姤', ('乾','坎'): '天水讼', ('乾','艮'): '天山遁', ('乾','坤'): '天地否',
    ('兑','乾'): '泽天夬', ('兑','兑'): '兑为泽', ('兑','离'): '泽火革', ('兑','震'): '泽雷随',
    ('兑','巽'): '泽风大过', ('兑','坎'): '泽水困', ('兑','艮'): '泽山咸', ('兑','坤'): '泽地萃',
    ('离','乾'): '火天大有', ('离','兑'): '火泽睽', ('离','离'): '离为火', ('离','震'): '火雷噬嗑',
    ('离','巽'): '火风鼎', ('离','坎'): '火水未济', ('离','艮'): '火山旅', ('离','坤'): '火地晋',
    ('震','乾'): '雷天大壮', ('震','兑'): '雷泽归妹', ('震','离'): '雷火丰', ('震','震'): '震为雷',
    ('震','巽'): '雷风恒', ('震','坎'): '雷水解', ('震','艮'): '雷山小过', ('震','坤'): '雷地豫',
    ('巽','乾'): '风天小畜', ('巽','兑'): '风泽中孚', ('巽','离'): '风火家人', ('巽','震'): '风雷益',
    ('巽','巽'): '巽为风', ('巽','坎'): '风水涣', ('巽','艮'): '风山渐', ('巽','坤'): '风地观',
    ('坎','乾'): '水天需', ('坎','兑'): '水泽节', ('坎','离'): '水火既济', ('坎','震'): '水雷屯',
    ('坎','巽'): '水风井', ('坎','坎'): '坎为水', ('坎','艮'): '水山蹇', ('坎','坤'): '水地比',
    ('艮','乾'): '山天大畜', ('艮','兑'): '山泽损', ('艮','离'): '山火贲', ('艮','震'): '山雷颐',
    ('艮','巽'): '山风蛊', ('艮','坎'): '山水蒙', ('艮','艮'): '艮为山', ('艮','坤'): '山地剥',
    ('坤','乾'): '地天泰', ('坤','兑'): '地泽临', ('坤','离'): '地火明夷', ('坤','震'): '地雷复',
    ('坤','巽'): '地风升', ('坤','坎'): '地水师', ('坤','艮'): '山地谦', ('坤','坤'): '坤为地',
}

# 卦序号 (用于查找)
HEXAGRAM_NUMBERS = {
    '乾为天':1, '泽天夬':43, '火天大有':14, '雷天大壮':34, '风天小畜':9, '水天需':5, '山天大畜':26, '地天泰':11,
    '天泽履':10, '兑为泽':58, '火泽睽':38, '雷泽归妹':54, '风泽中孚':61, '水泽节':60, '山泽损':41, '地泽临':19,
    '天火同人':13, '泽火革':49, '离为火':30, '雷火丰':55, '风火家人':37, '水火既济':63, '山火贲':22, '地火明夷':36,
    '天雷无妄':25, '泽雷随':17, '火雷噬嗑':21, '震为雷':51, '风雷益':42, '水雷屯':3, '山雷颐':27, '地雷复':24,
    '天风姤':44, '泽风大过':28, '火风鼎':50, '雷风恒':32, '巽为风':57, '水风井':48, '山风蛊':18, '地风升':46,
    '天水讼':6, '泽水困':47, '火水未济':64, '雷水解':40, '风水涣':59, '坎为水':29, '山水蒙':4, '地水师':7,
    '天山遁':33, '泽山咸':31, '火山旅':56, '雷山小过':62, '风山渐':53, '水山蹇':39, '艮为山':52, '山地剥':23,
    '天地否':12, '泽地萃':45, '火地晋':35, '雷地豫':16, '风地观':20, '水地比':8, '山地谦':15, '坤为地':2,
}

# 六十四卦卦辞 (简化版, 实际应完整收录)
HEXAGRAM_TEXTS = {
    1: {'name':'乾为天','judgment':'元亨利贞','image':'天行健，君子以自强不息'},
    2: {'name':'坤为地','judgment':'元亨，利牝马之贞','image':'地势坤，君子以厚德载物'},
    3: {'name':'水雷屯','judgment':'元亨利贞，勿用有攸往，利建侯','image':'云雷屯，君子以经纶'},
    4: {'name':'山水蒙','judgment':'亨。匪我求童蒙，童蒙求我','image':'山下出泉，蒙。君子以果行育德'},
    5: {'name':'水天需','judgment':'有孚，光亨，贞吉。利涉大川','image':'云上于天，需。君子以饮食宴乐'},
    6: {'name':'天水讼','judgment':'有孚，窒。惕中吉。终凶。利见大人','image':'天与水违行，讼。君子以作事谋始'},
    7: {'name':'地水师','judgment':'贞，丈人，吉无咎','image':'地中有水，师。君子以容民畜众'},
    8: {'name':'水地比','judgment':'吉。原筮元永贞，无咎','image':'地上有水，比。先王以建万国，亲诸侯'},
    9: {'name':'风天小畜','judgment':'亨。密云不雨，自我西郊','image':'风行天上，小畜。君子以懿文德'},
    10: {'name':'天泽履','judgment':'履虎尾，不咥人，亨','image':'上天下泽，履。君子以辨上下，定民志'},
    11: {'name':'地天泰','judgment':'小往大来，吉亨','image':'天地交，泰。后以财成天地之道'},
    12: {'name':'天地否','judgment':'否之匪人，不利君子贞','image':'天地不交，否。君子以俭德辟难'},
    13: {'name':'天火同人','judgment':'同人于野，亨。利涉大川','image':'天与火，同人。君子以类族辨物'},
    14: {'name':'火天大有','judgment':'元亨','image':'火在天上，大有。君子以遏恶扬善'},
    15: {'name':'山地谦','judgment':'亨，君子有终','image':'地中有山，谦。君子以裒多益寡'},
    16: {'name':'雷地豫','judgment':'利建侯行师','image':'雷出地奋，豫。先王以作乐崇德'},
    17: {'name':'泽雷随','judgment':'元亨利贞，无咎','image':'泽中有雷，随。君子以向晦入宴息'},
    18: {'name':'山风蛊','judgment':'元亨，利涉大川','image':'山下有风，蛊。君子以振民育德'},
    19: {'name':'地泽临','judgment':'元亨利贞。至于八月有凶','image':'泽上有地，临。君子以教思无穷'},
    20: {'name':'风地观','judgment':'盥而不荐，有孚颙若','image':'风行地上，观。先王以省方观民设教'},
    21: {'name':'火雷噬嗑','judgment':'亨。利用狱','image':'雷电，噬嗑。先王以明罚敕法'},
    22: {'name':'山火贲','judgment':'亨。小利有攸往','image':'山下有火，贲。君子以明庶政'},
    23: {'name':'山地剥','judgment':'不利有攸往','image':'山附于地，剥。上以厚下安宅'},
    24: {'name':'地雷复','judgment':'亨。出入无疾，朋来无咎','image':'雷在地中，复。先王以至日闭关'},
    25: {'name':'天雷无妄','judgment':'元亨，利贞。其匪正有眚','image':'天下雷行，物与无妄。先王以茂对时育万物'},
    26: {'name':'山天大畜','judgment':'利贞，不家食吉，利涉大川','image':'天在山中，大畜。君子以多识前言往行'},
    27: {'name':'山雷颐','judgment':'贞吉。观颐，自求口实','image':'山下有雷，颐。君子以慎言语，节饮食'},
    28: {'name':'泽风大过','judgment':'栋桡，利有攸往，亨','image':'泽灭木，大过。君子以独立不惧，遁世无闷'},
    29: {'name':'坎为水','judgment':'习坎，有孚，维心亨','image':'水洊至，习坎。君子以常德行，习教事'},
    30: {'name':'离为火','judgment':'利贞，亨。畜牝牛吉','image':'明两作，离。大人以继明照于四方'},
    31: {'name':'泽山咸','judgment':'亨，利贞，取女吉','image':'山上有泽，咸。君子以虚受人'},
    32: {'name':'雷风恒','judgment':'亨，无咎，利贞','image':'雷风，恒。君子以立不易方'},
    33: {'name':'天山遁','judgment':'亨，小利贞','image':'天下有山，遁。君子以远小人，不恶而严'},
    34: {'name':'雷天大壮','judgment':'利贞','image':'雷在天上，大壮。君子以非礼弗履'},
    35: {'name':'火地晋','judgment':'康侯用锡马蕃庶，昼日三接','image':'明出地上，晋。君子以自昭明德'},
    36: {'name':'地火明夷','judgment':'利艰贞','image':'明入地中，明夷。君子以莅众，用晦而明'},
    37: {'name':'风火家人','judgment':'利女贞','image':'风自火出，家人。君子以言有物而行有恒'},
    38: {'name':'火泽睽','judgment':'小事吉','image':'上火下泽，睽。君子以同而异'},
    39: {'name':'水山蹇','judgment':'利西南，不利东北','image':'山上有水，蹇。君子以反身修德'},
    40: {'name':'雷水解','judgment':'利西南，无所往','image':'雷雨作，解。君子以赦过宥罪'},
    41: {'name':'山泽损','judgment':'有孚，元吉，无咎','image':'山下有泽，损。君子以惩忿窒欲'},
    42: {'name':'风雷益','judgment':'利有攸往，利涉大川','image':'风雷，益。君子以见善则迁，有过则改'},
    43: {'name':'泽天夬','judgment':'扬于王庭，孚号，有厉','image':'泽上于天，夬。君子以施禄及下，居德则忌'},
    44: {'name':'天风姤','judgment':'女壮，勿用取女','image':'天下有风，姤。后以施命诰四方'},
    45: {'name':'泽地萃','judgment':'亨。王假有庙','image':'泽上于地，萃。君子以除戎器，戒不虞'},
    46: {'name':'地风升','judgment':'元亨，用见大人','image':'地中生木，升。君子以顺德，积小以高大'},
    47: {'name':'泽水困','judgment':'亨，贞，大人吉，无咎','image':'泽无水，困。君子以致命遂志'},
    48: {'name':'水风井','judgment':'改邑不改井，无丧无得','image':'木上有水，井。君子以劳民劝相'},
    49: {'name':'泽火革','judgment':'己日乃孚，元亨利贞','image':'泽中有火，革。君子以治历明时'},
    50: {'name':'火风鼎','judgment':'元吉，亨','image':'木上有火，鼎。君子以正位凝命'},
    51: {'name':'震为雷','judgment':'亨。震来虩虩，笑言哑哑','image':'洊雷，震。君子以恐惧修省'},
    52: {'name':'艮为山','judgment':'艮其背，不获其身','image':'兼山，艮。君子以思不出其位'},
    53: {'name':'风山渐','judgment':'女归吉，利贞','image':'山上有木，渐。君子以居贤德善俗'},
    54: {'name':'雷泽归妹','judgment':'征凶，无攸利','image':'泽上有雷，归妹。君子以永终知敝'},
    55: {'name':'雷火丰','judgment':'亨，王假之','image':'雷电皆至，丰。君子以折狱致刑'},
    56: {'name':'火山旅','judgment':'小亨，旅贞吉','image':'山上有火，旅。君子以明慎用刑而不留狱'},
    57: {'name':'巽为风','judgment':'小亨，利有攸往','image':'随风，巽。君子以申命行事'},
    58: {'name':'兑为泽','judgment':'亨，利贞','image':'丽泽，兑。君子以朋友讲习'},
    59: {'name':'风水涣','judgment':'亨。王假有庙','image':'风行水上，涣。先王以享于帝立庙'},
    60: {'name':'水泽节','judgment':'亨。苦节不可贞','image':'泽上有水，节。君子以制数度，议德行'},
    61: {'name':'风泽中孚','judgment':'豚鱼吉，利涉大川','image':'泽上有风，中孚。君子以议狱缓死'},
    62: {'name':'雷山小过','judgment':'亨利贞，可小事不可大事','image':'山上有雷，小过。君子以行过乎恭'},
    63: {'name':'水火既济','judgment':'亨小，利贞','image':'水在火上，既济。君子以思患而预防'},
    64: {'name':'火水未济','judgment':'亨。小狐汔济，濡其尾','image':'火在水上，未济。君子以慎辨物居方'},
}

# 六爻爻辞 (仅乾卦示例, 完整版需收录全部)
YAO_TEXTS = {
    1: ['初九：潜龙勿用', '九二：见龙在田，利见大人', '九三：君子终日乾乾，夕惕若厉', '九四：或跃在渊，无咎', '九五：飞龙在天，利见大人', '上九：亢龙有悔'],
    2: ['初六：履霜，坚冰至', '六二：直方大，不习无不利', '六三：含章可贞', '六四：括囊，无咎无誉', '六五：黄裳，元吉', '上六：龙战于野，其血玄黄'],
}

def get_bagua_from_lines(lines):
    """从三爻获取八卦名称"""
    # lines: [bottom, middle, top], 1=阳, 0=阴
    # 转为二进制: top*4 + middle*2 + bottom
    code = lines[2]*4 + lines[1]*2 + lines[0]
    bagua_map = {7:'乾', 6:'兑', 5:'离', 4:'震', 3:'巽', 2:'坎', 1:'艮', 0:'坤'}
    return bagua_map[code]

def lines_to_hexagram(lower_lines, upper_lines):
    """获取六十四卦"""
    lower_bagua = get_bagua_from_lines(lower_lines)
    upper_bagua = get_bagua_from_lines(upper_lines)
    hexagram_name = HEXAGRAM_NAMES.get((upper_bagua, lower_bagua), '未知')
    hexagram_num = HEXAGRAM_NUMBERS.get(hexagram_name, 0)
    return lower_bagua, upper_bagua, hexagram_name, hexagram_num

def coin_toss():
    """模拟一次铜钱摇卦 (正面=3, 反面=2)"""
    # 三枚铜钱, 每枚正面(有字)记3, 反面(无字)记2
    coins = [random.choice([2, 3]) for _ in range(3)]
    total = sum(coins)
    return coins, total

def total_to_yao(total):
    """铜钱总数转爻: 6=老阴(动), 7=少阳, 8=少阴, 9=老阳(动)"""
    if total == 6:
        return 0, True  # 阴, 动爻
    elif total == 7:
        return 1, False  # 阳, 静
    elif total == 8:
        return 0, False  # 阴, 静
    elif total == 9:
        return 1, True   # 阳, 动爻
    return 0, False

def coins_method(auto=True, coin_results=None):
    """金钱卦起卦"""
    lines = []  # 从初爻到上爻
    moving_lines = []
    coin_details = []

    for i in range(6):
        if auto:
            coins, total = coin_toss()
        else:
            # 解析用户提供的摇卦结果
            # coin_results 格式: ['HTT','HHH',...] H=正面, T=反面
            r = coin_results[i]
            coins = [3 if c == 'H' else 2 for c in r]
            total = sum(coins)

        yao, moving = total_to_yao(total)
        lines.append(yao)
        if moving:
            moving_lines.append(i + 1)  # 1-indexed

        coin_details.append({
            'position': i + 1,
            'coins': coins,
            'total': total,
            'yao': yao,
            'moving': moving,
            'yao_type': '老阴' if total == 6 else ('少阳' if total == 7 else ('少阴' if total == 8 else '老阳'))
        })

    return lines, moving_lines, coin_details

def numbers_method(num1, num2=None):
    """数字起卦"""
    if num2 is None:
        # 单数起卦: 上卦 = num % 8, 下卦 = (num // 8 + 1) % 8
        # 如果数字过大, 取上卦 = num % 8, 下卦 = num % 8 的变化
        upper_idx = ((num1 - 1) % 8) + 1
        lower_idx = ((num1 - 1) % 8 + 1) % 8 + 1
        # 动爻 = num % 6
        moving = num1 % 6 if num1 % 6 != 0 else 6
    else:
        # 双数起卦: 上卦 = num1 % 8, 下卦 = num2 % 8, 动爻 = (num1 + num2) % 6
        upper_idx = num1 % 8 if num1 % 8 != 0 else 8
        lower_idx = num2 % 8 if num2 % 8 != 0 else 8
        moving = (num1 + num2) % 6 if (num1 + num2) % 6 != 0 else 6

    upper_bagua = NUM_XIANTIAN[upper_idx]
    lower_bagua = NUM_XIANTIAN[lower_idx]

    # 从八卦名获取三爻
    upper_lines = BAGUA[[k for k, v in BAGUA.items() if v['name'] == upper_bagua][0]]['lines']
    lower_lines = BAGUA[[k for k, v in BAGUA.items() if v['name'] == lower_bagua][0]]['lines']

    # 合并六爻 (初爻到上爻)
    lines = lower_lines + upper_lines  # 下卦3爻 + 上卦3爻

    # 获取卦名
    hexagram_name = HEXAGRAM_NAMES.get((upper_bagua, lower_bagua), '未知')
    hexagram_num = HEXAGRAM_NUMBERS.get(hexagram_name, 0)

    moving_lines = [moving] if moving > 0 else []

    return lines, moving_lines, upper_bagua, lower_bagua, hexagram_name, hexagram_num

def time_method(dt=None):
    """时间起卦"""
    if dt is None:
        dt = datetime.now()

    # 年数: 取年份后两位
    year_num = dt.year % 100
    if year_num == 0:
        year_num = 100

    # 月数: 1-12 (农历月, 这里用公历月近似)
    month_num = dt.month

    # 日数
    day_num = dt.day

    # 时辰数: 子=1, 丑=2...
    hour = dt.hour
    if hour == 23 or hour == 0:
        hour_zhi_num = 1
    else:
        hour_zhi_num = (hour + 1) // 2 + 1

    # 上卦 = (年数 + 月数 + 日数) % 8
    upper_idx = (year_num + month_num + day_num) % 8
    if upper_idx == 0:
        upper_idx = 8

    # 下卦 = (年数 + 月数 + 日数 + 时辰数) % 8
    lower_idx = (year_num + month_num + day_num + hour_zhi_num) % 8
    if lower_idx == 0:
        lower_idx = 8

    # 动爻 = (年数 + 月数 + 日数 + 时辰数) % 6
    moving = (year_num + month_num + day_num + hour_zhi_num) % 6
    if moving == 0:
        moving = 6

    upper_bagua = NUM_XIANTIAN[upper_idx]
    lower_bagua = NUM_XIANTIAN[lower_idx]

    upper_lines = BAGUA[[k for k, v in BAGUA.items() if v['name'] == upper_bagua][0]]['lines']
    lower_lines = BAGUA[[k for k, v in BAGUA.items() if v['name'] == lower_bagua][0]]['lines']

    lines = lower_lines + upper_lines

    hexagram_name = HEXAGRAM_NAMES.get((upper_bagua, lower_bagua), '未知')
    hexagram_num = HEXAGRAM_NUMBERS.get(hexagram_name, 0)

    moving_lines = [moving]

    return lines, moving_lines, upper_bagua, lower_bagua, hexagram_name, hexagram_num

def get_changed_hexagram(lines, moving_lines):
    """获取变卦"""
    changed_lines = lines.copy()
    for m in moving_lines:
        idx = m - 1
        changed_lines[idx] = 1 - changed_lines[idx]  # 阴阳互变

    lower_changed = changed_lines[:3]
    upper_changed = changed_lines[3:]
    lower_bagua = get_bagua_from_lines(lower_changed)
    upper_bagua = get_bagua_from_lines(upper_changed)
    hexagram_name = HEXAGRAM_NAMES.get((upper_bagua, lower_bagua), '未知')
    hexagram_num = HEXAGRAM_NUMBERS.get(hexagram_name, 0)

    return upper_bagua, lower_bagua, hexagram_name, hexagram_num

def get_hexagram_info(hexagram_num):
    """获取卦象信息"""
    info = HEXAGRAM_TEXTS.get(hexagram_num, {'name':'未知','judgment':'','image':''})
    yao_texts = YAO_TEXTS.get(hexagram_num, [])
    return info, yao_texts

def format_hexagram_visual(lines, moving_lines):
    """格式化卦象可视化"""
    # 从上爻到初爻显示
    visual = []
    for i in range(5, -1, -1):
        yao = lines[i]
        is_moving = (i + 1) in moving_lines
        symbol = '━━━━━' if yao == 1 else '─ ─ ─'
        if is_moving:
            symbol += ' ○' if yao == 1 else ' ✕'
        position_names = ['初', '二', '三', '四', '五', '上']
        yang_yin = '九' if yao == 1 else '六'
        visual.append(f'{position_names[i]}{yang_yin} {symbol}')
    return '\n'.join(visual)

def main():
    parser = argparse.ArgumentParser(description='周易占卜起卦器')
    parser.add_argument('--question', type=str, default='', help='问测事项')
    parser.add_argument('--method', type=str, default='coins', choices=['coins', 'numbers', 'time'], help='起卦方式')
    parser.add_argument('--auto', action='store_true', help='自动起卦(随机)')
    parser.add_argument('--numbers', type=str, default='', help='数字起卦, 逗号分隔, 如 3,8')
    parser.add_argument('--coins', type=str, default='', help='手动摇卦结果, 如 HTT,HHH (H=正面,T=反面)')

    args = parser.parse_args()

    result = {
        'question': args.question,
        'method': args.method,
        'divination_time': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
    }

    if args.method == 'coins':
        if args.coins:
            coin_list = args.coins.split(',')
            lines, moving_lines, coin_details = coins_method(auto=False, coin_results=coin_list)
        else:
            lines, moving_lines, coin_details = coins_method(auto=True)

        lower_lines = lines[:3]
        upper_lines = lines[3:]
        lower_bagua, upper_bagua, hexagram_name, hexagram_num = lines_to_hexagram(lower_lines, upper_lines)

        result['coin_details'] = coin_details

    elif args.method == 'numbers':
        nums = [int(n) for n in args.numbers.split(',')]
        num1 = nums[0]
        num2 = nums[1] if len(nums) > 1 else None
        lines, moving_lines, upper_bagua, lower_bagua, hexagram_name, hexagram_num = numbers_method(num1, num2)
        result['numbers'] = nums

    elif args.method == 'time':
        lines, moving_lines, upper_bagua, lower_bagua, hexagram_name, hexagram_num = time_method()
        result['time'] = result['divination_time']

    # 主卦信息
    main_info, yao_texts = get_hexagram_info(hexagram_num)

    # 变卦
    if moving_lines:
        changed_upper, changed_lower, changed_name, changed_num = get_changed_hexagram(lines, moving_lines)
        changed_info, changed_yao_texts = get_hexagram_info(changed_num)
    else:
        changed_upper = changed_lower = changed_name = ''
        changed_num = 0
        changed_info = {'name':'', 'judgment':'', 'image':''}
        changed_yao_texts = []

    result.update({
        'main_hexagram': {
            'name': hexagram_name,
            'number': hexagram_num,
            'upper_bagua': upper_bagua,
            'lower_bagua': lower_bagua,
            'judgment': main_info.get('judgment', ''),
            'image': main_info.get('image', ''),
            'yao_texts': yao_texts,
            'visual': format_hexagram_visual(lines, moving_lines)
        },
        'moving_lines': moving_lines,
        'changed_hexagram': {
            'name': changed_name,
            'number': changed_num,
            'upper_bagua': changed_upper,
            'lower_bagua': changed_lower,
            'judgment': changed_info.get('judgment', ''),
            'image': changed_info.get('image', ''),
            'yao_texts': changed_yao_texts,
            'visual': format_hexagram_visual([1 - lines[i] if (i+1) in moving_lines else lines[i] for i in range(6)], [])
        } if moving_lines else None,
        'all_lines': lines
    })

    print(json.dumps(result, ensure_ascii=False, indent=2))

if __name__ == '__main__':
    main()
