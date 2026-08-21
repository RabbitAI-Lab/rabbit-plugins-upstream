# 打包 / cordis.yml / 部署 / 诊断

## 包结构（DSH checkout 内的插件包）

```
packages/<domain>/<name>/
├── package.json      # name: @deepseek-ai/dsh-<name>；依赖 @deepseek-ai/cordis
├── src/index.ts      # name / apply / Config / inject 导出
└── tests/*.spec.ts   # vitest 测试
```

- DSH 用 pnpm workspace：`vendor/cordis` 的包名是 `@deepseek-ai/cordis`（v4），`@deepseek-ai/schemastery` 也是 vendor 包。
- 真实样板：`vendor/timer/src/index.ts`（最小 Service 插件）、`vendor/group`、`packages/examples/agent-spine-demo/src/index.ts`（应用级组合）。
- 想要 Config schema 被 Loader 正确读取：**只导出命名导出**（`export function apply` / `export const Config`），不要默认导出插件——Loader 默认解包会丢弃 `Config` schema（见 docs/postmortem/0001-acp-default-export-drops-inject.zh.md）。

## cordis.yml：应用的插件树

```yaml
- id: greeter            # 稳定标识：HMR 对比的依据，必给
  name: './greeter.ts'   # 相对路径或 npm 包名
  config:                # 经插件 Config schema 校验
    greeting: 'Hi'
  disabled: true         # 保留条目但跳过挂载（改回即可重载）
```

条目元数据：`id` / `name` / `config` / `disabled` / `inject`（覆盖插件级 inject）。

### `!!js` 表达式（loader 扩展）

```yaml
- name: './config-demo.ts'
  config:
    greeting: !!js process.env.DEMO_GREETING ?? 'Hello'
```

- `!!js` 仅在 `config` 与条目 `disabled` 字段内有效；`disabled: !!js ...` 每次挂载决策时基于 loader 上下文求值，可做平台/环境门控。
- 其余元数据（`name`/`id`/`inject`）保持静态，其中表达式是普通真值。

### 组合原语

- **group**（`@deepseek-ai/cordis-plugin-group`）：嵌套一份条目子列表，作为单元加载/卸载。
- **isolate**：为组提供某项服务的独立实例——两个组各自看到配置不同的提供方，互不影响。
- **include**（`@deepseek-ai/cordis-plugin-include`）：YAML/JSON 配置文件 include，`!!js` 解析表达式节点。
- DSH 的部署用 overlay 修补 base 配置（见 `packages/bundle/base/cordis.patch.yml`）。

## 运行与部署路径

### 1. 教程/独立启动器（无 harness）

```sh
node --import tsx ../../vendor/cordis/bin.js   # 从 cwd 读 cordis.yml
```

### 2. DSH 应用（cordis.yml 由 loader 加载）

插件进入 `cordis.yml`（apps/cli、bundle 或用户配置），经 `@deepseek-ai/cordis-plugin-loader` 挂载。HMR 三件套：`cordis-plugin-logger-console` + `cordis-plugin-timer` + `cordis-plugin-hmr`。

### 3. 动态挂载（模型自写插件）

- `@deepseek-ai/dsh-tool-cordis`：自指工具集——检查运行时、**挂载/卸载模型写的插件**。
- `@deepseek-ai/dsh-cordis-host-runner` / `dsh-cordis-client-runner`：host 与浏览器两侧的插件运行时。
- `ui-cordis`（`@deepseek-ai/dsh-client-ui-cordis`）：GUI 里的动态插件定义卡片（cordis_define 工具行 + run/stop 开关）。

### 4. 打包成 bundle（profile 部署）

DSH 的正式部署单元是 **bundle + profile**（已验证于 `apps/cli/reference/README.md`、`docs/architecture.md`、`docs/user/develop/basic/publish.md`）：

- **bundle** = 一个 npm 包，其 `package.json` 声明：
  ```json
  { "dsh": { "bundle": { "patch": "./cordis.patch.yml" } } }
  ```
  实质是**一层 patch**（插入/覆盖插件行），可附带运行时胶水插件。内置 bundle：`@deepseek-ai/dsh-base`、`@deepseek-ai/dsh-web-app`、`@deepseek-ai/dsh-headless`。
