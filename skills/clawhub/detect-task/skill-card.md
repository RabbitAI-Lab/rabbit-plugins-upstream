## Description:

投前 AI 图真实性质检。待检图 -> 风险等级 + 8 项逐条判定 + 可直接追加到 prompt 的修正句，可自动重跑直到达标。

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External e-commerce operators, marketers, and developers use this skill to inspect AI-generated product images before listing or ad use. It returns a risk level, eight itemized visual checks, a launch recommendation, and concise prompt fixes that can drive a rerun loop.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected product images, prompts, and provider credentials may be sent to external model providers, and a custom ARK endpoint can receive sensitive inputs if configured.

Mitigation: Install only when sharing selected assets with the configured provider is acceptable; prefer official provider defaults and use ARK_BASE_URL only for trusted HTTPS endpoints you control.

Risk: Automated fix and rerun modes can write modified image outputs and spend credits through repeated generation.

Mitigation: Use dry-run and conservative max-round settings first, review generated manifests, and inspect outputs before accepting automated reruns.

Risk: The visual quality report can have false positives or false negatives and does not replace legal or platform-policy review.

Mitigation: Keep human final review for listing decisions and verify platform requirements against current official rules.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/dlazyai/skills/detect-task)
- [Model Flags](references/model-flags.md)
- [Platform Specs](references/platform-specs.md)
- [Provider CLI](references/provider-cli.md)
- [dLazy CLI](https://github.com/dlazy-ai/cli)
- [Example Report](https://github.com/dlazy-ai/ecommerce-skills/blob/main/docs/detect-task/example-report.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown quality-control report with optional JSON command output and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces a risk level, eight itemized checks, a launch recommendation, and one to three English prompt-fix sentences.]

## Skill Version(s):

1.0.10 (source: server release evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
