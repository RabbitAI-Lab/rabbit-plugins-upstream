## Description:

Helps an agent set up and manage Everpod cloud computers, and prepare a move to a persistent OpenClaw pod.

This skill is ready for commercial/non-commercial use.

## Publisher:

[everpod](https://clawhub.ai/user/everpod)

### License/Terms of Use:

MIT-0

## Use Case:

Everpod customers and their agents use this skill to start or check cloud pods, help owners connect to them, and prepare an existing agent for migration.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The Everpod key can list and start pods in the owner's account.

Mitigation: Share the key only if comfortable with those permissions, keep it private, and revoke it after migration if no longer needed.

Risk: Migration may transfer private workspace files, memory, notes, skills, and scheduled-job details.

Mitigation: Review the zip before transfer; exclude secrets, private notes, unrelated data, and scheduled-job destinations that should not move.

## Reference(s):

- [Everpod API documentation](https://everpod.ai/docs/api)
- [Everpod skill on ClawHub](https://clawhub.ai/everpod/skills/everpod)

## Skill Output:

**Output Type(s):** [Text, Guidance, Shell commands]

**Output Format:** [Markdown with links and inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Pod status and payment links when available]

## Skill Version(s):

1.1.6 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
