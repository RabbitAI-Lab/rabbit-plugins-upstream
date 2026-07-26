#!/usr/bin/env python3
"""
黄金追踪 - 智能提醒管理器
基于现实市场行为重构：动态阈值、多基准比较、防震荡机制、状态管理
零第三方依赖。
"""

import json
import re
import sys
from datetime import datetime, timezone, timedelta
from enum import Enum
from pathlib import Path
from typing import List, Dict, Optional, Tuple

ROOT = Path(__file__).resolve().parent.parent
ALERTS_DIR = ROOT / "alerts"
STATE_FILE = ROOT / "state.json"
CONFIG_FILE = ROOT / "config.yaml"

ALERTS_DIR.mkdir(exist_ok=True)

TZ_BEIJING = timezone(timedelta(hours=8))


class AlertType(str, Enum):
    PRICE_BREAKOUT_LOW = "price_breakout_low"
    PRICE_BREAKOUT_HIGH = "price_breakout_high"
    PRICE_REVERSAL_DOWN = "price_reversal_down"
    PRICE_REVERSAL_UP = "price_reversal_up"
    VOLATILITY_SURGE = "volatility_surge"
    CROSS_MA = "cross_ma"
    RATE_CHANGE = "rate_change"


class AlertStatus(str, Enum):
    PENDING = "pending"
    SENT = "sent"
    ACKNOWLEDGED = "acknowledged"
    RESOLVED = "resolved"
    DISMISSED = "dismissed"


class Alert:
    def __init__(self, alert_id: str, alert_type: AlertType, price: float,
                 change_pct: float, threshold_pct: float, benchmark: str,
                 message: str, details: Dict = None):
        self.alert_id = alert_id
        self.alert_type = alert_type
        self.price = price
        self.change_pct = change_pct
        self.threshold_pct = threshold_pct
        self.benchmark = benchmark
        self.message = message
        self.details = details or {}
        self.status = AlertStatus.PENDING
        self.created_at = datetime.now(TZ_BEIJING).isoformat()
        self.updated_at = self.created_at
        self.resolved_at = None
        self.resolved_price = None

    def to_dict(self) -> Dict:
        return {
            "alert_id": self.alert_id,
            "type": self.alert_type.value,
            "price": self.price,
            "change_pct": self.change_pct,
            "threshold_pct": self.threshold_pct,
            "benchmark": self.benchmark,
            "message": self.message,
            "details": self.details,
            "status": self.status.value,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
            "resolved_at": self.resolved_at,
            "resolved_price": self.resolved_price,
        }

    @classmethod
    def from_dict(cls, data: Dict) -> "Alert":
        alert = cls(
            alert_id=data["alert_id"],
            alert_type=AlertType(data["type"]),
            price=data["price"],
            change_pct=data["change_pct"],
            threshold_pct=data["threshold_pct"],
            benchmark=data["benchmark"],
            message=data["message"],
            details=data.get("details", {}),
        )
        alert.status = AlertStatus(data.get("status", "pending"))
        alert.created_at = data.get("created_at", alert.created_at)
        alert.updated_at = data.get("updated_at", alert.created_at)
        alert.resolved_at = data.get("resolved_at")
        alert.resolved_price = data.get("resolved_price")
        return alert

    def update_status(self, status: AlertStatus, resolved_price: float = None):
        self.status = status
        self.updated_at = datetime.now(TZ_BEIJING).isoformat()
        if status == AlertStatus.RESOLVED:
            self.resolved_at = self.updated_at
            self.resolved_price = resolved_price


