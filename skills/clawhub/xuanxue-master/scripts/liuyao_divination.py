#!/usr/bin/env python3
"""
六爻起卦器

功能：
- 支持自动起卦（模拟摇卦）
- 支持手动铜钱摇卦结果输入
- 计算六爻卦象、纳甲、六亲、六神、世应
- 识别动爻与变卦
- 输出 JSON 格式结果

用法：
    # 自动起卦
    python liuyao_divination.py --question "问事业" --auto
    # 手动摇卦
    python liuyao_divination.py --question "问事业" --coins "HTT,HHH,TTH,HTT,HHH,THT"
"""

import argparse
import json
import random
from datetime import datetime

# 天干地支
TIANGAN = ['甲','乙','丙','丁','戊','己','庚','辛','壬','癸']
DIZHI = ['子','丑','寅','卯','辰','巳','午','未','申','酉','戌','亥']

# 八卦
BAGUA = {
    '乾': {'lines': [1,1,1], 'nature': '天', 'wuxing': '金'},
    '兑': {'lines': [1,1,0], 'nature': '泽', 'wuxing': '金'},
    '离': {'lines': [1,0,1], 'nature': '火', 'wuxing': '火'},
    '震': {'lines': [1,0,0], 'nature': '雷', 'wuxing': '木'},
    '巽': {'lines': [0,1,1], 'nature': '风', 'wuxing': '木'},
    '坎': {'lines': [0,1,0], 'nature': '水', 'wuxing': '水'},
    '艮': {'lines': [0,0,1], 'nature': '山', 'wuxing': '土'},
    '坤': {'lines': [0,0,0], 'nature': '地', 'wuxing': '土'},
}

# 六十四卦名 (上卦, 下卦)
HEXAGRAM_NAMES = {
    ('乾','乾'):'乾为天', ('乾','兑'):'天泽履', ('乾','离'):'天火同人', ('乾','震'):'天雷无妄',
    ('乾','巽'):'天风姤', ('乾','坎'):'天水讼', ('乾','艮'):'天山遁', ('乾','坤'):'天地否',
    ('兑','乾'):'泽天夬', ('兑','兑'):'兑为泽', ('兑','离'):'泽火革', ('兑','震'):'泽雷随',
    ('兑','巽'):'泽风大过', ('兑','坎'):'泽水困', ('兑','艮'):'泽山咸', ('兑','坤'):'泽地萃',
    ('离','乾'):'火天大有', ('离','兑'):'火泽睽', ('离','离'):'离为火', ('离','震'):'火雷噬嗑',
    ('离','巽'):'火风鼎', ('离','坎'):'火水未济', ('离','艮'):'火山旅', ('离','坤'):'火地晋',
    ('震','乾'):'雷天大壮', ('震','兑'):'雷泽归妹', ('震','离'):'雷火丰', ('震','震'):'震为雷',
    ('震','巽'):'雷风恒', ('震','坎'):'雷水解', ('震','艮'):'雷山小过', ('震','坤'):'雷地豫',
    ('巽','乾'):'风天小畜', ('巽','兑'):'风泽中孚', ('巽','离'):'风火家人', ('巽','震'):'风雷益',
    ('巽','巽'):'巽为风', ('巽','坎'):'风水涣', ('巽','艮'):'风山渐', ('巽','坤'):'风地观',
    ('坎','乾'):'水天需', ('坎','兑'):'水泽节', ('坎','离'):'水火既济', ('坎','震'):'水雷屯',
    ('坎','巽'):'水风井', ('坎','坎'):'坎为水', ('坎','艮'):'水山蹇', ('坎','坤'):'水地比',
    ('艮','乾'):'山天大畜', ('艮','兑'):'山泽损', ('艮','离'):'山火贲', ('艮','震'):'山雷颐',
    ('艮','巽'):'山风蛊', ('艮','坎'):'山水蒙', ('艮','艮'):'艮为山', ('艮','坤'):'山地剥',
    ('坤','乾'):'地天泰', ('坤','兑'):'地泽临', ('坤','离'):'地火明夷', ('坤','震'):'地雷复',
    ('坤','巽'):'地风升', ('坤','坎'):'地水师', ('坤','艮'):'山地谦', ('坤','坤'):'坤为地',
}

