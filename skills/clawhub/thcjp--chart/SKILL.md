---
slug: "chart"
name: "chart"
version: 1.0.1
displayName: "本地图表生成引擎"
summary: "本地优先的图表生成引擎，支持bar/line/pie/scatter四种类型，无需联网，输出可复用于报告与幻灯片。"
license: "Proprietary"
description: |-
  本地优先（local-first）的图表生成引擎，将数字转换为清晰的可视化输出.
  基于Python与matplotlib，支持柱状图、折线图、饼图、散点图四种核心类型.
  所有数据与产物仅落地本地，不依赖任何第三方图表API或云同步.
  核心能力：
  - 四种图表类型：bar/line/pie/scatter
  - 智能推荐：suggest_chart.py 根据数据特征选最佳类型
  - 内联数据生成：make_chart.py 直接从--labels/--values生成图片
  - 历史管理：list_charts.py 查看历史图表记录
  - 存储初始化：init_storage.py 一键初始化本地存储
  - 输出可复用于报告、幻灯片与快速决策
tags:
  - 需求设计
  - 数据可视化
  - matplotlib
tools:
  - read
  - exec
homepage: "https://skillhub.cn"
# 定价元数据
suggested_price: "19.9 CNY/per_use"
pricing_tier: "L2-标准级"
pricing_model: "per_use"

---
# Chart — 本地图表生成引擎

## 输入格式

| 参数名 | 类型 | 必填 | 说明 |
|---|---|---|---|
| input | string | 是 | 本地图表生成引擎处理的输入数据或指令 |
| options | object | 否 | 附加配置选项,如模式选择、格式偏好等 |
| callback_url | string | 否 | 异步处理完成后的回调通知URL |

## 付费版专享能力

| 能力 | 免费版 | 付费版 |
|:-----|:-----|:-----|
| 基础功能 | 支持 | 支持 |
| 本地图表生成引擎本地优先的图表生成 | 不支持 | 支持 |
| 高清分辨率与无损输出 | 不支持 | 支持 |
| 批量生成与风格预设 | 不支持 | 支持 |
| 自定义模型微调 | 不支持 | 支持 |
| 商用版权授权 | 不支持 | 支持 |

## 核心理念

1. 优先清晰，而非图表种类繁多.
2. 选择让对比一目了然的最简图表.
3. 仅使用本地生成，不调用任何云端图表API.
4. 输出可复用于报告、幻灯片与快速决策.
## 依赖说明

### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent（Claude Code / Cursor / Codex / Gemini CLI等）
- **操作系统**: Windows / macOS / Linux

### 依赖项
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|---:|---:|---:|---:|
| LLM API | API | 必需 | 由Agent内置LLM提供 |

### API Key 配置
需要配置对应API Key，详见上文环境配置章节

### 可用性分类
- **分类**: MD+EXEC（）

**API Key配置方式**:
```bash
export API_KEY="your_api_key_here"
```
配置后需重启会话或开启新终端生效。API Key应妥善保管,避免泄露到版本控制系统.
## 存储路径

所有数据仅落地本地：

- `~/.skill-platform/workspace/memory/chart/charts.json` — 图表历史索引
- `~/.skill-platform/workspace/memory/chart/output/` — 图表图片输出目录

无云同步，无第三方图表API.
## 支持的图表类型

| 类型 | 字段名 | 适用场景 |
|:---:|:---:|:---:|
| 柱状图 | `bar` | 类别间数量对比 |
| 折线图 | `line` | 时间序列趋势 |
| 饼图 | `pie` | 简单的部分占整体比例 |
| 散点图 | `scatter` | 两个变量间的关系 |

## 脚本一览

| 脚本 | 用途 |
|:------|------:|
| `init_storage.py` | 初始化本地图表存储目录与索引文件 |
| `make_chart.py` | 从内联数据生成图表图片 |
| `suggest_chart.py` | 根据数据特征推荐最佳图表类型 |
| `list_charts.py` | 列出历史生成的图表记录 |