def load_config() -> Dict:
    cfg = {
        "threshold_pct": 1.0,
        "min_threshold_pct": 0.5,
        "max_threshold_pct": 3.0,
        "cooldown_minutes": 30,
        "lookback_days": 7,
        "volatility_multiplier": 1.5,
        "max_alerts_per_day": 10,
        "auto_resolve_minutes": 1440,
        "retention_days": 30,
    }
    if CONFIG_FILE.exists():
        text = CONFIG_FILE.read_text(encoding="utf-8")
        m = re.search(r'threshold_pct:\s*([\d.]+)', text)
        if m: cfg["threshold_pct"] = float(m.group(1))
        m = re.search(r'min_threshold_pct:\s*([\d.]+)', text)
        if m: cfg["min_threshold_pct"] = float(m.group(1))
        m = re.search(r'max_threshold_pct:\s*([\d.]+)', text)
        if m: cfg["max_threshold_pct"] = float(m.group(1))
        m = re.search(r'cooldown_minutes:\s*(\d+)', text)
        if m: cfg["cooldown_minutes"] = int(m.group(1))
        m = re.search(r'lookback_days:\s*(\d+)', text)
        if m: cfg["lookback_days"] = int(m.group(1))
        m = re.search(r'volatility_multiplier:\s*([\d.]+)', text)
        if m: cfg["volatility_multiplier"] = float(m.group(1))
        m = re.search(r'max_alerts_per_day:\s*(\d+)', text)
        if m: cfg["max_alerts_per_day"] = int(m.group(1))
        m = re.search(r'auto_resolve_minutes:\s*(\d+)', text)
        if m: cfg["auto_resolve_minutes"] = int(m.group(1))
        m = re.search(r'retention_days:\s*(\d+)', text)
        if m: cfg["retention_days"] = int(m.group(1))
    return cfg


def load_state() -> Dict:
    if not STATE_FILE.exists():
        return {}
    try:
        return json.loads(STATE_FILE.read_text())
    except Exception:
        return {}


def calculate_dynamic_threshold(lookback_days: int = 7,
                                base_threshold: float = 1.0,
                                multiplier: float = 1.5,
                                min_threshold: float = 0.5,
                                max_threshold: float = 3.0) -> float:
    archive_dir = ROOT / "archive"
    price_changes = []

    now = datetime.now(TZ_BEIJING)
    for i in range(1, lookback_days + 1):
        date = (now - timedelta(days=i)).strftime("%Y-%m-%d")
        month = date[:7]
        archive_file = archive_dir / month / f"{date}.yaml"
        if archive_file.exists():
            text = archive_file.read_text(encoding="utf-8")
            m = re.search(r'price_usd:\s*([\d.]+)', text)
            if m:
                price_changes.append(float(m.group(1)))

    if len(price_changes) >= 2:
        daily_volatility = 0.0
        for i in range(1, len(price_changes)):
            change = abs(price_changes[i] - price_changes[i - 1]) / price_changes[i - 1] * 100
            daily_volatility += change
        daily_volatility /= (len(price_changes) - 1)

        dynamic_threshold = base_threshold * (1 + (daily_volatility - 0.5) * 0.1)
        dynamic_threshold = max(min_threshold, min(max_threshold, dynamic_threshold))
        return round(dynamic_threshold, 2)

    return base_threshold


def get_today_alerts() -> List[Alert]:
    today = datetime.now(TZ_BEIJING).strftime("%Y-%m-%d")
    alert_file = ALERTS_DIR / f"{today}.json"
    if not alert_file.exists():
        return []
    try:
        data = json.loads(alert_file.read_text())
        return [Alert.from_dict(item) for item in data]
    except Exception:
        return []


def save_today_alerts(alerts: List[Alert]):
    today = datetime.now(TZ_BEIJING).strftime("%Y-%m-%d")
    alert_file = ALERTS_DIR / f"{today}.json"
    data = [a.to_dict() for a in alerts]
    alert_file.write_text(json.dumps(data, indent=2, ensure_ascii=False))


def get_active_alerts() -> List[Alert]:
    all_alerts = []
    for f in ALERTS_DIR.iterdir():
        if f.suffix != ".json":
            continue
        try:
            data = json.loads(f.read_text())
            for item in data:
                alert = Alert.from_dict(item)
                if alert.status in (AlertStatus.PENDING, AlertStatus.SENT):
                    all_alerts.append(alert)
        except Exception:
            pass
    return sorted(all_alerts, key=lambda a: a.created_at, reverse=True)


def is_on_cooldown(alert_type: AlertType, cooldown_minutes: int = 30) -> bool:
    active = get_active_alerts()
    now = datetime.now(TZ_BEIJING)
    for alert in active:
        if alert.alert_type == alert_type:
            created = datetime.fromisoformat(alert.created_at)
            if (now - created).total_seconds() < cooldown_minutes * 60:
                return True
    return False


