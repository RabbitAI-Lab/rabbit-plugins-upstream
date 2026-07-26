# 详细参考 - smart-reminder-free

> 本文件从SKILL.md拆分而来，包含详细代码示例和扩展章节。

## 代码示例 (python)

```python
import yaml
import subprocess
from pathlib import Path
from datetime import datetime, timedelta

EVENTS_FILE = Path.home() / "workspace" / "reminders" / "events.yml"
TIMEZONE = "Asia/Shanghai"
DEFAULT_OFFSETS = [1440, 60, 10]  # 24h/1h/10m前（分钟）
class SmartReminder:
    """智能提醒助手（免费版）"""

    def __init__(self):
        self.events_file = EVENTS_FILE
        self.events_file.parent.mkdir(parents=True, exist_ok=True)
        if not self.events_file.exists():
            self.events_file.write_text("[]", encoding="utf-8")

    def capture(self, title, start_datetime, notes="", offsets=None, repeat="none"):
        """捕获事件并创建提醒"""
        if offsets is None:
            offsets = DEFAULT_OFFSETS

        event = {
            "id": f"evt_{int(datetime.now().timestamp())}",
            "title": title,
            "start_datetime": start_datetime.isoformat(),
            "notes": notes,
            "reminders_offsets": offsets,
            "repeat": repeat,
            "timezone": TIMEZONE,
            "created_at": datetime.now().isoformat(),
            "status": "active"
        }

        events = self._load_events()
        events.append(event)
        self._save_events(events)

        for offset_min in offsets:
            remind_at = start_datetime - timedelta(minutes=offset_min)
            if remind_at <= datetime.now():
                continue  # 跳过已过去的提醒
            job_name = f"reminder-{event['id']}-{offset_min}m"
            subprocess.run([
                "skill-platform", "cron", "add",
                "--name", job_name,
                "--at", remind_at.strftime("%Y-%m-%dT%H:%M:%SZ"),
                "--session", "main",
                "--system-event", f"提醒：{title}（{offset_min}分钟后开始）",
                "--announce",
                "--channel", "telegram",
                "--to", "+8613800138000",
                "--delete-after-run"
            ], check=False)

        print(f"✓ 事件已捕获并设置{len(offsets)}个提醒")
        return event

    def query_upcoming(self, days=7):
        """查询即将到来的事件"""
        events = self._load_events()
        now = datetime.now()
        upcoming = []

        for event in events:
            if event["status"] != "active":
                continue
            start = datetime.fromisoformat(event["start_datetime"])
            if now <= start <= now + timedelta(days=days):
                upcoming.append(event)

        upcoming.sort(key=lambda e: e["start_datetime"])
        return upcoming

    def cancel(self, event_id):
        """取消事件"""
        events = self._load_events()
        for event in events:
            if event["id"] == event_id:
                event["status"] = "cancelled"
                self._save_events(events)
                print(f"✓ 事件已取消：{event['title']}")
                return event
        print(f"✗ 未找到事件：{event_id}")
        return None

    def _load_events(self):
        return yaml.safe_load(self.events_file.read_text(encoding="utf-8")) or []

    def _save_events(self, events):
        self.events_file.write_text(
            yaml.dump(events, allow_unicode=True, sort_keys=False),
            encoding="utf-8"
        )

sr = SmartReminder()

sr.capture(
    title="团队周会",
    start_datetime=datetime.now() + timedelta(days=2, hours=2),
    notes="讨论Q3规划"
)

sr.capture(
    title="妈妈生日",
    start_datetime=datetime(2026, 8, 2, 9, 0),
    notes="记得提前准备礼物",
    repeat="yearly"
)

upcoming = sr.query_upcoming(days=7)
for event in upcoming:
    print(f"  {event['start_datetime']}: {event['title']}")
```

## 代码示例 (python)