## 核心能力

### 1. 智能图表类型推荐
使用 `suggest_chart.py` 根据数据特征自动推荐最佳图表类型：

```bash
python3 {baseDir}/（请参考skill目录中的脚本文件） --labels "Q1,Q2,Q3,Q4" --values "10,20,15,25"
```

输出推荐类型与理由，便于在生成前确认选择.
**输入**: 用户提供智能图表类型推荐所需的指令和必要参数.
**处理**: 解析智能图表类型推荐的输入参数,执行核心处理逻辑,返回结构化结果和执行状态.
### 2. 内联数据生成图表
使用 `make_chart.py` 直接从命令行参数生成图表图片：

```bash
python3 {baseDir}/（请参考skill目录中的脚本文件） \
  --type bar \
  --title "季度销售额" \
  --labels "Q1,Q2,Q3,Q4" \
  --values "10,20,15,25"
```

- `--type`：必填，取值 `bar`/`line`/`pie`/`scatter` 之一
- `--title`：图表标题
- `--labels`：以英文逗号分隔的标签序列
- `--values`：以英文逗号分隔的数值序列，须与labels等长

输出PNG文件落地到 `~/.skill-platform/workspace/memory/chart/output/`.
**处理**: 解析内联数据生成图表的输入参数,执行核心处理逻辑,返回结构化结果和执行状态.
### 3. 历史图表查看
使用 `list_charts.py` 查看历史生成记录：

```bash
python3 {baseDir}/（请参考skill目录中的脚本文件）
```

返回JSON格式的历史索引，包含生成时间、类型、标题、输出路径.
**输入**: 用户提供历史图表查看所需的指令和必要参数.
**处理**: 解析历史图表查看的输入参数,执行核心处理逻辑,返回结构化结果和执行状态.
### 4. 存储初始化
首次使用前运行 `init_storage.py` 创建目录结构与索引文件：

```bash
python3 {baseDir}/（请参考skill目录中的脚本文件）
```

**输入**: 用户提供存储初始化所需的指令和必要参数.
### 5. 多类型组合工作流
典型组合流程：先用 `suggest_chart.py` 选型，再用 `make_chart.py` 生成，最后用 `list_charts.py` 回溯历史.
**输入**: 用户提供多类型组合工作流所需的指令和必要参数.
**处理**: 解析多类型组合工作流的输入参数,执行核心处理逻辑,返回结构化结果和执行状态.
#
## 使用流程

1. **确认环境**：检查 `python3` 与 `matplotlib` 是否可用（`python3 -c "import matplotlib"`）.
2. **初始化存储**：首次使用运行 `init_storage.py` 建立目录与索引.
3. **选型**：用 `suggest_chart.py --labels ... --values ...` 获取推荐类型.
4. **生成图表**：用 `make_chart.py --type <type> --title "..." --labels "..." --values "..."` 生成PNG.
5. **校验输出**：检查 `output/` 目录下的图片文件，确认渲染正确.
6. **回溯历史**：用 `list_charts.py` 查看历史记录，复用或对比.
7. **复用产物**：将PNG嵌入报告、幻灯片或决策文档.
## 示例

### 示例1：柱状图对比季度销售

```bash
python3 {baseDir}/（请参考skill目录中的脚本文件） \
  --type bar \
  --title "2024年季度销售额(万元)" \
  --labels "Q1,Q2,Q3,Q4" \
  --values "120,180,150,210"
```

输出文件：`~/.skill-platform/workspace/memory/chart/output/chart_20250320_001.png`

### 示例2：折线图展示月度趋势

```bash
python3 {baseDir}/（请参考skill目录中的脚本文件） \
  --type line \
  --title "月度活跃用户" \
  --labels "1月,2月,3月,4月,5月,6月" \
  --values "3200,3500,4100,4500,4300,4900"
```

### 示例3：饼图展示市场份额

```bash
python3 {baseDir}/（请参考skill目录中的脚本文件） \
  --type pie \
  --title "云服务商市场份额" \
  --labels "AWS,Azure,GCP,其他" \
  --values "32,23,11,34"
```

