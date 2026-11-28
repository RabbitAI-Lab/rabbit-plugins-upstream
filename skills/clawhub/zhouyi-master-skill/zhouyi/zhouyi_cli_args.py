#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""zhouyi_cli_args — CLI 参数解析（32 个子命令定义，与拆分前完全一致）。"""

from __future__ import annotations

import argparse
import json
import sys
from typing import Dict, List, Optional

from zhouyi_core import API_KEY_ENV, DEFAULT_BASE_URL, DEFAULT_OPEN_SOURCE


def _add_common_args(parser: argparse.ArgumentParser) -> None:
    parser.add_argument("--config", default=None, help="配置文件路径（默认自动读取包内 config.yaml）")
    parser.add_argument("--base-url", default=None,
                        help=f"服务根地址（参数 > ZHOUYI_BASE_URL > config.yaml > {DEFAULT_BASE_URL}）")
    parser.add_argument("--api-key", default=None,
                        help=f"API-KEY（默认读环境变量 {API_KEY_ENV}，官网注册获取）")
    parser.add_argument("--open-source", default=None,
                        help="X-Open-Source 来源标识（默认 skill）")
    parser.add_argument("--timeout", type=float, default=None, help="超时秒数（参数 > ZHOUYI_TIMEOUT > config.yaml > 30）")
    parser.add_argument("--save-html", metavar="DIR", default=None,
                        help="将 render.html 保存到指定目录")
    parser.add_argument("--raw", action="store_true", help="输出完整 JSON 响应（默认仅输出 data）")


def _print_result(result: Dict, raw: bool) -> None:
    payload = result if raw else result.get("data")
    print(json.dumps(payload, ensure_ascii=False, indent=2))
    render = result.get("render") or {}
    if isinstance(render, dict) and render.get("html"):
        print(f"\n[render.html] 可用 --save-html <目录> 保存（长度 {len(render['html'])} 字符）",
              file=sys.stderr)


