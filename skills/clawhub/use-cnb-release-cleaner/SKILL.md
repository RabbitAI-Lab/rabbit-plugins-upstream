---

name: use-cnb-release-cleaner

slug: use-cnb-release-cleaner

displayName: CNB Release / Tag 清理插件使用

version: "1.1.3"

summary: "在 CNB 流水线中配置、预演和清理 Release，并可独立清理 Git Tag。"

license: MIT

description: "帮助用户在 CNB 项目的 .cnb.yml 中配置流水线阶段，预演和清理 Release，并可独立清理 Git Tag。适用于流水线参数选择、阶段配置、预演核对、真实删除确认及权限和删除失败排障。"

---

# 使用 CNB Release Cleaner

## 适用范围

帮助终端用户在已有 CNB 项目中直接使用官方插件：

`docker.cnb.cool/dtapp/plugins/release-cleaner:latest`

只处理插件配置和使用，不涉及源码构建或插件开发。

## 配置前确认

- 确认目标 CNB 仓库和要清理的 Release 范围。
- 确认使用 `by_count`、`by_days` 还是 `regex`。
- 确认 `protect` 能覆盖正式版、`latest`、`stable` 等必须保留的版本。
- 默认只清理 Release；只有用户明确要求时才设置 `delete_git_tag: true`。
- 首次运行和每次修改规则后，都先设置 `dry_run: true`。

## 权限

- CNB 仓库角色需要管理员及以上。
- Token 需要 `repo-contents:rw` 和 `repo-code:rw` 权限。
- 使用 CNB 平台自动注入的 `CNB_TOKEN`，不要写进 YAML 或日志。

## 参数

| 参数             | 默认值            | 说明                                              |
|------------------|-------------------|---------------------------------------------------|
| `mode`           | `by_count`        | 清理模式：`by_count` / `by_days` / `regex`        |
| `keep`           | `5`               | `by_count` 下保留最近多少个未受保护版本，非负整数 |
| `days`           | `30`              | `by_days` 下保留多少天内的版本，非负整数          |
| `regex`          | 空                | `regex` 模式下必填，匹配要删除的版本名            |
| `protect`        | `^(v\d+\.\d+\.\d+ | latest                                            |
| `delete_git_tag` | `false`           | 是否同时独立清理 Git Tag                          |
| `dry_run`        | `true`            | 是否只输出计划、不执行删除                        |

## 清理规则

- `by_count`：保留最近 N 个未受保护版本，删除更早版本；受保护版本不占用保留名额。
- `by_days`：保留 N 天内的未受保护版本，删除更早版本。
- `regex`：删除名称匹配 `regex` 且未命中 `protect` 的版本，不依赖版本时间。
- `protect` 始终优先，匹配的 Release 和 Tag 都不会删除。
- Release 与 Git Tag 分别筛选、分别删除，不要求名称或数量一一对应。
- 开启 Tag 清理后，没有对应 Release 的 Tag 也会参与判断。

## 配置示例

将阶段合并到项目 `.cnb.yml` 现有事件的 `stages` 中，不要覆盖其他阶段。

### 保留 90 天内 Release

```yaml
- name: 预演 Release 清理
  image: docker.cnb.cool/dtapp/plugins/release-cleaner:latest
  settings:
    mode: by_days
    days: 90
    delete_git_tag: false
    dry_run: true
```

### 保留最近 5 个未受保护 Release

```yaml
- name: 预演 Release 数量清理
  image: docker.cnb.cool/dtapp/plugins/release-cleaner:latest
  settings:
    mode: by_count
    keep: 5
    protect: '^(v\d+\.\d+\.\d+|latest|stable|release-.*)$'
    delete_git_tag: false
    dry_run: true
```

### 清理测试版本

```yaml
- name: 预演测试 Release 清理
  image: docker.cnb.cool/dtapp/plugins/release-cleaner:latest
  settings:
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
  image: docker.cnb.cool/dtapp/plugins/release-cleaner:latest
  settings:
    mode: by_days
    days: 30
    protect: '^(v\d+\.\d+\.\d+|latest|stable)$'
    delete_git_tag: true
    dry_run: true
```

## 预演与真实删除

1. 使用 `dry_run: true` 运行流水线。
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

检查仓库角色和 Token 权限，确认 Token 属于目标仓库且具备 `repo-contents:rw`、`repo-code:rw`。

### Git Tag 缺少有效时间

`by_count` 和 `by_days` 需要版本时间。检查同名 Release 创建时间或 Tag 关联提交时间；如果版本命名明确，也可改用精确的 `regex` 模式。

### 部分删除失败

插件会继续处理其余候选，但最终返回失败。根据日志定位失败的 Release 或 Tag，检查权限和资源状态；不要用 `allowFailure: true` 掩盖失败。
