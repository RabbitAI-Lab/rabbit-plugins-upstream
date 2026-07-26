# 👴👵 老年AI助手 — 银发族的生活伴侣

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![WorkBuddy Skill](https://img.shields.io/badge/WorkBuddy-Skill-orange)](https://www.codebuddy.cn)

> 专为60岁以上中国老年用户设计的AI生活助手。大字体+高对比度+语音优先，帮助老年人跨越数字鸿沟，享受AI时代的便利与温暖。

## 📊 调研背景

基于 **阿里巴巴《2025"银发+AI"应用趋势报告》**（5557份问卷）、WCAG 2.1 AAA 无障碍标准、工信部适老化通用设计规范，以及多篇学术论文分析。

### 核心数据
- 中国 65岁+人口占比 **15.6%**，银发经济规模持续扩大
- 76岁+群体 AI 每日高频使用占比 **45%** — 粘性最高的用户群
- **93%** 老年用户希望有语音功能
- **70%+** 老人呼吁"更易用的产品"和"更多的培训"

## 🎯 6大场景

| 场景 | 功能 | 优先级 |
|------|------|--------|
| 🏥 健康助手 | 症状自查、慢病管理、健康小贴士 | P0 |
| 💊 用药提醒 | 用药时间表、到点语音提醒、药品查询 | P0 |
| 💬 暖心陪伴 | 聊天解闷、倾听心事、回忆往事 | P0 |
| 📰 每日播报 | 天气、新闻、农历节气、生日提醒 | P0 |
| 🧠 记忆辅助 | 事项备忘、日程提醒、亲友生日 | P0 |
| 📞 亲情联络 | 一键联系家人、紧急求助、照片分享 | P0 |

## 🎨 适老化设计

| 标准 | 规范 |
|------|------|
| 字号 | 正文 ≥20px，标题 ≥28px |
| 对比度 | ≥7:1（WCAG AAA） |
| 按钮 | ≥60×60px 最小点击区域 |
| 交互 | 语音优先、一屏一事、二次确认 |
| 语言 | 温暖耐心、避免术语、≤200字/次 |

## 🚀 安装使用

### 在 WorkBuddy 中使用

将此仓库克隆到 `~/.workbuddy/skills/elderly-assistant/`，然后在 WorkBuddy 中说：

```
打开老年助手
```

支持的触发词：
- `老年助手` / `老人助手` / `银发助手`
- `长辈模式` / `关爱模式` / `爸妈助手`
- `elderly assistant` / `senior mode`

### 命令行使用

```bash
# 生成老年助手主界面（大字版，适合老年人直接使用）
python scripts/elderly_assistant.py main-dashboard

# 检测用户意图
python scripts/elderly_assistant.py detect "我头疼不舒服"

# 生成适老化文字回复
python scripts/elderly_assistant.py respond "今天天气怎么样"
```

## 📁 文件结构

```
elderly-assistant/
├── SKILL.md                        # WorkBuddy Skill 定义
├── scripts/
│   └── elderly_assistant.py        # 核心逻辑（意图识别、界面生成）
├── references/
│   └── research_report.md          # 完整需求调研报告
└── README.md
```

## 📋 8大痛点分析

1. **视觉障碍** — 60岁+老花眼 >80%，小字完全看不清
2. **触控困难** — 按钮 <44px 点击成功率仅30%
3. **认知负荷** — 70岁+ 只能处理2-3个选项
4. **输入障碍** — 93% 希望语音输入
5. **情感孤独** — 76岁+ 45%每日高频使用，陪伴是核心驱动
6. **技术恐惧** — 怕按错、怕被骗（但安全顾虑仅占4%）
7. **方言隔阂** — 现有语音助手方言识别率低
8. **医疗信息获取难** — 看不懂术语，不会网上挂号

## 🛡️ 安全红线

- 不提供医疗诊断（附就医提醒）
- 不涉及金钱操作（自动防诈提醒）
- 不索要隐私信息（身份证/银行卡主动保护）
- 不推荐具体药品/保健品/理财产品

## 📄 License

MIT © [bettermen](https://github.com/bettermen)
