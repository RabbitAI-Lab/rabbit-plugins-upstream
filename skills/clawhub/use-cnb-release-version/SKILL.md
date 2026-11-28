---

name: use-cnb-release-version

slug: use-cnb-release-version

displayName: CNB Release 处理版本插件使用

version: "1.0.2"

summary: "在 CNB 流水线中解析发版版本号、推导 nightly，并校验版本号与 Git Tag。"

license: MIT

description: "帮助用户在 CNB 项目的流水线中配置 release-version 插件，解析正式版和 rc、beta、alpha、nightly 版本，推导 nightly 版本号，并校验版本号与 Git Tag。适用于版本参数选择、 nightly 基版本与回退策略配置、输出映射、重复 Tag 校验及权限和 Git 失败排障。"

---

# 使用 CNB Release Version

## 适用范围

在已有 CNB 项目中使用官方插件：

`docker.cnb.cool/dtapp/plugins/release-version:latest`

- `mode: parse`：归一化版本号、识别预发布渠道、推导 nightly，并输出版本和提交信息。
- `mode: validate`：校验具体版本号与 Git Tag，检查重复 Tag 和正式版新旧关系。

只处理插件配置和使用，不涉及源码构建或插件开发。

## 配置前确认

- 确认目标 CNB 仓库、版本号来源和发布渠道。
- 定时发布需要空版本默认 nightly 时，设置 `default_nightly: true`。
- 自动推导 nightly 前，确认使用最近正式版 Tag，还是显式指定 `nightly_base_version`。
- 没有正式版 Tag 时，确认 `nightly_fallback` 策略；不确定基准时使用 `error`。
- `validate` 必须接收 `parse` 输出的具体 Tag，不能直接传裸 `nightly`。
- 只有需要同日重跑并覆盖同名 nightly Tag 时，才设置 `allow_existing_nightly: true`。
- 插件不会执行 `git checkout`，也不会创建、删除或移动 Release/Tag；这些动作由调用方流水线负责。

## 权限与安全

- 不需要 `CNB_TOKEN`，不调用 CNB OpenAPI。
- `fetch_tags: true` 使用仓库现有 Git 凭据拉取远端 Tag；离线或没有远端时设置为 `false`。
- `validate` 和自动推导 nightly 需要可访问的 Git 仓库，运行环境必须安装 `git`。
- 插件会自动添加 `safe.directory` 并设置 `GIT_TERMINAL_PROMPT=0`，避免容器属主差异和交互式认证阻塞。
- Git 参数通过参数数组传递，不把版本号拼接进 shell 命令。

## 参数

CNB 会将 `settings` 转换为大写、带 `PLUGIN_` 前缀的环境变量。布尔值常见写法为 `true` / `false`。

| 参数                     | 类型    | 默认值       | 说明                                                                                                                        |
|--------------------------|---------|--------------|-----------------------------------------------------------------------------------------------------------------------------|
| `mode`                   | string  | 无，必填     | `parse` / `validate`                                                                                                        |
| `version`                | string  | 无，必填     | 待解析或校验的版本号；`validate` 必须传具体 Tag。`parse` 下设置 `default_nightly: true` 时可为空                            |
| `commit`                 | string  | `""`         | 仅 `parse`：透传上游提交，只接受 40 位小写十六进制 SHA；非法值按空字符串输出                                                |
| `default_nightly`        | boolean | `false`      | 仅 `parse`：`version` 为空或全是空白时按 `nightly` 处理                                                                     |
| `nightly_base_version`   | string  | `""`         | nightly 基版本 `X.Y.Z`；设置后不再读取 Git Tag，并在其后补丁号加一                                                          |
| `nightly_date`           | string  | `""`         | 覆盖 nightly 日期，格式为 8 位数字 `YYYYMMDD`；未设置时取 `nightly.YYYYMMDD` 中的日期，再回退到本地时区当天（默认北京时间） |
| `nightly_fallback`       | string  | `zero`       | 找不到正式版 Tag 时的策略：`zero` / `prerelease` / `prerelease_bump` / `prerelease_or_zero` / `error`                       |
| `fetch_tags`             | boolean | `true`       | 是否尽力执行 `git fetch --tags --quiet --force`；失败只告警，继续使用本地 Tag                                               |
| `allow_existing_nightly` | boolean | `false`      | 校验时是否允许同名 nightly Tag 已存在；对其他渠道无效                                                                       |
| `workspace`              | string  | 当前工作目录 | Git 仓库路径；CNB 默认工作区无需设置                                                                                        |

### nightly_fallback

