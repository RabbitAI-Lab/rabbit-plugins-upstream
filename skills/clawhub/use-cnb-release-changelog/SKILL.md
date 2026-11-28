---

name: use-cnb-release-changelog

slug: use-cnb-release-changelog

displayName: CNB Release 生成正文插件使用

version: "1.0.2"

summary: "在 CNB 流水线中生成分组变更日志或完整 Release 正文。"

license: MIT

description: "帮助用户在 CNB 流水线中配置 release-changelog 插件，按版本渠道生成变更日志，并输出包含发布信息、下载表格、校验说明和更新内容的完整 Release 正文。适用于模式选择、制品目录与布局、URL 覆盖、输出映射及 Git 历史排障。"

---

# 使用 CNB Release 正文插件

## 适用范围

在已有 CNB 项目中使用：

`docker.cnb.cool/dtapp/plugins/release-changelog:latest`

- `mode: changelog`：只生成分组提交变更。
- `mode: release`：生成完整 CNB Release 正文，包括发布信息、下载表格、校验说明和变更日志。

插件只生成正文，不创建或删除 Release/Tag，不上传制品，也不调用 CNB OpenAPI。

## 配置前确认

- 确认当前版本、发布渠道和产物目录。
- 只需要提交变更时使用 `changelog`。
- 需要下载表格时使用 `release`，并确保 `artifact_dir` 至少包含一个可识别制品。
- 多组件项目设置 `artifact_layout: triplet`。
- CNB 默认提供 `CNB_REPO_URL_HTTPS`，通常无需手动设置 URL。
- 制品不在 CNB 当前 Release 下时，显式设置 `download_base`。
- 浅克隆需要完整历史时保持 `fetch_history: true`；离线场景关闭 `fetch_tags`。
- 保留调用方原有的版本门禁、提交检出、Release 标题和发布步骤。

## 参数

CNB 会将 `settings` 转换为大写、带 `PLUGIN_` 前缀的环境变量。布尔值常用 `true` / `false`。

| 参数              | 默认值                       | 说明                                                                              |
|-------------------|------------------------------|-----------------------------------------------------------------------------------|
| `mode`            | 无，必填                     | `changelog` / `release`                                                           |
| `version`         | 无，必填                     | `vX.Y.Z` 或 `vX.Y.Z-rc.N`、`-beta.N`、`-alpha.N`、`-nightly.YYYYMMDD`；可省略 `v` |
| `workspace`       | `.`                          | Git 仓库路径；相对产物路径和输出文件相对于该路径                                  |
| `out_file`        | `release_body.md`            | 正文文件路径，可为绝对路径                                                        |
| `repo_url`        | `CNB_REPO_URL_HTTPS`         | CNB 仓库地址，用于生成提交、下载和稳定版链接                                      |
| `download_base`   | 自动生成                     | 制品下载基础地址，默认 `${repo_url}/-/releases/download/${version}`               |
| `stable_url`      | 自动生成                     | 预发布正文的稳定版入口，默认 `${repo_url}/-/releases`                             |
| `commit_url`      | 自动生成                     | 提交链接基础地址，默认 `${repo_url}/-/commit`                                     |
| `commit`          | `""`                         | 正文显示的 40 位小写提交 SHA；未设置时读取 HEAD                                   |
| `build_time`      | 当前本地时间（默认北京时间） | 构建时间，不能包含换行                                                            |
| `artifact_dir`    | `dist`                       | `release` 模式的制品目录，只读取第一层文件                                        |
| `artifact_layout` | `single`                     | `single` 或 `triplet`                                                             |
| `changelog_limit` | `50`                         | 每组最多列出的提交数；`0` 表示不限制                                              |
| `fetch_tags`      | `true`                       | 是否尽力拉取远端 Tag，失败只告警                                                  |
| `fetch_history`   | `true`                       | 是否尽力补全浅克隆历史                                                            |

`release` 模式需要 `repo_url`，或者同时提供 `download_base` 和 `commit_url`。

## 输出

| 输出             | 说明                                                                  |
|------------------|-----------------------------------------------------------------------|
| `body_file`      | 正文文件路径                                                          |
| `previous_tag`   | 基准 Tag；首次发布时为空                                              |
| `commit_count`   | 基准范围内提交总数，未按分组截断                                      |
| `artifact_count` | 识别到的制品数；`changelog` 模式为 `0`                                |
| `build_time`     | 仅 `release`：正文使用的构建时间                                      |
| `build_date`     | 仅 `release`：按 `timeutil.go` 的时区规则生成的构建日期，默认北京时间 |

