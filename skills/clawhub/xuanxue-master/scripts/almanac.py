#!/usr/bin/env python3
"""
黄历查询与择吉计算器

功能：
- 查询指定日期的干支、生肖、星座
- 计算十二值日（建除十二神）
- 计算冲煞
- 提供基础宜忌参考（按值日推算）
- 支持按事项搜索吉日

用法：
    # 查询某日黄历
    python almanac.py --date 2024-01-15
    # 查询日期范围
    python almanac.py --start 2024-01-01 --end 2024-01-31
    # 按事项择吉
    python almanac.py --action "嫁娶" --start 2024-01-01 --end 2024-01-31
"""

import argparse
import json
from datetime import datetime, timedelta

TIANGAN = ['甲','乙','丙','丁','戊','己','庚','辛','壬','癸']
DIZHI = ['子','丑','寅','卯','辰','巳','午','未','申','酉','戌','亥']
ZODIAC = ['鼠','牛','虎','兔','龙','蛇','马','羊','猴','鸡','狗','猪']
ZHI_WUXING = {
    '子':'水','丑':'土','寅':'木','卯':'木','辰':'土','巳':'火',
    '午':'火','未':'土','申':'金','酉':'金','戌':'土','亥':'水'
}
GAN_WUXING = {
    '甲':'木','乙':'木','丙':'火','丁':'火',
    '戊':'土','己':'土','庚':'金','辛':'金',
    '壬':'水','癸':'水'
}

# 建除十二神
JIANCHU = ['建','除','满','平','定','执','破','危','成','收','开','闭']

# 值日宜忌 (按建除十二神, 传统通则)
JIANCHU_YIJI = {
    '建': {'yi': ['出行', '上任', '会友', '上书', '见工'], 'ji': ['动土', '开仓', '掘井', '乘船', '嫁娶']},
    '除': {'yi': ['祭祀', '祈福', '除服', '求医', '治病', '扫舍'], 'ji': ['嫁娶', '出行', '开市', '签约']},
    '满': {'yi': ['祭祀', '祈福', '结婚', '开市', '交易', '移徙'], 'ji': ['服药', '求医', '栽种', '动土']},
    '平': {'yi': ['修造', '修饰', '平治道涂', '修路'], 'ji': ['祈福', '开市', '交易', '嫁娶', '掘井']},
    '定': {'yi': ['祭祀', '祈福', '嫁娶', '定盟', '签约', '交易'], 'ji': ['诉讼', '出行', '求医', '栽种']},
    '执': {'yi': ['捕捉', '祈福', '祭祀', '求嗣', '结婚', '签约'], 'ji': ['移徙', '入宅', '出行', '开市']},
    '破': {'yi': ['求医', '治病', '破屋', '坏垣', '拆卸'], 'ji': ['嫁娶', '开市', '签约', '交易', '出行', '入宅']},
    '危': {'yi': ['祭祀', '祈福', '安床', '拆卸'], 'ji': ['登高', '行船', '出行', '嫁娶', '开市']},
    '成': {'yi': ['嫁娶', '开市', '入宅', '移徙', '安床', '开光', '求嗣', '交易', '签约'], 'ji': ['诉讼', '安门', '词讼']},
    '收': {'yi': ['祭祀', '纳财', '进人口', '纳畜', '牧养', '捕捉', '栽种'], 'ji': ['开市', '出行', '安床', '破土', '安葬']},
    '开': {'yi': ['祭祀', '祈福', '开市', '入学', '上任', '修造', '动土', '开光'], 'ji': ['安床', '入宅', '栽种']},
    '闭': {'yi': ['祭祀', '安葬', '修坟', '填坑', '筑堤'], 'ji': ['开市', '出行', '嫁娶', '移徙', '入宅', '签约']}
}

# 黑黄道十二神
HUANGDAO = ['青龙', '明堂', '天刑', '朱雀', '金匮', '天德', '白虎', '玉堂', '天牢', '玄武', '司命', '勾陈']
HUANGDAO_LUCK = {'青龙': '吉', '明堂': '吉', '金匮': '吉', '天德': '吉', '玉堂': '吉', '司命': '吉',
                 '天刑': '凶', '朱雀': '凶', '白虎': '凶', '天牢': '凶', '玄武': '凶', '勾陈': '凶'}

# 黄道神排列 (日支起青龙)
HUANGDAO_TABLE = {
    '子': ['青龙','明堂','天刑','朱雀','金匮','天德','白虎','玉堂','天牢','玄武','司命','勾陈'],
    # 青龙起法: 子午日起申, 丑未日起酉, 寅申日起戌, 卯酉日起亥, 辰戌日起子, 巳亥日起丑
}
# 青龙起始: 日支→青龙所在支
QINGLONG_START = {
    '子': '申', '午': '申',
    '丑': '酉', '未': '酉',
    '寅': '戌', '申': '戌',
    '卯': '亥', '酉': '亥',
    '辰': '子', '戌': '子',
    '巳': '丑', '亥': '丑'
}
# 十二神按支顺序: 青龙(申)→明堂(酉)→天刑(戌)→朱雀(亥)→金匮(子)→天德(丑)→白虎(寅)→玉堂(卯)→天牢(辰)→玄武(巳)→司命(午)→勾陈(未)
HUANGDAO_ORDER = ['青龙','明堂','天刑','朱雀','金匮','天德','白虎','玉堂','天牢','玄武','司命','勾陈']