仅在未设置 `nightly_base_version` 且仓库找不到严格匹配 `vX.Y.Z` / `VX.Y.Z` 的正式版 Tag 时生效：

| 值                   | 行为                                                                                                              |
|----------------------|-------------------------------------------------------------------------------------------------------------------|
| `zero`               | 从 `0.0.0` 开始，补丁号加一，生成 `v0.0.1-nightly.YYYYMMDD`                                                       |
| `prerelease`         | 取数值最大的 `rc` / `beta` / `alpha` / `nightly` 版本核心，不增加补丁号；如果没有预发布 Tag，则回退到 `zero` 行为 |
| `prerelease_bump`    | 取数值最大的预发布版本核心，并增加补丁号；如果没有预发布 Tag，则回退到 `zero` 行为                                |
| `prerelease_or_zero` | 优先取数值最大的预发布版本核心且不增加补丁号；如果连预发布 Tag 也没有，则使用 `0.0.0` 且不增加补丁号              |
| `error`              | 直接失败，避免在缺少正式版基准时生成错误的 nightly 版本                                                           |

## 版本号规则

- 删除输入中的所有空白字符。
- 只允许字母、数字以及 `.`、`_`、`+`、`-`。
- 输入不以 `v` 或 `V` 开头时补充小写 `v`；已有大写 `V` 会保留。
- 根据末尾的 `-rc`、`-beta`、`-alpha`、`-nightly` 识别渠道，大小写不敏感。
- 未命中上述后缀的版本按正式版处理，例如 `v1.2.3-hotfix` 的 `channel` 为 `stable`。
- 该实现沿用现有脚本的白名单规则，不是严格的 SemVer 校验器。

| 输入                      | 输出 Tag                  | prerelease | channel   |
|---------------------------|---------------------------|------------|-----------|
| `1.2.3`                   | `v1.2.3`                  | `false`    | `stable`  |
| `V1.2.3-RC.1`             | `V1.2.3-RC.1`             | `true`     | `rc`      |
| `v1.2.3-beta.2`           | `v1.2.3-beta.2`           | `true`     | `beta`    |
| `v1.2.3-alpha.1.2`        | `v1.2.3-alpha.1.2`        | `true`     | `alpha`   |
| `v1.2.3-nightly.20261127` | `v1.2.3-nightly.20261127` | `true`     | `nightly` |
| `v1.2.3-hotfix`           | `v1.2.3-hotfix`           | `false`    | `stable`  |
| `nightly`                 | 自动推导                  | `true`     | `nightly` |
| `nightly.20261127`        | 使用指定日期自动推导      | `true`     | `nightly` |

普通版本解析不需要 Git 仓库。只有输入为 `nightly` / `nightly.YYYYMMDD` 且未设置 `nightly_base_version` 时，才会读取仓库 Tag。`head_commit` / `commit_full` / `commit_short` 是尽力输出：工作区不是 Git 仓库或读取 HEAD 失败时省略，不影响普通版本解析。

## 输出

### parse

| 输出           | 说明                                                          |
|----------------|---------------------------------------------------------------|
| `tag`          | 归一化后的 Git Tag / Release 版本号                           |
| `version`      | 去掉 `v` / `V` 前缀的版本号                                   |
| `prerelease`   | `true` / `false`                                              |
| `version_type` | `正式版` / `预发布`                                           |
| `channel`      | `stable` / `rc` / `beta` / `alpha` / `nightly`                |
| `version_base` | 三段数字打包基版本                                            |
| `version_pkg`  | 将 `-` 替换为 `~` 的打包版本                                  |
| `pre_note`     | 人类可读的版本摘要，与日志中的摘要一致                        |
| `commit`       | 上游 `commit` 输入；只接受 40 位小写十六进制 SHA，否则为 `""` |
| `head_commit`  | 当前 `HEAD` 的完整提交 SHA；仅在工作区可读取 Git HEAD 时输出  |
| `commit_full`  | 同 `head_commit`，用于兼容需要全量 SHA 的流水线               |
| `commit_short` | 当前 `HEAD` 的短提交 SHA；仅在工作区可读取 Git HEAD 时输出    |
| `nightly_base` | 仅自动推导 nightly 时输出，表示加一后的基版本，例如 `1.2.10`  |

### validate

仅在校验通过时输出：

| 输出            | 说明                                                |
|-----------------|-----------------------------------------------------|
| `validated`     | 固定为 `true`                                       |
| `tag`           | 归一化后的 Tag                                      |
| `prerelease`    | `true` / `false`                                    |
| `tag_exists`    | 同名 Tag 是否存在；允许覆盖的 nightly 场景为 `true` |
| `latest_stable` | 数值最大的严格正式版 Tag；没有时为 `""`             |
| `tag_commit`    | 同名 Tag 指向的完整提交 SHA；Tag 不存在时为 `""`    |
| `head_commit`   | 当前 `HEAD` 的完整提交 SHA                          |

