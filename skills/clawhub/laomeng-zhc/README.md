# 老孟中文编程（ZHC）· Agent Skill

面向各编程智能体（Claude Code / Codex / Cursor / Cline / 通义灵码 / 豆包 MarsCode 等支持 Agent Skills 的运行时）的分发包。安装后，智能体即可用中文编写、编译、诊断 ZHC 源码，并把数据导出为 Excel / Word / HTML / CSV。

## 版本

| 项 | 值 |
|---|---|
| 技能版本 | 1.0.0 |
| 语言面契约 | ZHC-LANG-1.0 |
| 桥面契约 | OFFICE-WEB 2.4 |
| 冻结日期 | 2026-11-09 |
| 语言规模 | 关键字 44 · 类型 11 · 内置函数 39 · 错误码 38 |

## 目录结构

```
laomeng-zhc/
├── SKILL.md                      # 技能主文件（元数据 + 指令）
├── README.md                     # 本文件
├── LICENSE.txt
├── references/
│   ├── 契约_1.0.md               # 语言契约全文
│   ├── 错误码表_E_1.0.md         # 38 个码位的成因与修法
│   └── 快速参考.md               # 一页速查（关键字/类型/内置/骨架）
├── scripts/
│   ├── zhc.py                    # 语言内核（单文件，无第三方依赖）
│   ├── 桥/zhc_bridge.py          # Office 导出桥（需 openpyxl / python-docx）
│   └── 示例/
│       ├── 基础.zc
│       ├── 语法骨架.zc
│       └── 导出表格.zc
└── assets/
    ├── lockup-language.png       # 横式组合标志
    └── logo-language-256.png     # 字标
```

> `scripts/桥/` 这个目录名不可改：内核按「与 `zhc.py` 同级的 `桥` 目录」定位桥脚本，该路径在编译期烧入产物。位移后须用环境变量 `ZHC_BRIDGE_HOME` 覆盖。

## 安装

### 方式一：放入智能体的技能目录

```bash
# 项目级
cp -r laomeng-zhc <项目>/.claude/skills/
# 或用户级
cp -r laomeng-zhc ~/.claude/skills/
```

其他运行时同理：放到其约定的 `skills/` 目录下，保持 `laomeng-zhc/` 整个文件夹完整。智能体启动时只读取 `SKILL.md` 的 `name` 与 `description`，命中中文编程类任务后再按渐进披露加载其余文件。

### 方式二：作为 MCP/工具集挂载

若运行时不支持 Agent Skills，把 `scripts/` 作为工具暴露，`references/` 与 `assets/` 作为只读资源挂载，`SKILL.md` 正文转成系统提示即可。

## 依赖

| 组件 | 要求 |
|---|---|
| Python | 3.9+（建议 3.11），运行需加 `-X utf8` |
| C 编译器 | gcc / clang，且必须在 PATH 中（内核生成 C 后调用） |
| Office 导出 | `pip install openpyxl python-docx`（仅导出 xlsx/docx 时需要） |
| 平台 | Windows x86-64（桥依赖 Win32 管道与宽字符 API） |

## 自检

```bash
python -X utf8 scripts/zhc.py --api            # 打印 11 类型 / 39 内置手册
python -X utf8 scripts/zhc.py scripts/示例/基础.zc --诊断
python -X utf8 scripts/zhc.py scripts/示例/基础.zc --run
python -X utf8 scripts/zhc.py scripts/示例/导出表格.zc --run   # 桥可用=真 时产出 xlsx
```

`--诊断` 返回 `{"ok": true}` 即环境正常。桥不通时导出会自动降级为 CSV（报文 `降级: true`），不影响编译执行。

## 与 IDE 插件的关系

配套编辑器扩展 `laomeng.zhc-chinese-language`（0.2.4）提供语法高亮、补全、诊断与 LSP 接入，其内核即为本包的 `scripts/zhc.py`。二者版本对应关系：

| 技能版本 | 扩展版本 | 契约 |
|---|---|---|
| 1.0.0 | 0.2.4 | ZHC-LANG-1.0 / OFFICE-WEB 2.4 |

## 许可

见 `LICENSE.txt`。语言内核、契约文档、错误码表与标志体系著作权归 BY LAOMENG 网络工作室。字标字体为 Noto Sans SC（SIL OFL 1.1）。