- **profile** = `$DSH_HOME/profiles/<name>` 目录，含 `package.json`（树外插件依赖 + `dsh.profile` manifest 的有序 `bundles` 列表）+ 用户自己的 `cordis.patch.yml`。`web`/`headless` 是自带模板。
- **patch 层语法**：`cordis.patch.yml` 用 `- insert:` 插入新行（与普通 cordis.yml 的 `- id/name/config` 条目不同！）；patch **整行替换**目标行的 `config`（不深度合并键）。
- **叠加顺序**（后层优先）：各 bundle patch（按 `dsh.profile.bundles` 顺序）→ profile 的 `cordis.patch.yml` → `$DSH_HOME/cordis.patch.yml` → 各 `--patch <path>` overlay（argv 顺序）。
- **安装树外插件**：`dsh plugin --profile <name> add <package-or-git-spec>`（转发 pnpm）；成功后若该包声明 `dsh.bundle` 则自动加入 `dsh.profile.bundles`。从插件 checkout 里 `add .` 会安装当前 checkout。
- 启动：`dsh --profile <name>`；`dsh web` 是 `--profile web` 的别名。

## npm pack 本地打包（方式 B：tarball，实测 2026-08）

不依赖 registry 发布权限的正式打包路径：产出标准 `.tgz`，可被 `dsh plugin add` / `npm install` 消费，且能立即本地验证。

### 打包前 package.json 硬要求（逐项核对）

| 字段 | 要求 |
|---|---|
| `main` / `exports["."]` | 指向 ESM 入口（`types` + `default` 双出口） |
| `type` | `"module"` |
| `files` | **必须包含** `lib` + 运行时资产目录（如 `python`）；`README.md` 可选 |
| `dependencies` | **禁写 `workspace:^`**（pnpm 内部协议，npm publish 拒绝/无法解析）——发布前替换为真实 semver |
| **peerDependencies** | **cordis / dsh-tools 等宿主已有服务放这里**（对齐 DSH 生态惯例，见下） |

### peerDependencies 惯例（对照 `@deepseek-ai/dsh-tool-cordis`）

- 插件运行在 DSH 进程内，`@deepseek-ai/cordis`、`@deepseek-ai/dsh-tools` 等**宿主已挂载**的服务必须声明为 **peerDependencies**——否则 pnpm/npm 装独立副本，Service 基类分裂 → `ctx.memory` 等注册到另一套 Context 原型，行为诡异。
- 真·独立依赖（如 schemastery 用于 Config schema，宿主也可能有）视情况 peer 或 dependency；**以宿主是否已提供为准**。
- 发布版本声明：`@deepseek-ai/cordis: ^4.0.1` 等（registry 可解析的版本）。

### registry 版本对齐检查（易踩）

- 本地构建用的版本（如 `@deepseek-ai/dsh-tools@0.1.0-rc.5`）**可能不在 registry**——先 `npm view <pkg> versions --json` 查。
- 声明 `^0.1.0-rc.5` 会解析到 registry 最高的 `0.1.0-rc.6`（本地无 rc.5 时）；rc 版本号语义与 API 稳定性不保证一致，**打包后用真实 registry 版本重跑验证**。

### 打包 + 验证链路（实测 PASS）

```
改 package.json ──► npm pack ──► <pkg>.tgz
   │  workspace:^→真实版本     │
   │  宿主服务→peerDependencies│
   │  registry 版本对齐        │
   ▼                          ▼
   ┌─────────────────────────────────────────────┐
   │ 解包验证：tar -xzf → junction 宿主 node_modules│
   │ → 用 verify-loader.ts 加载 tarball 内 lib     │
   │ → 工具注册 / Service 就绪 / 桥接拉起           │
   └─────────────────────────────────────────────┘
```

```sh
npm pack                       # → kiwifruit-dsh-memory-0.1.3.tgz
# 解包验证（tarball 内无 node_modules 是预期的——peer 由宿主提供）
tar -xzf <pkg>.tgz -C $env:TEMP/verify
# junction 宿主依赖树，模拟真实安装后的解析
New-Item -ItemType Junction "$env:TEMP/verify/package/node_modules" -Target "<插件目录>/node_modules"
# 用 verify-loader.ts 语义加载 tarball 内的 lib/index.js（createRequire 从 harness apps/cli 解析）
```

