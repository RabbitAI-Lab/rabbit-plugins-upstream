#!/usr/bin/env python3
"""
八字四柱排盘计算器

功能：
- 公历日期转农历干支
- 计算四柱（年柱、月柱、日柱、时柱）
- 计算纳音
- 计算十神
- 计算大运（起运年龄、顺逆排）
- 计算常用神煞
- 输出 JSON 格式排盘结果

用法：
    python bazi_chart.py --year 1990 --month 5 --day 15 --hour 10 --minute 30 --gender male
    python bazi_chart.py --year 1990 --month 5 --day 15 --hour 10 --gender female --calendar solar
    python bazi_chart.py --year 1988 --month 10 --day 7 --hour 14 --gender male --calendar lunar  # 农历转公历后排盘

输出：JSON 格式的四柱排盘数据
"""

import argparse
import json
import math
from datetime import datetime, timedelta

# lunar_python 精确历法库 (可选): 提供精确节气计算, 保证月柱/年柱分界准确
try:
    from lunar_python import Solar as _LP_Solar
    from lunar_python import Lunar as _LP_Lunar
    LUNAR_PYTHON_OK = True
except ImportError:
    LUNAR_PYTHON_OK = False

# 天干
TIANGAN = ['甲', '乙', '丙', '丁', '戊', '己', '庚', '辛', '壬', '癸']
# 地支
DIZHI = ['子', '丑', '寅', '卯', '辰', '巳', '午', '未', '申', '酉', '戌', '亥']
# 五行
WUXING = ['木', '火', '土', '金', '水']
# 阴阳
YINYANG = ['阳', '阴']

# 六十甲子
LIUJIAZI = []
for i in range(60):
    gan = TIANGAN[i % 10]
    zhi = DIZHI[i % 12]
    liujiazi = gan + zhi
    if gan not in liujiazi:  # skip invalid combos (干支不同步的组合不存在)
        pass
    LIUJIAZI.append(gan + zhi)
# 实际六十甲子只需要前60个有效组合
LIUJIAZI = [TIANGAN[i % 10] + DIZHI[i % 12] for i in range(60)]

# 纳音表 (60个纳音，每组两个干支对应一个纳音，共30组)
NAYIN_TABLE = [
    '海中金', '海中金', '炉中火', '炉中火', '大林木', '大林木',
    '路旁土', '路旁土', '剑锋金', '剑锋金', '山头火', '山头火',
    '涧下水', '涧下水', '城头土', '城头土', '白蜡金', '白蜡金',
    '杨柳木', '杨柳木', '井泉水', '井泉水', '屋上土', '屋上土',
    '霹雳火', '霹雳火', '松柏木', '松柏木', '长流水', '长流水',
    '沙中金', '沙中金', '山下火', '山下火', '平地木', '平地木',
    '壁上土', '壁上土', '金箔金', '金箔金', '覆灯火', '覆灯火',
    '天河水', '天河水', '大驿土', '大驿土', '钗钏金', '钗钏金',
    '桑柘木', '桑柘木', '大溪水', '大溪水', '沙中土', '沙中土',
    '天上火', '天上火', '石榴木', '石榴木', '大海水', '大海水'
]

# 天干五行属性
GAN_WUXING = {
    '甲': '木', '乙': '木', '丙': '火', '丁': '火',
    '戊': '土', '己': '土', '庚': '金', '辛': '金',
    '壬': '水', '癸': '水'
}

# 天干阴阳
GAN_YINYANG = {
    '甲': '阳', '乙': '阴', '丙': '阳', '丁': '阴',
    '戊': '阳', '己': '阴', '庚': '阳', '辛': '阴',
    '壬': '阳', '癸': '阴'
}

# 地支五行属性
ZHI_WUXING = {
    '子': '水', '丑': '土', '寅': '木', '卯': '木',
    '辰': '土', '巳': '火', '午': '火', '未': '土',
    '申': '金', '酉': '金', '戌': '土', '亥': '水'
}

