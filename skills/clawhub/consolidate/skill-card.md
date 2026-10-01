## Description:

Consolidates external PR and issue feedback into classified findings, review summaries, and next-step decisions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[drumrobot](https://clawhub.ai/user/drumrobot)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and maintainers use this skill to collect and assess PR or issue review feedback, publish a review summary and formal review, and decide how to handle remaining findings.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow can post or update GitHub reviews and comments with the agent's write authority.

Mitigation: Grant review access only when needed and prefer explicit interactive approval before posting.

Risk: Installing dependencies or registering hooks can change the local environment.

Mitigation: Pin installation sources and review any hook registration before use.

Risk: PR branch metadata may be used in unsafe checkout commands on untrusted branches.

Mitigation: Avoid untrusted PR branches until branch, base, and worktree paths are validated and quoted.

## Reference(s):

- [Consolidate on ClawHub](https://clawhub.ai/drumrobot/skills/consolidate)
- [Superpowers review primitives](https://github.com/obra/superpowers)

## Skill Output:

**Output Type(s):** [Markdown, Guidance]

**Output Format:** [Markdown review findings, PR comments, and next-step guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May publish review comments and summaries to GitHub.]

## Skill Version(s):

0.7.0 (source: skill frontmatter and server release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
