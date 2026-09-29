<!-- 轻档 README 模板，落地页式（样板 teamai-cli，规格调研 5.4/5.5）。骨架+占位符；风格细则按 oss-voice §2/§3 执行。README 即落地页，细节全部移 docs/（README 减肥，teamai-cli#722）。语言默认英文主文件 + README.zh-CN.md 对照（oss-voice §1）。 -->

<div align="center">

<img src="{{logo_path}}" width="{{logo_width}}" alt="{{project_name}} logo" />

# {{project_name}}

{{one_liner}}

{{trendshift_or_extra_badge}}

[![CI]({{repo_url}}/actions/workflows/ci.yml/badge.svg)]({{repo_url}}/actions) [![npm](https://img.shields.io/npm/v/{{npm_package_name}})](https://www.npmjs.com/package/{{npm_package_name}}) [![License: MIT](https://img.shields.io/badge/License-MIT-{{badge_color}}.svg)](LICENSE)

**English** | [简体中文](README.zh-CN.md)

</div>

## Why {{project_name}}?

| Before | After |
|---|---|
| {{pain_point}} | {{resolved_state}} |

## Quick Start

```bash
{{install_cmd}}
```

```bash
{{usage_cmd}}
```

## Support Matrix

| Target | Version | Status |
|---|---|---|
| {{target_1}} | {{version_1}} | ✓ / — |

Full matrix and rationale: [docs/product-overview.md](docs/product-overview.md)

## Learn More

- [Usage guide](docs/usage-guide.md)
- [Design notes](docs/designs/)

## Contributing

PRs welcome — see [CONTRIBUTING.md](CONTRIBUTING.md). Contributor wall:

{{contributors_wall_placeholder}}

## License

[MIT](LICENSE) Copyright (c) {{year}} {{repo_owner}}