# 地支藏干
ZHI_CANGGAN = {
    '子': ['癸'],
    '丑': ['己', '辛', '癸'],
    '寅': ['甲', '丙', '戊'],
    '卯': ['乙'],
    '辰': ['戊', '乙', '癸'],
    '巳': ['丙', '戊', '庚'],
    '午': ['丁', '己'],
    '未': ['己', '丁', '乙'],
    '申': ['庚', '壬', '戊'],
    '酉': ['辛'],
    '戌': ['戊', '辛', '丁'],
    '亥': ['壬', '甲']
}

# 地支藏干比例 (用于计算本气、中气、余气的力量)
ZHI_CANGGAN_RATIO = {
    '子': [1.0],
    '丑': [0.6, 0.2, 0.2],
    '寅': [0.6, 0.3, 0.1],
    '卯': [1.0],
    '辰': [0.6, 0.2, 0.2],
    '巳': [0.6, 0.1, 0.3],
    '午': [0.7, 0.3],
    '未': [0.6, 0.2, 0.2],
    '申': [0.6, 0.2, 0.2],
    '酉': [1.0],
    '戌': [0.6, 0.2, 0.2],
    '亥': [0.7, 0.3]
}

# 十神名称
# 比肩、劫财、食神、伤官、偏财、正财、偏官(七杀)、正官、偏印(枭神)、正印

# 五行生克关系
def get_wuxing_relation(day_gan_wuxing, other_wuxing):
    """返回五行关系: 同我、我生、生我、我克、克我"""
    if day_gan_wuxing == other_wuxing:
        return 'same'
    # 木生火, 火生土, 土生金, 金生水, 水生木
    sheng = {'木': '火', '火': '土', '土': '金', '金': '水', '水': '木'}
    # 木克土, 土克水, 水克火, 火克金, 金克木
    ke = {'木': '土', '土': '水', '水': '火', '火': '金', '金': '木'}
    if sheng[day_gan_wuxing] == other_wuxing:
        return 'generate'  # 我生
    if sheng[other_wuxing] == day_gan_wuxing:
        return 'generated'  # 生我
    if ke[day_gan_wuxing] == other_wuxing:
        return 'control'  # 我克
    if ke[other_wuxing] == day_gan_wuxing:
        return 'controlled'  # 克我
    return 'same'


def get_shishen(day_gan, target_gan):
    """计算十神"""
    day_wuxing = GAN_WUXING[day_gan]
    target_wuxing = GAN_WUXING[target_gan]
    day_yinyang = GAN_YINYANG[day_gan]
    target_yinyang = GAN_YINYANG[target_gan]
    same_yy = (day_yinyang == target_yinyang)

    relation = get_wuxing_relation(day_wuxing, target_wuxing)

    if relation == 'same':
        return '比肩' if same_yy else '劫财'
    elif relation == 'generate':  # 我生
        return '食神' if same_yy else '伤官'
    elif relation == 'generated':  # 生我 (印): 同性为偏印, 异性为正印
        return '偏印' if same_yy else '正印'
    elif relation == 'control':  # 我克 (财): 同性为偏财, 异性为正财
        return '偏财' if same_yy else '正财'
    elif relation == 'controlled':  # 克我 (官杀): 同性为偏官, 异性为正官
        return '偏官' if same_yy else '正官'
    return ''


# 月柱推算: 年干决定月干起点
# 甲己之年丙作首 (寅月起丙), 乙庚之岁戊为头, 丙辛之岁寻庚上, 丁壬壬寅顺水流, 戊癸甲寅好追求
YUE_GAN_START = {
    '甲': '丙', '己': '丙',
    '乙': '戊', '庚': '戊',
    '丙': '庚', '辛': '庚',
    '丁': '壬', '壬': '壬',
    '戊': '甲', '癸': '甲'
}

# 月支对应 (从寅开始, 寅=1月/正月, 卯=2月...丑=12月)
# 节气对应月份:
# 寅: 立春-惊蛰 (约2/4-3/5)
# 卯: 惊蛰-清明 (约3/5-4/5)
# 辰: 清明-立夏 (约4/5-5/5)
# 巳: 立夏-芒种 (约5/5-6/5)
# 午: 芒种-小暑 (约6/5-7/7)
# 未: 小暑-立秋 (约7/7-8/7)
# 申: 立秋-白露 (约8/7-9/7)
# 酉: 白露-寒露 (约9/7-10/8)
# 戌: 寒露-立冬 (约10/8-11/7)
# 亥: 立冬-大雪 (约11/7-12/7)
# 子: 大雪-小寒 (约12/7-1/5)
# 丑: 小寒-立春 (约1/5-2/4)

