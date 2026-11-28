---

name: github-release-changelog-action-use

slug: github-release-changelog-action-use

displayName: GitHub Release 生成正文 Action 使用

version: '1.0.2'

summary: 在 GitHub Actions 中生成 Markdown 更新内容和 GitHub Release 正文。

license: MIT

description: "帮助用户配置 dtapps/release-changelog-action，选择 changelog 或 release 模式，生成更新内容与 Release 正文，配置产物目录、下载链接、步骤输出以及 Git 拉取和排障选项。"

---

# 使用 GitHub Release 更新内容生成 Action

## 适用范围

在已有 GitHub 项目中使用 Action：

`dtapps/release-changelog-action@main`

- `mode: changelog`：根据 Git Tag 和提交记录生成 Markdown 更新内容。
- `mode: release`：生成包含版本、提交、构建时间、下载附件和校验说明的 Release 正文。

Action 只生成正文文件，不创建、删除或移动 Release / Git Tag。生产环境建议将 `@main` 替换为已验证的版本 Tag 或 commit SHA。

## 配置前确认

- 确认版本号来源和目标发布渠道。
- 生成更新内容前，确认仓库 Tag 和提交历史完整。
- 生成 Release 正文前，确认发布产物已放入产物目录。
- 多组件项目使用 `artifact_layout: triplet`。
- 需要离线或使用本地 Tag 时，设置 `fetch_tags: false`。
- 声明 `permissions: contents: read`，不要授予不必要的写权限。

## 权限与检出

```yaml
permissions:
  contents: read

steps:
  - uses: actions/checkout@v4
    with:
      fetch-depth: 0
```

`fetch_tags: true` 会使用检出仓库的 Git 凭据拉取远端 Tag。浅克隆时，`fetch_history: true` 会尽力补全历史。两项操作失败都只告警，继续使用本地数据。

## 参数

GitHub Actions 会将 `with` 参数注入为 `INPUT_*` 环境变量。布尔值使用 `true` / `false`。

| 参数              | 类型    | 默认值                                   | 说明                                             |
|-------------------|---------|------------------------------------------|--------------------------------------------------|
| `mode`            | string  | 无，必填                                 | `changelog` / `release`                          |
| `version`         | string  | 无，必填                                 | 具体版本号，例如 `v1.2.3` 或 `1.2.3-rc.1`        |
| `workspace`       | string  | `GITHUB_WORKSPACE`                       | Git 仓库目录                                     |
| `out_file`        | string  | `release_body.md`                        | 正文输出文件，相对路径基于 `workspace`           |
| `repo_url`        | string  | `GITHUB_SERVER_URL/GITHUB_REPOSITORY`    | 仓库页面地址                                     |
| `download_base`   | string  | `{repo_url}/releases/download/{version}` | 附件下载地址前缀                                 |
| `stable_url`      | string  | `{repo_url}/releases`                    | 最新正式版页面地址                               |
| `commit_url`      | string  | `{repo_url}/commit`                      | 提交详情页地址前缀                               |
| `commit`          | string  | `GITHUB_SHA`                             | 40 位小写十六进制提交 SHA                        |
| `build_time`      | string  | 当前本地时区；无法获取时 UTC             | 构建时间，默认格式为 `YYYY-MM-DD HH:mm:ss`       |
| `artifact_dir`    | string  | `dist`                                   | 发布产物目录                                     |
| `artifact_layout` | string  | `single`                                 | `single` / `triplet`                             |
| `changelog_limit` | integer | `50`                                     | 每个分组最多展示的提交数，`0` 表示不展示具体条目 |
| `fetch_tags`      | boolean | `true`                                   | 是否尽力拉取远端 Tag                             |
| `fetch_history`   | boolean | `true`                                   | 浅克隆时是否尽力补全历史                         |

`repo_url` 默认从 GitHub 环境变量生成，兼容 GitHub.com 和 GitHub Enterprise。离线渲染 Release 正文时，可不设置 `repo_url`，但必须同时提供 `download_base` 和 `commit_url`。

## 输出

通过 `${{ steps.<step-id>.outputs.<output-name> }}` 读取。