# 纳甲表: 八卦对应的天干地支
# 乾纳甲壬, 坤纳乙癸, 坎纳戊, 离纳己, 震纳庚, 巽纳辛, 艮纳丙, 兑纳丁
NAYIN_GAN = {
    '乾': ['甲','壬'], '坤': ['乙','癸'],
    '坎': ['戊'], '离': ['己'],
    '震': ['庚'], '巽': ['辛'],
    '艮': ['丙'], '兑': ['丁']
}

# 纳甲地支 (内卦/外卦)
# 乾: 内卦子寅辰, 外卦午申戌
# 坤: 内卦未巳卯, 外卦丑亥酉
# 坎: 内卦寅辰午, 外卦申戌子
# 离: 内卦卯丑亥, 外卦酉未巳
# 震: 内卦子寅辰, 外卦午申戌
# 巽: 内卦丑亥酉, 外卦未巳卯
# 艮: 内卦辰午申, 外卦戌子寅
# 兑: 内卦巳卯丑, 外卦亥酉未
NAYIN_ZHI = {
    '乾': {'inner': ['子','寅','辰'], 'outer': ['午','申','戌']},
    '坤': {'inner': ['未','巳','卯'], 'outer': ['丑','亥','酉']},
    '坎': {'inner': ['寅','辰','午'], 'outer': ['申','戌','子']},
    '离': {'inner': ['卯','丑','亥'], 'outer': ['酉','未','巳']},
    '震': {'inner': ['子','寅','辰'], 'outer': ['午','申','戌']},
    '巽': {'inner': ['丑','亥','酉'], 'outer': ['未','巳','卯']},
    '艮': {'inner': ['辰','午','申'], 'outer': ['戌','子','寅']},
    '兑': {'inner': ['巳','卯','丑'], 'outer': ['亥','酉','未']},
}

# 六亲 (根据卦宫五行与爻支五行的关系确定)
# 六亲: 父母、兄弟、子孙、妻财、官鬼
WUXING = {'金':'金','木':'木','水':'水','火':'火','土':'土'}
ZHI_WUXING = {
    '子':'水','丑':'土','寅':'木','卯':'木','辰':'土','巳':'火',
    '午':'火','未':'土','申':'金','酉':'金','戌':'土','亥':'水'
}

# 卦宫五行
GUA_GONG_WUXING = {
    '乾': '金', '兑': '金',
    '离': '火',
    '震': '木', '巽': '木',
    '坎': '水',
    '艮': '土', '坤': '土'
}

def get_liuqin(gong_wuxing, zhi_wuxing):
    """根据卦宫五行和爻支五行确定六亲"""
    if gong_wuxing == zhi_wuxing:
        return '兄弟'
    # 生我者为父母
    sheng = {'金':'土','木':'水','水':'金','火':'木','土':'火'}
    if sheng[zhi_wuxing] == gong_wuxing:
        return '父母'
    # 我生者为子孙
    if sheng[gong_wuxing] == zhi_wuxing:
        return '子孙'
    # 克我者为官鬼
    ke = {'金':'火','木':'金','水':'土','火':'水','土':'木'}
    if ke[zhi_wuxing] == gong_wuxing:
        return '官鬼'
    # 我克者为妻财
    if ke[gong_wuxing] == zhi_wuxing:
        return '妻财'
    return '兄弟'

# 六神 (根据日干确定)
LIUSHEN = ['青龙', '朱雀', '勾陈', '腾蛇', '白虎', '玄武']
# 日干起六神: 甲乙→青龙起, 丙丁→朱雀起, 戊→勾陈起, 己→腾蛇起, 庚辛→白虎起, 壬癸→玄武起
GAN_TO_LIUSHEN_START = {
    '甲': 0, '乙': 0,  # 青龙
    '丙': 1, '丁': 1,  # 朱雀
    '戊': 2,            # 勾陈
    '己': 3,            # 腾蛇
    '庚': 4, '辛': 4,  # 白虎
    '壬': 5, '癸': 5,  # 玄武
}