验证通过 = tarball 产物 + 宿主依赖树可完整装配（工具注册、Service 就绪、桥接进程拉起）。

## 插件发布：npm 包（可被 `dsh plugin add` 安装）

要让插件能被 `dsh plugin add` 安装，需发布为遵循 DSH 约定的 npm 包。

### 核心要求：`package.json` 中声明 `dsh.bundle`

```json
{
  "name": "dsh-hello-plugin",
  "version": "0.1.0",
  "type": "module",
  "main": "index.js",
  "files": ["index.js", "cordis.patch.yml"],
  "dsh": {
    "bundle": {
      "patch": "./cordis.patch.yml"
    }
  }
}
```

- `dsh.bundle.patch`：告诉 DSH 安装后应用哪个 patch 文件来挂载插件
- `files`：确保构建产物和 patch 文件被包含进 npm 包

### 发布版 cordis.patch.yml

```yaml
- insert:
  - id: hello
    name: dsh-hello-plugin
```

与本地开发用的 `cordis.yml` 类似，但 `name` 用 npm 包名而非 `file://` URL。

### 发布到 npm

```bash
npm login
npm publish --access public  # scoped 包需要 --access public
```

### 发布者验证

发布后，在另一个 profile 中测试安装确认：

```bash
dsh plugin --profile test add dsh-hello-plugin
dsh plugin --profile test list
```

## 用户安装插件的方式

### 方式一：通过插件市场（GUI）

1. 先安装市场插件：`dsh plugin --profile web add dshmarket`（或 `@ace-zone/dsh-market`）
2. 重启 DSH Web
3. 进入 `设置 → 插件 → 插件市场`，浏览并一键安装

### 方式二：通过命令行（CLI）

```bash
dsh plugin --profile <配置名> add <插件标识>
```

| 来源类型 | 命令格式 | 示例 |
|---------|---------|------|
| npm 包（推荐） | `dsh plugin add <包名>` | `dsh plugin --profile web add @kiwifruit/dsh-context-pro` |
| GitHub 仓库 | `dsh plugin add github:所有者/仓库` | `dsh plugin --profile web add github:owner/repo` |
| 本地目录 | `dsh plugin add <绝对路径>` | `dsh plugin --profile web add /path/to/my-plugin` |

### 升级插件

与安装命令相同，**再次执行 `dsh plugin add` 即升级**。

### 安全提醒

安装社区插件等同于运行第三方代码，具有与你本人相同的权限。建议：
- 安装前查看插件源码
- 不熟悉的插件在隔离环境中测试
- 选择知名或源码公开的插件
- 安装时指定具体版本号而非 `@latest`

## 多语言内核集成（JS/TS 外壳 + 任意语言内核）

```
DSH 插件(TS/JS) ── child_process ──→ Python/Rust/二进制内核
     │                                   │
     │ ctx.effect(disposer)              │ 常驻：stdin/stdout JSON 行协议
     │ 启动/停止生命周期                   │ 一次性：stdout 收集 + 退出码
     └── 路径绝对化 / 错误包装 / 配置映射  ←─┘
```

1. **路径绝对化**：`./script.py` 相对路径是相对 **Node CWD**，不是插件源码目录。用 `path.join(__dirname, './script.py')` 转绝对路径。
2. **子进程错误包装**：Python 报错不会自动转成 Node 异常。用 try-catch 包裹调用，把子进程 `stderr` 经 `ctx.logger` 格式化（最好转成 Cordis `Error`），否则底层崩溃会静默拖垮 Harness。
3. **常驻进程释放**：若底层启动常驻进程（WebSocket 服务等），释放逻辑必须放 `ctx.effect()`，否则 HMR 重载产生"僵尸进程"。
4. **运行环境在场证明**：Cordis 只管调用不管安装——目标机必须预装解释器/动态库（`.dll`/`.so`），否则 `ENOENT`。
5. **配置预留**：底层硬编码的路径/超时先用常量占位，封装时全部映射到 `Config` schema；接口草图（入参/出参/异常码）先行，避免底层写完参数传不进。

### 常驻内核通信协议（dsh-memory 实测）