# 时柱推算: 日干决定时干起点
# 甲己还加甲, 乙庚丙作初, 丙辛从戊起, 丁壬庚子居, 戊癸壬子头
SHI_GAN_START = {
    '甲': '甲', '己': '甲',
    '乙': '丙', '庚': '丙',
    '丙': '戊', '辛': '戊',
    '丁': '庚', '壬': '庚',
    '戊': '壬', '癸': '壬'
}

# 时辰地支对照 (子时=23:00-00:59, 丑时=01:00-02:59...)
def hour_to_zhi(hour, minute):
    """将小时分钟转换为时辰地支"""
    # 23:00-00:59 为子时, 早子(00:00-00:59)和夜子(23:00-23:59)
    if hour == 23 or (hour == 0 and minute < 60):
        return '子'
    elif hour == 1 or hour == 2:
        return '丑'
    elif hour == 3 or hour == 4:
        return '寅'
    elif hour == 5 or hour == 6:
        return '卯'
    elif hour == 7 or hour == 8:
        return '辰'
    elif hour == 9 or hour == 10:
        return '巳'
    elif hour == 11 or hour == 12:
        return '午'
    elif hour == 13 or hour == 14:
        return '未'
    elif hour == 15 or hour == 16:
        return '申'
    elif hour == 17 or hour == 18:
        return '酉'
    elif hour == 19 or hour == 20:
        return '戌'
    elif hour == 21 or hour == 22:
        return '亥'
    return '子'


# ============== 节气计算 ==============
# 使用近似日期计算节气, 精度约±1天
# 基于回归年公式: 节气日期每年小幅波动

# 二十四节气近似日期 (月, 日) - 以2020年为基准
SOLAR_TERMS_APPROX = [
    ('小寒', 1, 6), ('大寒', 1, 20),
    ('立春', 2, 4), ('雨水', 2, 19),
    ('惊蛰', 3, 5), ('春分', 3, 20),
    ('清明', 4, 4), ('谷雨', 4, 20),
    ('立夏', 5, 5), ('小满', 5, 21),
    ('芒种', 6, 5), ('夏至', 6, 21),
    ('小暑', 7, 7), ('大暑', 7, 22),
    ('立秋', 8, 7), ('处暑', 8, 23),
    ('白露', 9, 7), ('秋分', 9, 23),
    ('寒露', 10, 8), ('霜降', 10, 23),
    ('立冬', 11, 7), ('小雪', 11, 22),
    ('大雪', 12, 7), ('冬至', 12, 22)
]

# 节气对应的月支 (节, 非中气)
JIE_TERMS = ['小寒', '立春', '惊蛰', '清明', '立夏', '芒种',
             '小暑', '立秋', '白露', '寒露', '立冬', '大雪']

# 节气对应月支
JIE_TO_ZHI = {
    '立春': '寅', '惊蛰': '卯', '清明': '辰', '立夏': '巳',
    '芒种': '午', '小暑': '未', '立秋': '申', '白露': '酉',
    '寒露': '戌', '立冬': '亥', '大雪': '子', '小寒': '丑'
}


def get_solar_term_date(year, term_index):
    """获取某年某节气的公历日期 (优先 lunar_python 精确计算, 降级为估算)"""
    name, month, base_day = SOLAR_TERMS_APPROX[term_index]
    if LUNAR_PYTHON_OK:
        try:
            # getJieQiTable 返回当年全部节气 (Solar 对象), 键为节气名
            lunar = _LP_Solar.fromYmd(year, 1, 1).getLunar()
            item = lunar.getJieQiTable().get(name)
            if item is not None:
                return (item.getMonth(), item.getDay())
        except Exception:
            pass
    # 降级估算: 基准年2020, 仅建议在 1990-2050 范围内使用
    year_diff = year - 2020
    approx_day = base_day + year_diff * 0.2422
    day = int(round(approx_day))
    # 日期边界保护: 每月天数上限
    month_days = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30,
                  7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
    max_day = month_days.get(month, 28)
    if day > max_day:
        day = max_day
    if day < 1:
        day = 1
    return (month, day)


