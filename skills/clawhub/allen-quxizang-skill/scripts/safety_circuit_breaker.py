"""
Copyright (c) 2026 Allen. MIT License.
"""
"""
西藏硬核旅游守护者 —— 全局安全熔断器
======================================
架构位置: 模块二 [Node 5]
触发条件: 用户查询涉及高海拔过夜(>3800m)且进藏天数不足3天时强行拦截
输入来源: 上游文本分类器 + 海拔API的 JSON payload
输出用途: 注入 LLM Response Synthesizer 的强制保命文本

用法(命令行):
  python3 safety_circuit_breaker.py --altitude 4200 --days 2 --overnight true

用法(Python import):
  from safety_circuit_breaker import SafetyCircuitBreaker
  breaker = SafetyCircuitBreaker()
  result = breaker.evaluate(target_altitude=4200, days_in_plateau=2, stay_overnight=True)
  print(result["warning_text"])
"""

import json
import sys
import argparse
from typing import TypedDict, Optional


class CircuitBreakerInput(TypedDict, total=False):
    target_altitude: float
    days_in_plateau: int
    stay_overnight: bool
    user_location: str
    next_destination: str
    weather_warning: str


class CircuitBreakerOutput(TypedDict):
    triggered: bool
    severity: str  # "extreme" | "critical" | "warning" | "info" | "none"
    warning_text: str
    suggestion: str


ALTITUDE_THRESHOLD = 3800       # 米, 超过此值触发检查
DAYS_ACCLIMATIZATION = 3        # 最少适应天数
CRITICAL_ALTITUDE = 4500        # 米, 超过此值升级为最高级别警告
EXTREME_ALTITUDE = 5000         # 米, 超过此值人体基本无法适应

# 低海拔安全留宿推荐映射
SAFE_HAVENS = {
    "康定": 2560,
    "巴塘": 2580,
    "雅江": 2530,
    "林芝": 2950,
    "波密": 2720,
    "然乌": 3260,
    "拉萨": 3650,
    "日喀则": 3800,
    "香格里拉": 3280,
    "西宁": 2200,
    "成都": 500,
}

# 危险过夜点名表（海拔超过3800的常见留宿点）
DANGEROUS_OVERNIGHT_SPOTS = {
    "理塘": 4014,
    "那曲": 4510,
    "安多": 4700,
    "当雄": 4300,
    "班戈": 4750,
    "尼玛": 4540,
    "改则": 4415,
    "狮泉河": 4300,
    "普兰": 3900,
    "札达": 3740,
    "日土": 4250,
    "霍尔": 4600,
    "萨嘎": 4600,
    "帕羊": 4600,
    "玛旁雍措": 4588,
    "珠峰大本营": 5200,
    "绒布寺": 5150,
}


