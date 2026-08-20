## Description:

Multi Agent Team coordinates proposer, critic, fact-checker, and synthesis roles to produce a weighted consensus answer with confidence and dissent details for complex decisions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qq435912743](https://clawhub.ai/user/qq435912743)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users can use this skill to run a local multi-role deliberation workflow for decision support, cross-checking role outputs and aggregating them into a consensus report.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Decision tasks, role stances, consensus output, and optional learning or preference data may be written to local JSON files.

Mitigation: Avoid entering secrets or highly sensitive business data unless output paths are controlled and reviewed.

Risk: Consensus recommendations can be incorrect or misleading if role templates, task framing, or verification signals are weak.

Mitigation: Review the generated report before using it for material decisions, especially where safety, legal, financial, or operational impact is high.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/qq435912743/skills/multi-agent-team)
- [Publisher profile](https://clawhub.ai/user/qq435912743)

## Skill Output:

**Output Type(s):** [text, json, shell commands, guidance]

**Output Format:** [Markdown guidance with shell command examples and local JSON report output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces team_report.json with task, roles, stances, consensus, agreement, confidence, dissent, and completion timestamp.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
