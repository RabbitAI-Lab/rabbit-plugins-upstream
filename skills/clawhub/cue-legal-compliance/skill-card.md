## Description:

用 Cue 运行法律合规场景的深度研究，检索国内法律法规、监管材料和公开案例，并产出带来源链接的合规体检、法律研判或文书草稿。

This skill is ready for commercial/non-commercial use.

## Publisher:

[wangxiaoxu](https://clawhub.ai/user/wangxiaoxu)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to run Cue-based legal compliance research for regulatory inquiries, enterprise due diligence, domestic regulation surveys, legal issue assessment, enforcement monitoring, and litigation document drafting.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The external Cue runner may be cloned or updated in the user's home directory.

Mitigation: Review the runner source and repository destination before installation or update.

Risk: Legal queries, uploaded case details, and the Cue API key may be sent to Cue during research runs.

Mitigation: Use only data appropriate for Cue processing and confirm API key handling before running the skill.

Risk: Deep legal research consumes credits and may produce material that users could mistake for professional legal advice.

Mitigation: Require explicit credit confirmation before execution and treat generated reports as sourced research drafts for qualified review.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wangxiaoxu/skills/cue-legal-compliance)
- [Cue playbook API](https://cuecue.cn/api/playbook)
- [Cue skills runner repository](https://github.com/sensedeal/cue-skills)
- [Cue skills runner mirror](https://gitee.com/sensedeal/cue-skills)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown report with source links and inline shell commands for runner setup and execution]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Deep research runs may take 3-15 minutes and should preserve source links in the final report.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