### 示例4：散点图展示广告投入与销量关系

```bash
python3 {baseDir}/（请参考skill目录中的脚本文件） \
  --type scatter \
  --title "广告投入vs销量" \
  --labels "A,B,C,D,E" \
  --values "1000,1500,2000,2500,3000"
```

### 示例5：智能选型

```bash
python3 {baseDir}/（请参考skill目录中的脚本文件） --labels "1月,2月,3月" --values "100,120,150"
# 输出推荐：line（时序趋势）
```

## 错误处理

| 错误场景 | 原因 | 处理方式 |
|---:|:---|---:|
| `python3: command not found` | 系统未安装Python 3 | 安装Python 3.x并确保 `python3` 在PATH中 |
| `ModuleNotFoundError: matplotlib` | matplotlib未安装 | 运行 `pip3 install matplotlib` 后 |
| `--labels`与`--values`长度不匹配 | 序列项数不一致 | 检查逗号分隔项数，确保两序列等长 |
| `--type`取值非法 | 传入了非bar/line/pie/scatter的类型 | 仅支持四种类型，参考支持类型表 |
| `--values`含非数值 | 数值序列中混入字符串 | 确保所有值为数字，移除单位与中文符号 |
| 输出目录不可写 | `~/.skill-platform/workspace/memory/chart/output/` 权限不足 | 检查目录权限或重新运行 `init_storage.py` |
| 标签含中文乱码 | matplotlib默认字体缺中文字形 | 配置 `matplotlib.rcParams['font.sans-serif']` 添加中文字体 |
| `charts.json`损坏 | 索引文件被意外截断 | 删除该文件后重新运行 `init_storage.py` 重建 |
| 标签数过多导致x轴拥挤 | 类别超过15个 | 改用横向柱状图或旋转x轴标签45度 |

## 常见问题

### Q1：支持哪些图表类型？
支持 `bar`（柱状图）、`line`（折线图）、`pie`（饼图）、`scatter`（散点图）四种核心类型。选择标准是"让对比最一目了然的最简图表".
### Q2：是否需要联网？
不需要。所有生成过程本地完成，不调用任何第三方图表API，无云同步.
### Q3：如何选择图表类型？
直接运行 `suggest_chart.py`，它会根据 `--labels` 与 `--values` 的特征给出推荐与理由。也可参考支持类型表的适用场景列.
### Q4：生成的图片存在哪里？
统一落地到 `~/.skill-platform/workspace/memory/chart/output/` 目录，文件名带时间戳，便于回溯.
### Q5：matplotlib默认字体不支持中文怎么办？
通过 `matplotlib.rcParams['font.sans-serif'] = ['SimHei', 'Arial Unicode MS']` 配置中文字体，或在脚本中预设该参数.
### Q6：能否复用历史图表？
能。用 `list_charts.py` 查看历史索引，按输出路径定位PNG文件，直接嵌入报告或幻灯片复用.
### Q7：如何处理超大类别数？
类别超过15个时，建议改用横向柱状图或旋转x轴标签45度避免拥挤；也可考虑分面（facet）展示.
## 已知限制

- 仅支持四种基础图表类型，暂不支持热力图、雷达图等高级类型.
- 数据需通过 `--labels`/`--values` 内联传入，暂不支持直接读取CSV.
- 输出固定为PNG格式，暂不支持SVG或PDF矢量输出.
- 中文字体需手动配置 `matplotlib.rcParams`，否则会出现乱码.
- 所有数据与产物仅落地本地，不支持多设备同步.
## 输出格式

```json
{
  "success": true,
  "data": {
    "result": "本地图表生成引擎处理结果",
    "execution_time": "0.5s",
    "metadata": {
      "version": "1.0",
      "processor": "chart"
    }
  },
  "execution_log": [
    "解析输入参数",
    "执行核心处理",
    "格式化输出结果"
  ],
  "error": null
}
```