def get_day_ganzhi(date):
    """计算日干支"""
    year, month, day = date.year, date.month, date.day
    a = (14 - month) // 12
    y = year + 4800 - a
    m = month + 12 * a - 3
    jdn = day + (153 * m + 2) // 5 + 365 * y + y // 4 - y // 100 + y // 400 - 32045
    offset = (jdn + 49) % 60
    gan = TIANGAN[offset % 10]
    zhi = DIZHI[offset % 12]
    return gan, zhi

def get_month_ganzhi(date):
    """计算月干支 (以节气近似分界)"""
    year, month, day = date.year, date.month, date.day
    # 节气近似日
    jie = {2: 4, 3: 6, 4: 5, 5: 6, 6: 6, 7: 7, 8: 8, 9: 8, 10: 8, 11: 7, 12: 7, 1: 6}
    # 确定月支
    if month == 1 and day < jie[1]:
        month_zhi_idx = 0  # 子
    elif month == 12 and day >= jie[12]:
        month_zhi_idx = 0  # 子
    else:
        if day >= jie[month]:
            effective = month
        else:
            effective = month - 1
        month_zhi_idx = (effective + 1) % 12  # 寅月=2月→idx 2
    # 年干
    if month < 2 or (month == 2 and day < jie[2]):
        y = year - 1
    else:
        y = year
    year_gan = TIANGAN[(y - 4) % 10]
    # 月干
    yuegan_start = {'甲':'丙','己':'丙','乙':'戊','庚':'戊','丙':'庚','辛':'庚',
                    '丁':'壬','壬':'壬','戊':'甲','癸':'甲'}
    start_idx = TIANGAN.index(yuegan_start[year_gan])
    zhi_order = ['寅','卯','辰','巳','午','未','申','酉','戌','亥','子','丑']
    month_zhi = zhi_order[month_zhi_idx] if month_zhi_idx < 12 else '寅'
    # 重算: 寅=索引0
    zhi_order2 = ['寅','卯','辰','巳','午','未','申','酉','戌','亥','子','丑']
    # 月份到索引
    month_to_idx = {2:0, 3:1, 4:2, 5:3, 6:4, 7:5, 8:6, 9:7, 10:8, 11:9, 12:10, 1:11}
    if month == 1 and day < jie[1]:
        idx = 10  # 子
    elif month == 12 and day >= jie[12]:
        idx = 10  # 子
    else:
        effective = month if day >= jie[month] else month - 1
        if effective == 0:
            effective = 12
        idx = month_to_idx[effective]
    month_zhi = zhi_order2[idx]
    month_gan = TIANGAN[(start_idx + idx) % 10]
    return month_gan, month_zhi

def get_year_ganzhi(date):
    """年干支"""
    year, month, day = date.year, date.month, date.day
    if month < 2 or (month == 2 and day < 4):
        year -= 1
    gan = TIANGAN[(year - 4) % 10]
    zhi = DIZHI[(year - 4) % 12]
    return gan, zhi

def get_jianchu(day_zhi, month_zhi):
    """建除十二神: 月建(月支)起建, 数至日支"""
    month_idx = DIZHI.index(month_zhi)
    day_idx = DIZHI.index(day_zhi)
    offset = (day_idx - month_idx + 12) % 12
    return JIANCHU[offset], offset

def get_huangdao(day_zhi):
    """黄黑道十二神"""
    ql_start_zhi = QINGLONG_START[day_zhi]
    # 黄道吉神
    gods = {}
    ql_idx = DIZHI.index(ql_start_zhi)
    for i, god in enumerate(HUANGDAO_ORDER):
        zhi = DIZHI[(ql_idx + i) % 12]
        gods[zhi] = god
    # 日的黄道神 = 起始位置的推算
    # 该日对应的黄道神: 从青龙起子起申, 顺序排
    # 日支相对青龙起始支的偏移
    day_idx = DIZHI.index(day_zhi)
    ql_idx = DIZHI.index(QINGLONG_START[day_zhi])
    god = '青龙'  # 每日值神 = 该日青龙所在支对应的神
    # 值神规则: 日支决定青龙位置, 值神从青龙位置按日支推
    # 简化: 值神 = HUANGDAO_ORDER 中索引 = 日支相对青龙支偏移
    offset = (day_idx - ql_idx + 12) % 12
    god = HUANGDAO_ORDER[offset]
    return god

