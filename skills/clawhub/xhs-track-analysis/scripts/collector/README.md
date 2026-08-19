# 受监督有界采集器（collector）

> 本目录是 `xhs-track-analysis` Skill 的**可选独立组件**，用于把"网页端手动翻页查看"的过程在**你本人监督下**自动化，产出可被 Skill 分析的原始公开资料。

## 边界（务必遵守）
- ✅ 仅本人/授权账号、你本人在场（headed 浏览器）、仅**公开搜索/笔记页**。
- ✅ 限关键词、限排序、限条数、限频（见 config）。
- ❌ **不**实现任何反爬/请求签名伪造/滑块绕过/设备指纹伪造。
- ❌ **不**采集非公开数据，不做超范围使用。
- ⚠️ 运行即表示你已知悉并自行承担账号与合规风险（含评论数据的个人信息处理合规）。

## 安装
```bash
pip install -r requirements.txt
playwright install chromium
```

## 配置
复制并修改：
```bash
cp config.example.json config.json
```
`config.json` 字段：
- `keywords`：要研究的关键词列表
- `sorts`：排序角度（综合/最新/最多点赞/最多收藏/最多评论）
- `max_notes_per_query`：每个「关键词×排序」最多摘取条数
- `scroll_times`：每个查询滚动次数
- `delay_sec`：操作间隔（限频）
- `output_dir`：输出目录

## 运行
```bash
python3 collect.py config.json
```
1. 启动后会打印免责声明，需键入 `我已知悉并承担合规责任` 才继续。
2. 自动打开浏览器并展示登录二维码，**请用手机扫码**。
3. 登录成功后按 config 自动摘取，结果写入 `output/`：
   - `raw_notes_<时间戳>.csv`：每条笔记的原始字段
   - `collection_report_<时间戳>.md`：主表风格的原始资料（**不含判断**）

## 与 Skill 的衔接
采集产物是**原始资料**。把 `collection_report.md` 交给 `xhs-track-analysis` Skill，按其 `references/methodology.md` 完成：四分组、四排序角度、合并去重、商业化浓度标注、达人解读、评论四行为归类、决策收敛。采集器**不做**这些判断——这正是"人在回路 / 受监督"的设计意图。

## 维护提示
小红书前端选择器会变。若摘取为空，请核对 `collect.py` 顶部 `SELECTORS` 字典，按当前页面结构更新选择器即可。
