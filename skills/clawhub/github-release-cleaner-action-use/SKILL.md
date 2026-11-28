---

name: github-release-cleaner-action-use

slug: github-release-cleaner-action-use

displayName: GitHub Release / Tag 清理 Action 使用

version: '1.1.3'

summary: 配置、预演和排障 GitHub Release Cleaner Action。

license: MIT

description: "帮助用户在 GitHub Actions 中直接配置 dtapps/release-cleaner-action，按数量、天数或正则预演和清理 Release，并可独立清理 Git Tag。适用于 with 参数选择、工作流配置、预演核对、真实删除确认及权限和删除失败排障。"

---

# GitHub Release Cleaner Action 使用

## 适用范围

帮助终端用户在已有 GitHub 项目中直接使用 Action：

`dtapps/release-cleaner-action@main`

只处理 Action 配置和使用，不涉及源码构建或插件开发。生产环境建议将 `@main` 替换为已验证的版本 Tag 或 commit SHA。

## 配置前确认

- 确认目标仓库和要清理的 Release 范围。
- 确认使用 `by_count`、`by_days` 还是 `regex`。
- 确认 `protect` 能覆盖正式版、`latest`、`stable` 等必须保留的版本。
- 默认只清理 Release；只有用户明确要求时才设置 `delete_git_tag: true`。
- 首次运行和每次修改规则后，都先设置 `dry_run: true`。

## 权限

- 在 Workflow 或 Job 中声明 `contents: write`。
- 默认使用平台注入的 `${{ github.token }}`，不要写进 YAML 或日志。
- 默认 Token 受仓库策略限制时，可通过 Secret 传入具备写权限的 PAT。

```yaml
permissions:
  contents: write
```

## 参数

| 参数             | 默认值                | 说明                                              |
|------------------|-----------------------|---------------------------------------------------|
| `token`          | `${{ github.token }}` | 具有 `contents: write` 权限的 GitHub Token        |
| `mode`           | `by_count`            | 清理模式：`by_count` / `by_days` / `regex`        |
| `keep`           | `5`                   | `by_count` 下保留最近多少个未受保护版本，非负整数 |
| `days`           | `30`                  | `by_days` 下保留多少天内的版本，非负整数          |
| `regex`          | 空                    | `regex` 模式下必填，匹配要删除的版本名            |
| `protect`        | 见下方                | 保护名单正则，匹配的版本不会删除                  |
| `delete_git_tag` | `false`               | 是否同时独立清理 Git Tag                          |
| `dry_run`        | `true`                | 是否只输出计划、不执行删除                        |

默认保护正则：

```yaml
protect: '^(v\d+\.\d+\.\d+|latest|stable)$'
```

布尔值使用 `true` / `false`。正则默认按子串匹配，需要完整匹配时使用 `^` 和 `$`。不要把 `protect` 留空作为关闭保护的方法；空值会使用默认保护正则。

## 清理规则

- `by_count`：保留最近 N 个未受保护版本，删除更早版本；受保护版本不占用保留名额。
- `by_days`：保留 N 天内的未受保护版本，删除更早版本。
- `regex`：删除名称匹配 `regex` 且未命中 `protect` 的版本，不依赖版本时间。
- `protect` 始终优先，匹配的 Release 和 Tag 都不会删除。
- Release 与 Git Tag 分别筛选、分别删除，不要求名称或数量一一对应。
- 开启 Tag 清理后，没有对应 Release 的 Tag 也会参与判断。
- `by_days` 优先使用 `TZ` 指定时区，未设置时使用运行环境本地时区，无法获取时回退 UTC。

## 配置示例

将 Step 合并到项目现有 Job 的 `steps` 中，不要覆盖其他步骤，并确保 Job 已有 `contents: write` 权限。

### 保留 90 天内 Release

```yaml
- name: 预演 Release 清理
  uses: dtapps/release-cleaner-action@main
  with:
    mode: by_days
    days: 90
    delete_git_tag: false
    dry_run: true
```

### 保留最近 5 个未受保护 Release

```yaml
- name: 预演 Release 数量清理
  uses: dtapps/release-cleaner-action@main
  with:
    mode: by_count
    keep: 5
    protect: '^(v\d+\.\d+\.\d+|latest|stable|release-.*)$'
    delete_git_tag: false
    dry_run: true
```

### 清理测试版本

```yaml
- name: 预演测试 Release 清理
  uses: dtapps/release-cleaner-action@main
  with:
    mode: regex
    regex: '^test-'
    protect: '^(v\d+\.\d+\.\d+|latest|stable)$'
    delete_git_tag: false
    dry_run: true
```

### 同时清理 Git Tag

Git Tag 删除不可恢复。仅在用户明确要求时开启，并先预演：

```yaml
- name: 预演 Release 与 Git Tag 清理
  uses: dtapps/release-cleaner-action@main
  with:
    mode: by_days
    days: 30
    protect: '^(v\d+\.\d+\.\d+|latest|stable)$'
    delete_git_tag: true
    dry_run: true
```

## 预演与真实删除

1. 使用 `dry_run: true` 运行工作流。
2. 查看日志中的“共发现”和“计划删除”，核对每个候选 Release 和 Tag。
3. 向用户展示候选清单，确认目标仓库、规则和是否删除 Tag。
4. 用户明确确认后，仅将 `dry_run` 改为 `false`，不要同时修改其他参数。
5. 检查最终“成功 / 失败”计数；有失败时修正问题并重新预演。

## 排障

### 没有删除任何版本

检查：

1. `dry_run` 是否为 `true`。
2. 版本是否全部命中 `protect`。
3. 仓库中是否存在符合规则的版本。
4. 是否想清理 Tag，但 `delete_git_tag` 仍为 `false`。

### 403 Forbidden

检查 Workflow 或 Job 的 `permissions: contents: write`，确认 Token 属于目标仓库且具备写权限；默认 Token 受限时改用 PAT。

### Git Tag 缺少有效时间

`by_count` 和 `by_days` 需要版本时间。检查同名 Release 创建时间或 Tag 关联提交时间；如果版本命名明确，也可改用精确的 `regex` 模式。

### 部分删除失败

Action 会继续处理其余候选，但最终返回失败。根据日志定位失败的 Release 或 Tag，检查权限和资源状态；不要用 `continue-on-error: true` 掩盖失败。
