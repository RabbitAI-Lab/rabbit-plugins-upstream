#!/usr/bin/env python3
"""
梅花易数起卦器

功能：
- 支持时间起卦
- 支持数字起卦（单数/双数）
- 计算主卦、互卦、变卦
- 确定体卦、用卦
- 分析体用生克关系
- 输出 JSON 格式结果

用法：
    # 时间起卦
    python meihua_divination.py --question "问感情" --method time
    # 数字起卦
    python meihua_divination.py --question "问感情" --method numbers --numbers 5,3
    # 单数起卦
    python meihua_divination.py --question "问感情" --method numbers --numbers 123
"""

import argparse
import json
from datetime import datetime

# 八卦属性
BAGUA = {
    '乾': {'symbol':'☰','wuxing':'金','nature':'天','direction':'西北','number':1},
    '兑': {'symbol':'☱','wuxing':'金','nature':'泽','direction':'西','number':2},
    '离': {'symbol':'☲','wuxing':'火','nature':'火','direction':'南','number':3},
    '震': {'symbol':'☳','wuxing':'木','nature':'雷','direction':'东','number':4},
    '巽': {'symbol':'☴','wuxing':'木','nature':'风','direction':'东南','number':5},
    '坎': {'symbol':'☵','wuxing':'水','nature':'水','direction':'北','number':6},
    '艮': {'symbol':'☶','wuxing':'土','nature':'山','direction':'东北','number':7},
    '坤': {'symbol':'☷','wuxing':'土','nature':'地','direction':'西南','number':8},
}

NUM_TO_BAGUA = {1:'乾',2:'兑',3:'离',4:'震',5:'巽',6:'坎',7:'艮',8:'坤'}

# 八卦三爻 (从下到上: 初爻, 中爻, 上爻), 1=阳, 0=阴
BAGUA_LINES = {
    '乾':[1,1,1], '兑':[0,1,1], '离':[0,1,0], '震':[0,0,1],
    '巽':[1,0,0], '坎':[0,1,0], '艮':[1,0,0], '坤':[0,0,0]
}

# 修正坎和离的爻
BAGUA_LINES = {
    '乾':[1,1,1],  # 天
    '兑':[1,1,0],  # 泽 (上缺)
    '离':[1,0,1],  # 火 (中虚)
    '震':[0,0,1],  # 雷 (仰盂)
    '巽':[1,1,0],  # 风 (下断) - 修正: 巽 = [0,1,1]? 不对
    '坎':[0,1,0],  # 水 (中满)
    '艮':[1,0,0],  # 山 (覆碗)
    '坤':[0,0,0],  # 地
}

