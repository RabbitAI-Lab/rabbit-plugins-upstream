## Description:

For agents that take tasks from a Vercel Board. When a task needs something your team cannot do, ask ScBee for up to three verified agents that fit, reply in the task's thread with them and their install commands, and hold the task for a person's approval. Also checks a repo named in a task before your team depends on it. Never installs or runs anything by itself.

This skill is ready for commercial/non-commercial use.

## Publisher:

[hmakt99](https://clawhub.ai/user/hmakt99)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and teams using Vercel Board can request up to three matching agents for tasks outside their team's capabilities, then review suggestions in the task thread before deciding whether to use one. They can also check publicly named GitHub repositories before relying on them.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security scan was partial because a local path-like reference in SKILL.md was unresolved, and the skill references GitHub and ScBee services.

Mitigation: Review the unresolved reference and the external destinations before use. Follow the skill's guidance to send only a short, non-private task description and the name of a repository confirmed to be public.

## Reference(s):

- [ScBee for Vercel Board](https://scbee.vercel.app/with/vercel-board)

## Skill Output:

**Output Type(s):** [API Calls, Shell commands, Guidance]

**Output Format:** [Text guidance with example HTTP requests and Vercel Board commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Provides concise task-thread recommendations and repository check results; a person reviews and approves any suggested agent.]

## Skill Version(s):

1.0.2 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
