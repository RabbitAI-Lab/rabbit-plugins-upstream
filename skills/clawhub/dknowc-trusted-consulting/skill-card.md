## Description:

深知可信咨询调用深知可信统一问答接口，为政策法规、政务办事、税务社保、公积金、企业补贴、资质证照、行业标准、公共服务和合规咨询生成带来源角标的答案、本地溯源 HTML 和干净 Markdown。

This skill is ready for commercial/non-commercial use.

## Publisher:

[dylanzhangzx](https://clawhub.ai/user/dylanzhangzx)

### License/Terms of Use:

MIT-0

## Use Case:

External users and employees use this skill to answer policy, regulation, government-service, tax, social-security, housing-fund, subsidy, licensing, public-service, and compliance questions with source-cited consultation output. It is intended for workflows that need a cited answer, a local interactive provenance HTML report, and a clean Markdown copy.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Consultation prompts and phone-based registration details are sent through dknowc external services.

Mitigation: Avoid entering unnecessary personal, business-confidential, or regulated details, and install only when this data flow is acceptable.

Risk: API-key handling occurs through the agent workflow.

Mitigation: Configure DKNOWC_API_KEY through a platform secret store and do not expose the raw key in chat or tool output.

Risk: Generated output paths may be broader than expected.

Mitigation: Keep generated consultation artifacts within the skill's official-docs/search-results and official-docs/output directories.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dylanzhangzx/skills/dknowc-trusted-consulting)
- [dknowc MaaS platform](https://platform.dknowc.cn/)
- [dknowc trusted unified chat API endpoint](https://open.dknowc.cn/chat/trusted/unification)

## Skill Output:

**Output Type(s):** [text, markdown, files, shell commands, configuration, guidance]

**Output Format:** [Markdown answer with numeric source markers, plus generated HTML and clean Markdown files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires DKNOWC_API_KEY from the environment before consultation calls; generated consultation artifacts are intended to stay under the skill's official-docs directories.]

## Skill Version(s):

1.0.4 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