## 配置示例

将阶段合并到项目 `.cnb.yml` 现有事件的 `stages` 中，不要覆盖其他阶段。通过 `exports` 将插件输出映射为后续 stage 的环境变量。

### 解析并校验正式版

```yaml
- name: 解析版本号
  image: docker.cnb.cool/dtapp/plugins/release-version:latest
  settings:
    mode: parse
    version: ${version}
    fetch_tags: false
  exports:
    tag: INTERIOR_VERSION
    prerelease: INTERIOR_PRERELEASE
    version_base: INTERIOR_VERSION_BASE
    version_pkg: INTERIOR_VERSION_PKG

- name: 校验版本号与 Tag
  image: docker.cnb.cool/dtapp/plugins/release-version:latest
  settings:
    mode: validate
    version: ${INTERIOR_VERSION}
    fetch_tags: true
  exports:
    validated: VERSION_VALIDATED
    latest_stable: LATEST_STABLE
```

### 空版本默认 nightly

```yaml
- name: 解析 nightly
  image: docker.cnb.cool/dtapp/plugins/release-version:latest
  settings:
    mode: parse
    version: ${version}
    default_nightly: true
    fetch_tags: true
    nightly_fallback: error
  exports:
    tag: INTERIOR_VERSION
    prerelease: INTERIOR_PRERELEASE

- name: 校验 nightly
  image: docker.cnb.cool/dtapp/plugins/release-version:latest
  settings:
    mode: validate
    version: ${INTERIOR_VERSION}
    fetch_tags: true
    allow_existing_nightly: true
```

`allow_existing_nightly: true` 仅允许校验通过。插件本身不会删除或重建 Release/Tag，覆盖动作仍由后续发布步骤负责。

### 固定 nightly 基版本和日期

```yaml
- name: 解析固定 nightly
  image: docker.cnb.cool/dtapp/plugins/release-version:latest
  settings:
    mode: parse
    version: nightly
    nightly_base_version: 1.2.9
    nightly_date: 20261127
    fetch_tags: false
  exports:
    tag: NIGHTLY_TAG
    nightly_base: NIGHTLY_BASE
```

输出为 `v1.2.10-nightly.20261127`，`nightly_base` 为 `1.2.10`。

## 校验规则

- 同名正式版、`rc`、`beta`、`alpha` Tag 已存在时失败，避免重复发布或移动历史 Tag。
- 同名 nightly Tag 已存在时，只有 `allow_existing_nightly: true` 才通过。
- 正式版按 major / minor / patch 数值比较，不使用字符串排序。
- “最近正式版”只认严格的 `vX.Y.Z` / `VX.Y.Z` Tag，忽略预发布、四段版本及格式不完整的历史 Tag。
- 预发布版本不与正式版比较新旧，例如已有 `v2.0.0` 时仍可发布 `v1.0.0-rc.1`。
- 参数非法、Git 命令失败、Tag 重复或正式版版本过旧都会以非零退出码结束。

## 排障

### 缺少必要环境变量 PLUGIN_VERSION

检查 `settings.version` 是否传入。定时发布希望空版本按 nightly 处理时，设置 `default_nightly: true`。

### 解析 nightly 提示需要 Git 仓库或基版本

自动推导 nightly 需要最近正式版 Tag。检查工作区是否是 Git 仓库，或显式设置 `nightly_base_version`。设置后不再读取仓库 Tag。

### 拉取 Tag 失败

`fetch_tags` 是尽力执行，失败后继续使用本地 Tag，并输出提示。如果本地 Tag 不完整，校验结果可能不完整；需要完整基准时应确保 Git 凭据和远端访问正常，离线场景可设置 `fetch_tags: false`。

### 校验 nightly 提示不能重复发布

`allow_existing_nightly` 默认是 `false`。只有需要同日重跑并覆盖同名 nightly Tag 时，才显式设置为 `true`，并确认后续步骤会删除并重建同名 Release/Tag。

### 正式版提示比已有版本旧

数值比较发现待发布版本小于本地最近正式版。预发布渠道不会执行这项比较；如果确实需要回退正式版，应人工确认历史版本策略，而不是绕过校验。

### 仓库没有正式版 Tag

`nightly_fallback` 默认按 `zero` 策略生成 `v0.0.1-nightly.YYYYMMDD`。可改为 `prerelease` 使用最近预发布核心，或改为 `error` 明确失败。
