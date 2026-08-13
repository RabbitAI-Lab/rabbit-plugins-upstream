## Description:

面向跨境电商的 Google AI Mode 搜索研究专家。适用于需要带引用的最新 Google AI Overview 结果，用于海外消费者偏好、产品趋势、市场问题、技术趋势或连续追问式网页调研的场景。

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External cross-border e-commerce sellers, product research teams, and brand operators use this skill to request one Google AI Mode query at a time, receive cited AI Overview Markdown for market research, and save longer findings as HTML reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The release bundles Google search with account, billing, public upload, and text-generation capabilities that are broader than the top-level purpose.

Mitigation: Review the bundled LinkFox skills before installation and enable only the capabilities acceptable for the deployment.

Risk: Queries, prompts, media URLs, and uploaded files may be transmitted to LinkFox services; uploaded files receive public URLs.

Mitigation: Avoid sensitive inputs and upload only content approved for public access.

Risk: The skill depends on API keys and configurable gateway environment variables.

Mitigation: Verify LINKFOX_AGENT_API_KEY or LINKFOXAGENT_API_KEY and LINKFOX_TOOL_GATEWAY before use, and store credentials securely.

Risk: Google AI Overview may not trigger for a query, and live search summaries can vary across calls.

Mitigation: Check resultsNum and cited links before relying on output; retry or rephrase only after the user accepts any additional cost.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/linkfox-ai/skills/linkfox-expert-google-search-researcher)
- [Google AI Mode Search API Reference](artifact/skills/linkfox-ai-mode-google-search/references/api.md)
- [Google AI Mode Onboarding and Auth Guidance](artifact/skills/linkfox-ai-mode-google-search/references/onboarding.md)
- [File Upload API Reference](artifact/skills/linkfox-file-upload/references/api.md)
- [AI Text Generation API Reference](artifact/skills/linkfox-aigc-textgen/references/api.md)
- [Report Layout Reference](artifact/skills/linkfox-report-generator/references/analysis-layouts.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown responses with cited links, JSON tool responses, HTML report files for long outputs, and shell command examples.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Single-question Google AI Overview lookup; same parameters are cached for 24 hours; long outputs may be written as HTML reports; companion upload behavior can create public URLs.]

## Skill Version(s):

1.0.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