- **stdio JSON-RPC**：请求 `{"id","method","params"}` → 响应 `{"id","result"|"error"}`，**每行一个 JSON**，UTF-8。
- **Windows 编码坑**：Python 默认 locale 是 GBK——必须 `sys.stdout/err.reconfigure(encoding='utf-8')` 强制 UTF-8，否则中文乱码/崩溃。
- **会话隔离**：`init(user_id, session_id)` 按会话缓存内核 orchestrator；跨会话不共享状态。
- **胶水转换**：TS camelCase ↔ Python snake_case 必须显式转换（见 [traps.md](../06-experience/traps.md) #23）；不透传裸 RPC 结果。
- **崩溃自动重启**：`waitReady` 探测 + 指数退避重启（`RESTART_BASE * 2^n`）；重启后重发未完成请求。
- **优雅关闭**：stop 时先 `end_session` 再 kill；验证脚本需显式 `process.exit(0)` 释放句柄（见 [traps.md](../06-experience/traps.md) #19）。

### 桥接层职责边界（红线）

- 胶水只做：类型转换、参数适配、协议转换、调用转发——**不承载业务逻辑**（见 CLAUDE.md 胶水规范）。
- 下游异常统一翻译为业务错误码；跨系统调用设超时 + 重试（注意幂等性）。
- 可观测：胶水日志含 caller/callee/req/res/cost_ms，链路可追踪。

## dsh plugin add 安装踩坑（实测）

> 来源：DSH-Context-Pro 项目实测

### 坑 1：`dsh` 命令不存在于 PATH

**现象**：`dsh: The term 'dsh' is not recognized`

**根因**：`dsh` CLI 是 `@deepseek-ai/dsh` 包，安装在 harness 的 `node_modules/.pnpm/node_modules/@deepseek-ai/dsh/lib/bin.js`，没有注册到系统 PATH。

**规避**：直接通过 node 调用：
```
node "D:\Git\github\deepseek-harness-master\node_modules\.pnpm\node_modules\@deepseek-ai\dsh\lib\bin.js" <command>
```

### 坑 2：`--profile <name>` 是必选参数

**现象**：`error: required option '--profile <name>' not specified`

**规避**：显式指定 `--profile web`（web profile 在 `~/.dsh/profiles/web`）。

### 坑 3：版本解析到坏版本，依赖冲突

**现象**：`[ERR_PNPM_NO_MATCHING_VERSION] No matching version found for @deepseek-ai/schemastery@^4.0.0`

**根因**：`dsh plugin add` 默认解析到**最新发布版**（npm `latest` tag），但最新版的依赖可能已损坏（如声明了不存在的版本范围）。

**规避**：显式指定版本号 `@0.2.0`；发布前在 `dependencies` 中确认版本范围在 registry 上可解析。

### 完整安装命令

```bash
node "D:\Git\github\deepseek-harness-master\node_modules\.pnpm\node_modules\@deepseek-ai\dsh\lib\bin.js" plugin add @kiwifruit/dsh-context-pro@0.2.0 --profile web
```

### 安装后验证

```bash
# 检查 profile 的 node_modules 中是否有该包
ls "C:\Users\<user>\.dsh\profiles\web\node_modules\@kiwifruit\dsh-context-pro"

# 检查 composition 是否包含插件条目
cat "C:\Users\<user>\.dsh\profiles\web\cordis.yml" | grep context-pro
```

## 诊断：插件加载失败/不工作

```ts
import { FiberState, type Context } from '@deepseek-ai/cordis'

export function apply(ctx: Context) {
  setTimeout(() => {
    for (const runtime of ctx.registry.values()) {
      for (const fiber of runtime.fibers) {
        if (fiber.state === FiberState.PENDING) {
          console.log(`${fiber.name} is PENDING — a required service is missing`)
        }
      }
    }
  }, 500)
}
```

排查顺序：
1. **不输出且进程静默退出** → 检查 fiber 状态：多半是 `inject` 的服务无人提供（PENDING 合法，不崩溃不报错）。
2. **配置错误** → `ValidationError: invalid config:` 指明字段与期望类型。
3. **HMR 不生效** → 确认 logger-console 与 timer 插件已挂载；条目带 `id`。
4. **插件似乎没运行** → 先查 `cordis.yml` 拼写（解析失败只走 logger，启动早期可能丢失）。
5. **FAILED 但原因不明** → `apply` 抛错会终止进程，检查 `apply` 内同步抛出的异常。