def get_chongsha(day_zhi):
    """冲煞"""
    chong_map = {
        '子': ('午', '马'), '丑': ('未', '羊'), '寅': ('申', '猴'), '卯': ('酉', '鸡'),
        '辰': ('戌', '狗'), '巳': ('亥', '猪'), '午': ('子', '鼠'), '未': ('丑', '牛'),
        '申': ('寅', '虎'), '酉': ('卯', '兔'), '戌': ('辰', '龙'), '亥': ('巳', '蛇')
    }
    chong_zhi, chong_animal = chong_map[day_zhi]
    sha_direction = {
        '子': '南', '丑': '东', '寅': '北', '卯': '西',
        '辰': '南', '巳': '东', '午': '北', '未': '西',
        '申': '南', '酉': '东', '戌': '北', '亥': '西'
    }
    return f'冲{chong_zhi}({chong_animal})', f'煞{sha_direction[day_zhi]}'

def get_constellation(month, day):
    """星座"""
    # 每月分界日: 日期 < 分界日属上一个星座, >= 分界日属当月起始星座
    edges = [20, 19, 21, 20, 21, 22, 23, 23, 23, 24, 23, 22]
    names = ['摩羯座', '水瓶座', '双鱼座', '白羊座', '金牛座', '双子座',
             '巨蟹座', '狮子座', '处女座', '天秤座', '天蝎座', '射手座', '摩羯座']
    if day < edges[month - 1]:
        idx = month - 1
    else:
        idx = month
    return names[idx]


def get_almanac(date):
    """获取某日完整黄历"""
    year_gan, year_zhi = get_year_ganzhi(date)
    month_gan, month_zhi = get_month_ganzhi(date)
    day_gan, day_zhi = get_day_ganzhi(date)

    zodiac = ZODIAC[DIZHI.index(year_zhi)]
    jianchu, _ = get_jianchu(day_zhi, month_zhi)
    god = get_huangdao(day_zhi)
    god_luck = HUANGDAO_LUCK.get(god, '')
    chong, sha = get_chongsha(day_zhi)
    constellation = get_constellation(date.month, date.day)

    yiji = JIANCHU_YIJI.get(jianchu, {'yi': [], 'ji': []})
    is_huangdao = god_luck == '吉'

    return {
        'date': date.strftime('%Y-%m-%d'),
        'weekday': ['周一','周二','周三','周四','周五','周六','周日'][date.weekday()],
        'year_ganzhi': year_gan + year_zhi,
        'month_ganzhi': month_gan + month_zhi,
        'day_ganzhi': day_gan + day_zhi,
        'day_wuxing': GAN_WUXING[day_gan] + ZHI_WUXING[day_zhi],
        'zodiac': zodiac,
        'constellation': constellation,
        'jianchu': jianchu,
        'day_god': god,
        'god_luck': god_luck,
        'is_huangdao_day': is_huangdao,
        'chong': chong,
        'sha': sha,
        'yi': yiji['yi'],
        'ji': yiji['ji'],
    }

def main():
    parser = argparse.ArgumentParser(description='黄历查询与择吉')
    parser.add_argument('--date', type=str, default='', help='查询日期 YYYY-MM-DD')
    parser.add_argument('--start', type=str, default='', help='起始日期 YYYY-MM-DD')
    parser.add_argument('--end', type=str, default='', help='结束日期 YYYY-MM-DD')
    parser.add_argument('--action', type=str, default='', help='择吉事项 (如 嫁娶/搬家/开业)')

    args = parser.parse_args()

    if args.date:
        date = datetime.strptime(args.date, '%Y-%m-%d')
        result = get_almanac(date)
        print(json.dumps(result, ensure_ascii=False, indent=2))
        return

    if args.start and args.end:
        start = datetime.strptime(args.start, '%Y-%m-%d')
        end = datetime.strptime(args.end, '%Y-%m-%d')
        results = []
        current = start
        while current <= end:
            almanac = get_almanac(current)
            if args.action:
                # 检查该日是否宜于所问事项
                if args.action in almanac['yi'] and almanac['is_huangdao_day']:
                    almanac['recommended'] = True
                elif args.action in almanac['yi']:
                    almanac['recommended'] = 'maybe'
                else:
                    almanac['recommended'] = False
            results.append(almanac)
            current += timedelta(days=1)

        if args.action:
            good_days = [r for r in results if r['recommended'] is True]
            output = {
                'action': args.action,
                'range': f'{args.start} ~ {args.end}',
                'total_days': len(results),
                'good_days': good_days,
                'good_days_count': len(good_days),
                'all_days': results,
            }
        else:
            output = results
        print(json.dumps(output, ensure_ascii=False, indent=2))
        return

    # 默认: 今天
    result = get_almanac(datetime.now())
    print(json.dumps(result, ensure_ascii=False, indent=2))

if __name__ == '__main__':
    main()