def get_current_month_zhi(year, month, day):
    """根据日期确定当前月支"""
    # 找到当前日期所在的节气段
    for term_name in ['立春', '惊蛰', '清明', '立夏', '芒种', '小暑',
                      '立秋', '白露', '寒露', '立冬', '大雪', '小寒']:
        term_idx = next(i for i, (n, m, d) in enumerate(SOLAR_TERMS_APPROX) if n == term_name)
        t_month, t_day = get_solar_term_date(year, term_idx)

        # 检查是否在当前节气之后
        if (month == t_month and day >= t_day) or (month > t_month) or \
           (month < t_month and month + 12 > t_month + 12 and
            (month + 12 == t_month and day >= t_day)):
            # 小寒(1月) 立春(2月) 的跨年处理
            pass

    # 简化方法: 直接比较
    # 构建当年节气日期列表
    term_dates = []
    for term_name in ['立春', '惊蛰', '清明', '立夏', '芒种', '小暑',
                      '立秋', '白露', '寒露', '立冬', '大雪', '小寒']:
        term_idx = next(i for i, (n, m, d) in enumerate(SOLAR_TERMS_APPROX) if n == term_name)
        t_month, t_day = get_solar_term_date(year, term_idx)
        term_dates.append((term_name, t_month, t_day))

    # 小寒在1月, 如果当前日期在1月且在小寒之前, 属于上一年12月(丑月)
    target_date = (month, day)

    # 找到当前日期所在的月支
    # 按时间顺序: 立春(2月)→寅月, 惊蛰(3月)→卯月...小寒(1月)→丑月, 大雪(12月)→子月
    ordered_terms = [
        ('小寒', '丑'), ('立春', '寅'), ('惊蛰', '卯'), ('清明', '辰'),
        ('立夏', '巳'), ('芒种', '午'), ('小暑', '未'), ('立秋', '申'),
        ('白露', '酉'), ('寒露', '戌'), ('立冬', '亥'), ('大雪', '子')
    ]

    current_zhi = '丑'  # 默认
    for term_name, zhi in ordered_terms:
        term_idx = next(i for i, (n, m, d) in enumerate(SOLAR_TERMS_APPROX) if n == term_name)
        t_month, t_day = get_solar_term_date(year, term_idx)
        if (month == t_month and day >= t_day) or (month > t_month if t_month <= 12 else False):
            current_zhi = zhi

    # 处理跨年: 如果在1月小寒之前, 属于上一年子月(大雪到小寒之间)
    # 小寒约1/5-1/6, 如果1月1日-1月4日, 属于子月
    xh_month, xh_day = get_solar_term_date(year, 0)  # 小寒
    dl_month, dl_day = get_solar_term_date(year, 22)  # 大雪(上一年12月)
    if month == 1 and day < xh_day:
        current_zhi = '子'

    return current_zhi


def get_year_ganzhi(year, month, day):
    """计算年柱干支"""
    # 以立春为分界
    lc_month, lc_day = get_solar_term_date(year, 2)  # 立春
    if month < lc_month or (month == lc_month and day < lc_day):
        # 立春前, 属于上一年
        year = year - 1
    # 年干支: (year - 4) % 60 对应六十甲子
    # 甲子=0, 乙丑=1...
    # 年干 = (year - 4) % 10
    # 年支 = (year - 4) % 12
    gan_idx = (year - 4) % 10
    zhi_idx = (year - 4) % 12
    return TIANGAN[gan_idx] + DIZHI[zhi_idx], year


def get_month_ganzhi(year_gan, year_for_calc, month, day):
    """计算月柱干支"""
    month_zhi = get_current_month_zhi(year_for_calc, month, day)
    # 月干: 由年干决定
    start_gan = YUE_GAN_START[year_gan]
    # 从寅月(丙)开始数到当前月支
    zhi_order = ['寅', '卯', '辰', '巳', '午', '未', '申', '酉', '戌', '亥', '子', '丑']
    start_gan_idx = TIANGAN.index(start_gan)
    zhi_idx = zhi_order.index(month_zhi)
    month_gan = TIANGAN[(start_gan_idx + zhi_idx) % 10]
    return month_gan + month_zhi, month_gan, month_zhi


