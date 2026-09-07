## Description:

多商品批量生图流水线。商品清单 CSV -> 整批统一视觉的商拍图，带并发、重试、断点续跑、成本熔断与挑图联系表。当用户说「批量生图」「一批商品」「跑整个 SKU 表」「几百个商品出图」时使用。

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and ecommerce operators use this skill to turn a CSV product manifest into a repeatable batch image-generation workflow with consistent visual specifications, retry handling, resumable runs, budget controls, output manifests, and contact sheets.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Manifests, remote image URLs, provider environment variables, and broad output paths can expose sensitive data or overwrite files.

Mitigation: Use trusted CSV manifests and local reference images when possible, review output directories before running resume or contact-sheet workflows, and avoid passing sensitive product data to untrusted providers.

Risk: Custom provider endpoints can redirect production credentials or image payloads outside the intended service boundary.

Mitigation: Do not set custom ARK_BASE_URL with production keys, and review provider environment variables before execution.

Risk: Batch generation can spend credits quickly when run at scale or with expensive model settings.

Mitigation: Run dry-run estimates first, set a max-credit budget, keep batch size and resolution aligned with the documented guidance, and start with sample SKUs before full runs.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/batch-image)
- [Provider CLI reference](references/provider-cli.md)
- [seedream-5.0 model flags](references/model-flags.md)
- [Platform image specifications](references/platform-specs.md)
- [dLazy CLI](https://github.com/dlazy-ai/cli)
- [detect-task quality check skill](https://github.com/dlazy-ai/ecommerce-skills/blob/main/skills/detect-task/skill.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with bash, CSV, YAML, and JavaScript command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guides generation of local image files, manifests, reports, and contact-sheet HTML through external provider tools.]

## Skill Version(s):

1.0.6 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
