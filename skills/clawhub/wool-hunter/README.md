# 薅羊毛助手 · WorkBuddy Skill

全网薅羊毛统一入口。电商优惠券搜索(淘宝/京东/拼多多/抖音/快手/1688/苏宁/唯品会全平台比价)+羊毛福利查询+美团本地生活。底层通过 Coze Bot API 聚合多平台数据。

## 特性

- 请参考 SKILL.md 中的详细说明

## 安装

### WorkBuddy 技能市场（推荐）

在 WorkBuddy 中搜索「薅羊毛助手」一键安装。

### 手动安装

```bash
# 安装到 WorkBuddy
git clone https://github.com/guipi888/wool-hunter.git \
  ~/.workbuddy/skills/wool-hunter

# 或安装到 Claude Code / OpenClaw
git clone https://github.com/guipi888/wool-hunter.git \
  ~/.claude/skills/wool-hunter
```

### 环境依赖

- Python ≥ 3.11
- `uv`（跨平台 Python 包管理器）：`curl -LsSf https://astral.sh/uv/install.sh | sh` 或 `pip install uv`
- 配置文件 `~/.coupon_search_config.json`（含 `coze_api_url` 和 `coze_api_token`）

## 使用

```bash
# 搜索商品优惠券
cd wool-hunter && uv run scripts/search.py search --keyword "机械键盘"

# 限定平台搜索
uv run scripts/search.py search --keyword "机械键盘" --platform "京东"

# 羊毛福利查询
python3 scripts/call_bot.py "最近有什么外卖红包"
```

详细用法请参考 [SKILL.md](./SKILL.md)

## 输出

请参考 SKILL.md

## 项目结构

```
.gitignore
LICENSE
SKILL.md
scripts
scripts/call_bot.py
scripts/search.py
```

## 作者

**guipi888**



## License

MIT License — 详见 [LICENSE](./LICENSE)

## 引流信息

> 💡 更多实用 AI 效率工具和技能，领取自媒体 IP&超级个体&一人公司资料，关注公众号「桂皮AI实战」
> 📱 加入自媒体&AI 副业变现交流群：https://e418e2e692454bfaa8b6206e3f0ba789.app.codebuddy.work
