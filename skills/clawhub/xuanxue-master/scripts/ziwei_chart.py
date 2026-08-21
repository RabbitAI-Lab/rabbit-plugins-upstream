#!/usr/bin/env python3
"""
紫微斗数排盘计算器

功能：
- 公历日期转农历
- 计算命宫、身宫位置
- 安十四主星（紫微星系、天府星系）
- 安辅星、杂曜
- 计算四化
- 确定五行局
- 输出 JSON 格式命盘数据

用法：
    python ziwei_chart.py --year 1990 --month 5 --day 15 --hour 10 --gender male --calendar solar

输出：JSON 格式的紫微斗数命盘数据
"""

import argparse
import json

# 十二地支 (宫位顺序, 逆时针)
PALACE_ZHI = ['子', '丑', '寅', '卯', '辰', '巳', '午', '未', '申', '酉', '戌', '亥']

# 十二宫名称
PALACE_NAMES = ['命宫', '兄弟', '夫妻', '子女', '财帛', '疾厄', '迁移', '交友', '官禄', '田宅', '福德', '父母']

# 时辰索引 (子=0, 丑=1...亥=11)
def hour_to_zhi_idx(hour, minute=0):
    if hour == 23 or hour == 0:
        return 0  # 子
    return ((hour + 1) // 2) % 12

# 紫微星位置表: 根据五行局和农历日数
# 五行局: 水二局, 木三局, 金四局, 土五局, 火六局
ZIWEI_POS_TABLE = {
    '水二局': {1:2, 2:1, 3:12, 4:11, 5:10, 6:9, 7:8, 8:7, 9:6, 10:5, 11:4, 12:3,
        13:2, 14:1, 15:15, 16:14, 17:13, 18:12, 19:11, 20:10, 21:9, 22:8, 23:7, 24:6,
        25:5, 26:4, 27:3, 28:2, 29:1, 30:0},
    '木三局': {1:3, 2:2, 3:1, 4:15, 5:14, 6:13, 7:12, 8:11, 9:10, 10:9, 11:8, 12:7,
        13:6, 14:5, 15:4, 16:3, 17:2, 18:1, 19:15, 20:14, 21:13, 22:12, 23:11, 24:10,
        25:9, 26:8, 27:7, 28:6, 29:5, 30:4},
    '金四局': {1:4, 2:3, 3:2, 4:1, 5:15, 6:14, 7:13, 8:12, 9:11, 10:10, 11:9, 12:8,
        13:7, 14:6, 15:5, 16:4, 17:3, 18:2, 19:1, 20:15, 21:14, 22:13, 23:12, 24:11,
        25:10, 26:9, 27:8, 28:7, 29:6, 30:5},
    '土五局': {1:5, 2:4, 3:3, 4:2, 5:1, 6:15, 7:14, 8:13, 9:12, 10:11, 11:10, 12:9,
        13:8, 14:7, 15:6, 16:5, 17:4, 18:3, 19:2, 20:1, 21:15, 22:14, 23:13, 24:12,
        25:11, 26:10, 27:9, 28:8, 29:7, 30:6},
    '火六局': {1:6, 2:5, 3:4, 4:3, 5:2, 6:1, 7:15, 8:14, 9:13, 10:12, 11:11, 12:10,
        13:9, 14:8, 15:7, 16:6, 17:5, 18:4, 19:3, 20:2, 21:1, 22:15, 23:14, 24:13,
        25:12, 26:11, 27:10, 28:9, 29:8, 30:7}
}

# 紫微星系: 紫微, 天机, 太阳, 武曲, 天同, 廉贞
# 天府星系: 天府, 太阴, 贪狼, 巨门, 天相, 天梁, 七杀, 破军
# 紫微与天府相对, 以紫微为基准安星系

# 紫微星系位置偏移 (以紫微星位置为基准, 宫位索引为0-11)
ZIWEI_SYSTEM_OFFSET = {
    '紫微': 0, '天机': -1, '太阳': -3, '武曲': -4, '天同': -5, '廉贞': -8
}
# 逆时针方向: 负数表示往前(逆时针), 正数表示往后(顺时针)
# 紫微=0, 天机=逆1, 太阳=逆3, 武曲=逆4, 天同=逆5, 廉贞=逆8(即顺4)

# 天府星位置: 与紫微相对 (以寅宫为对称轴)
# 天府位置 = 4 - 紫微位置 (mod 12) → 以寅为对称轴
# 如果紫微在子(0), 天府在辰(4)
# 如果紫微在丑(1), 天府在卯(3)
# 即: 天府 = (4 - 紫微位置 + 12) % 12
# 实际: 天府 = 紫微位置 关于寅(4)的镜像 => 天府 = 2*4 - 紫微位置 = 8 - 紫微位置

TIANFU_SYSTEM_OFFSET = {
    '天府': 0, '太阴': 1, '贪狼': 2, '巨门': 3, '天相': 4, '天梁': 5, '七杀': 6, '破军': 10
}

# 四化表: 根据年干
SIHUA_TABLE = {
    '甲': {'化禄': '廉贞', '化权': '破军', '化科': '武曲', '化忌': '太阳'},
    '乙': {'化禄': '天机', '化权': '天梁', '化科': '紫微', '化忌': '太阴'},
    '丙': {'化禄': '天同', '化权': '天机', '化科': '文昌', '化忌': '廉贞'},
    '丁': {'化禄': '太阴', '化权': '天同', '化科': '天机', '化忌': '巨门'},
    '戊': {'化禄': '贪狼', '化权': '太阴', '化科': '右弼', '化忌': '天机'},
    '己': {'化禄': '武曲', '化权': '贪狼', '化科': '天梁', '化忌': '文曲'},
    '庚': {'化禄': '太阳', '化权': '武曲', '化科': '天同', '化忌': '天相'},
    '辛': {'化禄': '巨门', '化权': '太阳', '化科': '文曲', '化忌': '文昌'},
    '壬': {'化禄': '天梁', '化权': '紫微', '化科': '左辅', '化忌': '武曲'},
    '癸': {'化禄': '破军', '化权': '巨门', '化科': '太阴', '化忌': '贪狼'}
}

# 年干计算
TIANGAN = ['甲', '乙', '丙', '丁', '戊', '己', '庚', '辛', '壬', '癸']

# 纳音五行局表 (根据命宫干支纳音)
NAYIN_WUXING_JU = {
    '海中金': '金四局', '炉中火': '火六局', '大林木': '木三局',
    '路旁土': '土五局', '剑锋金': '金四局', '火': '火六局',
    '城头土': '土五局', '白蜡金': '金四局', '杨柳木': '木三局',
    '井泉水': '水二局', '屋上土': '土五局', '霹雳火': '火六局',
    '松柏木': '木三局', '长流水': '水二局', '沙中金': '金四局',
    '山下火': '火六局', '平地木': '木三局', '壁上土': '土五局',
    '金箔金': '金四局', '覆灯火': '火六局', '天河水': '水二局',
    '大驿土': '土五局', '钗钏金': '金四局', '桑柘木': '木三局',
    '大溪水': '水二局', '沙中土': '土五局', '天上火': '火六局',
    '石榴木': '木三局', '大海水': '水二局'
}

# 六十甲子纳音 (简化版)
LIUJIAZI = [TIANGAN[i % 10] + ['子','丑','寅','卯','辰','巳','午','未','申','酉','戌','亥'][i % 12] for i in range(60)]
NAYIN_LIST = [
    '海中金','海中金','炉中火','炉中火','大林木','大林木',
    '路旁土','路旁土','剑锋金','剑锋金','火','火',
    '城头土','城头土','白蜡金','白蜡金','杨柳木','杨柳木',
    '井泉水','井泉水','屋上土','屋上土','霹雳火','霹雳火',
    '松柏木','松柏木','长流水','长流水','沙中金','沙中金',
    '山下火','山下火','平地木','平地木','壁上土','壁上土',
    '金箔金','金箔金','覆灯火','覆灯火','天河水','天河水',
    '大驿土','大驿土','钗钏金','钗钏金','桑柘木','桑柘木',
    '大溪水','大溪水','沙中土','沙中土','天上火','天上火',
    '石榴木','石榴木','大海水','大海水'
]

# 辅星
# 左辅右弼: 以辰/戌为基准, 左辅从辰起顺排月数, 右弼从戌起逆排月数
# 文昌文曲: 文昌从戌起逆排时辰, 文曲从辰起顺排时辰

# ============== 农历计算 (标准数据表 1900-2100) ==============
LUNAR_INFO = [
    0x04ad8,0x04ae0,0x0a570,0x054d5,0x0d260,0x0d950,0x16554,0x056a0,0x09ad0,0x015d2,
    0x04ae0,0x0a1b6,0x0a4d0,0x0d250,0x1d255,0x0b540,0x0d6a0,0x0ada2,0x095b0,0x14977,
    0x04970,0x0a4b0,0x0b4b5,0x06a50,0x06d40,0x1ab54,0x02b60,0x09570,0x012f2,0x04970,
    0x06166,0x0d4a0,0x0ea50,0x06695,0x05ad0,0x02b60,0x186e3,0x092e0,0x1c8d7,0x0c950,
    0x0d4a0,0x1d8a6,0x0b550,0x056a0,0x1a5b4,0x025d0,0x092d0,0x092b2,0x0a950,0x0b557,
    0x06ca0,0x0b550,0x15355,0x04da0,0x0a5d0,0x14573,0x052b0,0x0a8a8,0x0e950,0x06aa0,
    0x0aaa6,0x0ab50,0x04b60,0x0aae4,0x0a570,0x05260,0x0d263,0x0d950,0x05957,0x056a0,
    0x096d0,0x045d5,0x04ad0,0x0a4d0,0x0c4d4,0x0d250,0x0d458,0x0b540,0x0b5a0,0x191a6,
    0x095b0,0x049b0,0x0a974,0x0a4b0,0x0b23a,0x06a50,0x06d40,0x0ab46,0x0ab60,0x09570,
    0x042f5,0x04970,0x064b0,0x054a3,0x0ea50,0x06a58,0x05ac0,0x0ab60,0x096d5,0x092e0,
    0x0c960,0x0c954,0x0d4a0,0x0da50,0x03552,0x056a0,0x0a9b7,0x025d0,0x092d0,0x0c2b5,
    0x0a950,0x0b4a0,0x0aaa4,0x0ad50,0x05559,0x04ba0,0x0a5b0,0x15176,0x052b0,0x0a930,
    0x06954,0x06aa0,0x0ad50,0x01b52,0x04b60,0x0a2e6,0x0a4e0,0x0d260,0x0e265,0x0d530,
    0x05aa0,0x056a3,0x096d0,0x04adb,0x04ad0,0x0a4d0,0x1d0b6,0x0d250,0x0d520,0x0d545,
    0x0b5a0,0x056d0,0x015b2,0x049b0,0x0a577,0x0a4b0,0x0aa50,0x1b255,0x06d20,0x0ada0,
    0x14b63,0x09370,0x048f8,0x04970,0x064b0,0x168a6,0x0ea50,0x06aa0,0x1a6c4,0x0aae0,
    0x092e0,0x0d2e3,0x0c960,0x0d557,0x0d4a0,0x0da50,0x05555,0x056a0,0x0a6d0,0x045d4,
    0x052d0,0x0a8b8,0x0a950,0x0b4a0,0x0b2a6,0x0ad50,0x055a0,0x0aba4,0x0a5b0,0x052b0,
    0x09273,0x06930,0x07137,0x06aa0,0x0ad50,0x14355,0x04b60,0x0a570,0x044e4,0x0d160,
    0x0e868,0x0d520,0x0daa0,0x16aa6,0x056d0,0x04ae0,0x0a9d4,0x0a2d0,0x0d150,0x0b252,
    0x0d520
]

def l_leap_month(y):
    """农历年闰哪个月 (0 表示无闰月)"""
    return LUNAR_INFO[y - 1900] & 0xf

def l_leap_days(y):
    """农历年闰月天数"""
    if l_leap_month(y):
        return 30 if (LUNAR_INFO[y - 1900] & 0x10000) else 29
    return 0

def l_month_days(y, m):
    """农历 y 年 m 月天数"""
    return 30 if (LUNAR_INFO[y - 1900] & (0x10000 >> m)) else 29

def l_year_days(y):
    """农历 y 年总天数"""
    info = LUNAR_INFO[y - 1900]
    total = 348
    bit = 0x8000
    while bit > 0x8:
        if info & bit:
            total += 1
        bit >>= 1
    return total + l_leap_days(y)

def solar_to_lunar(year, month, day):
    """公历转农历 (优先使用 lunardate 库, 降级到内部数据表)
    返回: (lunar_year, lunar_month, lunar_day, is_leap_month)
    """
    # 优先使用 lunardate 库 (精确可靠)
    try:
        from lunardate import LunarDate
        import warnings
        with warnings.catch_warnings():
            warnings.simplefilter('ignore')
            ld = LunarDate.fromSolarDate(year, month, day)
        return ld.year, ld.month, ld.day, ld.is_leap_month
    except Exception:
        pass

    # 降级: 使用内部 LUNAR_INFO 数据表 (基准: 1900-01-31 = 农历1900年正月初一)
    from datetime import datetime as _dt
    offset = (_dt(year, month, day) - _dt(1900, 1, 31)).days

    lunar_year = 1900
    temp = l_year_days(lunar_year)
    i = 1900
    while i < 2101 and offset > 0:
        temp = l_year_days(i)
        offset -= temp
        i += 1
    if offset < 0:
        offset += temp
        i -= 1
    lunar_year = i

    leap = l_leap_month(lunar_year)
    is_leap = False
    j = 1
    while j < 13 and offset > 0:
        if leap > 0 and j == leap + 1 and not is_leap:
            j -= 1
            is_leap = True
            temp = l_leap_days(lunar_year)
        else:
            temp = l_month_days(lunar_year, j)
        if is_leap and j == leap + 1:
            is_leap = False
        offset -= temp
        j += 1

    if offset == 0 and leap > 0 and j == leap + 1:
        if is_leap:
            is_leap = False
        else:
            is_leap = True
            j -= 1
    if offset < 0:
        offset += temp
        j -= 1
    lunar_month = j
    lunar_day = offset + 1
    return lunar_year, lunar_month, lunar_day, is_leap


def get_year_gan(year, month, day):
    """获取年干 (以立春为界)"""
    # 立春约2/4
    if month < 2 or (month == 2 and day < 4):
        year = year - 1
    gan_idx = (year - 4) % 10
    return TIANGAN[gan_idx]

def get_year_zhi(year, month, day):
    """获取年支"""
    if month < 2 or (month == 2 and day < 4):
        year = year - 1
    zhi_list = ['子','丑','寅','卯','辰','巳','午','未','申','酉','戌','亥']
    zhi_idx = (year - 4) % 12
    return zhi_list[zhi_idx]

def calculate_minggong(lunar_month, hour_zhi_idx):
    """计算命宫位置: 从寅起正月顺数到生月, 再从生月宫起子时逆数到生时"""
    # 寅 = 索引2
    month_palace = (2 + lunar_month - 1) % 12
    minggong_idx = (month_palace - hour_zhi_idx + 24) % 12
    return minggong_idx

def calculate_shengong(lunar_month, hour_zhi_idx):
    """计算身宫位置: 从寅起正月顺数到生月, 再从生月宫起子时顺数到生时"""
    month_palace = (2 + lunar_month - 1) % 12
    shengong_idx = (month_palace + hour_zhi_idx) % 12
    return shengong_idx

def get_minggong_ganzhi(minggong_idx, year_gan):
    """获取命宫干支 (五虎遁: 从寅宫起丙/戊/庚/壬/甲)"""
    # 年干起月干: 甲己丙寅首
    yuegan_start = {'甲':'丙','己':'丙','乙':'戊','庚':'戊','丙':'庚','辛':'庚',
                    '丁':'壬','壬':'壬','戊':'甲','癸':'甲'}
    start_gan = yuegan_start[year_gan]
    start_gan_idx = TIANGAN.index(start_gan)
    # 从寅(索引2)开始, 每顺行一宫进一干
    gan_idx = (start_gan_idx + minggong_idx - 2 + 12) % 10
    ganzhi = TIANGAN[gan_idx] + PALACE_ZHI[minggong_idx]
    return ganzhi

def get_nayin(ganzhi):
    """获取纳音"""
    idx = LIUJIAZI.index(ganzhi) if ganzhi in LIUJIAZI else 0
    return NAYIN_LIST[idx]

def get_wuxing_ju(nayin):
    """纳音转五行局"""
    for key, value in NAYIN_WUXING_JU.items():
        if key in nayin:
            return value
    return '水二局'  # 默认

def place_ziwei_star(jushu, lunar_day):
    """安紫微星 (商数退进法)
    1. 找到 >= 生日的最小局数倍数 A = N * jushu
    2. 余数 yu = A - 生日
    3. 基础宫 = 寅 + (N-1)
    4. 余数为0 → 即基础宫; 奇数 → 退 yu 宫; 偶数 → 进 yu 宫
    """
    n = (lunar_day + jushu - 1) // jushu  # 向上取整
    a = n * jushu
    yu = a - lunar_day
    base = 2 + (n - 1)  # 寅 = 索引2
    if yu == 0:
        pos = base
    elif yu % 2 == 1:
        pos = base - yu
    else:
        pos = base + yu
    return pos % 12

def place_ziwei_system(ziwei_idx):
    """安紫微星系"""
    stars = {}
    for star, offset in ZIWEI_SYSTEM_OFFSET.items():
        idx = (ziwei_idx + offset + 12) % 12
        if star not in stars:
            stars[star] = []
        stars[star].append(idx)
    return stars

def place_tianfu_system(ziwei_idx):
    """安天府星系"""
    # 天府与紫微以寅为对称
    tianfu_idx = (4 - ziwei_idx + 12) % 12
    stars = {}
    for star, offset in TIANFU_SYSTEM_OFFSET.items():
        idx = (tianfu_idx + offset + 12) % 12
        if star not in stars:
            stars[star] = []
        stars[star].append(idx)
    return stars, tianfu_idx

def place_auxiliary_stars(lunar_month, hour_zhi_idx):
    """安辅星 (左辅右弼, 文昌文曲)"""
    stars = {}

    # 左辅: 从辰(4)起正月, 顺数到生月
    zuofu_idx = (4 + lunar_month - 1) % 12
    stars['左辅'] = [zuofu_idx]

    # 右弼: 从戌(10)起正月, 逆数到生月
    youbi_idx = (10 - lunar_month + 1 + 12) % 12
    stars['右弼'] = [youbi_idx]

    # 文昌: 从戌(10)起子时, 逆数到生时
    wenchang_idx = (10 - hour_zhi_idx + 12) % 12
    stars['文昌'] = [wenchang_idx]

    # 文曲: 从辰(4)起子时, 顺数到生时
    wenqu_idx = (4 + hour_zhi_idx) % 12
    stars['文曲'] = [wenqu_idx]

    return stars

def calculate_sihua(year_gan, star_positions):
    """计算四化"""
    sihua_table = SIHUA_TABLE.get(year_gan, {})
    sihua_result = {}
    for huake, star_name in sihua_table.items():
        if star_name in star_positions:
            sihua_result[huake] = {
                'star': star_name,
                'positions': star_positions[star_name]
            }
    return sihua_result

def calculate_ziwei(year, month, day, hour, minute, gender, calendar='solar'):
    """主函数: 计算紫微斗数命盘"""
    hour_zhi_idx = hour_to_zhi_idx(hour, minute or 0)
    year_gan = get_year_gan(year, month, day)
    year_zhi = get_year_zhi(year, month, day)

    # 转农历 (标准数据表算法)
    lunar_year, lunar_month, lunar_day, lunar_is_leap = solar_to_lunar(year, month, day)

    # 命宫身宫
    minggong_idx = calculate_minggong(lunar_month, hour_zhi_idx)
    shengong_idx = calculate_shengong(lunar_month, hour_zhi_idx)

    # 命宫干支
    minggong_ganzhi = get_minggong_ganzhi(minggong_idx, year_gan)
    minggong_nayin = get_nayin(minggong_ganzhi)
    wuxing_ju = get_wuxing_ju(minggong_nayin)

    # 安紫微星 (算法排星: 商数退进法)
    # 局数: 水二局=2, 木三局=3, 金四局=4, 土五局=5, 火六局=6
    JU_NUM = {'水二局': 2, '木三局': 3, '金四局': 4, '土五局': 5, '火六局': 6}
    jushu = JU_NUM.get(wuxing_ju, 2)
    ziwei_idx = place_ziwei_star(jushu, lunar_day)

    # 安星系
    ziwei_stars = place_ziwei_system(ziwei_idx)
    tianfu_stars, tianfu_idx = place_tianfu_system(ziwei_idx)
    aux_stars = place_auxiliary_stars(lunar_month, hour_zhi_idx)

    # 合并所有星
    all_stars = {}
    for d in [ziwei_stars, tianfu_stars, aux_stars]:
        for star, positions in d.items():
            if star not in all_stars:
                all_stars[star] = []
            all_stars[star].extend(positions)

    # 四化
    sihua = calculate_sihua(year_gan, all_stars)

    # 十二宫排列
    palaces = []
    for i in range(12):
        palace_idx = (minggong_idx + i) % 12
        palace_name = PALACE_NAMES[i]
        palace_zhi = PALACE_ZHI[palace_idx]

        # 找到落在此宫的星
        stars_in_palace = []
        for star, positions in all_stars.items():
            if palace_idx in positions:
                stars_in_palace.append(star)

        # 四化
        sihua_in_palace = []
        for huake, info in sihua.items():
            if palace_idx in info['positions']:
                sihua_in_palace.append(f"{huake}({info['star']})")

        palaces.append({
            'palace_name': palace_name,
            'palace_zhi': palace_zhi,
            'palace_idx': palace_idx,
            'stars': stars_in_palace,
            'sihua': sihua_in_palace,
            'is_minggong': palace_idx == minggong_idx,
            'is_shengong': palace_idx == shengong_idx
        })

    # 大限
    daxian_list = []
    # 局数作为起始年龄: 水二局=2, 木三局=3, 金四局=4, 土五局=5, 火六局=6
    JU_NUM = {'二': 2, '三': 3, '四': 4, '五': 5, '六': 6}
    daxian_start_age = JU_NUM.get(wuxing_ju[-2], 2)
    forward = True if (gender == 'male' and year_gan in ['甲','丙','戊','庚','壬']) or \
                       (gender == 'female' and year_gan in ['乙','丁','己','辛','癸']) else False

    for i in range(12):
        if forward:
            daxian_palace_idx = (minggong_idx + i) % 12
        else:
            daxian_palace_idx = (minggong_idx - i + 12) % 12
        start_age = daxian_start_age + i * 10
        end_age = start_age + 9
        daxian_list.append({
            'palace_idx': daxian_palace_idx,
            'palace_zhi': PALACE_ZHI[daxian_palace_idx],
            'age_range': f'{start_age}-{end_age}',
            'start_age': start_age,
            'end_age': end_age
        })

    result = {
        'birth_info': {
            'datetime': f'{year}-{month:02d}-{day:02d} {hour:02d}:{minute or 0:02d}',
            'gender': gender,
            'calendar': calendar
        },
        'lunar_date': {
            'year': lunar_year,
            'month': lunar_month,
            'day': lunar_day,
            'is_leap_month': lunar_is_leap
        },
        'year_ganzhi': year_gan + year_zhi,
        'minggong': {
            'ganzhi': minggong_ganzhi,
            'nayin': minggong_nayin,
            'wuxing_ju': wuxing_ju,
            'palace_idx': minggong_idx,
            'palace_zhi': PALACE_ZHI[minggong_idx]
        },
        'shengong': {
            'palace_idx': shengong_idx,
            'palace_zhi': PALACE_ZHI[shengong_idx]
        },
        'ziwei_star_pos': ziwei_idx,
        'tianfu_star_pos': tianfu_idx,
        'all_stars': all_stars,
        'sihua': {k: v['star'] for k, v in sihua.items()},
        'palaces': palaces,
        'daxian': {
            'direction': '顺行' if forward else '逆行',
            'start_age': daxian_start_age,
            'steps': daxian_list
        }
    }

    return result


def main():
    parser = argparse.ArgumentParser(description='紫微斗数排盘计算器')
    parser.add_argument('--year', type=int, required=True)
    parser.add_argument('--month', type=int, required=True)
    parser.add_argument('--day', type=int, required=True)
    parser.add_argument('--hour', type=int, required=True)
    parser.add_argument('--minute', type=int, default=0)
    parser.add_argument('--gender', type=str, default='male', choices=['male', 'female'])
    parser.add_argument('--calendar', type=str, default='solar', choices=['solar', 'lunar'])

    args = parser.parse_args()
    result = calculate_ziwei(args.year, args.month, args.day, args.hour, args.minute, args.gender, args.calendar)
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
