# laomeng-zhc-agent

老孟中文编程（ZHC）**智能体身份** Agent Skill。给自动化运行环境用的 ZHC 接入包：
语言服务、编译调度、桥后端与合规红线。

## 这是什么

ZHC 生态有两套对外身份，共用同一份语言内核：

| 包 | 身份 | 面向 |
|---|---|---|
| `laomeng-zhc` | 语言身份 | 想写中文代码的人与模型 |
| `laomeng-zhc-agent` | 智能体身份 | 想把 ZHC 接进自动化流程的智能体与编辑器 |

本包是后者：它假定你要**驱动** ZHC，而不是**阅读** ZHC。

## 结构

```
laomeng-zhc-agent/
├── SKILL.md                       入口，含身份边界与红线
├── README.md                      本文件
├── LICENSE.txt
├── assets/                        标志（带朱点，智能体版）
├── references/
│   ├── 快速参考.md                 关键字 44 / 类型 11 / 内置 39 / 错误码 38
│   ├── 契约_1.0.md                 语言面契约
│   ├── 错误码表_E_1.0.md           E001~E2xx 全码位
│   ├── LSP协议.md                  语言服务方法与排障
│   ├── 桥报文协议.md               桥的请求/响应/降级规则
│   └── 智能体工作流.md             从探测到出产物的完整序列
└── scripts/
    ├── zhc.py                      语言内核
    ├── zhc_lsp.py                  语言服务（LSP over stdio）
    ├── 桥/zhc_bridge.py             Office / 网页产物后端
    └── 示例/                       三个可跑通的最小样例
```

## 三分钟验证

要求 Python 3.8+，无需第三方依赖。

```bash
python -X utf8 scripts/zhc.py --api
python -X utf8 scripts/zhc.py scripts/示例/基础.zc --诊断
python -X utf8 scripts/zhc.py scripts/示例/基础.zc --run
```

第三条应打印 `1 到 100 之和是 5050`。

起语言服务：

```bash
python -X utf8 scripts/zhc_lsp.py --stdio
```

## 硬约束（踩过的坑）

- 函数参数必须 `名:类型`，否则 `E014`。
- 语言没有 `break` / `continue`，`结束循环` 会 `E202`。
- `zhc.py` 与 `zhc_lsp.py` 必须同级，否则 LSP 起不来。
- 桥必须在 `桥/` 子目录，路径编译期烧入；换机器需重编译或设 `ZHC_BRIDGE_HOME`。
- 一切命令加 `-X utf8`，否则中文乱码。

## 版本

- Skill 版本 1.0.0
- 语言面契约 ZHC-LANG-1.0，智能体契约 ZHC-AGENT-1.0，协议面 ZHC-LSP-1.0
- Office 契约 OFFICE-WEB 2.4
- 冻结日 2026-11-09

## 许可

内核与标志体系归 BY LAOMENG 网络工作室，详见 `LICENSE.txt`。
字标字体 Noto Sans SC（SIL OFL 1.1）。