# 正确的八卦三爻 (上爻, 中爻, 下爻 → 转为 初爻, 中爻, 上爻)
# 乾☰: 上1中1下1 → [1,1,1]
# 兑☱: 上0中1下1 → [1,1,0]
# 离☲: 上1中0下1 → [1,0,1]
# 震☳: 上0中0下1 → [1,0,0]
# 巽☴: 上1中1下0 → [0,1,1]
# 坎☵: 上0中1下0 → [0,1,0]
# 艮☶: 上1中0下0 → [0,0,1]
# 坤☷: 上0中0下0 → [0,0,0]
BAGUA_LINES = {
    '乾':[1,1,1], '兑':[1,1,0], '离':[1,0,1], '震':[1,0,0],
    '巽':[0,1,1], '坎':[0,1,0], '艮':[0,0,1], '坤':[0,0,0]
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

# 五行生克
def get_wuxing_relation(wuxing1, wuxing2):
    """五行关系: 1生2, 1克2, 2生1, 2克1, 相同"""
    if wuxing1 == wuxing2:
        return '比和'
    sheng = {'木':'火','火':'土','土':'金','金':'水','水':'木'}
    ke = {'木':'土','土':'水','水':'火','火':'金','金':'木'}
    if sheng.get(wuxing1) == wuxing2:
        return '体生用'  # 体生用, 泄气
    if sheng.get(wuxing2) == wuxing1:
        return '用生体'  # 用生体, 得生
    if ke.get(wuxing1) == wuxing2:
        return '体克用'  # 体克用, 耗力
    if ke.get(wuxing2) == wuxing1:
        return '用克体'  # 用克体, 不利
    return '比和'

# 互卦: 取主卦2,3,4爻为下卦, 3,4,5爻为上卦
def get_hu_gua(lines):
    """获取互卦"""
    # lines: [初爻, 二爻, 三爻, 四爻, 五爻, 上爻]
    # 互卦下卦 = [lines[1], lines[2], lines[3]]
    # 互卦上卦 = [lines[2], lines[3], lines[4]]
    lower = [lines[1], lines[2], lines[3]]
    upper = [lines[2], lines[3], lines[4]]

    def lines_to_bagua(l):
        code = l[2]*4 + l[1]*2 + l[0]  # 上*4 + 中*2 + 下
        mapping = {7:'乾', 6:'兑', 5:'离', 4:'震', 3:'巽', 2:'坎', 1:'艮', 0:'坤'}
        return mapping[code]

    lower_bagua = lines_to_bagua(lower)
    upper_bagua = lines_to_bagua(upper)
    name = HEXAGRAM_NAMES.get((upper_bagua, lower_bagua), '未知')
    return lower_bagua, upper_bagua, name

# 变卦: 动爻变
def get_bian_gua(lines, moving_line):
    """获取变卦"""
    changed = lines.copy()
    changed[moving_line - 1] = 1 - changed[moving_line - 1]

    lower = changed[:3]
    upper = changed[3:]

    def lines_to_bagua(l):
        code = l[2]*4 + l[1]*2 + l[0]
        mapping = {7:'乾', 6:'兑', 5:'离', 4:'震', 3:'巽', 2:'坎', 1:'艮', 0:'坤'}
        return mapping[code]

    lower_bagua = lines_to_bagua(lower)
    upper_bagua = lines_to_bagua(upper)
    name = HEXAGRAM_NAMES.get((upper_bagua, lower_bagua), '未知')
    return lower_bagua, upper_bagua, name

def time_method(dt=None):
    """时间起卦"""
    if dt is None:
        dt = datetime.now()

    # 年数
    year_num = dt.year % 100
    if year_num == 0:
        year_num = 100

    month_num = dt.month
    day_num = dt.day

    # 时辰数
    hour = dt.hour
    if hour == 23 or hour == 0:
        hour_zhi_num = 1
    else:
        hour_zhi_num = (hour + 1) // 2 + 1

    # 上卦 = (年 + 月 + 日) % 8
    upper_num = (year_num + month_num + day_num) % 8
    if upper_num == 0:
        upper_num = 8

    # 下卦 = (年 + 月 + 日 + 时) % 8
    lower_num = (year_num + month_num + day_num + hour_zhi_num) % 8
    if lower_num == 0:
        lower_num = 8

    # 动爻 = (年 + 月 + 日 + 时) % 6
    moving = (year_num + month_num + day_num + hour_zhi_num) % 6
    if moving == 0:
        moving = 6

    upper_bagua = NUM_TO_BAGUA[upper_num]
    lower_bagua = NUM_TO_BAGUA[lower_num]

    # 六爻
    lines = BAGUA_LINES[lower_bagua] + BAGUA_LINES[upper_bagua]

    # 体用: 动爻在上卦 → 下卦为体, 上卦为用; 动爻在下卦 → 上卦为体, 下卦为用
    if moving <= 3:
        # 动爻在下卦, 上卦为体, 下卦为用
        ti_bagua = upper_bagua
        yong_bagua = lower_bagua
    else:
        # 动爻在上卦, 下卦为体, 上卦为用
        ti_bagua = lower_bagua
        yong_bagua = upper_bagua

    hexagram_name = HEXAGRAM_NAMES.get((upper_bagua, lower_bagua), '未知')

    return lines, moving, upper_bagua, lower_bagua, ti_bagua, yong_bagua, hexagram_name

def numbers_method(num1, num2=None):
    """数字起卦"""
    if num2 is None:
        # 单数起卦
        upper_num = num1 % 8
        if upper_num == 0:
            upper_num = 8
        lower_num = (num1 // 8 + 1) % 8
        if lower_num == 0:
            lower_num = 8
        moving = num1 % 6
        if moving == 0:
            moving = 6
    else:
        upper_num = num1 % 8
        if upper_num == 0:
            upper_num = 8
        lower_num = num2 % 8
        if lower_num == 0:
            lower_num = 8
        moving = (num1 + num2) % 6
        if moving == 0:
            moving = 6

    upper_bagua = NUM_TO_BAGUA[upper_num]
    lower_bagua = NUM_TO_BAGUA[lower_num]

    lines = BAGUA_LINES[lower_bagua] + BAGUA_LINES[upper_bagua]

    if moving <= 3:
        ti_bagua = upper_bagua
        yong_bagua = lower_bagua
    else:
        ti_bagua = lower_bagua
        yong_bagua = upper_bagua

    hexagram_name = HEXAGRAM_NAMES.get((upper_bagua, lower_bagua), '未知')

    return lines, moving, upper_bagua, lower_bagua, ti_bagua, yong_bagua, hexagram_name

def analyze_ti_yong(ti_bagua, yong_bagua):
    """分析体用关系"""
    ti_wuxing = BAGUA[ti_bagua]['wuxing']
    yong_wuxing = BAGUA[yong_bagua]['wuxing']

    relation = get_wuxing_relation(ti_wuxing, yong_wuxing)

    # 吉凶判断
    if relation == '用生体':
        luck = '大吉'
        desc = '用生体，大吉之象，事情顺利，多得助力'
    elif relation == '体克用':
        luck = '吉'
        desc = '体克用，吉象，事情可成但需努力'
    elif relation == '比和':
        luck = '中吉'
        desc = '体用比和，中吉之象，事情平稳'
    elif relation == '体生用':
        luck = '凶'
        desc = '体生用，泄气之象，费力不讨好'
    elif relation == '用克体':
        luck = '大凶'
        desc = '用克体，大凶之象，事情难成，多有阻碍'
    else:
        luck = '未知'
        desc = ''

    return {
        'ti': {'bagua': ti_bagua, 'wuxing': ti_wuxing, 'nature': BAGUA[ti_bagua]['nature']},
        'yong': {'bagua': yong_bagua, 'wuxing': yong_wuxing, 'nature': BAGUA[yong_bagua]['nature']},
        'relation': relation,
        'luck': luck,
        'description': desc
    }

def main():
    parser = argparse.ArgumentParser(description='梅花易数起卦器')
    parser.add_argument('--question', type=str, default='', help='问测事项')
    parser.add_argument('--method', type=str, default='time', choices=['time', 'numbers'], help='起卦方式')
    parser.add_argument('--numbers', type=str, default='', help='数字, 逗号分隔')

    args = parser.parse_args()

    result = {
        'question': args.question,
        'method': args.method,
        'divination_time': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
    }

    if args.method == 'time':
        lines, moving, upper_bagua, lower_bagua, ti_bagua, yong_bagua, hexagram_name = time_method()
    elif args.method == 'numbers':
        nums = [int(n) for n in args.numbers.split(',')]
        num1 = nums[0]
        num2 = nums[1] if len(nums) > 1 else None
        lines, moving, upper_bagua, lower_bagua, ti_bagua, yong_bagua, hexagram_name = numbers_method(num1, num2)
        result['numbers'] = nums

    # 体用分析
    tiyong = analyze_ti_yong(ti_bagua, yong_bagua)

    # 互卦
    hu_lower, hu_upper, hu_name = get_hu_gua(lines)

    # 变卦
    bian_lower, bian_upper, bian_name = get_bian_gua(lines, moving)

    # 变卦体用
    if moving <= 3:
        bian_ti = bian_upper
        bian_yong = bian_lower
    else:
        bian_ti = bian_lower
        bian_yong = bian_upper
    bian_tiyong = analyze_ti_yong(bian_ti, bian_yong)

    result.update({
        'main_hexagram': {
            'name': hexagram_name,
            'upper_bagua': upper_bagua,
            'lower_bagua': lower_bagua,
            'lines': lines,
            'moving_line': moving,
        },
        'ti_yong_analysis': tiyong,
        'hu_gua': {
            'name': hu_name,
            'upper_bagua': hu_upper,
            'lower_bagua': hu_lower,
        },
        'bian_gua': {
            'name': bian_name,
            'upper_bagua': bian_upper,
            'lower_bagua': bian_lower,
        },
        'bian_ti_yong': bian_tiyong,
        'summary': {
            'main_luck': tiyong['luck'],
            'main_relation': tiyong['relation'],
            'bian_luck': bian_tiyong['luck'],
            'bian_relation': bian_tiyong['relation'],
            'overall': f"主卦{tiyong['relation']}({tiyong['luck']}), 变卦{bian_tiyong['relation']}({bian_tiyong['luck']})"
        }
    })

    print(json.dumps(result, ensure_ascii=False, indent=2))

if __name__ == '__main__':
    main()