| 输出             | 模式      | 说明                                      |
|------------------|-----------|-------------------------------------------|
| `body_file`      | 全部      | 生成的 Markdown 文件路径                  |
| `previous_tag`   | 全部      | 上一个基准 Tag；首次发布时为空            |
| `commit_count`   | 全部      | 基准 Tag 到当前提交之间的提交数           |
| `artifact_count` | 全部      | 识别的产物数量；`changelog` 模式为 `0`    |
| `build_time`     | `release` | 构建时间                                  |
| `build_date`     | `release` | 运行时区下的构建日期，格式为 `YYYY-MM-DD` |

## 配置示例

### 生成更新内容

```yaml
- name: 生成更新内容
  id: changelog
  uses: dtapps/release-changelog-action@main
  with:
    mode: changelog
    version: ${{ github.ref_name }}
    fetch_tags: false

- name: 读取更新内容
  env:
    BODY_FILE: ${{ steps.changelog.outputs.body_file }}
    PREVIOUS_TAG: ${{ steps.changelog.outputs.previous_tag }}
    COMMIT_COUNT: ${{ steps.changelog.outputs.commit_count }}
  run: |
    printf 'previous_tag=%s\n' "$PREVIOUS_TAG"
    printf 'commit_count=%s\n' "$COMMIT_COUNT"
    cat "$BODY_FILE"
```

### 生成 Release 正文

```yaml
- name: 生成 Release 正文
  id: release
  uses: dtapps/release-changelog-action@main
  with:
    mode: release
    version: ${{ github.ref_name }}
    artifact_dir: dist
    artifact_layout: single
    changelog_limit: 50
    fetch_tags: false

- name: 上传正文附件
  uses: actions/upload-artifact@v4
  with:
    name: release-body
    path: ${{ steps.release.outputs.body_file }}
```

### 多组件产物

```yaml
- name: 生成多组件 Release 正文
  uses: dtapps/release-changelog-action@main
  with:
    mode: release
    version: v1.2.3
    artifact_dir: dist
    artifact_layout: triplet
```

文件名第一段作为组件名，例如 `backend-linux-amd64.tar.gz`、`frontend-windows-amd64.exe.zip`。

## 版本与产物规则

- 版本号可省略 `v` 前缀，输出统一使用小写 `v`。
- 支持正式版和 `rc`、`beta`、`alpha`、`nightly` 预发布版本。
- `version` 必须是具体版本号，不会自动推导 nightly 日期。
- 更新内容优先使用同渠道的上一个 Tag，预发布版本可回退到正式版 Tag。
- `release` 模式支持 `.pkg.tar.zst`、`.exe.zip`、`.tar.gz`、`.AppImage`、`.deb`、`.rpm`、`.apk`、`.ipk`、`.fpk`、`.zip`、`.exe`。
- 产物目录存在 `SHA256SUMS` 时，正文会追加校验命令。
- 没有可识别产物时，`release` 模式失败；`changelog` 模式不需要产物目录。

## 排障

### 提示版本号非法

检查 `version` 是否为 `vX.Y.Z` 或受支持的预发布版本。不要传入裸 `nightly`，应传入类似 `v1.2.3-nightly.20261128` 的具体版本。

### 提示找不到更早基准

仓库存在其他版本 Tag，但没有可用于比较的更早 Tag。检查 Tag 是否完整，确认当前版本是否应当发布。

### 提示没有可发布产物

检查 `artifact_dir` 路径和文件扩展名。相对路径基于 `workspace`，默认读取 `dist`。

### 更新内容不完整

使用 `actions/checkout@v4` 并设置 `fetch-depth: 0`。确认 `fetch_tags` 和 `fetch_history` 未被禁用，并检查 Git 凭据和远端访问。

### 无法写入步骤输出

确认运行环境提供 `GITHUB_OUTPUT`。本地运行时需要显式设置该变量为输出文件路径。

### 403 Forbidden

检查 Workflow 或 Job 的 `permissions: contents: read`，并确认 Token 可以访问目标仓库。私有仓库拉取 Tag 还需要有效的检出凭据。