def _emit(client, result: Dict, args: argparse.Namespace,
          func_name: str, key_params: Optional[List[str]] = None) -> None:
    _print_result(result, args.raw)
    if args.save_html:
        path = client.save_render(result, output_dir=args.save_html,
                                  func_name=func_name, key_params=key_params)
        print(f"[已保存 HTML] {path}", file=sys.stderr)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="zhouyi_client.py",
        description="周易大师开放平台 CLI（49 项功能 / X-API-Key 鉴权 / 免费 500 次每日）",
        epilog=f"环境变量 {API_KEY_ENV} 提供 API-KEY；--help 查看各命令参数。")
    sub = parser.add_subparsers(dest="command", metavar="<command>")

    def new(name: str, help_text: str) -> argparse.ArgumentParser:
        p = sub.add_parser(name, help=help_text, description=help_text)
        _add_common_args(p)
        return p

    # --- 支撑接口 ---
    p = new("quota", "额度查询（限额/已用/剩余，不消耗额度）")
    p = new("calls-recent", "最近调用记录")
    p.add_argument("--limit", type=int, default=10, help="条数（默认 10，上限 100）")

    # --- F1 地理编码 ---
    p = new("geocode", "F1 出生地经纬度（模糊检索/省市级联）")
    p.add_argument("--keyword", default=None,
                   help="自由文本关键词（城市/省份模糊检索，最多 20 条，优先于 --province，如 北京）")
    p.add_argument("--province", default=None, help="省份名，缺省返回省份列表")

    # --- F3 八字 ---
    p = new("bazi", "F3 八字测算")
    p.add_argument("--name", required=True)
    p.add_argument("--gender", required=True, help="男/女")
    p.add_argument("--birth-date", required=True, help="yyyy-MM-dd")
    p.add_argument("--birth-time", required=True, help="HH:mm")
    p.add_argument("--blood-type", default=None)
    p.add_argument("--longitude", type=float, default=None)
    p.add_argument("--true-solar-time", action="store_true", default=None, help="使用真太阳时")

    # --- F4 优生择吉 ---
    p = new("select-birth-date", "F4 优生择吉")
    p.add_argument("--start-date", default=None, help="yyyy-MM-dd")
    p.add_argument("--end-date", default=None, help="yyyy-MM-dd")
    p.add_argument("--page", type=int, default=None)
    p.add_argument("--page-size", type=int, default=None)

    # --- F5/F6 姓名测试 ---
    p = new("name-test", "F5/F6 姓名测试")
    p.add_argument("--surname", required=True, help="姓")
    p.add_argument("--given-name", required=True, help="名")
    p.add_argument("--charset", choices=["simplified", "kangxi"], default="simplified",
                   help="simplified=简体笔画(F5) / kangxi=康熙字典(F6)")

    # --- F7 日干论命 ---
    p = new("daystem", "F7 日干论命（birthDate 与 ganZhi 二选一）")
    p.add_argument("--birth-date", default=None, help="yyyy-MM-dd")
    p.add_argument("--gan-zhi", default=None, help="干支，如 甲子")

    # --- F8 称骨 ---
    p = new("bone-weight", "F8 称骨论命")
    p.add_argument("--year", type=int, required=True)
    p.add_argument("--month", type=int, default=None)
    p.add_argument("--day", type=int, default=None)
    p.add_argument("--hour", type=int, default=None, help="24 小时制")
    p.add_argument("--lunar", action="store_true", default=None, help="农历")
    p.add_argument("--gender", default=None)

    # --- F9 企业起名 ---
    p = new("company-name", "F9 企业起名")
    p.add_argument("--com-name", required=True, help="企业核心名")
    p.add_argument("--com-pre", default=None, help="前缀（如 北京）")
    p.add_argument("--com-suf", default=None, help="后缀（如 有限公司）")

    # --- F10 桃花 ---
    p = new("peach-blossom", "F10 桃花运势")
    p.add_argument("--name", required=True)
    p.add_argument("--gender", required=True)
    p.add_argument("--birthday", required=True, help="yyyy-MM-dd")
    p.add_argument("--hour", type=int, required=True, help="0-23")

    # --- F11–F14 大运/流年/流月/流日 ---
    def yunshi_args(sp, extras):
        sp.add_argument("--name", required=True)
        sp.add_argument("--gender", required=True)
        sp.add_argument("--birth-date", required=True, help="yyyy-MM-dd")
        sp.add_argument("--birth-time", required=True, help="HH:mm")
        sp.add_argument("--longitude", type=float, default=None)
        sp.add_argument("--true-solar-time", action="store_true", default=None)
        for args_, kwargs_ in extras:
            sp.add_argument(*args_, **kwargs_)

    p = new("dayun", "F11 大运")
    yunshi_args(p, [(("--with-bazi",), {"action": "store_true", "default": True,
                                        "help": "附带八字基础信息（默认开启，与移动端页面口径一致）"}),
                    (("--no-with-bazi",), {"action": "store_false", "dest": "with_bazi",
                                            "help": "显式关闭附带八字基础信息"})])

    p = new("liunian", "F12 流年")
    yunshi_args(p, [(("--dayun-index",), {"type": int, "required": True, "help": "大运序号 0-9"})])

    p = new("liuyue", "F13 流月")
    yunshi_args(p, [(("--dayun-index",), {"type": int, "required": True, "help": "大运序号 0-9"}),
                    (("--target-year",), {"type": int, "required": True, "help": "目标年份"})])

    p = new("liuri", "F14 流日（target-date 与 target-year-month 二选一）")
    yunshi_args(p, [(("--target-date",), {"default": None, "help": "yyyy-MM-dd 单日含流时"}),
                    (("--target-year-month",), {"default": None, "help": "yyyy-MM 整月"})])

    # --- F15–F21 排盘 ---
    p = new("paipan", "F15–F21 排盘统一入口（bazi/liuyao/liuren/qimen/feixing/ziwei/jinkoujue）")
    p.add_argument("--type", required=True, dest="paipan_type",
                   choices=["bazi", "liuyao", "liuren", "qimen", "feixing", "ziwei", "jinkoujue"])
    p.add_argument("--name", default=None)
    p.add_argument("--gender", default=None)
    p.add_argument("--birth-date", default=None, help="yyyy-MM-dd（bazi/ziwei 必填）")
    p.add_argument("--birth-time", default=None, help="HH:mm（bazi/ziwei 必填）")
    p.add_argument("--city", default=None)
    p.add_argument("--full-chart", action="store_true", default=None)
    p.add_argument("--da-yun-count", type=int, default=None)
    p.add_argument("--year", type=int, default=None, help="liuyao/liuren/qimen/jinkoujue 用")
    p.add_argument("--month", type=int, default=None)
    p.add_argument("--day", type=int, default=None)
    p.add_argument("--hour", type=int, default=None)
    p.add_argument("--minute", type=int, default=None)
    p.add_argument("--sex", default=None,
                   help="liuyao 用（男/女）；liuren/jinkoujue 为整数 1=男/0=女（后端口径，旧写法 2=女 服务端自动归一为 0）")
    p.add_argument("--reason", default=None, help="liuyao 占事")
    p.add_argument("--mode", default=None, help="qimen：zhuanpan|feigong")
    p.add_argument("--sx-id", type=int, default=None, help="feixing：二十四山编号 0-23")
    p.add_argument("--dy", type=int, default=None, help="feixing：大运序号 0-8")
    p.add_argument("--pai-fa", type=int, default=None, help="feixing：1=下卦 2=替卦")
    p.add_argument("--json", dest="json_body", default=None,
                   help="完整 JSON 请求体（优先于其他参数，字段名与后端一致）")

    # --- F22 解梦 ---
    p = new("dream", "F22 周公解梦")
    p.add_argument("--keyword", required=True)

    # --- F23–F27 灵签 ---
    p = new("lingqian", "F23–F27 灵签")
    p.add_argument("--lot-type", required=True,
                   choices=["guanyin", "lvzu", "huangdaxian", "guandi", "mazu"])
    p.add_argument("--qian-num", type=int, default=None, help="指定签号（妈祖 1-60，观音/关帝/吕祖/黄大仙 1-100）")

    # --- F28 诸葛神数 ---
    p = new("zhuge", "F28 诸葛神数")
    p.add_argument("--text", required=True, help="1–3 个汉字")

    # --- F29–F34 配对 ---
    p = new("match", "F29–F34 配对")
    p.add_argument("--match-type", required=True,
                   choices=["astro", "name", "wuge", "zodiac", "blood", "qq"])
    p.add_argument("--c1", default=None, help="astro：星座1")
    p.add_argument("--c2", default=None, help="astro：星座2")
    p.add_argument("--name1", default=None, help="name/wuge：姓名1")
    p.add_argument("--name2", default=None, help="name/wuge：姓名2")
    p.add_argument("--sex1", default=None, help="wuge 可选")
    p.add_argument("--sex2", default=None, help="wuge 可选")
    p.add_argument("--z1", default=None, help="zodiac：生肖1")
    p.add_argument("--z2", default=None, help="zodiac：生肖2")
    p.add_argument("--bt1", default=None, help="blood：血型1 A/B/O/AB")
    p.add_argument("--bt2", default=None, help="blood：血型2 A/B/O/AB")
    p.add_argument("--qq1", default=None)
    p.add_argument("--qq2", default=None)

    # --- F35 黄历 ---
    p = new("huangli", "F35 黄道日历（date 单日；year+month 月度视图；start-date+end-date 区间）")
    p.add_argument("--date", default=None, help="yyyy-MM-dd，缺省今天（单日详情含十二时辰）")
    p.add_argument("--year", type=int, default=None)
    p.add_argument("--month", type=int, default=None)
    p.add_argument("--start-date", default=None,
                   help="区间起始日期（yyyy-MM-dd，需与 --end-date 同时提供，上限 92 天）")
    p.add_argument("--end-date", default=None, help="区间结束日期（yyyy-MM-dd，需与 --start-date 同时提供）")

    # --- F36 三世财运 ---
    p = new("three-life-wealth", "F36 三世财运")
    p.add_argument("--year", type=int, required=True)
    p.add_argument("--month", type=int, default=None)
    p.add_argument("--day", type=int, default=None)

    # --- F37 生男生女 ---
    p = new("baby-gender", "F37 生男生女")
    p.add_argument("--age", type=int, required=True, help="母亲虚岁")
    p.add_argument("--month", type=int, default=None, help="农历怀孕月")
    p.add_argument("--gender", default=None)
    p.add_argument("--best-months", action="store_true", default=None, help="查适宜月份")

    # --- F38 号码吉凶 ---
    p = new("number-luck", "F38 号码吉凶")
    p.add_argument("--number", required=True)

    # --- F39 指纹 ---
    p = new("fingerprint", "F39 指纹算命")
    p.add_argument("--code", required=True, help="5 位 O/X 序列")
    p.add_argument("--gender", default=None)

    # --- F40–F44 征兆 ---
    p = new("omen", "F40–F44 民俗征兆")
    p.add_argument("--omen-type", required=True, choices=["耳鸣", "眼跳", "心惊", "面热", "喷嚏"])
    p.add_argument("--hour", type=int, required=True, help="时辰 1-12")
    p.add_argument("--side", choices=["左", "右"], default=None, help="耳鸣/眼跳必填")

    # --- F45 属相性格 ---
    p = new("zodiac-personality", "F45 属相性格")
    p.add_argument("--animal", required=True, help="属相名，如 龙")

    # --- F46 周易起名 ---
    JX_CHOICES = ["0", "大吉", "中吉", "半吉", "平", "凶", "大凶"]
    p = new("qiming", "F46 周易起名（默认仅返回笔画组合列表；传 --zuhe 查看该组合推荐用字）")
    p.add_argument("--surname", required=True, help="姓氏（1–2 字，单姓/复姓）")
    p.add_argument("--name-type", required=True, choices=["single", "double"],
                   help="single 单名 / double 双名")
    p.add_argument("--zuhe", default=None,
                   help="要查看推荐汉字的笔画组合（如 11-28-24）；缺省仅返回笔画组合列表")
    p.add_argument("--spec", type=int, default=None, choices=[0, 1, 2],
                   help="指定名字的字：0-不指定，1-第一个字，2-第二个字")
    p.add_argument("--spec-word", default=None, help="指定的名字字内容（spec≠0 时搭配）")
    p.add_argument("--wx-first", type=int, default=None, choices=range(0, 6),
                   help="首字五行：0-忽略，1-金，2-木，3-水，4-火，5-土")
    p.add_argument("--wx-sec", type=int, default=None, choices=range(0, 6),
                   help="第二个字五行（取值同 wx-first）")
    p.add_argument("--score", type=int, default=None, choices=[0, 90, 80, 70],
                   help="格局分数：0-忽略，或 90/80/70")
    p.add_argument("--sancai-jixiong", default=None, choices=JX_CHOICES,
                   help="三才配置吉凶（0-忽略）")
    p.add_argument("--renge-jixiong", default=None, choices=JX_CHOICES, help="人格吉凶（0-忽略）")
    p.add_argument("--dige-jixiong", default=None, choices=JX_CHOICES, help="地格吉凶（0-忽略）")
    p.add_argument("--waige-jixiong", default=None, choices=JX_CHOICES, help="外格吉凶（0-忽略）")
    p.add_argument("--zongge-jixiong", default=None, choices=JX_CHOICES, help="总格吉凶（0-忽略）")
    p.add_argument("--jichuyun-jixiong", default=None,
                   choices=["0", "大吉", "中吉", "凶", "大凶"], help="基础运吉凶（0-忽略）")
    p.add_argument("--chenggongyun-jixiong", default=None,
                   choices=["0", "大吉", "中吉", "半吉", "凶", "大凶"], help="成功运吉凶（0-忽略）")
    p.add_argument("--shejiaoyun-jixiong", default=None,
                   choices=["0", "大吉", "中吉", "半吉", "凶", "大凶"], help="社交运吉凶（0-忽略）")

    # --- F47 身份证解析 ---
    p = new("idcard", "F47 身份证解析（18 位身份证号；属敏感信息，服务端日志已脱敏）")
    p.add_argument("--id-card", required=True, help="18 位身份证号")

    # --- F48 十神论命 ---
    p = new("shishen-lunming", "F48 十神论命（日主旺衰/十神心性/四宫位条款，文案三语）")
    p.add_argument("--name", required=True)
    p.add_argument("--gender", required=True, help="male/female（兼容 男/女）")
    p.add_argument("--birth-date", required=True, help="yyyy-MM-dd")
    p.add_argument("--birth-time", required=True, help="HH:mm")
    p.add_argument("--longitude", type=float, default=None, help="出生地经度（配合真太阳时）")
    p.add_argument("--city", default=None, help="出生地城市（可选）")
    p.add_argument("--true-solar-time", action="store_true", default=None, help="使用真太阳时")
    p.add_argument("--lang", choices=["zh-CN", "zh-TW", "en-US"], default=None,
                   help="输出语言（缺省 zh-CN）")

    # --- F49 运势图 ---
    p = new("fortune-chart", "F49 运势图（月运12点/日运14点/一生大运及流年）")
    p.add_argument("--mode", required=True, choices=["monthly", "daily", "lifetime"])
    p.add_argument("--gender", required=True, help="male/female（兼容 男/女）")
    p.add_argument("--birth-date", required=True, help="yyyy-MM-dd")
    p.add_argument("--birth-time", required=True, help="HH:mm")
    p.add_argument("--spec-date", default=None, help="yyyy-MM-dd，缺省当天；lifetime 忽略")

    return parser
