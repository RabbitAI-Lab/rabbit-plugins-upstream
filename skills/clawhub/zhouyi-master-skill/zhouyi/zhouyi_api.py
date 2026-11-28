#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""zhouyi_api — 49 项开放 API 功能方法 Mixin（F1–F49，方法与拆分前一一对应）。"""

from __future__ import annotations

from typing import Any, Dict, Optional

from zhouyi_core import ZhouyiApiError


class OpenApiMixin:
    """开放 API 功能方法（依赖传输层的 _get/_post）。"""

    # ==================== 支撑接口（不消耗额度） ====================

    def quota(self) -> Dict:
        """额度查询：限额/已用/剩余/有效期。GET /api/open/quota"""
        return self._get("/api/open/quota")

    def calls_recent(self, limit: int = 10) -> Dict:
        """最近调用记录（limit 默认 10，上限 100）。GET /api/open/calls/recent"""
        return self._get("/api/open/calls/recent", {"limit": limit})

    # ==================== F1 地理编码 ====================

    def geocode(self, province: Optional[str] = None, keyword: Optional[str] = None) -> Dict:
        """F1 出生地经纬度：传 keyword 按城市/省份模糊检索（最多 20 条，优先于 province）；
        缺省 province 返回省份列表，指定则返回该省城市（含经纬度）。"""
        return self._post("/api/open/geocode", {"province": province, "keyword": keyword})

    # ==================== F3–F9 算命类 ====================

    def bazi(self, name: str, gender: str, birthDate: str, birthTime: str,
             bloodType: Optional[str] = None, longitude: Optional[float] = None,
             useTrueSolarTime: Optional[bool] = None) -> Dict:
        """F3 八字测算。birthDate=yyyy-MM-dd，birthTime=HH:mm。"""
        return self._post("/api/open/fortune/bazi", {
            "name": name, "gender": gender, "birthDate": birthDate, "birthTime": birthTime,
            "bloodType": bloodType, "longitude": longitude, "useTrueSolarTime": useTrueSolarTime,
        })

    def select_birth_date(self, startDate: Optional[str] = None, endDate: Optional[str] = None,
                          page: Optional[int] = None, pageSize: Optional[int] = None) -> Dict:
        """F4 优生择吉。startDate/endDate=yyyy-MM-dd，均可选。"""
        return self._post("/api/open/select/birth-date", {
            "startDate": startDate, "endDate": endDate, "page": page, "pageSize": pageSize,
        })

    def name_test(self, surname: str, givenName: str, charset: str = "simplified") -> Dict:
        """F5/F6 姓名测试。charset=simplified(简体笔画)/kangxi(康熙字典繁体笔画)。"""
        return self._post("/api/open/name/test", {
            "surname": surname, "givenName": givenName, "charset": charset,
        })

    def daystem(self, birthDate: Optional[str] = None, ganZhi: Optional[str] = None) -> Dict:
        """F7 日干论命。birthDate(yyyy-MM-dd) 与 ganZhi(如 甲子) 二选一。"""
        if not birthDate and not ganZhi:
            raise ZhouyiApiError(40001, "本地参数校验：birthDate 与 ganZhi 二选一必填")
        return self._post("/api/open/fortune/daystem", {"birthDate": birthDate, "ganZhi": ganZhi})

    def bone_weight(self, year: int, month: Optional[int] = None, day: Optional[int] = None,
                    hour: Optional[int] = None, isLunar: Optional[bool] = None,
                    gender: Optional[str] = None) -> Dict:
        """F8 称骨论命。hour 为 24 小时制，isLunar 是否农历。"""
        return self._post("/api/open/fortune/bone-weight", {
            "year": year, "month": month, "day": day, "hour": hour,
            "isLunar": isLunar, "gender": gender,
        })

    def company_name(self, comName: str, comPre: Optional[str] = None,
                     comSuf: Optional[str] = None) -> Dict:
        """F9 企业起名。comName 为核心名（必填），comPre/comSuf 为前后缀（可选）。"""
        return self._post("/api/open/name/company", {
            "comName": comName, "comPre": comPre, "comSuf": comSuf,
        })

    # ==================== F10–F14 运势类 ====================

    def peach_blossom(self, name: str, gender: str, birthday: str, hour: int) -> Dict:
        """F10 桃花运势。birthday=yyyy-MM-dd，hour=0-23。"""
        return self._post("/api/open/fortune/peach-blossom", {
            "name": name, "gender": gender, "birthday": birthday, "hour": hour,
        })

    def _yunshi_base(self, name: str, gender: str, birthDate: str, birthTime: str,
                     longitude: Optional[float], useTrueSolarTime: Optional[bool]) -> Dict:
        return {
            "name": name, "gender": gender, "birthDate": birthDate, "birthTime": birthTime,
            "longitude": longitude, "useTrueSolarTime": useTrueSolarTime,
        }

    def dayun(self, name: str, gender: str, birthDate: str, birthTime: str,
              longitude: Optional[float] = None, useTrueSolarTime: Optional[bool] = None,
              withBazi: Optional[bool] = None) -> Dict:
        """F11 大运。withBazi=true 时附带八字基础信息。"""
        body = self._yunshi_base(name, gender, birthDate, birthTime, longitude, useTrueSolarTime)
        body["withBazi"] = withBazi
        return self._post("/api/open/fortune/dayun", body)

    def liunian(self, name: str, gender: str, birthDate: str, birthTime: str, dayunIndex: int,
                longitude: Optional[float] = None, useTrueSolarTime: Optional[bool] = None) -> Dict:
        """F12 流年。dayunIndex 大运序号（0-9）。"""
        body = self._yunshi_base(name, gender, birthDate, birthTime, longitude, useTrueSolarTime)
        body["dayunIndex"] = dayunIndex
        return self._post("/api/open/fortune/liunian", body)

    def liuyue(self, name: str, gender: str, birthDate: str, birthTime: str,
               dayunIndex: int, targetYear: int,
               longitude: Optional[float] = None, useTrueSolarTime: Optional[bool] = None) -> Dict:
        """F13 流月。dayunIndex 大运序号（0-9），targetYear 目标年份。"""
        body = self._yunshi_base(name, gender, birthDate, birthTime, longitude, useTrueSolarTime)
        body["dayunIndex"] = dayunIndex
        body["targetYear"] = targetYear
        return self._post("/api/open/fortune/liuyue", body)

    def liuri(self, name: str, gender: str, birthDate: str, birthTime: str,
              targetDate: Optional[str] = None, targetYearMonth: Optional[str] = None,
              longitude: Optional[float] = None, useTrueSolarTime: Optional[bool] = None) -> Dict:
        """F14 流日。targetDate(yyyy-MM-dd 单日含流时) 与 targetYearMonth(yyyy-MM 整月) 二选一。"""
        if not targetDate and not targetYearMonth:
            raise ZhouyiApiError(40001, "本地参数校验：targetDate 与 targetYearMonth 二选一必填")
        body = self._yunshi_base(name, gender, birthDate, birthTime, longitude, useTrueSolarTime)
        body["targetDate"] = targetDate
        body["targetYearMonth"] = targetYearMonth
        return self._post("/api/open/fortune/liuri", body)

    # ==================== F15–F21 排盘类（统一入口 type） ====================

    def paipan(self, type: str, params: Optional[Dict[str, Any]] = None, **extra) -> Dict:
        """F15–F21 排盘统一入口。POST /api/open/paipan/{type}

        :param type: bazi|liuyao|liuren|qimen|feixing|ziwei|jinkoujue
        :param params: 请求体字典（字段名与后端一致），也可用关键字参数补充
        """
        if type not in ("bazi", "liuyao", "liuren", "qimen", "feixing", "ziwei", "jinkoujue"):
            raise ZhouyiApiError(40001,
                                 "本地参数校验：type 取值必须为 bazi|liuyao|liuren|qimen|feixing|ziwei|jinkoujue")
        body = dict(params or {})
        body.update({k: v for k, v in extra.items() if v is not None})
        return self._post(f"/api/open/paipan/{type}", body)

    def paipan_bazi(self, name: str, gender: str, birthDate: str, birthTime: str,
                    longitude: Optional[float] = None, city: Optional[str] = None,
                    useTrueSolarTime: Optional[bool] = None, fullChart: Optional[bool] = None,
                    daYunCount: Optional[int] = None) -> Dict:
        """F15 八字排盘（name/gender/birthDate/birthTime 必填）。"""
        return self.paipan("bazi", {
            "name": name, "gender": gender, "birthDate": birthDate, "birthTime": birthTime,
            "longitude": longitude, "city": city, "useTrueSolarTime": useTrueSolarTime,
            "fullChart": fullChart, "daYunCount": daYunCount,
        })

    # ==================== F22–F28 抽签类 ====================

    def dream(self, keyword: str) -> Dict:
        """F22 周公解梦（关键词检索式）。"""
        return self._post("/api/open/dream", {"keyword": keyword})

    def lingqian(self, lotType: str, qianNum: Optional[int] = None) -> Dict:
        """F23–F27 灵签。lotType=guanyin|lvzu|huangdaxian|guandi|mazu；
        五种签均支持指定签号（妈祖 1-60，观音/关帝/吕祖/黄大仙 1-100）。"""
        return self._post("/api/open/lingqian", {"lotType": lotType, "qianNum": qianNum})

    def zhuge(self, text: str) -> Dict:
        """F28 诸葛神数。text 为 1–3 个汉字。"""
        return self._post("/api/open/zhuge", {"text": text})

    # ==================== F29–F34 配对类 ====================

    def match(self, matchType: str, **fields) -> Dict:
        """F29–F34 配对。matchType=astro|name|wuge|zodiac|blood|qq；
        字段按类型传：astro→c1/c2，name/wuge→name1/name2(wuge 可选 sex1/sex2)，
        zodiac→z1/z2，blood→bt1/bt2，qq→qq1/qq2。"""
        body = {"matchType": matchType}
        for key in ("c1", "c2", "name1", "name2", "sex1", "sex2",
                    "z1", "z2", "bt1", "bt2", "qq1", "qq2"):
            if fields.get(key) is not None:
                body[key] = fields[key]
        return self._post("/api/open/match", body)

    # ==================== F35–F45 民俗预测类 ====================

    def huangli(self, date: Optional[str] = None, year: Optional[int] = None,
                month: Optional[int] = None, startDate: Optional[str] = None,
                endDate: Optional[str] = None) -> Dict:
        """F35 黄道日历。date=yyyy-MM-dd 单日详情（缺省今天，含十二时辰）；
        year+month 月度视图；startDate+endDate 区间批量（需同时提供，上限 92 天）。"""
        return self._get("/api/open/huangli", {"date": date, "year": year, "month": month,
                                              "startDate": startDate, "endDate": endDate})

    def three_life_wealth(self, year: int, month: Optional[int] = None,
                          day: Optional[int] = None) -> Dict:
        """F36 三世财运（阳历出生年月日）。"""
        return self._post("/api/open/wealth/three-life", {"year": year, "month": month, "day": day})

    def baby_gender(self, age: int, month: Optional[int] = None, gender: Optional[str] = None,
                    bestMonths: Optional[bool] = None) -> Dict:
        """F37 生男生女。age=母亲虚岁，month=农历怀孕月；bestMonths=true 查适宜月份。"""
        return self._post("/api/open/predict/baby-gender", {
            "age": age, "month": month, "gender": gender, "bestMonths": bestMonths,
        })

    def number_luck(self, number: str) -> Dict:
        """F38 号码吉凶（仅数字）。"""
        return self._post("/api/open/number-luck", {"number": number})

    def fingerprint(self, code: str, gender: Optional[str] = None) -> Dict:
        """F39 指纹算命。code 为 5 位 O/X 序列（O=斗/箩，X=簸箕）。"""
        return self._post("/api/open/fingerprint", {"code": code, "gender": gender})

    def omen(self, omenType: str, hour: int, side: Optional[str] = None) -> Dict:
        """F40–F44 民俗征兆。omenType=耳鸣|眼跳|心惊|面热|喷嚏，hour=时辰 1–12；
        side(左/右) 仅耳鸣/眼跳必填。"""
        return self._post("/api/open/omen", {"omenType": omenType, "hour": hour, "side": side})

    def zodiac_personality(self, animal: str) -> Dict:
        """F45 属相性格。animal 为属相名（如 龙）。"""
        return self._get("/api/open/zodiac-personality", {"animal": animal})

    # ==================== F46–F48 起名/身份证解析/十神论命 ====================

    def qiming(self, surname: str, nameType: str, zuhe: Optional[str] = None,
               spec: Optional[int] = None,
               specWord: Optional[str] = None, wxFirst: Optional[int] = None,
               wxSec: Optional[int] = None, score: Optional[int] = None,
               sancaiJixiong: Optional[str] = None, rengeJixiong: Optional[str] = None,
               digeJixiong: Optional[str] = None, waigeJixiong: Optional[str] = None,
               zonggeJixiong: Optional[str] = None, jichuyunJixiong: Optional[str] = None,
               chenggongyunJixiong: Optional[str] = None,
               shejiaoyunJixiong: Optional[str] = None) -> Dict:
        """F46 周易起名。surname 姓氏（1–2 字），nameType=single 单名/double 双名；
        zuhe 为空仅返回笔画组合列表（不含候选字）；传入某组合（如 11-28-24）时仅返回该组合的候选汉字；
        spec 0-不指定/1-第一个字/2-第二个字（搭配 specWord）；wxFirst/wxSec 0-忽略，1-金，2-木，3-水，4-火，5-土；
        8 个吉凶筛选字段为 string 枚举（0-忽略，或 大吉/中吉/半吉/平/凶/大凶，基础运/成功运/社交运无半吉）；
        score 0-忽略或 90/80/70。"""
        return self._post("/api/open/name/qiming", {
            "surname": surname, "nameType": nameType, "zuhe": zuhe,
            "spec": spec, "specWord": specWord,
            "wxFirst": wxFirst, "wxSec": wxSec, "score": score,
            "sancaiJixiong": sancaiJixiong, "rengeJixiong": rengeJixiong,
            "digeJixiong": digeJixiong, "waigeJixiong": waigeJixiong,
            "zonggeJixiong": zonggeJixiong, "jichuyunJixiong": jichuyunJixiong,
            "chenggongyunJixiong": chenggongyunJixiong, "shejiaoyunJixiong": shejiaoyunJixiong,
        })

    def idcard_parse(self, idCard: str) -> Dict:
        """F47 身份证解析：18 位身份证号解析地区/出生日期/年龄/性别/生肖/星座。
        注意：idCard 属敏感信息，服务端调用日志已脱敏哈希存储。"""
        return self._post("/api/open/idcard/parse", {"idCard": idCard})

    def shishen_lunming(self, name: str, gender: str, birthDate: str, birthTime: str,
                        longitude: Optional[float] = None, city: Optional[str] = None,
                        useTrueSolarTime: Optional[bool] = None, lang: Optional[str] = None) -> Dict:
        """F48 十神论命。birthDate=yyyy-MM-dd，birthTime=HH:mm；gender=male/female（兼容 男/女）；
        lang=zh-CN|zh-TW|en-US（缺省 zh-CN），返回 bazi/summary/features/palaces 四段 + lang，
        四宫位（年干/月干/地支/时干）逐条吉凶条款含命中判定与白话解读。"""
        return self._post("/api/open/fortune/shishen-lunming", {
            "name": name, "gender": gender, "birthDate": birthDate, "birthTime": birthTime,
            "longitude": longitude, "city": city, "useTrueSolarTime": useTrueSolarTime, "lang": lang,
        })

    def fortune_chart(self, mode: str, gender: str, birthDate: str, birthTime: str,
                      specDate: Optional[str] = None) -> Dict:
        """F49 运势图。mode=monthly/daily/lifetime；specDate=yyyy-MM-dd（缺省当天，lifetime 忽略）；
        monthly 返回 type/points/avg（12点），daily 同结构（14点），lifetime 返回 dayun/liunian。"""
        if mode not in ("monthly", "daily", "lifetime"):
            raise ZhouyiApiError(40001, "本地参数校验：mode 取值必须为 monthly/daily/lifetime")
        return self._post("/api/open/fortune/chart", {
            "mode": mode, "gender": gender, "birthDate": birthDate, "birthTime": birthTime,
            "specDate": specDate,
        })
