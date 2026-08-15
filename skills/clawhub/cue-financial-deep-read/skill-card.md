## Description:

This skill helps agents run Cue's Financial Deep Read workflow for public-company earnings research, including financial-statement analysis, funding-flow review, financial-quality checks, forward-guidance follow-up, convertible-bond review, audit-opinion checks, and source-linked risk-signal reporting.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wangxiaoxu](https://clawhub.ai/user/wangxiaoxu)

### License/Terms of Use:

MIT-0

## Use Case:

External users and analysts use this skill to ask an agent to run Cue-based deep research on listed-company financial reports and return a source-linked analysis with financial-quality and risk signals. The skill is useful for earnings review, disclosure and regulatory checks, funding-flow analysis, and audit or convertible-bond due diligence support.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can fetch and run mutable remote Cue runner code from GitHub or Gitee.

Mitigation: Review and pin the runner code before first use, and update it only after review.

Risk: The runner can read the local Cue API key and contact cuecue.cn.

Mitigation: Install only in an environment where Cue account access is intended, and avoid exposing unrelated credentials.

Risk: Deep research runs can consume Cue credits.

Mitigation: Require explicit user confirmation before each credit-consuming run.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wangxiaoxu/skills/cue-financial-deep-read)
- [Cue playbook API](https://cuecue.cn/api/playbook)
- [Cue runner repository](https://github.com/sensedeal/cue-skills)
- [Cue runner mirror](https://gitee.com/sensedeal/cue-skills)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown report with source links and inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The agent should confirm credit use before running Cue and should report empty runner results without fabricating analysis.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
