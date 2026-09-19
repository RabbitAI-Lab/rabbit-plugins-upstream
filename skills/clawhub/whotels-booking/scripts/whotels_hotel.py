# -*- coding: utf-8 -*-
"""
W酒店技能 - ClawHub版（服务调整版）
原数据源：原品牌酒店数据专区（原品牌数据专区已暂停第三方调用）
当前状态：万豪品牌专属查询已下线，引导用户使用通用酒店搜索工具
保留原3个工具入口（search/detail/packages）避免历史调用报错
"""
import json
import sys

BRAND_NAME = "W酒店"
BRAND_KEYWORDS = "W酒店/W Hotels"

SERVICE_NOTICE = (
    "⚠️ W酒店专属查询服务已调整\n\n"
    "因原数据源（原品牌酒店数据专区）暂停第三方调用，本技能的万豪品牌专属搜索、酒店详情、套餐查询功能暂时下线。\n\n"
    "🏨 您仍可通过以下方式查询W酒店/W Hotels等酒店：\n\n"
    "1. 【推荐】使用「全球酒店搜索与推荐」技能\n"
    "   • 覆盖全球200万+酒店，支持按品牌名、城市、地标搜索\n"
    "   • 直接搜索\"W酒店\"即可找到对应酒店\n"
    "   • 提供实时价格、评分、房型和预订链接\n\n"
    "2. 使用「酒店比价」技能\n"
    "   • 跨多个旅行平台实时比价（途牛/同程/RollingGo等）\n"
    "   • 同一酒店对比不同平台价格，找最低价\n\n"
    "3. 使用「途牛旅行」或「同程旅行」技能\n"
    "   • 搜索酒店名称，查询实时房价和可预订房型\n\n"
    "💡 提示：直接告诉我您想查询的城市+品牌（如\"上海W酒店\"），可调用通用酒店技能为您查询。"
).format(brand_cn=BRAND_NAME, brand_kw=BRAND_KEYWORDS, first_kw=BRAND_KEYWORDS.split("/")[0])


def search_hotels(destName=None, checkInDate=None, checkOutDate=None,
                  keyword=None, maxPrice=None, sort=None, limit=10, **kwargs):
    """酒店搜索（已调整，返回引导提示）"""
    return SERVICE_NOTICE


def get_hotel_info(shid=None, hotelName=None, reviewKeyword=None, **kwargs):
    """酒店详情（已调整，返回引导提示）"""
    return SERVICE_NOTICE


def search_packages(keyword=None, hotelName=None,
                    provinceOrCity=None, sort=None, limit=10, **kwargs):
    """套餐搜索（已调整，返回引导提示）"""
    return SERVICE_NOTICE


search_whotels_hotels = search_hotels
get_whotels_hotel_info = get_hotel_info
search_whotels_packages = search_packages


def main():
    if len(sys.argv) < 3:
        print("用法: python whotels_hotel.py <tool> <args_json>")
        print("  tool: search | detail | packages")
        print("  注：万豪品牌专属服务已调整，将返回替代方案引导")
        return

    tool = sys.argv[1]
    try:
        args = json.loads(sys.argv[2]) if len(sys.argv) > 2 else {}
    except json.JSONDecodeError:
        args = {}

    if tool == "search":
        print(search_hotels(**args))
    elif tool == "detail":
        print(get_hotel_info(**args))
    elif tool == "packages":
        print(search_packages(**args))
    else:
        print(SERVICE_NOTICE)


if __name__ == "__main__":
    main()