```python
import re
from datetime import datetime, timedelta

class NaturalLanguageParser:
    """中文自然语言事件解析（免费版）"""

    def parse(self, text, current_time=None):
        """解析自然语言事件描述"""
        if current_time is None:
            current_time = datetime.now()

        result = {
            "title": "",
            "start_datetime": None,
            "notes": "",
            "repeat": "none"
        }

        if "后天" in text:
            date = current_time + timedelta(days=2)
        elif "明天" in text:
            date = current_time + timedelta(days=1)
        elif "今天" in text:
            date = current_time
        elif match := re.search(r"下周([一二三四五六日天])", text):
            day_map = {"一": 0, "二": 1, "三": 2, "四": 3, "五": 4, "六": 5, "日": 6, "天": 6}
            target_day = day_map[match.group(1)]
            days_ahead = (target_day - current_time.weekday()) % 7
            if days_ahead == 0:
                days_ahead = 7
            date = current_time + timedelta(days=days_ahead)
        elif match := re.search(r"周([一二三四五六日天])", text):
            day_map = {"一": 0, "二": 1, "三": 2, "四": 3, "五": 4, "六": 5, "日": 6, "天": 6}
            target_day = day_map[match.group(1)]
            days_ahead = (target_day - current_time.weekday()) % 7
            date = current_time + timedelta(days=days_ahead)
        elif match := re.search(r"(\d+)月(\d+)号", text):
            month, day = int(match.group(1)), int(match.group(2))
            date = current_time.replace(month=month, day=day)
            if date < current_time:
                date = date.replace(year=date.year + 1)
        else:
            date = None  # 需要澄清
        if match := re.search(r"上午(\d+)点", text):
            hour = int(match.group(1))
            time = (hour, 0)
        elif match := re.search(r"下午(\d+)点", text):
            hour = int(match.group(1)) + 12
            time = (hour, 0)
        elif match := re.search(r"(\d+)点(\d+)分", text):
            time = (int(match.group(1)), int(match.group(2)))
        elif match := re.search(r"(\d+)点", text):
            time = (int(match.group(1)), 0)
        else:
            time = None  # 需要澄清
        if date and time:
            result["start_datetime"] = date.replace(
                hour=time[0], minute=time[1], second=0, microsecond=0
            )
        elif date:
            result["start_datetime"] = date  # 仅有日期，需澄清时间
        if "生日" in text or "纪念日" in text:
            result["repeat"] = "yearly"

        if match := re.search(r"有(.+)$", text):
            result["title"] = match.group(1).strip()
        elif match := re.search(r"是(.+)$", text):
            result["title"] = match.group(1).strip()
        else:
            cleaned = re.sub(r"(后天|明天|今天|下周[一二三四五六日天]|周[一二三四五六日天]|\d+月\d+号|上午|\d+点|\d+分|下午|有个|有)", "", text)
            result["title"] = cleaned.strip() or "未命名事件"

        return result

    def needs_clarification(self, parsed):
        """判断是否需要澄清"""
        missing = []
        if parsed["start_datetime"] is None:
            missing.append("时间")
        if not parsed["title"]:
            missing.append("标题")
        return missing

parser = NaturalLanguageParser()

texts = [
    "后天上午10点有个会",
    "下个月2号我妈生日",
    "周五下午三点交报告",
    "明天上午9点站会"
]

for text in texts:
    print(f"\n输入：{text}")
    parsed = parser.parse(text)
    print(f"  标题：{parsed['title']}")
    print(f"  时间：{parsed['start_datetime']}")
    print(f"  重复：{parsed['repeat']}")

    missing = parser.needs_clarification(parsed)
    if missing:
        print(f"  ⚠️ 需要澄清：{', '.join(missing)}")
```

## 代码示例 (python)

```python
import yaml
from pathlib import Path
from datetime import datetime, timedelta

EVENTS_FILE = Path.home() / "workspace" / "reminders" / "events.yml"

def capture_event(natural_text, current_time=None):
    """捕获自然语言事件（基础版）"""
    if current_time is None:
        current_time = datetime.now()

    event_date = current_time + timedelta(days=2)
    start_datetime = event_date.replace(hour=10, minute=0, second=0, microsecond=0)

    event = {
        "id": f"evt_{int(current_time.timestamp())}",
        "title": "会议",  # 从"有个会"提取
        "start_datetime": start_datetime.isoformat(),
        "notes": "",
        "reminders_offsets": [1440, 60, 10],  # 24h/1h/10m前（分钟）
        "repeat": "none",
        "timezone": "Asia/Shanghai",
        "created_at": current_time.isoformat(),
        "status": "active"
    }

    EVENTS_FILE.parent.mkdir(parents=True, exist_ok=True)
    events = []
    if EVENTS_FILE.exists():
        events = yaml.safe_load(EVENTS_FILE.read_text(encoding="utf-8")) or []

    events.append(event)
    EVENTS_FILE.write_text(
        yaml.dump(events, allow_unicode=True, sort_keys=False),
        encoding="utf-8"
    )

    print(f"✓ 事件已捕获：{event['title']}")
    print(f"  时间：{start_datetime.strftime('%Y-%m-%d %H:%M')}")
    print(f"  提醒：24小时前、1小时前、10分钟前")

    return event

capture_event("后天上午10点有个会")
```

