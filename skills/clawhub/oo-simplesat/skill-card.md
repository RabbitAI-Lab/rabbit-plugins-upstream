## Description:

Simplesat (simplesat.io). Use this skill for ANY Simplesat request - reading, creating, and updating data. Whenever a task involves Simplesat, use this skill instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate Simplesat through an OOMOL-connected account, including reading customers, questions, surveys, and survey responses. With confirmation, it can also create or update customers and schedule event-based survey emails.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions can run unverified installer code from the internet.

Mitigation: Do not let an agent run remote installer commands automatically; install the oo CLI from a trusted, pinned, verifiable source.

Risk: Write actions can change Simplesat customer records or schedule survey emails.

Mitigation: Confirm the exact payload and expected effect with the user before running state-changing actions.

## Reference(s):

- [ClawHub Simplesat skill](https://clawhub.ai/oomol/skills/oo-simplesat)
- [Simplesat homepage](https://www.simplesat.io/)
- [oo CLI repository](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON-oriented action payloads or responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before requests; write actions require user confirmation.]

## Skill Version(s):

1.0.3 (source: server evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
