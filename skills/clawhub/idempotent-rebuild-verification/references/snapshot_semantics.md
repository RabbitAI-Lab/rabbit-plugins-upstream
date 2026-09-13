# 快照擦除语义（供参考 · 定性）

> 依据：本 agent 沙箱工作区文档化的快照排除清单（2026-09-06，workspace spec）：
> 快照不持久化的目录名：`.arena .cache .local .mypy_cache .next .nox .npm .nuxt .output
> .parcel-cache .pytest_cache .ruff_cache .svelte-kit .tox .turbo .venv .vite __pycache__
> build coverage dist node_modules out target`（最佳努力上限 ~128MB / 10000 文件）。
> 普通文件（如 `~/*.sh`、配置、脚本）在轮间/会话间存活。不同环境清单可能不同 ——
> 按所在环境文档校准：环境变量 `RV_SNAPSHOT_EXCLUDED`（空白/逗号/分号/冒号分隔）
> 覆盖内置 `SNAPSHOT_EXCLUDED` 常量（rebuild_verify.py 顶部）。

## 擦除后正常态判定（wipe-audit 逻辑）

扫描根目录（上限 5000 条目）五类：

| 类 | 判据 |
|---|---|
| 排除目录产物 | `SNAPSHOT_EXCLUDED` 中目录存在（build/、node_modules/…） |
| 脚本 | 深度 ≤1 的 `*.sh`/`*.py`/`Makefile` |
| 二进制 | `*/bin/*` 文件（深度 ≤2） |
| 模型 | `*.gguf`/`*.safetensors`/含 model 的 `*.bin`（深度 ≤2） |
| shim | `~/.shim`、`node_modules/.bin` |

判定（固定路由表内嵌于代码）：

| 脚本 | 产物 | verdict | next_action |
|---|---|---|---|
| 无 | 无 | clean | 空工作区/未开始 |
| 有 | 无 | normal_post_wipe | 仅重跑产物步骤：bin 缺→compile；模型缺→model_download；shim 缺→shim |
| 有 | 有 | pre_wipe_or_full | 无需动作 |
| 无 | 有 | scripts_missing_too（exit 3） | 异常：先恢复脚本（git/备份），再谈重跑 |

## 症状 → 步骤路由（v1 表，代码化为 STEP_ROUTER）

```
cmake/g++ 缺失 ............... toolchain 安装步骤
~/.shim 消失 / npx 挂死 ....... shim 步骤（stdin 关闭的沙箱需要 npx --yes）
build/bin/* 缺失 .............. compile 步骤（build/ 快照排除，擦除后正常缺失）
*.gguf 缺失 ................... model 下载步骤
脚本哈希不符 .................. 先跑 verify 分类（良性→重跑 writer，勿盲目重贴）
skill 数量减少 ................ mass-install 步骤（幂等，可安全重跑）
```

## 实践要点

- 擦除后"脚本在、产物不在"是**正常态**：只有产物步骤需要重跑，不要全量重放 runbook。
- 二进制下载断言字节数（v1 Rule 6）：`verify FILE --want <sha> --want-size <n>` 一条命令
  同时钉内容+尺寸，HTML 错误页会被 `html_error_page` 类抓出。
- 并行只在独立步骤间做（clone ∥ 装工具链；compile ∥ 下载模型）；声明的依赖顺序不动。