# 世应位置表 (根据卦在卦宫中的位置)
# 八宫卦序: 本宫卦(一世~五世, 六世), 游魂, 归魂
# 世爻位置: 1-6 (初爻到上爻)
SHIYAO_TABLE = {
    # 每个卦的世爻位置 (从初爻=1到上爻=6)
    '乾为天': 6, '天风姤': 1, '天山遁': 2, '天地否': 3,
    '风地观': 4, '山地剥': 5, '火地晋': 4, '火天大有': 3,
    '坎为水': 5, '水泽节': 1, '水雷屯': 2, '水火既济': 3,
    '泽火革': 4, '雷火丰': 5, '地火明夷': 4, '地水师': 3,
    '艮为山': 6, '山火贲': 1, '山天大畜': 2, '山泽损': 3,
    '火泽睽': 4, '天泽履': 5, '风泽中孚': 4, '风山渐': 3,
    '震为雷': 6, '雷地豫': 1, '雷水解': 2, '雷风恒': 3,
    '地风升': 4, '水风井': 5, '泽风大过': 4, '泽雷随': 3,
    '巽为风': 6, '风天小畜': 1, '风火家人': 2, '风雷益': 3,
    '天雷无妄': 4, '火雷噬嗑': 5, '山雷颐': 4, '山风蛊': 3,
    '离为火': 6, '火山旅': 1, '火风鼎': 2, '火水未济': 3,
    '山水蒙': 4, '风水涣': 5, '天水讼': 4, '天火同人': 3,
    '坤为地': 6, '地雷复': 1, '地泽临': 2, '地天泰': 3,
    '雷天大壮': 4, '泽天夬': 5, '水天需': 4, '水地比': 3,
    '兑为泽': 6, '泽水困': 1, '泽地萃': 2, '泽山咸': 3,
    '水山蹇': 4, '地山谦': 5, '雷山小过': 4, '雷泽归妹': 3,
}

def coin_toss():
    """模拟一次三铜钱摇卦"""
    coins = [random.choice([2, 3]) for _ in range(3)]
    total = sum(coins)
    return coins, total

def total_to_yao(total):
    """铜钱总数转爻"""
    if total == 6:
        return 0, True   # 老阴, 动爻
    elif total == 7:
        return 1, False  # 少阳
    elif total == 8:
        return 0, False  # 少阴
    elif total == 9:
        return 1, True   # 老阳, 动爻
    return 0, False

def cast_hexagram(auto=True, coin_results=None):
    """起卦"""
    lines = []
    moving_lines = []
    details = []

    for i in range(6):
        if auto:
            coins, total = coin_toss()
        else:
            r = coin_results[i]
            coins = [3 if c == 'H' else 2 for c in r]
            total = sum(coins)

        yao, moving = total_to_yao(total)
        lines.append(yao)
        if moving:
            moving_lines.append(i + 1)

        details.append({
            'position': i + 1,
            'coins': coins,
            'total': total,
            'yao': yao,
            'moving': moving,
            'yao_name': '老阴' if total == 6 else ('少阳' if total == 7 else ('少阴' if total == 8 else '老阳'))
        })

    return lines, moving_lines, details

def lines_to_bagua(lines):
    """三爻转八卦"""
    code = lines[2] * 4 + lines[1] * 2 + lines[0]
    mapping = {7:'乾', 6:'兑', 5:'离', 4:'震', 3:'巽', 2:'坎', 1:'艮', 0:'坤'}
    return mapping[code]

def get_nayin_for_hexagram(upper_bagua, lower_bagua):
    """获取六爻纳甲"""
    nayin = []

    # 下卦 (内卦) 三爻: 初爻, 二爻, 三爻
    inner_gan = NAYIN_GAN[lower_bagua][0]
    inner_zhi = NAYIN_ZHI[lower_bagua]['inner']
    for i in range(3):
        nayin.append({'gan': inner_gan, 'zhi': inner_zhi[i]})

    # 上卦 (外卦) 三爻: 四爻, 五爻, 上爻
    if len(NAYIN_GAN[upper_bagua]) > 1:
        outer_gan = NAYIN_GAN[upper_bagua][1]
    else:
        outer_gan = NAYIN_GAN[upper_bagua][0]
    outer_zhi = NAYIN_ZHI[upper_bagua]['outer']
    for i in range(3):
        nayin.append({'gan': outer_gan, 'zhi': outer_zhi[i]})

    return nayin

def get_gong(hexagram_name):
    """获取卦宫"""
    # 根据卦名首字判断卦宫 (简化版)
    first_char = hexagram_name[0]
    gong_map = {'乾':'乾','天':'乾','泽':'兑','兑':'兑','火':'离','雷':'震',
                '风':'巽','水':'坎','山':'艮','地':'坤'}
    return gong_map.get(first_char, '乾')

