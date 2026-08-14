## Description:

This skill uses Cue to run industry research workflows for sectors or companies, covering market size, competition, business models, supply chains, policy impact, compliance risks, and source-linked research drafts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wangxiaoxu](https://clawhub.ai/user/wangxiaoxu)

### License/Terms of Use:

MIT-0

## Use Case:

External analysts, investors, and research teams use this skill to run Cue-backed industry research on a company, sector, theme, or ETF and receive a sourced research draft for review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may clone or update the Cue runner before use.

Mitigation: Review the runner source and install path before allowing git clone or git pull operations.

Risk: The skill uses a local Cue API key and makes network calls to Cue services.

Mitigation: Use an authorized Cue account and confirm that the research query may be sent to Cue before running the workflow.

Risk: Deep research runs consume Cue credits.

Mitigation: Require explicit user confirmation for the selected buddy, subject, and credit use before execution.

Risk: Industry research based on public data may be incomplete or unsuitable as a sole basis for investment, legal, or diligence decisions.

Mitigation: Preserve source links in the output and require human review before relying on conclusions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wangxiaoxu/skills/cue-industry-research)
- [Cue playbook API](https://cuecue.cn/api/playbook)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown report text with source links and inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a Cue account API key; deep research may take 3-15 minutes and consume credits after explicit confirmation.]

## Skill Version(s):

1.0.1 (source: evidence.release.version)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
