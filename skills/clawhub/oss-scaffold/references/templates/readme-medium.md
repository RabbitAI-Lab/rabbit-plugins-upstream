<!-- 中档 README 模板，默认档（样板 Agent-Memory，规格调研 5.3/5.5）。骨架+占位符；风格细则按 oss-voice §2/§3 执行。语言默认英文主文件 + README.zh-CN.md 对照（oss-voice §1）。 -->

# {{project_name}}

[![License: MIT](https://img.shields.io/badge/License-MIT-{{badge_color}}.svg)](LICENSE) [![CI]({{repo_url}}/actions/workflows/ci.yml/badge.svg)]({{repo_url}}/actions) [![Release](https://img.shields.io/github/v/release/{{repo_owner}}/{{project_name}})](https://github.com/{{repo_owner}}/{{project_name}}/releases)

**English** | [简体中文](README.zh-CN.md)

> {{one_liner}}

## Highlights

- {{highlight_1}}
- {{highlight_2}}

| Benchmark | {{project_name}} | {{baseline}} |
|---|---|---|
| {{metric_1}} | {{value}} | {{baseline_value}} |

## Overview

{{overview_paragraph}}

## How It Works

```mermaid
{{mermaid_diagram}}
```

## Quick Start

Pick the path that matches your environment:

**Path 1: Docker**

```bash
{{quick_start_cmd_1}}
```

**Path 2: Install from package manager**

```bash
{{quick_start_cmd_2}}
```

**Path 3: Build from source**

```bash
{{quick_start_cmd_3}}
```

Detailed setup: [INSTALL.md](docs/INSTALL.md) · [deployment](docs/deployment.md) · [docker](docs/docker.md)

## Configuration

<details><summary>🟢 Daily</summary>

| Parameter | Default | Description |
|---|---|---|
| {{param_1}} | {{default_1}} | {{desc_1}} |

</details>

<details><summary>🟡 Advanced</summary>

{{advanced_params_table_or_placeholder}}

</details>

<details><summary>🔴 Full reference</summary>

See [docs/configuration.md](docs/configuration.md).

</details>

## Documentation

See [docs/](docs/).

## Community & Contributing

- Issues: we respond within {{response_sla}} on business days
- See [CONTRIBUTING.md](CONTRIBUTING.md) for the contribution workflow

## Roadmap

- [ ] {{roadmap_item_1}}
- [ ] {{roadmap_item_2}}

## License

[MIT](LICENSE) Copyright (c) {{year}} {{repo_owner}}