正文同时写入文件和标准输出，并通过 `##[set-output name=value]` 输出上述值。

## 配置示例

将 stage 合并到项目 `.cnb.yml` 现有事件的 `stages` 中，不要覆盖其他阶段。

### 完整 Release 正文

放在产物构建之后、Release 发布之前：

```yaml
- name: 生成 Release 正文
  image: docker.cnb.cool/dtapp/plugins/release-changelog:latest
  settings:
    mode: release
    version: ${INTERIOR_VERSION}
    artifact_dir: dist
    artifact_layout: single
    out_file: release_body.md
    fetch_tags: true
    fetch_history: true
  exports:
    body_file: RELEASE_BODY_FILE
    previous_tag: PREVIOUS_TAG
    commit_count: RELEASE_COMMIT_COUNT
    artifact_count: RELEASE_ARTIFACT_COUNT
```

后续 `git:release` 的 `descriptionFromFile` 使用 `release_body.md` 或 `${RELEASE_BODY_FILE}`。

### 只生成变更日志

```yaml
- name: 生成变更日志
  image: docker.cnb.cool/dtapp/plugins/release-changelog:latest
  settings:
    mode: changelog
    version: ${INTERIOR_VERSION}
    out_file: LATEST_CHANGELOG.md
    changelog_limit: 50
  exports:
    body_file: CHANGELOG_FILE
    previous_tag: PREVIOUS_TAG
    commit_count: CHANGELOG_COMMIT_COUNT
```

### 多组件产物

```yaml
- name: 生成完整正文
  image: docker.cnb.cool/dtapp/plugins/release-changelog:latest
  settings:
    mode: release
    version: ${INTERIOR_VERSION}
    artifact_dir: dist
    artifact_layout: triplet
```

### 覆盖下载地址

```yaml
- name: 生成完整正文
  image: docker.cnb.cool/dtapp/plugins/release-changelog:latest
  settings:
    mode: release
    version: ${INTERIOR_VERSION}
    artifact_dir: dist
    repo_url: ${CNB_REPO_URL_HTTPS}
    download_base: https://downloads.example.com/${INTERIOR_VERSION}
```

## 制品命名

支持 `.pkg.tar.zst`、`.exe.zip`、`.tar.gz`、`.AppImage`、`.deb`、`.rpm`、`.apk`、`.ipk`、`.fpk`、`.zip`、`.exe`。

推荐命名：

```text
App-linux-amd64.tar.gz
App-linux-arm64.tar.gz
App-windows-amd64.exe.zip
App-darwin-arm64.zip
App-arm64.fpk
backend-linux-amd64.tar.gz
```

`SHA256SUMS` 不进入下载表格；存在时正文会追加校验命令。插件只检测其是否存在，不验证哈希内容。

## 上线前检查

- `version` 能解析为支持的三段版本。
- `release` 模式的 `artifact_dir` 存在且包含可识别制品。
- `download_base` 指向本次 Release 实际可下载的地址。
- `artifact_layout` 与项目产物结构一致。
- 需要完整提交历史时没有关闭 `fetch_history`。
- 后续 Release 参数引用的 `descriptionFromFile` 与 `out_file` 一致。
- 原有 `preRelease`、标题和删除旧 Release/Tag 的步骤仍然保留。

## 排障

### 提示没有可发布制品

检查 `artifact_dir` 和文件名。`release` 模式至少需要一个支持的制品；只生成变更日志时改用 `changelog`。

### 提示找不到更早基准

检查 Tag 是否完整、版本格式是否受支持，以及当前版本是否已是最早有效版本。浅克隆场景保持 `fetch_history: true`。

### 拉取 Tag 失败

插件继续使用本地 Tag 并输出提示。检查 Git 凭据和远端访问；离线场景设置 `fetch_tags: false`。

### 更新内容只有少量提交

可能是浅克隆历史未补全。保持 `fetch_history: true`，确认流水线允许执行 `git fetch --unshallow` 或 `git fetch --depth 1000`。

### 下载链接不正确

显式设置 `download_base`。默认地址只适用于制品上传到当前 CNB Release 的场景。

### 输出文件路径不符合预期

相对 `out_file` 和 `artifact_dir` 均相对于 `workspace` 解析；需要固定位置时使用绝对路径。