def get_day_ganzhi(year, month, day):
    """计算日柱干支 - 使用Julian Day Number"""
    # 使用公历转JDN的公式
    a = (14 - month) // 12
    y = year + 4800 - a
    m = month + 12 * a - 3
    # JDN (Gregorian calendar)
    jdn = day + (153 * m + 2) // 5 + 365 * y + y // 4 - y // 100 + y // 400 - 32045

    # 日干支: (JDN + 49) % 60 → 六十甲子索引
    # 甲子日 JDN=11 (公元前4713年1月1日是壬子日)
    # 常用公式: (JDN + 49) % 60 或 (JDN - 11) % 60
    gan_idx = (jdn - 1) % 10  # 日干
    zhi_idx = (jdn - 1) % 12  # 日支
    # 调整: 甲子日对应 JDN=11 (参考日)
    # 更准确的公式:
    offset = (jdn + 49) % 60
    gan_idx = offset % 10
    zhi_idx = offset % 12
    return TIANGAN[gan_idx] + DIZHI[zhi_idx], TIANGAN[gan_idx], DIZHI[zhi_idx]


def get_hour_ganzhi(day_gan, hour, minute):
    """计算时柱干支"""
    hour_zhi = hour_to_zhi(hour, minute)
    start_gan = SHI_GAN_START[day_gan]
    start_gan_idx = TIANGAN.index(start_gan)
    zhi_order = ['子', '丑', '寅', '卯', '辰', '巳', '午', '未', '申', '酉', '戌', '亥']
    zhi_idx = zhi_order.index(hour_zhi)
    hour_gan = TIANGAN[(start_gan_idx + zhi_idx) % 10]
    return hour_gan + hour_zhi, hour_gan, hour_zhi


def get_nayin(ganzhi):
    """获取纳音"""
    idx = LIUJIAZI.index(ganzhi)
    return NAYIN_TABLE[idx]


def calculate_dayun(year_gan, gender, birth_datetime):
    """计算大运"""
    # 阳男阴女顺排, 阴男阳女逆排
    year_gan_yy = GAN_YINYANG[year_gan]
    is_male = gender == 'male'
    # 顺排: 阳男、阴女; 逆排: 阴男、阳女
    forward = (is_male and year_gan_yy == '阳') or (not is_male and year_gan_yy == '阴')

    # 起运年龄计算: 从出生到最近一个节的天数, 3天=1年
    # 顺排: 从出生日到下一个节
    # 逆排: 从出生日到上一个节
    birth_year = birth_datetime.year
    birth_month = birth_datetime.month
    birth_day = birth_datetime.day

    # 找到所有节气日期
    jie_terms_data = []
    for term_name in JIE_TERMS:
        term_idx = next(i for i, (n, m, d) in enumerate(SOLAR_TERMS_APPROX) if n == term_name)
        t_month, t_day = get_solar_term_date(birth_year, term_idx)
        term_date = datetime(birth_year, t_month, t_day)
        jie_terms_data.append((term_name, term_date))

    # 也加上前一年和后一年的节气
    for term_name in JIE_TERMS:
        term_idx = next(i for i, (n, m, d) in enumerate(SOLAR_TERMS_APPROX) if n == term_name)
        t_month, t_day = get_solar_term_date(birth_year - 1, term_idx)
        term_date = datetime(birth_year - 1, t_month, t_day)
        jie_terms_data.append((term_name, term_date))

    for term_name in JIE_TERMS:
        term_idx = next(i for i, (n, m, d) in enumerate(SOLAR_TERMS_APPROX) if n == term_name)
        t_month, t_day = get_solar_term_date(birth_year + 1, term_idx)
        term_date = datetime(birth_year + 1, t_month, t_day)
        jie_terms_data.append((term_name, term_date))

    jie_terms_data.sort(key=lambda x: x[1])

    # 找到出生日前后的节
    prev_term = None
    next_term = None
    for i, (name, date) in enumerate(jie_terms_data):
        if date <= birth_datetime:
            prev_term = (name, date)
        if date > birth_datetime and next_term is None:
            next_term = (name, date)

    if forward:
        # 顺排: 从出生到下一个节
        if next_term:
            delta = next_term[1] - birth_datetime
            days = delta.total_seconds() / 86400
            start_age = round(days / 3, 1)
            start_term = next_term[0]
        else:
            start_age = 0
            start_term = ''
    else:
        # 逆排: 从出生到上一个节
        if prev_term:
            delta = birth_datetime - prev_term[1]
            days = delta.total_seconds() / 86400
            start_age = round(days / 3, 1)
            start_term = prev_term[0]
        else:
            start_age = 0
            start_term = ''

    # 生成大运干支 (8步大运, 每步10年)
    # 月柱是基准, 顺排或逆排
    # 大运从月柱的下一个/上一个干支开始
    dayun_list = []
    for i in range(1, 9):
        # 月柱干支在六十甲子中的位置
        # 需要从外部传入月柱信息
        dayun_list.append(i)  # placeholder

    return {
        'forward': forward,
        'start_age': start_age,
        'start_term': start_term,
        'direction': '顺排' if forward else '逆排'
    }


