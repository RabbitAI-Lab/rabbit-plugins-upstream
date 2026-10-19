## Description:

Reviews an agent session for lessons learned, actionable improvements, and opportunities to improve invoked skills.

This skill is ready for commercial/non-commercial use.

## Publisher:

[iliaal](https://clawhub.ai/user/iliaal)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and other agent users can review a session to identify evidenced mistakes, useful practices, and prioritized improvements, and audit skills used during the work.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Retrospective notes could persist sensitive details or unwanted cross-project guidance.

Mitigation: Exclude credential values, avoid sensitive details in memory requests, and review and approve specific cross-project memory items before writing.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/iliaal/skills/compound-eng-reflect)
- [Capture and routing reference](references/capture-and-routing.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown retrospective with findings, prioritized improvements, and skill-audit proposals]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May propose durable project or cross-project learnings; memory writes require existing authorization or approval of specific items.]

## Skill Version(s):

5.1.2 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
