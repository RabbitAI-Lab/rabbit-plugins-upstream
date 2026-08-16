## Description:

Uses Cue deep research to cross-check public evidence, verify business and disclosure claims, and produce reviewable findings with source links and red-flag notes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wangxiaoxu](https://clawhub.ai/user/wangxiaoxu)

### License/Terms of Use:

MIT-0

## Use Case:

External users and analysts use this skill to run Cue deep verification workflows for corporate due diligence, disclosure and regulatory checks, counterparty qualification, address checks, intellectual property review, and research-report credibility review. It helps produce source-linked verification notes, evidence chains, and red-flag findings from public data.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First use may clone or update Cue runner code under ~/.cue.

Mitigation: Review and trust the Cue runner source before installing or running the skill.

Risk: The runner uses the user's Cue login/API key and sends the research query to Cue.

Mitigation: Use an appropriate Cue account and avoid submitting sensitive or unauthorized information.

Risk: Deep research consumes Cue credits after user confirmation.

Mitigation: Require explicit confirmation before running any credit-consuming research.

Risk: Results are based on public data and may not replace formal due diligence, legal review, or underwriting.

Mitigation: Treat outputs as reviewable verification notes and preserve source links for human assessment.

## Reference(s):

- [Cue playbook API](https://cuecue.cn/api/playbook)
- [Cue skills runner source](https://github.com/sensedeal/cue-skills)
- [Cue skills runner mirror](https://gitee.com/sensedeal/cue-skills)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Markdown]

**Output Format:** [Markdown report with source links and inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires explicit user confirmation before credit-consuming research; the runner may return an empty result instead of a report.]

## Skill Version(s):

1.0.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