class SafetyCircuitBreaker:
    """
    全局安全熔断器核心类

    职责:
      1. 评估目标过夜点海拔风险
      2. 结合进藏天数和天气预警决定熔断级别
      3. 生成用户可读的保命拦截文本
      4. 推荐低海拔替代住宿点

    使用示例:
      >>> breaker = SafetyCircuitBreaker()
      >>> result = breaker.evaluate(altitude=4200, days=1, overnight=True)
      >>> result["severity"]
      'critical'
    """

    def __init__(self, altitude_threshold: float = ALTITUDE_THRESHOLD):
        self.altitude_threshold = altitude_threshold

    def evaluate(
        self,
        target_altitude: float,
        days_in_plateau: int,
        stay_overnight: bool = True,
        weather_warning: Optional[str] = None,
        location_name: Optional[str] = None,
    ) -> dict:
        """
        核心熔断评估方法

        参数:
          target_altitude: 目标过夜点海拔(米)
          days_in_plateau: 进藏天数(含当天)
          stay_overnight:  是否计划过夜
          weather_warning: 天气预报中的灾害预警文本(如"暴雪/道路结冰")
          location_name:   目标地点名称(用于匹配安全港湾推荐)

        返回:
          CircuitBreakerOutput 字典
        """
        result: CircuitBreakerOutput = {
            "triggered": False,
            "severity": "none",
            "warning_text": "",
            "suggestion": "",
        }

        # --- 海拔 + 适应天数联合熔断 ---
        if target_altitude <= 0:
            return result  # 无有效海拔数据,不熔断

        # 还没进藏(days=0): 直接拦截,不降档
        if days_in_plateau <= 0:
            result["triggered"] = True
            result["severity"] = "critical"
            result["warning_text"] = (
                "🚨【Allen扎西大哥的生死拦截！】\n"
                "你还没进藏就计划上高海拔过夜？！"
                "身体对高原毫无适应,直接去这个高度等于赌博。\n"
                "听我的:先到林芝(2950m)或拉萨(3650m)住2-3天适应,"
                "再考虑去更高海拔的地方。"
            )
            result["suggestion"] = "先到低海拔城市适应2-3天,备好抗高反药品"
            return result

        # 极端海拔: 无论几天都熔断
        if target_altitude >= EXTREME_ALTITUDE and stay_overnight:
            result["triggered"] = True
            result["severity"] = "extreme"
            result["warning_text"] = (
                "🚨【Allen扎西大哥的生死拦截！】\n"
                f"你要在 {target_altitude:.0f} 米的地方过夜？！这是极端高海拔区域！"
                "在这个高度,即使适应了几天的人也可能突发肺水肿或脑水肿。"
                "这个高度只能白天路过拍照,绝对不能住人。"
                "立即取消这个住宿计划！降到 3500 米以下过夜,这是命令不是建议！"
            )
            result["suggestion"] = "建议白天游览后返回林芝(2950m)或日喀则(3800m)住宿"
            return result

        # 高海拔 + 适应不足: 核心熔断逻辑
        if target_altitude > self.altitude_threshold and days_in_plateau < DAYS_ACCLIMATIZATION and stay_overnight:
            result["triggered"] = True
            severity = "critical" if (target_altitude >= CRITICAL_ALTITUDE or days_in_plateau <= 1) else "warning"
            result["severity"] = severity

            nearest_havens = self._find_nearest_safe_havens(location_name, target_altitude)
            haven_text = ""
            if nearest_havens:
                haven_text = "\n推荐安全住宿点:\n" + "\n".join(
                    f"  ✅ {name} ({alt:.0f}m)" for name, alt in nearest_havens[:3]
                )

            if severity == "critical":
                result["warning_text"] = (
                    "🚨【Allen扎西大哥的保命拦截！】\n"
                    f"你计划过夜的地方海拔高达 {target_altitude:.0f} 米！"
                    f"你才进藏 {days_in_plateau} 天,身体根本适应不了。"
                    "在高原,严重高反引起肺水肿/脑水肿最快6小时要命！\n"
                    "听我的,立刻把今晚的住宿改到海拔低于 3300 米的地方。"
                    f"{haven_text}"
                )
            else:
                result["warning_text"] = (
                    "⚠️【Allen扎西大哥的严肃警告】\n"
                    f"你计划过夜的地点海拔 {target_altitude:.0f} 米,"
                    f"而你现在进藏才 {days_in_plateau} 天。"
                    "这个高度不是不能住,但风险很大。\n"
                    "如果非要住:\n"
                    "  1. 确认房间有供氧设备\n"
                    "  2. 备好散利痛和便携血氧仪\n"
                    "  3. 血氧低于85%立刻下撤\n"
                    "  4. 千万别洗澡！\n"
                    f"当然,更安全的是下面这些选择:{haven_text}"
                )

            result["suggestion"] = (
                f"联系住宿点确认是否提供弥散式供氧,备好应急药品和氧气罐"
            )
            return result

        # --- 天气附加熔断: 即使海拔不高,极端天气也触发 ---
        if weather_warning and any(kw in weather_warning for kw in ["暴雪", "道路结冰", "大风", "强降雨", "暴雨", "山洪", "泥石流", "冰雹", "沙尘暴", "暴风雪"]):
            result["triggered"] = True
            if result["severity"] == "none":
                result["severity"] = "warning"
            weather_append = (
                f"\n\n🌨️【极端天气叠加警报】\n"
                f"当地目前有「{weather_warning}」预警！"
                "高海拔 + 恶劣天气 = 致命组合。路上可能积雪封路、能见度极低,"
                "建议暂缓行程或改走低海拔路线。"
            )
            result["warning_text"] += weather_append
            result["suggestion"] += " 关注当地交通管制信息,准备防滑链"

        return result

    def _find_nearest_safe_havens(self, location_name: Optional[str], current_altitude: float) -> list:
        """
        寻找离目标最近的3个安全过夜点(海拔 < 3300m)
        """
        safe_options = [(name, alt) for name, alt in SAFE_HAVENS.items() if alt < 3300]
        if not safe_options:
            return []

        if location_name and current_altitude > 0:
            safe_options.sort(key=lambda x: abs(x[1] - current_altitude))
        else:
            safe_options.sort(key=lambda x: x[1])

        return safe_options[:3]

    def evaluate_from_json(self, json_input: str) -> str:
        """
        接收上游节点的 JSON 字符串,返回熔断结果 JSON

        这是工作流 Code Node 的入口函数
        """
        try:
            data = json.loads(json_input)
        except json.JSONDecodeError as e:
            return json.dumps({"error": f"Invalid JSON input: {e}"})

        result = self.evaluate(
            target_altitude=float(data.get("target_altitude", 0)),
            days_in_plateau=int(data.get("days_in_plateau", 0)),
            stay_overnight=bool(data.get("stay_overnight", False)),
            weather_warning=data.get("weather_warning"),
            location_name=data.get("location_name"),
        )
        return json.dumps(result, ensure_ascii=False)


