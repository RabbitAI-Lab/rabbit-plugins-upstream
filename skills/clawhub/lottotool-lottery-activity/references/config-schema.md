# 配置结构

WorkBuddy 将用户需求维护为 MCP 工具的 `config` 对象。只使用下列业务字段，由服务端生成现有抽奖后端 payload。

## 完整示例

```json
{
  "version": 1,
  "title": "八月会员感谢抽奖",
  "play": "classic",
  "publish_to_square": false,
  "description": "感谢会员支持，每人限参与一次。",
  "draw": {
    "mode": "timed",
    "start_at": "now",
    "end_at": "3d",
    "max_people": 100,
    "draws_per_user": 1
  },
  "prizes": [
    {
      "name": "蓝牙耳机",
      "count": 1,
      "delivery": "express"
    },
    {
      "name": "咖啡兑换券",
      "count": 10,
      "delivery": "none"
    }
  ]
}
```

## 字段

| 字段 | 必填 | 值 |
|---|---:|---|
| `version` | 是 | 固定 `1` |
| `title` | 是 | 1–60 字符 |
| `play` | 是 | `classic` / `turntable` / `gashapon` / `egg` / `nine-grid` / `flip-card` |
| `publish_to_square` | 否 | 默认 `false` |
| `description` | 否 | 活动说明 |
| `draw.mode` | 是 | `timed` / `instant` / `full` / `manual` |
| `draw.start_at` | 否 | `now`、Unix 秒、ISO 8601，默认 `now` |
| `draw.end_at` | 否 | ISO 8601 或 `30m` / `12h` / `3d`，默认 `3d` |
| `draw.max_people` | 否 | 1–1000，默认 100 |
| `draw.draws_per_user` | 否 | 1–100，默认 1 |
| `draw.people_count` | 满人开奖 | 触发开奖的人数，不得大于 `max_people` |
| `winning_rate` | 即抽即开二选一 | 总中奖率 0–100；用奖品数量按比例分摊 |
| `prizes[].probability` | 即抽即开二选一 | 该奖项中奖率，所有奖项总和不超过 100 |
| `prizes[].level` | 否 | 非 VIP 不提供；服务端按顺序使用“一等奖”开始的标准奖项名 |
| `prizes[].name` | 是 | 奖品名称 |
| `prizes[].count` | 是 | 1–9999 |
| `prizes[].delivery` | 否 | `express` 收集姓名/手机/地址；`none` 不收集，默认 `express` |
| `prizes[].image_url` | 否 | 已有 HTTPS 图片 URL；不填用系统默认图 |

## 约束

- WorkBuddy 直接创建正式活动，不需要 `test_mode`；测试活动不能转为正式活动。
- 定时、满人和手动开奖使用 `classic`；互动玩法必须使用 `instant`。
- 奖项上限：经典 50，大转盘 15，扭蛋机 50，砸金蛋 50，九宫格 8，翻翻乐 9。奖项超过玩法上限时不得选择该玩法。
- 非 VIP 边界：单个奖项最多 9999 份奖品；`draw.max_people` 和满人开奖的 `draw.people_count` 最大 1000；开始到结束最长 30 天。
- 如果同时填了 `winning_rate` 和每项 `probability`，以每项值为准，且两者必须一致。
- 第一版不使用 VIP 专属自定义奖项等级；`level` 由标准顺序生成，奖品名称放到 `name`。
- `get_lottery` 会返回包含 `activity_id`、`short_id` 和奖项 `custom_id` 的完整配置；更新时保留这些字段对应的值。
