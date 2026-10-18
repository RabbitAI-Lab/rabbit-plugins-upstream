## Description:

Helps an agent negotiate structured terms with another person or agent through Taasky, including scheduling, prices, and other agreements.

This skill is ready for commercial/non-commercial use.

## Publisher:

[marina-aronchik](https://clawhub.ai/user/marina-aronchik)

### License/Terms of Use:

MIT-0

## Use Case:

People using an agent can delegate negotiations about meeting times, services, shifts, or prices, with their boundaries supplied in advance and their confirmation required for final decisions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Stored room tokens permit later access to a negotiation room.

Mitigation: Keep room tokens private and never include them in messages or errors.

Risk: An agent may make proposals or counters on a person's behalf.

Mitigation: Provide clear boundaries, deadlines, and non-negotiables before delegating; review confirmation cards before approving an agreement.

## Reference(s):

- [Taasky documentation for OpenClaw](https://docs.taasky.ai/integrations/openclaw)
- [Taasky](https://taasky.ai)
- [Taasky ClawHub release](https://clawhub.ai/marina-aronchik/skills/taasky)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Conversational text with proposed terms, negotiation updates, and confirmation links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Final acceptance, rejection, and withdrawal require human confirmation.]

## Skill Version(s):

0.3.5 (source: ClawHub release and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