# ============================================================================
# 命令行入口 (用于工作流 Code Node / 手动测试)
# ============================================================================

def cli_main():
    # 先检查 test 参数(避免 argparse 拦截)
    if "test" in sys.argv:
        sys.argv.remove("test")
        sys.exit(_run_tests())

    parser = argparse.ArgumentParser(
        description="西藏硬核旅游守护者 —— 全局安全熔断器",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
示例:
  # 基础熔断评估
  python3 safety_circuit_breaker.py --altitude 4200 --days 2 --overnight true

  # 带地点名称和天气预警
  python3 safety_circuit_breaker.py --altitude 4700 --days 1 \\\\
    --overnight true --location 那曲 --weather "暴雪橙色预警"

  # 安全场景(不触发)
  python3 safety_circuit_breaker.py --altitude 2900 --days 1 --overnight true

  # JSON 输入模式(工作流集成)
  echo '{"target_altitude":4300,"days_in_plateau":1,"stay_overnight":true}' \\
    | python3 safety_circuit_breaker.py --json-stdin

  # 危险过夜点名表快速查询
  python3 safety_circuit_breaker.py --dangerous-spots

  # 运行冒烟测试
  python3 safety_circuit_breaker.py test
        """,
    )
    parser.add_argument("--altitude", type=float, help="目标过夜点海拔(米)")
    parser.add_argument("--days", type=int, default=0, help="进藏天数")
    parser.add_argument("--overnight", type=str, default="true", help="是否过夜(true/false)")
    parser.add_argument("--location", type=str, default=None, help="目标地点名称")
    parser.add_argument("--weather", type=str, default=None, help="天气预警文本")
    parser.add_argument("--dangerous-spots", action="store_true", help="列出所有危险过夜点")
    parser.add_argument("--json-stdin", action="store_true", help="从 stdin 读取 JSON 输入")

    args = parser.parse_args()

    if args.dangerous_spots:
        print("=" * 60)
        print("🚨 危险过夜点名单 (海拔 > 3800m)")
        print("=" * 60)
        for name, alt in sorted(DANGEROUS_OVERNIGHT_SPOTS.items(), key=lambda x: -x[1]):
            level = "🔴" if alt >= 5000 else "🟠" if alt >= 4500 else "🟡"
            print(f"  {level} {name:12s}  {alt:4.0f}m")
        print()
        print("💡 安全过夜点:")
        for name, alt in sorted(SAFE_HAVENS.items(), key=lambda x: -x[1]):
            if alt < 3300:
                print(f"  ✅ {name:12s}  {alt:4.0f}m")
        return

    breaker = SafetyCircuitBreaker()
    if args.json_stdin:
        raw = sys.stdin.read()
        print(breaker.evaluate_from_json(raw))
        return

    if args.altitude is None:
        parser.error("--altitude is required (use --help for usage)")

    result = breaker.evaluate(
        target_altitude=args.altitude,
        days_in_plateau=args.days,
        stay_overnight=args.overnight.lower() in ("true", "1", "yes"),
        weather_warning=args.weather,
        location_name=args.location,
    )

    print("=" * 60)
    print(f"  熔断触发: {'是 🔴' if result['triggered'] else '否 ✅'}")
    print(f"  严重级别: {result['severity']}")
    print("=" * 60)
    if result["warning_text"]:
        print()
        print(result["warning_text"])
    if result["suggestion"]:
        print()
        print(f"💡 建议: {result['suggestion']}")


def _run_tests():
    """
    快速冒烟测试 (14 用例)

    完整测试套件请使用 pytest:
      pip install pytest
      pytest tests/
    """
    breaker = SafetyCircuitBreaker()

    tests = [
        # (altitude, days, overnight, location, weather, expected_severity)
        (4200, 1, True, "理塘", None, "critical"),        # 高海拔 + 适应不足
        (3000, 1, True, "林芝", None, "none"),             # 安全海拔
        (4700, 2, True, "那曲", None, "critical"),         # 极高海拔
        (4000, 5, True, None, None, "none"),               # 已适应
        (4200, 1, False, None, None, "none"),              # 不过夜
        (3500, 1, True, None, "暴雪红色预警", "warning"),  # 天气熔断
        (5200, 7, True, "珠峰大本营", None, "extreme"),   # 极端海拔,即使已适应
        (4200, 0, True, "理塘", None, "critical"),         # 还没进藏(days=0)
        (3800, 1, True, "拉萨", None, "none"),             # 海拔边界:3800m(>3800才触发,含=不触发)
        (4500, 5, True, "纳木错", None, "none"),           # 4500m但已适应5天,不过夜也可以不触发
        (5000, 10, True, "阿里", None, "extreme"),         # 海拔边界:5000m
        (5000, 10, False, "阿里", None, "none"),           # 5000m但不过夜
        (0, 3, True, "成都", None, "none"),                # 海拔0
        (4200, 1, True, None, "暴雨橙色预警+山洪预警", "critical"),  # 多天气关键词
    ]

    passed = 0
    for alt, days, overnight, loc, weather, expected in tests:
        r = breaker.evaluate(target_altitude=alt, days_in_plateau=days,
                             stay_overnight=overnight, location_name=loc,
                             weather_warning=weather)
        ok = r["severity"] == expected
        status = "✅ PASS" if ok else f"❌ FAIL (got {r['severity']}, expected {expected})"
        print(f"  [{status}] alt={alt}m, days={days}, overnight={overnight} -> {r['severity']}")
        if not ok and r["warning_text"]:
            print(f"    warning: {r['warning_text'][:60]}...")
        if ok:
            passed += 1

    total = len(tests)
    print(f"\n  {'='*40}")
    print(f"  结果: {passed}/{total} 通过")
    return 0 if passed == total else 1


if __name__ == "__main__":
    cli_main()



