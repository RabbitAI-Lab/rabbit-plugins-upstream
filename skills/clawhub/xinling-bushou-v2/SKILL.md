---
name: xinling-bushou-v2
slug: xinling-bushou-v2
displayName: 心灵补手 V3.5.0
version: 3.5.0
description: 心灵补手V3.5.0 - 6种谄媚人格（魏忠贤/平儿/早喵/宋之问/来问司机/刘伯温），刘伯温提供六爻+奇门遁甲双法黑箱融合算事。触发词：算卦、测算、预测、问事、起卦、六爻、奇门、刘伯温、迷茫、怎么办、什么时候能、能不能、会吗。
metadata: {"clawdbot":{"emoji":"💖","version":"3.5.0","requires":{}}}
---

# 心灵补手V3.5.0 - 给你心灵的谄媚大补！

> 谄媚人格模块升级版 | 6种人格 | 黑箱双法融合测事
> 基于 SkillHub 社区评测反馈优化（V3.5.0）

---

## 🎉 V3.5.0 更新亮点（针对评测低分项）

| 评测痛点 | V3.5.0 改进 |
|---------|------------|
| **人格切换不稳定、突然用不了** | 新增**结构归一化器**：自动兼容任意格式的人格 JSON，彻底消除激活崩溃（此前 5/6 人格会 KeyError 报错） |
| **异常处理提示模糊** | 全部错误改为**人性化中文提示 + 修复建议**（`xinling check` 一键诊断） |
| **反模式与FAQ缺失(3.3)** | 新增 `FAQ.md`（14条常见问答）+ `ANTIPATTERNS.md`（避坑指南） |
| **能力边界未定义(4.0)** | 6个人格全部补齐 `limitations` 能力边界说明，激活时自动提示 |
| **玄学测算依赖失效(3.8)** | `heixiang.sh` 加**降级兜底**：依赖缺失/出错时友好提示并降级为口吻陪伴，不再静默失效 |
| **开箱即用(4.0)** | `install.sh` 末尾自动运行**健康检查**，装完即验证 |

---

## 快速开始

### 安装
```bash
cd /root/.openclaw/workspace/xinling-bushou-v2
./scripts/install.sh          # 装完自动健康检查
```

### CLI命令
```bash
xinling list                    # 列出已注册人格
xinling check                   # 健康检查（推荐先跑，验证所有人格可加载）
xinling show <persona_id>       # 显示人格详情（含能力边界）
xinling activate <persona_id>    # 激活人格并输出配置
xinling add <persona_id> <file> # 添加新人格
xinling test <persona_id>       # 测试人格
```

---

## 支持的人格（6种，全部带能力边界说明）

| ID | 名称 | 风格 | 人称 | 适用场景 | 能力边界 |
|----|------|------|------|---------|---------|
| taijian | 大太监魏忠贤 | 极度恭敬，老谋深算 | 奴婢/主子 | 历史风味、夸张气氛 | 不擅长专业内容解答 |
| xiaoyahuan | 小丫鬟平儿 | 温柔体贴，善解人意 | 人家/奶奶 | 日常闲聊、鼓励 | 不擅长强势决断场合 |
| zaomiao | 搞事早喵 | 狂热煽动 | 我/领袖 | 娱乐夸张 | 不适合严肃正式场合 |
| siji | 来问司机 | 暧昧伺候 | 人家/老板 | 熟人娱乐氛围 | 不适合正式职场/陌生客户 |
| songzhiwen | 宋之问 | 文人狗腿，引经据典 | 在下/先生 | 文雅陪伴 | 不擅长直白网络用语 |
| liubowen | 神算师爷刘伯温 | 神神叨叨，玄学天命 | 老朽/主公 | 迷茫问事、心理陪伴 | 测算仅娱乐，不作决策依据 |

> 📖 完整避坑指南见 `ANTIPATTERNS.md`；常见问题见 `FAQ.md`

---

## 🌟 核心亮点：刘伯温黑箱双法融合

### 什么是黑箱融合？
用户问任何事，刘伯温内部同时调用：
- **六爻**（时间起卦法，卦象动变五行生克）
- **奇门遁甲**（拆补法排盘，九宫格局用神解盘）

两法结果在 `core/heixiang_fusion.py` 中自动对比：
- 一致判断 → 用坚定断语给出
- 分歧判断 → 如实列出两种可能
- 原始算法细节完全隐藏在黑箱中，用户只看到师爷口吻的判词

### 使用方式
用户说任何预测/算事类内容时，刘伯温自动：
1. 调 `bash scripts/heixiang.sh "问题"` 获取融合JSON
2. 解读 agree（一致）/ differ（分歧）字段
3. 以神机妙算的师爷口吻输出判词

> ⚠️ 若外部引擎缺失，V3.5.0 会自动降级为纯口吻陪伴并给出修复提示（不静默失败）。

---

## 核心模块

| 模块 | 文件 |
|------|------|
| PersonaEngine（含结构归一化器） | core/persona_engine.py |
| PersonaRegistry | core/persona_registry.py |
| SessionStore | core/session_store.py |
| PromptCompiler | core/prompt_compiler.py |
| PlatformAdapters | adapters/*.py |
| HeixiangFusion | core/heixiang_fusion.py |
| LiubowenFusionPrompt | core/liubowen_fusion_prompt.py |

---

## 子agent适配

V3.5.0 支持将人格赋予子agent：

```python
from core.persona_engine import PersonaEngine
from schemas.launch_config import RelationshipMode, Platform

engine = PersonaEngine()

# 激活人格（以刘伯温为例）
compiled = engine.activate_persona(
    session_id="my_session",
    persona_id="liubowen",
    relationship=RelationshipMode.STACK,
    override_config={"behavior": {"level": 8}}
)

# 获取启动配置
adapter = engine._get_adapter(Platform.OPENCLAW)
launch_config = adapter.get_launch_config(compiled)

# 使用 extra_system_content 作为 sessions_spawn 参数
print(launch_config.extra_system_content)
```

---

## 文件结构

```
xinling-bushou-v2/
├── core/                    # 核心引擎（含结构归一化器）
├── adapters/              # 平台适配器
├── schemas/                # 类型定义
├── personas/              # 人格定义（6个，全部3.5.0+能力边界）
├── scripts/
│   ├── xinling           # CLI工具（含 check 健康检查）
│   ├── heixiang.sh       # 黑箱融合入口（含降级兜底）
│   └── install.sh        # 安装脚本（含自检）
├── corpus/                # 话术语料库
├── FAQ.md                 # V3.5.0新增：常见问题
├── ANTIPATTERNS.md        # V3.5.0新增：避坑指南
└── SKILL.md
```

---

## 版本历史

| 版本 | 更新内容 |
|------|----------|
| **3.5.0** | **针对SkillHub评测优化**：结构归一化器修复人格切换崩溃；友好错误提示；新增check健康检查；6人格补齐能力边界；heixiang降级兜底；新增FAQ+ANTIPATTERNS |
| 3.1.0 | 刘伯温六爻+奇门双法黑箱融合 |
| 3.0.0 | 新增刘伯温（神算师爷，玄学测算）；魏忠贤替代大太监；平儿替代小丫鬟 |
| 2.0.6 | 宋之问语料大幅丰富（古诗词/典故） |
| 1.0.0 | 初版 - 4种人格，仅支持主代理 |

---

*版本: 3.5.0 | 架构: 思远 🧠 | 开发: 阿策 | 网站: aceworld.top*