def calculate_dayun_ganzhi(month_ganzhi, forward, count=8):
    """生成大运干支序列"""
    base_idx = LIUJIAZI.index(month_ganzhi)
    dayun = []
    for i in range(1, count + 1):
        if forward:
            idx = (base_idx + i) % 60
        else:
            idx = (base_idx - i) % 60
        ganzhi = LIUJIAZI[idx]
        dayun.append({
            'step': i,
            'ganzhi': ganzhi,
            'nayin': get_nayin(ganzhi)
        })
    return dayun


# ============== 神煞计算 ==============

def get_shensha(year_gan, year_zhi, month_gan, month_zhi, day_gan, day_zhi, hour_gan, hour_zhi, gender):
    """计算常用神煞"""
    shensha = {}

    # 天乙贵人
    tianyi_map = {
        '甲': ['未', '丑'], '戊': ['未', '丑'],
        '乙': ['子', '申'], '己': ['子', '申'],
        '丙': ['酉', '亥'], '丁': ['酉', '亥'],
        '庚': ['丑', '未'], '辛': ['寅', '午'],
        '壬': ['卯', '巳'], '癸': ['卯', '巳']
    }
    day_gan_gui = tianyi_map.get(day_gan, [])
    all_zhi = [year_zhi, month_zhi, day_zhi, hour_zhi]
    found = [z for z in all_zhi if z in day_gan_gui]
    if found:
        shensha['天乙贵人'] = found

    # 文昌贵人
    wenchang_map = {
        '甲': '巳', '乙': '午', '丙': '申', '丁': '酉',
        '戊': '申', '己': '酉', '庚': '亥', '辛': '子',
        '壬': '寅', '癸': '卯'
    }
    wc = wenchang_map.get(day_gan, '')
    if wc in all_zhi:
        shensha['文昌贵人'] = [wc]

    # 驿马 (以年支起算: 申子辰马在寅, 寅午戌马在申, 巳酉丑马在亥, 亥卯未马在巳)
    yima_map = {
        '申': '寅', '子': '寅', '辰': '寅',
        '寅': '申', '午': '申', '戌': '申',
        '巳': '亥', '酉': '亥', '丑': '亥',
        '亥': '巳', '卯': '巳', '未': '巳'
    }
    ym = yima_map.get(year_zhi, '')
    if ym in all_zhi:
        shensha['驿马'] = [ym]

    # 桃花 (申子辰→酉, 寅午戌→卯, 巳酉丑→午, 亥卯未→子)
    taohua_map = {
        '申': '酉', '子': '酉', '辰': '酉',
        '寅': '卯', '午': '卯', '戌': '卯',
        '巳': '午', '酉': '午', '丑': '午',
        '亥': '子', '卯': '子', '未': '子'
    }
    th = taohua_map.get(year_zhi, '')
    if th in all_zhi:
        shensha['桃花'] = [th]

    # 华盖 (申子辰→辰, 寅午戌→戌, 巳酉丑→丑, 亥卯未→未)
    huagai_map = {
        '申': '辰', '子': '辰', '辰': '辰',
        '寅': '戌', '午': '戌', '戌': '戌',
        '巳': '丑', '酉': '丑', '丑': '丑',
        '亥': '未', '卯': '未', '未': '未'
    }
    hg = huagai_map.get(year_zhi, '')
    if hg in all_zhi:
        shensha['华盖'] = [hg]

    # 将星 (申子辰→子, 寅午戌→午, 巳酉丑→酉, 亥卯未→卯)
    jiangxing_map = {
        '申': '子', '子': '子', '辰': '子',
        '寅': '午', '午': '午', '戌': '午',
        '巳': '酉', '酉': '酉', '丑': '酉',
        '亥': '卯', '卯': '卯', '未': '卯'
    }
    jx = jiangxing_map.get(year_zhi, '')
    if jx in all_zhi:
        shensha['将星'] = [jx]

    # 羊刃 (以日干起算; 阴干取帝旺: 乙寅/丁巳/己巳/辛申/癸亥)
    yangren_map = {
        '甲': '卯', '乙': '寅', '丙': '午', '丁': '巳',
        '戊': '午', '己': '巳', '庚': '酉', '辛': '申',
        '壬': '子', '癸': '亥'
    }
    yr = yangren_map.get(day_gan, '')
    if yr in all_zhi:
        shensha['羊刃'] = [yr]

    return shensha