def calculate_liuyao(question, auto=True, coin_results=None, day_gan=None):
    """主函数: 六爻起卦"""
    # 起卦
    lines, moving_lines, coin_details = cast_hexagram(auto, coin_results)

    # 上下卦
    lower_bagua = lines_to_bagua(lines[:3])
    upper_bagua = lines_to_bagua(lines[3:])

    # 卦名
    hexagram_name = HEXAGRAM_NAMES.get((upper_bagua, lower_bagua), '未知')

    # 卦宫
    gong = get_gong(hexagram_name)
    gong_wuxing = GUA_GONG_WUXING.get(gong, '金')

    # 纳甲
    nayin = get_nayin_for_hexagram(upper_bagua, lower_bagua)

    # 六亲
    liuqin_list = []
    for n in nayin:
        zhi_wx = ZHI_WUXING[n['zhi']]
        liuqin = get_liuqin(gong_wuxing, zhi_wx)
        liuqin_list.append(liuqin)

    # 六神
    if day_gan is None:
        # 默认用当天的日干 (简化: 用当前日期估算)
        now = datetime.now()
        # 简化: 用年干代替
        day_gan = TIANGAN[(now.year - 4) % 10]

    liushen_start = GAN_TO_LIUSHEN_START.get(day_gan, 0)
    liushen_list = []
    for i in range(6):
        liushen_list.append(LIUSHEN[(liushen_start + i) % 6])

    # 世应
    shi_pos = SHIYAO_TABLE.get(hexagram_name, 6)
    ying_pos = ((shi_pos + 2) % 6) + 1 if shi_pos <= 4 else ((shi_pos + 2) % 6) + 1

    # 简化世应: 世爻与应爻相隔三爻
    ying_pos = (shi_pos + 3 - 1) % 6 + 1

    # 变卦
    if moving_lines:
        changed_lines = lines.copy()
        for m in moving_lines:
            changed_lines[m - 1] = 1 - changed_lines[m - 1]
        changed_lower = lines_to_bagua(changed_lines[:3])
        changed_upper = lines_to_bagua(changed_lines[3:])
        changed_name = HEXAGRAM_NAMES.get((changed_upper, changed_lower), '未知')
    else:
        changed_lines = lines
        changed_lower = changed_upper = ''
        changed_name = '无变卦'

    # 构建六爻详情 (从上爻到初爻)
    yao_details = []
    position_names = ['初', '二', '三', '四', '五', '上']
    for i in range(5, -1, -1):
        yao_info = {
            'position': i + 1,
            'position_name': position_names[i],
            'yin_yang': '阳' if lines[i] == 1 else '阴',
            'is_moving': (i + 1) in moving_lines,
            'nayin_gan': nayin[i]['gan'],
            'nayin_zhi': nayin[i]['zhi'],
            'liuqin': liuqin_list[i],
            'liushen': liushen_list[i],
            'is_shi': (i + 1) == shi_pos,
            'is_ying': (i + 1) == ying_pos,
        }
        yao_details.append(yao_info)

    result = {
        'question': question,
        'divination_time': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'main_hexagram': {
            'name': hexagram_name,
            'upper_bagua': upper_bagua,
            'lower_bagua': lower_bagua,
            'gong': gong,
            'gong_wuxing': gong_wuxing,
        },
        'moving_lines': moving_lines,
        'changed_hexagram': {
            'name': changed_name,
            'upper_bagua': changed_upper if changed_upper else '',
            'lower_bagua': changed_lower if changed_lower else '',
        } if moving_lines else None,
        'yao_details': yao_details,
        'shi_yao': shi_pos,
        'ying_yao': ying_pos,
        'coin_details': coin_details,
        'day_gan': day_gan,
    }

    return result

def main():
    parser = argparse.ArgumentParser(description='六爻起卦器')
    parser.add_argument('--question', type=str, default='', help='问测事项')
    parser.add_argument('--auto', action='store_true', help='自动起卦')
    parser.add_argument('--coins', type=str, default='', help='手动摇卦: HTT,HHH (H=正面,T=反面)')
    parser.add_argument('--day-gan', type=str, default='', help='日干 (用于六神)')

    args = parser.parse_args()

    auto = args.auto
    coin_results = None
    if args.coins:
        coin_results = args.coins.split(',')
        auto = False

    day_gan = args.day_gan if args.day_gan else None

    result = calculate_liuyao(args.question, auto, coin_results, day_gan)
    print(json.dumps(result, ensure_ascii=False, indent=2))

if __name__ == '__main__':
    main()
