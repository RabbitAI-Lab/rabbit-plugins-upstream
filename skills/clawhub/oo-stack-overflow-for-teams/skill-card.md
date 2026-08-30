## Description:

Stack Internal (stackoverflow.co). Use this skill for ANY Stack Internal request - searching and reading data through the OOMOL Stack Overflow for Teams connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Employees and developers use this skill to search and read Stack Internal team questions, answers, tags, and current user information through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The agent can query Stack Internal team content through OOMOL when a request is broad or ambiguous.

Mitigation: Use this skill only when Stack Internal access is intended, and scope requests to the specific team content needed.

Risk: Setup commands connect an account and rely on OOMOL-provided CLI and server-side credentials.

Mitigation: Run install, login, and connection steps only after confirming that OOMOL is trusted and the target account should be connected.

Risk: Connector responses may contain internal questions, answers, tags, or user details.

Mitigation: Review retrieved content before sharing it outside the intended team or workflow.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-stack-overflow-for-teams)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)
- [Stack Internal homepage](https://stackoverflow.co/internal/)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schema inspection before forming action payloads; connector responses are JSON when run with --json.]

## Skill Version(s):

1.0.0 (source: server evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
