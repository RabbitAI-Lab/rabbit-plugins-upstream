# 牛来风格Skill: 国产低成本3D动画视觉导演 v1.0.0

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Author: Qomob.AI](https://img.shields.io/badge/Author-Qomob.AI-blue)](https://qomob.ai)
[![Version: 1.0.0](https://img.shields.io/badge/Version-1.0.0-green.svg)](https://qomob.ai)

**牛来风格Skill** 是一款国产低成本3D动画视觉导演引擎。它将任何创意意图，通过 7 步 Pipeline 流程，重新设计成一部低预算国产3D动画里"本来就应该存在"的画面。

- **核心美学**: 2000年代国产低成本3D动画（粗糙建模/笨拙比例/僵硬动作/简单贴图/廉价材质/木讷表情）
- **设计哲学**: 不是模拟"旧"，而是模拟"当年真的没钱"
- **输出格式**: 可直接用于图像生成的英文 Prompt + Negative Prompt

## 与其他 3D 风格工具的区别

| 维度 | 典型 3D 风格工具 | 牛来风格Skill |
|------|----------------|---------------|
| **风格理解** | 堆砌 low-poly / retro CGI 关键词 | 重建"低成本动画生产逻辑"--建模/材质/灯光/渲染全链路模拟 |
| **核心定位** | 复古艺术化低模 | 真的粗糙：技术/预算/建模能力都有限但认真做了 |
| **世界一致性** | 粗糙角色 + 高级背景（割裂） | 角色+材质+场景+灯光+渲染全部粗糙（统一） |
| **风格控制** | 靠 Negative Prompt 防御 | 80% 正向风格架构控制 + 20% Negative Prompt |
| **质量验证** | 无 | 7 维度 Style Score + 风格漂移检测（< 75 分回退重编译） |
| **预算等级** | 固定风格 | Level 1（真实参考图级）/ Level 2（稍好看）可切换 |

## Pipeline 流程

```
用户创意
    ↓
Step 1: Intent Parser（意图解析）
    ↓
Step 2: Style Constitution（风格宪法 + Style DNA）
    ↓
Step 3: Subject Rebuilder（视觉对象重构）
    ↓
Step 4: Character & World Design（角色 + 世界设计）
    ↓
Step 5: Production & Render（制作模拟 + 渲染降级）
    ↓
Step 6: Prompt Compiler（提示词编译）
    ↓
Step 7: Style Validator（风格验证，< 75 分回退）
    ↓
最终 Prompt + Negative Prompt
```

## 文件结构

```
low-budget-3d/
├── SKILL.md                          # 路由 manifest + Pipeline 概览
├── version.json                      # 版本管理
├── evals/                            # 触发测试用例
│   ├── trigger_cases.json            # 正面触发（10 用例）
│   ├── negative_cases.json           # 不应触发（7 用例，含 5 near-miss）
│   └── orthogonal_cases.json         # 语义盲区（3 用例）
└── references/
    ├── style-constitution.md         # Style DNA + 4 Rules + 预算等级
    ├── subject-rebuilder.md          # 6 类对象转换矩阵
    ├── character-director.md         # 角色建模 + 脸部 + 材质
    ├── world-builder.md              # 场景 + 灯光 + 色彩 + 构图
    ├── production-and-render.md      # 制作模拟 + 渲染降级
    ├── prompt-compiler.md            # Prompt 汇编 + Negative + 适配器
    └── style-validator.md            # 7 维度评分 + 漂移检测
```

## 风格判断标准

> "如果把这张图放到一部2005年前后的国产儿童3D动画里，会不会毫无违和感？"

如果答案是"不会"，说明风格跑偏。

## 已知陷阱

| 陷阱 | 说明 |
|------|------|
| **"low-poly" 陷阱** | 引向精致低多边形插画，而非低成本动画感 |
| **"retro CGI" 陷阱** | 引向有意做旧的高级艺术风格，而非真的粗糙 |
| **真实毛发陷阱** | 绝对不要真实毛发，用简单贴图/塑料/黏土/橡胶 |
| **场景精致陷阱** | 不能"粗糙角色 + 高级电影背景" |
| **Pixar 漂移陷阱** | 模型默认倾向精致 CG，必须在每步主动降级 |

## 不处理

- Pixar / Disney / DreamWorks 风格或任何高级 CG
- 现代低模艺术（low-poly art）或精致低多边形插画
- 2D 动画 / 手绘 / 水彩 / 油画风格
- 真实渲染 / 电影级渲染 / photorealistic
- anime / 日系动画风格

## 加入群聊

<div align="center">
  <img src="https://qomob.ai/xskill.jpg" width="600" alt="XSkill">
</div>

---

## 许可证

本项目采用 [MIT License](https://opensource.org/licenses/MIT) 开源协议。

---
**牛来风格Skill v1.0.0** - 国产低成本3D动画视觉导演 | Created by **[Qomob.AI](https://qomob.ai)**
