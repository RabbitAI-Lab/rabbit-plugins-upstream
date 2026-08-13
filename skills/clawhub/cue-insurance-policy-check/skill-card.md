## Description:

用 Cue 逐条核验保险产品的保障责任、责任免除、等待期、费率与退保损失，并与同类产品客观对比，产出可向客户如实说明的条款理解底稿。

This skill is ready for commercial/non-commercial use.

## Publisher:

[panting09266-ai](https://clawhub.ai/user/panting09266-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External insurance and compliance users use this skill to check policy coverage, exclusions, waiting periods, rates, surrender losses, comparable products, and customer-facing disclosure boundaries.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Insurance product queries and API-authenticated requests are sent to Cue's online service.

Mitigation: Do not include customer PII, secrets, internal files, or confidential business details unless organizational policy allows Cue processing.

Risk: The skill depends on an external runner, Cue service availability, and external data sources.

Mitigation: Use a dedicated revocable API key, review the external runner or install source before first use, and verify generated policy findings against authoritative source documents.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/panting09266-ai/skills/cue-insurance-policy-check)
- [Cue runner source](https://github.com/sensedeal/cue-skills)
- [Cue runner Gitee mirror](https://gitee.com/sensedeal/cue-skills)
- [Cue service](https://cuecue.cn)
- [Cue sample report](https://cuecue.cn/share/1c3d67d8bc4c)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown report with optional shell commands and file output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces a structured policy-understanding draft with source links; optional conversion to Word or PDF is documented.]

## Skill Version(s):

1.0.3 (source: server release evidence; artifact frontmatter reports 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
