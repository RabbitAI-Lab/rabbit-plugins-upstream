## Description:

Uses Cue to run investment research workflows for equity valuation, financial statement analysis, fundamental risk checks, index comparison, convertible bond risk alerts, and source-linked research drafts from public data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wangxiaoxu](https://clawhub.ai/user/wangxiaoxu)

### License/Terms of Use:

MIT-0

## Use Case:

Investors, analysts, and agents assisting investment research use this skill to select a Cue investment-research workflow, confirm credit use, run the workflow, and return a source-linked report. Outputs are informational research drafts over public data and do not replace due diligence, legal review, underwriting, or investment advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may install or update Cue's runner in the user's home directory.

Mitigation: Review the runner source and use a trusted local or pinned checkout before execution.

Risk: The workflow uses a Cue API key from ~/.cue/config.json, contacts Cue services, and consumes credits.

Mitigation: Confirm the selected workflow and credit use with the user before running, and protect the local Cue configuration file.

Risk: Financial research can be incomplete, stale, or misleading if used as a decision source by itself.

Mitigation: Treat outputs as informational drafts, verify cited sources, and perform independent investment, legal, and risk review before acting.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wangxiaoxu/skills/cue-equity-research)
- [Cue playbook API](https://cuecue.cn/api/playbook)
- [Cue skills runner repository](https://github.com/sensedeal/cue-skills)
- [Cue skills runner mirror](https://gitee.com/sensedeal/cue-skills)

## Skill Output:

**Output Type(s):** [Markdown, Shell commands, Guidance]

**Output Format:** [Markdown report with source links and inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires user confirmation before consuming Cue credits; final reports should retain source links and avoid fabricated results when no content is returned.]

## Skill Version(s):

1.0.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
