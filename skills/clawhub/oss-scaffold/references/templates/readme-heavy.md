<!-- 重档 README 模板（样板 WeKnora；段序与组件实证 WeKnora#3676/#3117/#3679/#3688，文档站 #2350/#3580，全量引句见 oss-voice §2 与 corpus/three-repos-raw/analysis/out-voice-weknora.md）。骨架+占位符；风格细则按 oss-voice §2/§3 执行，不在此复制。语言默认英文主文件 + 中文对照，多语命名**仓内必须统一一套**：重档跟样板 WeKnora 用 README_CN.md / README_JA.md / README_KO.md（#2757），轻档 teamai-cli 用 README.zh-CN.md（#767）——两套都是真实惯例，混用即破绽。中文社区型仓中英并重（oss-voice §1）。 -->

# {{project_name}}

[![License: MIT](https://img.shields.io/badge/License-MIT-{{badge_color}}.svg)](LICENSE) [![Release](https://img.shields.io/github/v/release/{{repo_owner}}/{{project_name}})](https://github.com/{{repo_owner}}/{{project_name}}/releases) [![Docs]({{docs_site_badge_url}})]({{docs_site_url}})

**English** | [简体中文](README_CN.md)

> {{one_liner}}

[Overview](#overview) · [Quick Start](#quick-start) · [What's New](#whats-new) · [Features](#features) · [Clients](#clients-and-integrations) · [Docs](#documentation) · [Development](#development)

## Overview

{{overview_paragraph}}

## Quick Start

Three entry points — pick one:

**Option 1: Hosted platform**

```bash
{{quick_start_cmd_1}}
```

**Option 2: Docker Compose**

```bash
{{quick_start_cmd_2}}
```

**Option 3: Build from source**

```bash
{{quick_start_cmd_3}}
```

## What's New

- **v{{latest_version}}** ({{date}}): {{release_highlight}} — see [CHANGELOG.md](CHANGELOG.md)

## Product Tour

{{product_tour_bullet_list}}

## Architecture

{{architecture_diagram_or_link}}

## Features

| Area | Capability | Status |
|---|---|---|
| {{feature_area_1}} | {{capability_1}} | {{status_1}} |
| {{feature_area_2}} | {{capability_2}} | {{status_2}} |

## Clients and Integrations

| Client | Supported | Notes |
|---|---|---|
| {{client_1}} | ✓ / — | {{note}} |

## Documentation

Full docs at {{docs_site_url}} (source in `docs/`; site built with VitePress).

## Development

```bash
{{dev_cmd}}
```

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md). Contributions welcome — check [good first issues]({{repo_url}}/issues?q=is%3Aissue+is%3Aopen+label%3A%22good+first+issue%22).

## Contributors

<a href="{{repo_url}}/graphs/contributors"><img src="https://contrib.rocks/image?repo={{repo_owner}}/{{project_name}}" /></a>

## License

[MIT](LICENSE) Copyright (c) {{year}} {{repo_owner}}
