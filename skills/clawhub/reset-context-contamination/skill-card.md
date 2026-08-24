## Description:

Discards accumulated drafts and framings from a thread, then re-derives the task from a clean problem statement when the user asks for a reset or fresh take.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tenequm](https://clawhub.ai/user/tenequm)

### License/Terms of Use:

Apache 2.0

## Use Case:

Agents and their users use this skill to recover from stale, circular, or contaminated conversation framing by extracting durable facts and re-deriving the task from a cleaner brief. For deep contamination or high-stakes work, the skill directs the agent to hand the brief to a fresh context instead of attempting an in-thread reset.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad activation wording may reset conversation framing when the user intended only a casual fresh perspective.

Mitigation: Use narrower trigger wording or ask for confirmation before applying the reset in ambiguous cases.

Risk: In deep contamination or high-stakes work, an in-thread reset may preserve flawed assumptions from the existing conversation.

Mitigation: Extract only durable facts and constraints, then hand the brief to a fresh context or recommend a new session.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/tenequm/skills/reset-context-contamination)
- [Metadata Homepage](https://github.com/tenequm/skills/tree/main/skills/reset-context-contamination)

## Skill Output:

**Output Type(s):** [Text, Guidance]

**Output Format:** [Markdown or plain-language guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [No code execution, shell commands, data access, or generated files are required by the skill.]

## Skill Version(s):

0.1.3 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
