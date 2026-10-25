## Description:

Reviews agent sessions and skill use to identify evidence-backed lessons and prioritized improvements.

This skill is ready for commercial/non-commercial use.

## Publisher:

[iliaal](https://clawhub.ai/user/iliaal)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use this skill to review a session, audit skills used, and propose concrete improvements grounded in available evidence.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A remember: request may cause the agent to persist text the user did not intend to retain long term.

Mitigation: Review the proposed memory content and authorize persistence only for the specific items you want saved.

Risk: Sensitive credential values could be carried into lasting memory notes.

Mitigation: Exclude credential values from any saved note; retain only a variable name or safe location reference.

## Reference(s):

- [ia-reflect on ClawHub](https://clawhub.ai/iliaal/skills/compound-eng-reflect)
- [Capture and remedy routing](references/capture-and-routing.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown retrospective with prioritized improvement proposals]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Cites reviewed evidence and its limits; memory updates require prior authorization or approval of specific items.]

## Skill Version(s):

5.1.2 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
