#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""zhouyi_cli_dispatch — CLI 命令分发与 main 入口（行为与拆分前完全一致）。"""

from __future__ import annotations

import argparse
import json
import sys
from typing import List, Optional

from zhouyi_core import API_KEY_ENV, ZhouyiApiError
from zhouyi_cli_args import _emit, build_parser


def _dispatch(client, args: argparse.Namespace) -> None:
    cmd = args.command
    if cmd == "quota":
        _emit(client, client.quota(), args, "quota")
    elif cmd == "calls-recent":
        _emit(client, client.calls_recent(args.limit), args, "calls_recent")
    elif cmd == "geocode":
        _emit(client, client.geocode(args.province, keyword=args.keyword), args, "geocode",
              [args.keyword] if args.keyword else ([args.province] if args.province else None))
    elif cmd == "bazi":
        _emit(client, client.bazi(args.name, args.gender, args.birth_date, args.birth_time,
                                  bloodType=args.blood_type, longitude=args.longitude,
                                  useTrueSolarTime=args.true_solar_time),
              args, "bazi", [args.name, args.birth_date])
    elif cmd == "select-birth-date":
        _emit(client, client.select_birth_date(args.start_date, args.end_date,
                                               args.page, args.page_size),
              args, "select_birth_date")
    elif cmd == "name-test":
        _emit(client, client.name_test(args.surname, args.given_name, args.charset),
              args, "name_test", [args.surname + args.given_name])
    elif cmd == "daystem":
        _emit(client, client.daystem(args.birth_date, args.gan_zhi), args, "daystem",
              [args.gan_zhi or args.birth_date])
    elif cmd == "bone-weight":
        _emit(client, client.bone_weight(args.year, args.month, args.day, args.hour,
                                         args.lunar, args.gender), args, "bone_weight",
              [f"{args.year}"])
    elif cmd == "company-name":
        _emit(client, client.company_name(args.com_name, args.com_pre, args.com_suf),
              args, "company_name", [args.com_name])
    elif cmd == "peach-blossom":
        _emit(client, client.peach_blossom(args.name, args.gender, args.birthday, args.hour),
              args, "peach_blossom", [args.name])
    elif cmd == "dayun":
        _emit(client, client.dayun(args.name, args.gender, args.birth_date, args.birth_time,
                                   args.longitude, args.true_solar_time, args.with_bazi),
              args, "dayun", [args.name])
    elif cmd == "liunian":
        _emit(client, client.liunian(args.name, args.gender, args.birth_date, args.birth_time,
                                     args.dayun_index, args.longitude, args.true_solar_time),
              args, "liunian", [args.name])
    elif cmd == "liuyue":
        _emit(client, client.liuyue(args.name, args.gender, args.birth_date, args.birth_time,
                                    args.dayun_index, args.target_year,
                                    args.longitude, args.true_solar_time),
              args, "liuyue", [args.name, str(args.target_year)])
    elif cmd == "liuri":
        _emit(client, client.liuri(args.name, args.gender, args.birth_date, args.birth_time,
                                   args.target_date, args.target_year_month,
                                   args.longitude, args.true_solar_time),
              args, "liuri", [args.name, args.target_date or args.target_year_month])
    elif cmd == "paipan":
        body = None
        if args.json_body:
            body = json.loads(args.json_body)
        else:
            body = {}
            for key, attr in (("name", "name"), ("gender", "gender"), ("city", "city"),
                              ("mode", "mode"), ("reason", "reason"), ("sex", "sex"),
                              ("fullChart", "full_chart"), ("daYunCount", "da_yun_count"),
                              ("birthDate", "birth_date"), ("birthTime", "birth_time"),
                              ("year", "year"), ("month", "month"), ("day", "day"),
                              ("hour", "hour"), ("minute", "minute"),
                              ("sxId", "sx_id"), ("dy", "dy"), ("paiFa", "pai_fa")):
                value = getattr(args, attr, None)
                if value is not None:
                    body[key] = value
        result = client.paipan(args.paipan_type, body)
        _emit(client, result, args, f"paipan_{args.paipan_type}",
              [body.get("name")] if isinstance(body, dict) and body.get("name") else None)
    elif cmd == "dream":
        _emit(client, client.dream(args.keyword), args, "dream", [args.keyword])
    elif cmd == "lingqian":
        _emit(client, client.lingqian(args.lot_type, args.qian_num), args, "lingqian",
              [args.lot_type] + ([str(args.qian_num)] if args.qian_num else []))
    elif cmd == "zhuge":
        _emit(client, client.zhuge(args.text), args, "zhuge", [args.text])
    elif cmd == "match":
        result = client.match(args.match_type, c1=args.c1, c2=args.c2,
                              name1=args.name1, name2=args.name2,
                              sex1=args.sex1, sex2=args.sex2,
                              z1=args.z1, z2=args.z2, bt1=args.bt1, bt2=args.bt2,
                              qq1=args.qq1, qq2=args.qq2)
        _emit(client, result, args, f"match_{args.match_type}")
    elif cmd == "huangli":
        if bool(args.start_date) != bool(args.end_date):
            raise ZhouyiApiError(40001, "本地参数校验：--start-date 与 --end-date 需同时提供（区间上限 92 天）")
        if args.date or args.year:
            key_params = [args.date or f"{args.year}-{args.month:02d}"]
        elif args.start_date:
            key_params = [f"{args.start_date}~{args.end_date}"]
        else:
            key_params = None
        _emit(client, client.huangli(args.date, args.year, args.month,
                                     startDate=args.start_date, endDate=args.end_date),
              args, "huangli", key_params)
    elif cmd == "three-life-wealth":
        _emit(client, client.three_life_wealth(args.year, args.month, args.day),
              args, "three_life_wealth", [f"{args.year}"])
    elif cmd == "baby-gender":
        _emit(client, client.baby_gender(args.age, args.month, args.gender, args.best_months),
              args, "baby_gender", [f"{args.age}"])
    elif cmd == "number-luck":
        _emit(client, client.number_luck(args.number), args, "number_luck", [args.number])
    elif cmd == "fingerprint":
        _emit(client, client.fingerprint(args.code, args.gender), args, "fingerprint",
              [args.code])
    elif cmd == "omen":
        _emit(client, client.omen(args.omen_type, args.hour, args.side), args, "omen",
              [args.omen_type])
    elif cmd == "zodiac-personality":
        _emit(client, client.zodiac_personality(args.animal), args, "zodiac_personality",
              [args.animal])
    elif cmd == "qiming":
        _emit(client, client.qiming(args.surname, args.name_type,
                                    zuhe=args.zuhe,
                                    spec=args.spec, specWord=args.spec_word,
                                    wxFirst=args.wx_first, wxSec=args.wx_sec, score=args.score,
                                    sancaiJixiong=args.sancai_jixiong,
                                    rengeJixiong=args.renge_jixiong,
                                    digeJixiong=args.dige_jixiong,
                                    waigeJixiong=args.waige_jixiong,
                                    zonggeJixiong=args.zongge_jixiong,
                                    jichuyunJixiong=args.jichuyun_jixiong,
                                    chenggongyunJixiong=args.chenggongyun_jixiong,
                                    shejiaoyunJixiong=args.shejiaoyun_jixiong),
              args, "qiming", [args.surname])
    elif cmd == "idcard":
        _emit(client, client.idcard_parse(args.id_card), args, "idcard_parse", [args.id_card])
    elif cmd == "shishen-lunming":
        _emit(client, client.shishen_lunming(args.name, args.gender, args.birth_date, args.birth_time,
                                             longitude=args.longitude, city=args.city,
                                             useTrueSolarTime=args.true_solar_time, lang=args.lang),
              args, "shishen_lunming", [args.name])
    elif cmd == "fortune-chart":
        _emit(client, client.fortune_chart(args.mode, args.gender, args.birth_date, args.birth_time,
                                          specDate=args.spec_date),
              args, "fortune_chart", [args.mode, args.birth_date])
    else:  # pragma: no cover
        raise ZhouyiApiError(-1, f"未知命令: {cmd}")


def main(argv: Optional[List[str]] = None) -> int:
    from zhouyi import ZhouyiClient

    parser = build_parser()
    args = parser.parse_args(argv)
    if not args.command:
        parser.print_help()
        return 1
    try:
        client = ZhouyiClient(base_url=args.base_url, api_key=args.api_key,
                              open_source=args.open_source, timeout=args.timeout,
                              config_path=args.config)
    except (ValueError, OSError):
        print("错误：配置文件或服务地址/超时格式错误，请检查配置。", file=sys.stderr)
        return 2
    if not client.api_key:
        print(f"错误：未提供 API-KEY。请使用 --api-key 参数、环境变量 {API_KEY_ENV}"
              " 或包内 config.yaml（官网 https://iching.jiuchongju.com 注册获取）。", file=sys.stderr)
        return 2
    try:
        _dispatch(client, args)
    except ZhouyiApiError as exc:
        print(f"调用失败: {exc}", file=sys.stderr)
        if exc.code == 42901:
            print("提示：免费额度 500 次/日已用尽，请明日再试或联系官网升级额度。", file=sys.stderr)
        return 1
    return 0
