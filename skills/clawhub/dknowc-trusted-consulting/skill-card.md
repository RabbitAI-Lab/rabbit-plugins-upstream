## Description:

深知可信咨询 helps agents answer Chinese policy, government-service, tax, social-security, housing-fund, subsidy, licensing, standards, compliance, and public-service questions through DKNOWC's trusted consultation API, producing citation-marked answers plus local provenance HTML and clean Markdown when configured with DKNOWC_API_KEY.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dylanzhangzx](https://clawhub.ai/user/dylanzhangzx)

### License/Terms of Use:

MIT-0

## Use Case:

External users, business operators, and agents use this skill to ask Chinese policy, government-service, tax and social insurance, housing fund, subsidy, licensing, standards, compliance, and public-service questions and receive source-cited consultation output. Agents can use it to generate a cited answer, an interactive provenance HTML report, and a clean Markdown copy after API-key initialization.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Consultation questions are sent to DKNOWC endpoints when the skill runs.

Mitigation: Avoid unnecessary sensitive business or personal details and confirm API use is acceptable before invoking the skill.

Risk: The skill can create local HTML, Markdown, and intermediate traceability files in its workspace.

Mitigation: Request no HTML or files when local artifacts are not desired, and review generated files before sharing them.

Risk: The optional MaaS registration flow can return an API key.

Mitigation: Treat any returned key as a secret and persist it only through approved environment-variable or secret-management flows.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dylanzhangzx/skills/dknowc-trusted-consulting)
- [Publisher profile](https://clawhub.ai/user/dylanzhangzx)
- [DKNOWC MaaS management platform](https://platform.dknowc.cn/)
- [DKNOWC trusted unified chat endpoint](https://open.dknowc.cn/chat/trusted/unification)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance, files]

**Output Format:** [Markdown answer with citation markers, local HTML provenance report, and clean Markdown file; may include setup commands.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires DKNOWC_API_KEY; can call external DKNOWC endpoints and write local traceability files.]

## Skill Version(s):

1.0.3 (source: release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