def calculate_wuxing_strength(year_gan, year_zhi, month_gan, month_zhi,
                               day_gan, day_zhi, hour_gan, hour_zhi):
    """计算五行力量分布"""
    wuxing_count = {'木': 0, '火': 0, '土': 0, '金': 0, '水': 0}

    # 天干五行
    for gan in [year_gan, month_gan, day_gan, hour_gan]:
        wuxing_count[GAN_WUXING[gan]] += 1.0

    # 地支藏干五行
    for zhi in [year_zhi, month_zhi, day_zhi, hour_zhi]:
        canggan = ZHI_CANGGAN[zhi]
        ratios = ZHI_CANGGAN_RATIO[zhi]
        for j, cg in enumerate(canggan):
            wuxing_count[GAN_WUXING[cg]] += ratios[j] * 0.5

    total = sum(wuxing_count.values())
    for k in wuxing_count:
        wuxing_count[k] = round(wuxing_count[k] / total * 100, 1) if total > 0 else 0

    return wuxing_count


def calculate_bazi(year, month, day, hour, minute, gender, calendar='solar'):
    """主函数: 计算八字排盘 (calendar: 'solar' 公历 / 'lunar' 农历, 农历需 lunar_python 转公历)"""
    original_input = None
    if calendar == 'lunar':
        original_input = '农历 %d-%02d-%02d %02d:%02d' % (year, month, day, hour, minute or 0)
        if not LUNAR_PYTHON_OK:
            raise ValueError("农历排盘需要 lunar_python 库，请先安装：pip install lunar_python")
        _solar = _LP_Lunar.fromYmdHms(year, month, day, hour, minute or 0, 0).getSolar()
        year, month, day = _solar.getYear(), _solar.getMonth(), _solar.getDay()
        calendar = 'solar'  # 转公历后按公历流程计算

    birth_datetime = datetime(year, month, day, hour, minute or 0)

    # 年柱
    year_ganzhi, year_for_calc = get_year_ganzhi(year, month, day)
    year_gan = year_ganzhi[0]
    year_zhi = year_ganzhi[1]

    # 月柱
    month_ganzhi, month_gan, month_zhi = get_month_ganzhi(year_gan, year_for_calc, month, day)

    # 日柱
    day_ganzhi, day_gan, day_zhi = get_day_ganzhi(year, month, day)

    # 时柱
    hour_ganzhi, hour_gan, hour_zhi = get_hour_ganzhi(day_gan, hour, minute or 0)

    # 纳音
    year_nayin = get_nayin(year_ganzhi)
    month_nayin = get_nayin(month_ganzhi)
    day_nayin = get_nayin(day_ganzhi)
    hour_nayin = get_nayin(hour_ganzhi)

    # 十神 (以日干为主)
    shishen = {
        'year_gan': get_shishen(day_gan, year_gan),
        'month_gan': get_shishen(day_gan, month_gan),
        'hour_gan': get_shishen(day_gan, hour_gan),
    }
    # 地支藏干十神
    for pos, zhi in [('year', year_zhi), ('month', month_zhi), ('day', day_zhi), ('hour', hour_zhi)]:
        canggan = ZHI_CANGGAN[zhi]
        shishen[f'{pos}_zhi_canggan'] = []
        for cg in canggan:
            shishen[f'{pos}_zhi_canggan'].append({
                'gan': cg,
                'shishen': get_shishen(day_gan, cg)
            })

    # 大运
    dayun_info = calculate_dayun(year_gan, gender, birth_datetime)
    dayun_list = calculate_dayun_ganzhi(month_ganzhi, dayun_info['forward'])

    # 神煞
    shensha = get_shensha(year_gan, year_zhi, month_gan, month_zhi,
                          day_gan, day_zhi, hour_gan, hour_zhi, gender)

    # 五行力量
    wuxing_strength = calculate_wuxing_strength(
        year_gan, year_zhi, month_gan, month_zhi, day_gan, day_zhi, hour_gan, hour_zhi)

    # 日主
    day_master = day_gan
    day_master_wuxing = GAN_WUXING[day_gan]

    result = {
        'birth_info': {
            'datetime': birth_datetime.strftime('%Y-%m-%d %H:%M'),
            'gender': gender,
            'calendar': calendar,
            'original_input': original_input
        },
        'four_pillars': {
            'year': {
                'ganzhi': year_ganzhi,
                'gan': year_gan,
                'zhi': year_zhi,
                'nayin': year_nayin,
                'gan_wuxing': GAN_WUXING[year_gan],
                'zhi_wuxing': ZHI_WUXING[year_zhi],
                'gan_yinyang': GAN_YINYANG[year_gan],
                'zhi_canggan': ZHI_CANGGAN[year_zhi]
            },
            'month': {
                'ganzhi': month_ganzhi,
                'gan': month_gan,
                'zhi': month_zhi,
                'nayin': month_nayin,
                'gan_wuxing': GAN_WUXING[month_gan],
                'zhi_wuxing': ZHI_WUXING[month_zhi],
                'gan_yinyang': GAN_YINYANG[month_gan],
                'zhi_canggan': ZHI_CANGGAN[month_zhi]
            },
            'day': {
                'ganzhi': day_ganzhi,
                'gan': day_gan,
                'zhi': day_zhi,
                'nayin': day_nayin,
                'gan_wuxing': GAN_WUXING[day_gan],
                'zhi_wuxing': ZHI_WUXING[day_zhi],
                'gan_yinyang': GAN_YINYANG[day_gan],
                'zhi_canggan': ZHI_CANGGAN[day_zhi]
            },
            'hour': {
                'ganzhi': hour_ganzhi,
                'gan': hour_gan,
                'zhi': hour_zhi,
                'nayin': hour_nayin,
                'gan_wuxing': GAN_WUXING[hour_gan],
                'zhi_wuxing': ZHI_WUXING[hour_zhi],
                'gan_yinyang': GAN_YINYANG[hour_gan],
                'zhi_canggan': ZHI_CANGGAN[hour_zhi]
            }
        },
        'day_master': {
            'gan': day_master,
            'wuxing': day_master_wuxing,
            'yinyang': GAN_YINYANG[day_gan]
        },
        'shishen': shishen,
        'wuxing_strength': wuxing_strength,
        'dayun': {
            'direction': dayun_info['direction'],
            'start_age': dayun_info['start_age'],
            'start_term': dayun_info['start_term'],
            'steps': dayun_list
        },
        'shensha': shensha,
    }

    return result


def main():
    parser = argparse.ArgumentParser(description='八字四柱排盘计算器')
    parser.add_argument('--year', type=int, required=True, help='出生年 (公历)')
    parser.add_argument('--month', type=int, required=True, help='出生月 (1-12)')
    parser.add_argument('--day', type=int, required=True, help='出生日')
    parser.add_argument('--hour', type=int, required=True, help='出生时 (0-23)')
    parser.add_argument('--minute', type=int, default=0, help='出生分 (0-59, 默认0)')
    parser.add_argument('--gender', type=str, default='male', choices=['male', 'female'], help='性别')
    parser.add_argument('--calendar', type=str, default='solar', choices=['solar', 'lunar'], help='历法 (默认公历)')

    args = parser.parse_args()

    result = calculate_bazi(args.year, args.month, args.day, args.hour, args.minute, args.gender, args.calendar)
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
