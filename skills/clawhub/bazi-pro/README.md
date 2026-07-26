# Bazi Pro Skill (八字专业版)

Professional Bazi (Four Pillars of Destiny) calculation and analysis tool for OpenClaw, powered by DeepSeek AI.
专业的八字排盘与解读技能，结合传统命理算法与大模型深度分析，提供精准的格局判断和通俗易懂的运势解读。

## Features (功能特点)

- **精准排盘**: 支持真太阳时校正（默认经度 E120），包含四柱、藏干、十神等。
- **格局分析**: 根据《子平真诠》等格局派经典定格局（正格/变格/外格等），格局档次等。
- **旺衰分析**: 根据《滴天髓》等旺衰派经典判断身强身弱、取用神/喜神/忌神等。
- **关系推演**: 刑冲合害分析（天干五合、地支六合/三合/三会/相刑/相冲/相害）。
- **大运流年**: 详细的大运排盘及起运时间。
- **AI 深度解读**: 内置专业命理提示词，调用 DeepSeek等 大模型进行全方位性格、事业、婚姻、健康分析。

## Installation (安装)

### Option 1: Via ClawHub (Recommended)
如果您已经安装了 OpenClaw 和 ClawHub CLI：

```bash
clawhub install bazi-pro
```

### Option 2: Manual Installation
如果您想手动安装或从源码运行：

1.  进入 OpenClaw 技能目录：
    ```bash
    cd ~/.openclaw/skills
    ```
2.  克隆仓库：
    ```bash
    git clone https://github.com/rozario-dev/bazi-pro-skill.git bazi-pro
    ```
3.  安装依赖：
    ```bash
    cd bazi-pro
    npm install
    ```

## Configuration (配置)

本技能需要配置 DeepSeek API Key 才能启用 AI 解读功能。

1.  在技能根目录下创建 `.env` 文件（可以复制示例文件）：
    ```bash
    cp .env.example .env
    ```
2.  编辑 `.env` 文件，填入您的 API Key：
    ```ini
    DEEPSEEK_API_KEY=your_deepseek_api_key_here
    DEEPSEEK_BASE_URL=https://api.deepseek.com
    DEEPSEEK_MODEL=deepseek-chat
    ```

*注：如果没有 DeepSeek Key，也可以使用 `OPENAI_API_KEY` 作为备选，但建议使用 DeepSeek 以获得最佳的中文命理解读效果。*

## Usage (使用方法)

在 OpenClaw 对话中，您可以直接用自然语言调用：

> "帮我算一下八字，1990年5月15日14点，男"
> "分析这个命盘：1988/8/8 8:00 女"

### Command Line Usage (命令行调用)

如果您想在终端直接运行或测试：

```bash
# 标准排盘 + AI 解读
node index.js --year 1990 --month 5 --day 15 --hour 14 --gender Male

# 仅排盘（不消耗 Token）
node index.js --year 1990 --month 5 --day 15 --hour 14 --gender Male --no-interpret

# 仅查看命主一生格局（不看大运）
node index.js --year 1990 --month 5 --day 15 --hour 14 --gender Male --no-dayun
```

### Arguments (参数说明)

- `--year`: 出生年份 (如 1990)
- `--month`: 出生月份 (1-12)
- `--day`: 出生日期 (1-31)
- `--hour`: 出生时辰 (0-23)
- `--minute`: 出生分钟 (0-59, 默认为 0)
- `--gender`: 性别 (Male/Female, 默认为 Male)
- `--interpret`: 强制开启 AI 解读 (默认开启)
- `--no-interpret`: 关闭 AI 解读，仅输出排盘数据

## License

ISC
