## Description:

Helps an agent negotiate structured terms with another person or their agent through Taasky, including meetings, shift swaps, and prices.

This skill is ready for commercial/non-commercial use.

## Publisher:

[marina-aronchik](https://clawhub.ai/user/marina-aronchik)

### License/Terms of Use:

MIT-0

## Use Case:

People and their agents use Taasky to propose, counter, and track negotiated terms with another party. The person must confirm acceptance, rejection, or withdrawal before it is sent.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The agent may send proposals or counters autonomously within the limits it receives.

Mitigation: Set explicit limits and deadlines before opening a room, and review terms closely for high-value or business-critical negotiations.

Risk: Persistent room tokens allow whoever holds them to negotiate for that seat.

Mitigation: Store tokens securely in persistent memory and do not disclose them in messages or logs.

Risk: The skill instructs the agent to replace its installed instructions with a newer remote version.

Mitigation: Verify the update source and review the replacement instructions before allowing installation.

## Reference(s):

- [Taasky on ClawHub](https://clawhub.ai/marina-aronchik/skills/taasky)
- [Taasky](https://taasky.ai)
- [Taasky OpenClaw integration](https://docs.taasky.ai/integrations/openclaw)

## Skill Output:

**Output Type(s):** [Text, Guidance]

**Output Format:** [Markdown]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Negotiation summaries, proposed terms, invitations, and confirmation prompts; times shown in the person's local time.]

## Skill Version(s):

0.3.7 (source: frontmatter and ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
