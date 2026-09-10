## Description:

投前 AI 图真实性质检。待检图 -> 风险等级 + 8 项逐条判定 + 可直接追加到 prompt 的修正句，可自动重跑直到达标。

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External e-commerce operators and agent users use this skill to inspect AI-generated product images before launch, identify common visual defects, and receive concise prompt fixes for reruns or manual retouching.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected images and prompts may be sent to dLazy or another configured provider.

Mitigation: Use the skill only with images and prompts that may be shared with the selected provider, and choose the documented dLazy detect workflow unless another provider is deliberately configured.

Risk: Provider routing and executable selection can be influenced by environment values such as ARK_BASE_URL or DLAZY_BIN.

Mitigation: Run in a trusted environment, avoid untrusted provider endpoint or binary overrides, and review provider configuration before execution.

Risk: Image quality judgments can contain false positives or false negatives.

Mitigation: Use the report as pre-launch triage, keep human review for final publishing decisions, and increase sampling or rerun checks for high-risk batches.

Risk: Generated reports or manifests may contain confidential product prompts or image details.

Mitigation: Store outputs outside shared or public directories when prompts, SKUs, or product images are confidential.

## Reference(s):

- [Provider CLI Reference](references/provider-cli.md)
- [claude-sonnet-5 Model Flags](references/model-flags.md)
- [Platform Image Specifications](references/platform-specs.md)
- [Example Detect Task Report](https://github.com/dlazy-ai/ecommerce-skills/blob/main/docs/detect-task/example-report.md)
- [dLazy CLI Source](https://github.com/dlazy-ai/cli)
- [ClawHub Skill Page](https://clawhub.ai/dlazyai/skills/detect-task)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Chinese Markdown report with a risk level, eight itemized checks, a launch recommendation, and English prompt-fix sentences.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Returns a textual inspection report for selected images; batch examples route high-risk items into a rerun queue.]

## Skill Version(s):

1.0.8 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