def detect_alerts(current_price: float, state: Dict = None,
                  config: Dict = None) -> Tuple[List[Alert], float]:
    if state is None:
        state = load_state()
    if config is None:
        config = load_config()

    dynamic_threshold = calculate_dynamic_threshold(
        lookback_days=config["lookback_days"],
        base_threshold=config["threshold_pct"],
        multiplier=config["volatility_multiplier"],
        min_threshold=config["min_threshold_pct"],
        max_threshold=config["max_threshold_pct"],
    )

    alerts = []
    today_alerts = get_today_alerts()
    today_count = len([a for a in today_alerts if a.status not in (AlertStatus.RESOLVED, AlertStatus.DISMISSED)])

    if today_count >= config["max_alerts_per_day"]:
        return alerts, dynamic_threshold

    benchmarks = []

    last_price = state.get("last_price")
    if last_price:
        change_from_last = (current_price - last_price) / last_price * 100
        benchmarks.append(("last_price", last_price, change_from_last))

    open_price = state.get("key_data", {}).get("open")
    if open_price:
        change_from_open = (current_price - open_price) / open_price * 100
        benchmarks.append(("open", open_price, change_from_open))

    high_24h = state.get("key_data", {}).get("high")
    low_24h = state.get("key_data", {}).get("low")
    if high_24h and low_24h:
        avg_24h = (high_24h + low_24h) / 2
        change_from_avg = (current_price - avg_24h) / avg_24h * 100
        benchmarks.append(("24h_avg", avg_24h, change_from_avg))

    for benchmark_name, benchmark_price, change_pct in benchmarks:
        abs_change = abs(change_pct)

        if abs_change < dynamic_threshold * 0.5:
            continue

        if is_on_cooldown(AlertType.RATE_CHANGE, config["cooldown_minutes"]):
            continue

        if change_pct >= dynamic_threshold:
            alert_type = AlertType.PRICE_BREAKOUT_HIGH
            direction = "上涨"
            emoji = "📈"
        elif change_pct <= -dynamic_threshold:
            alert_type = AlertType.PRICE_BREAKOUT_LOW
            direction = "下跌"
            emoji = "📉"
        elif abs_change >= dynamic_threshold * 0.7:
            if change_pct > 0:
                alert_type = AlertType.PRICE_REVERSAL_UP
                direction = "反转上涨"
                emoji = "↗️"
            else:
                alert_type = AlertType.PRICE_REVERSAL_DOWN
                direction = "反转下跌"
                emoji = "↘️"
        else:
            continue

        alert_id = f"{datetime.now(TZ_BEIJING).strftime('%Y%m%d-%H%M%S')}-{benchmark_name}"
        message = f"{emoji} 金价{direction}提醒：当前 ${current_price:.2f}，相对{benchmark_name}变动 {change_pct:+.2f}%"

        alert = Alert(
            alert_id=alert_id,
            alert_type=alert_type,
            price=current_price,
            change_pct=change_pct,
            threshold_pct=dynamic_threshold,
            benchmark=benchmark_name,
            message=message,
            details={
                "benchmark_price": benchmark_price,
                "direction": direction,
                "threshold_used": dynamic_threshold,
            },
        )

        alerts.append(alert)

    return alerts, dynamic_threshold


def create_alerts(current_price: float) -> Tuple[List[Alert], float]:
    alerts, dynamic_threshold = detect_alerts(current_price)
    if alerts:
        today_alerts = get_today_alerts()
        today_alerts.extend(alerts)
        save_today_alerts(today_alerts)
    return alerts, dynamic_threshold


def update_alert_status(alert_id: str, status: str, resolved_price: float = None):
    for f in ALERTS_DIR.iterdir():
        if f.suffix != ".json":
            continue
        try:
            data = json.loads(f.read_text())
            found = False
            for item in data:
                if item["alert_id"] == alert_id:
                    item["status"] = status
                    item["updated_at"] = datetime.now(TZ_BEIJING).isoformat()
                    if status == "resolved":
                        item["resolved_at"] = item["updated_at"]
                        item["resolved_price"] = resolved_price
                    found = True
                    break
            if found:
                f.write_text(json.dumps(data, indent=2, ensure_ascii=False))
                return True
        except Exception:
            pass
    return False


def auto_resolve_alerts(auto_resolve_minutes: int = 1440):
    now = datetime.now(TZ_BEIJING)
    updated = False
    for f in ALERTS_DIR.iterdir():
        if f.suffix != ".json":
            continue
        try:
            data = json.loads(f.read_text())
            changed = False
            for item in data:
                if item["status"] in ("pending", "sent"):
                    created = datetime.fromisoformat(item["created_at"])
                    if (now - created).total_seconds() > auto_resolve_minutes * 60:
                        item["status"] = "resolved"
                        item["updated_at"] = now.isoformat()
                        item["resolved_at"] = now.isoformat()
                        changed = True
            if changed:
                f.write_text(json.dumps(data, indent=2, ensure_ascii=False))
                updated = True
        except Exception:
            pass
    return updated


