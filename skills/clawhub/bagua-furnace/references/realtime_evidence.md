# 八卦炉 · 真机测试证据（2026-08-26）

> 目的：用用户真实素材跑通八卦炉第 0 关 + 九转，验证技能真能炼出方法卡（非占位）。
> 素材（用户现场提供）：
> - `H:/书单Top10_获取PDF用.xlsx` —— Top10 书单（含 ISBN、出版社）
> - `H:/书单.zip` —— 12 个图书 PDF（10 本书，毛选分 4 卷；缺《人有人的用处》《第一哲学沉思集》两本 PDF）
> - `C:/Users/zyd/WorkBuddy/2026-07-10-22-37-49/抖音文案提取_7671986884592010673.md` —— 抖音「大李书房一盏灯」《最值得被蒸馏的书 Top10》口播文案转写稿

---

## 一、第 0 关 接料辨体（路由实测）

| 输入 | 判定 | 转换动作 | 结果 |
|---|---|---|---|
| 抖音文案 `.md` | 已是文本 → 直入 | 直接进九转 | ✅ 无需转换 |
| `书单.zip` 内 PDF | `.pdf` | 解压（cp437→gbk 还原中文名）→ 读正文 | ⚠️ Read 工具报二进制 → 改用 pypdf 抽取（见 G4） |
| `书单Top10.xlsx` | 表格 | openpyxl 读（仅确认书单，与文案一致） | ✅ 非提炼主输入，作交叉核对 |
| 抖音链接 `douyin.com/video/767...` | 短视频域名 | 用户已给转写稿，跳过；若仅给链接则走 `douyin_copy_extract` | ✅ 文案已就绪 |

**关键发现 G4**：本环境 Read 工具对 PDF（含中文名与 ASCII 名）返回「Cannot display content of binary file」，SKILL.md 原「Read 工具直接读 PDF 全文」在本沙箱不成立。已用隔离 venv `pypdf` 抽取《失控》前 60 页（共 632 页）兜底，验证九转可跑通。

---

## 二、九转提炼实测

### Path A · 抖音文案（文本直入）
- 收料定标：提炼「每本书的可迁移方法论」+ 博主「蒸馏书方法论」元框架。
- 辨体选型：视频转写稿 → 按「书原理」透镜逐本萃取。
- 粗炼取料：原样抽取每本书「为什么值得蒸馏 + 能蒸出什么 + 底层原理」。
- 淬炼抽象：把「这本书讲啥」拆成「可迁移底层模式」（涌现/系统思考/英雄之旅/第一性原理/自我质疑/Harness/媒介即信息/多Agent管理/人的价值/战略行动）。
- 成丹定型：11 张标准卡（1 元卡 + 10 书卡），字段齐全含来源溯源。
- 对勘校验：置信度分级（板上钉钉 / 八成·需看原始材料）。

### Path B · 《失控》PDF 正文（pypdf 抽取）
- 抽前 60 页正文，识别「涌现」核心论述。
- 与文案 Top10 提炼互证：序言 p3–4、p59–61 明确「大量个体遵循简单规则+大规模协作→涌现复杂能力；深度学习是涌现最好例证」，**与文案一致**。
- 方法卡 #1「涌现思维」置信度上调：板上钉钉（书+文案双源互证）。

---

## 三、产物

- 方法卡集：`~/.workbuddy/methodology-library/distill-books-top10.md`（11 卡，可溯源）。
- 本证据文件：`references/realtime_evidence.md`。

---

## 四、结论

- ✅ 八卦炉第 0 关 + 九转在真实素材上跑通，产出**非占位真卡**（抖音文案 10 本 + 元框架 + 《失控》正文交叉验证）。
- ✅ 差异化成立：产的是「顾问级方法卡」（扫地僧可"想"着用），不是可执行 Skill。
- ⚠️ G4 缺口已发现并兜底：PDF 读取在本环境需 pypdf，非 Read 工具。
- 待补（不阻塞）：G1 ASR 端点未部署；两本 PDF（《人有人的用处》《第一哲学沉思集》）缺失未测。

## 五、复现命令（PDF 路径）

```bash
# 隔离 venv（仅一次）
<managed_python> -m venv <runtime>/envs/default
<runtime>/envs/default/Scripts/pip install pypdf
# 抽《失控》前 60 页
<runtime>/envs/default/Scripts/python - <<'PY'
import pypdf
r=pypdf.PdfReader(r"test-materials/失控.pdf")
open("kongzhi_text.txt","w",encoding="utf-8").write(
  "\n".join((p.extract_text() or "") for p in r.pages[:60]))
PY
```
