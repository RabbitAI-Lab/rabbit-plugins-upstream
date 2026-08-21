# @fslong/dsh-yishi

忆时记忆系统之 DSH 插件（**自包含**）。全部功能迁入插件：apply 时把忆时资源同步至忆时根目录 `~/.local/share/忆时/`，注入忆时指令、注册 `memocap` 技能——opencode 忆时技能作废后，插件为唯一提供者。

## 职责

1. **同步资源**——把插件包内 `docs/`（SKILL.md / yishi-instructions.md / modules / references）与 `scripts/`（memory_core.py / viz/）复制到忆时根目录，幂等覆盖，插件版本为权威。
2. **注入忆时指令**——经 `systemPrompt.section` 读 `<忆时根>/docs/yishi-instructions.md` 注入每个 agent 系统提示。
3. **注册忆时技能**——经 `ctx.skills.registerProvider` 注册 `memocap`，读 `<忆时根>/docs/SKILL.md`，resourceBase 指向 docs/。

忆时根目录为数据家园：`data/`（Chroma 库）、`models/`（bge 模型）、`scripts/`（功能脚本）、`docs/`（技能文档）。

## 目录结构

```
~/.local/share/忆时/
├── data/        # Chroma 记忆库（642+ 条，双栖共用）
├── models/      # bge-base-zh-v1.5 embedding 模型
├── scripts/     # memory_core.py + viz/（记忆之书、画像）
├── docs/        # SKILL.md + yishi-instructions.md + modules/ + references/
└── memories_backup.jsonl
```

## 安装

```bash
# 1. 构建
cd /home/fslong/Documents/yishi && pnpm i && pnpm build

# 2. 装进 profile（以 web 为例）
cd ~/.dsh/profiles/web
pnpm add file:/home/fslong/Documents/yishi
```

再于 `~/.dsh/profiles/web/package.json` 之 `dsh.profile.bundles` 追加 `@fslong/dsh-yishi`，重启 DSH 生效。

## 环境变量

| 变量 | 默认 | 说明 |
|------|------|------|
| `YISHI_DATA_DIR` | `~/.local/share/忆时` | 忆时根目录（数据+脚本+文档） |
| `DSH_YISHI_DISABLE` | 未设 | `1` 禁用插件 |

## 模型安装

忆时依赖 **bge-base-zh-v1.5**（中文语义 embedding，~400MB，768 维）。**插件包不含模型**——安装后首次运行，插件检测到模型缺失会自动在后台下载（`hf-mirror`）。亦可手动安装：

```bash
# 手动下载（幂等：模型已在则跳过）
cd <插件目录> && pnpm models:install
# 或直接运行
python3 ~/.local/share/忆时/scripts/models-install.py
```

模型落于 `~/.local/share/忆时/models/bge-base-zh-v1.5/`。缺失时记忆的 embedding 检索不可用（memory_core.py 会报错提示），请等待下载完成或手动安装。

> 首次下载约 400MB，受网络影响可能较慢；若自动下载不成功，手动运行上方命令重试（脚本带锁防并发、原子写入防残缺）。

## 命令速查

所有忆时命令均须设 `MEMO_DIR`：

```bash
LOCAL_BASE=~/.local/share/忆时
YISHI=$LOCAL_BASE/scripts/memory_core.py
VIZ=$LOCAL_BASE/scripts/viz/viz.py
MEMO_DIR=$LOCAL_BASE/data
python3 $YISHI recall "关键词" --limit 5          # 检索
python3 $YISHI store --type decision --keywords "k" --emotion 0.5 "内容"  # 存储
python3 $VIZ --no-open                           # 记忆之书（可视化）
python3 $LOCAL_BASE/scripts/viz/profile.py --content 正文.md --out 画像.html  # 画像
```

## 开发

```bash
pnpm build   # src/index.ts → lib/index.js
node real-test.mjs   # 真实 cordis 环境全链验证（同步+注入+技能+脚本）
```

## 许可

MIT