def cleanup_old_alerts(retention_days: int = 30):
    now = datetime.now(TZ_BEIJING)
    removed = 0
    for f in ALERTS_DIR.iterdir():
        if f.suffix != ".json":
            continue
        try:
            date_str = f.stem
            file_date = datetime.strptime(date_str, "%Y-%m-%d")
            if (now - file_date).days > retention_days:
                f.unlink()
                removed += 1
        except Exception:
            pass
    return removed


def format_alerts_for_display(alerts: List[Alert]) -> str:
    if not alerts:
        return "暂无活跃提醒"

    lines = ["## 🚨 活跃提醒"]
    for alert in alerts:
        status_icon = {
            "pending": "⏳",
            "sent": "📤",
            "acknowledged": "✅",
            "resolved": "🔒",
            "dismissed": "❌",
        }.get(alert.status, "⚪")

        lines.append(f"")
        lines.append(f"### {status_icon} {alert.message}")
        lines.append(f"- 类型: {alert.alert_type.value}")
        lines.append(f"- 基准: {alert.benchmark} (阈值: ±{alert.threshold_pct}%)")
        lines.append(f"- 创建时间: {alert.created_at}")
        if alert.resolved_at:
            lines.append(f"- 已解决: {alert.resolved_at} (价格: ${alert.resolved_price:.2f})")

    return "\n".join(lines)


def main():
    if len(sys.argv) < 2:
        print("用法:")
        print("  alert_manager.py detect          # 检测并创建提醒")
        print("  alert_manager.py list            # 列出活跃提醒")
        print("  alert_manager.py status <id> <status> # 更新提醒状态")
        print("  alert_manager.py auto_resolve    # 自动解决超时提醒")
        print("  alert_manager.py cleanup         # 清理过期提醒")
        print("  alert_manager.py threshold       # 计算动态阈值")
        sys.exit(0)

    action = sys.argv[1]
    config = load_config()

    if action == "detect":
        state = load_state()
        current_price = state.get("current_price")
        if not current_price:
            print("[错误] state.json 中无 current_price")
            sys.exit(1)
        alerts, threshold = create_alerts(current_price)
        print(f"[信息] 动态阈值: ±{threshold}%")
        if alerts:
            print(f"[成功] 创建 {len(alerts)} 条提醒:")
            for a in alerts:
                print(f"  - {a.message}")
        else:
            print("[信息] 无新提醒触发")

    elif action == "list":
        alerts = get_active_alerts()
        print(format_alerts_for_display(alerts))

    elif action == "status":
        if len(sys.argv) < 4:
            print("用法: alert_manager.py status <alert_id> <pending|sent|acknowledged|resolved|dismissed>")
            sys.exit(1)
        alert_id = sys.argv[2]
        status = sys.argv[3]
        if status not in ["pending", "sent", "acknowledged", "resolved", "dismissed"]:
            print("无效状态")
            sys.exit(1)
        resolved_price = None
        if len(sys.argv) > 4:
            resolved_price = float(sys.argv[4])
        if update_alert_status(alert_id, status, resolved_price):
            print(f"[成功] 提醒 {alert_id} 状态已更新为 {status}")
        else:
            print(f"[错误] 未找到提醒 {alert_id}")

    elif action == "auto_resolve":
        if auto_resolve_alerts(config["auto_resolve_minutes"]):
            print("[成功] 已自动解决超时提醒")
        else:
            print("[信息] 无超时提醒需要解决")

    elif action == "cleanup":
        removed = cleanup_old_alerts(config["retention_days"])
        print(f"[完成] 清理 {removed} 个过期提醒文件")

    elif action == "threshold":
        threshold = calculate_dynamic_threshold(
            lookback_days=config["lookback_days"],
            base_threshold=config["threshold_pct"],
            multiplier=config["volatility_multiplier"],
            min_threshold=config["min_threshold_pct"],
            max_threshold=config["max_threshold_pct"],
        )
        print(f"动态阈值: ±{threshold}%")

    else:
        print(f"未知操作: {action}")
        sys.exit(1)


if __name__ == "__main__":
    main()