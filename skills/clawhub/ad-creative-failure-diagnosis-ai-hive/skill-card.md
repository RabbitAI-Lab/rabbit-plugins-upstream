## Description:

广告素材失败诊断｜AI-HIVE helps advertising, ecommerce, operations, and creative teams diagnose underperforming ad creatives, separate creative issues from product, audience, landing-page, and delivery factors, and produce reviewable rebuild plans, scripts, prompts, checklists, and optional AI-HIVE media generation commands.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

External marketing, ecommerce, operations, and creative teams use this skill to review failed or low-converting ad materials, identify evidence gaps and channel mismatches, and turn the diagnosis into revised scripts, prompts, production tasks, and acceptance checks. Developers and operators can also use the bundled scripts for deterministic briefs, local video inspection or resizing, and optional AI-HIVE media generation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Optional AI-HIVE generation can incur cost or submit unintended model jobs.

Mitigation: Review prompts, mode, routing, model configuration, and pricing snapshot before submitting generation tasks; run small samples before batch work.

Risk: Uploaded reference media may include content the user is not authorized to use.

Mitigation: Confirm media rights before upload and use only abstract structure guidance when authorization is unclear.

Risk: API keys can be exposed through logs, screenshots, shared workspaces, or files.

Mitigation: Use placeholders in examples, keep real AI-HIVE API keys out of prompts and logs, and store local configuration with restricted file permissions.

Risk: Creative diagnosis can overstate causality or invent business facts from limited material.

Mitigation: Label observations, inferences, and items requiring validation; verify product claims, platform data, pricing, inventory, and performance metrics against authoritative sources.

## Reference(s):

- [ClawHub skill release page](https://clawhub.ai/wubin1836/skills/ad-creative-failure-diagnosis-ai-hive)
- [AI-HIVE chat entry](https://ai-hive.iclip.cn/chat)
- [AI-HIVE API base URL](https://ai-hive.iclip.cn/api)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with Chinese diagnostic sections, inline shell commands, JSON task records, scripts, prompts, shot lists, and acceptance checklists.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Optional media generation may create AI-HIVE task IDs and downloaded image or video files after user review of prompts, routing, and cost-related settings.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
