## Description:

Dev.to (dev.to). Use this skill for ANY Dev.to request - reading, creating, and updating data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to operate Dev.to through an OOMOL-connected account, including reading articles, users, organizations, tags, and videos, and creating or updating Dev.to articles after confirming write payloads.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include direct execution of remote installer scripts.

Mitigation: Review the setup path before installing, prefer an official versioned or verifiable oo CLI installation method, and avoid letting an agent run the remote installer automatically.

Risk: The skill can create or update Dev.to articles through write actions.

Mitigation: Confirm exact payloads and expected effects with the user before running article creation or update actions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-devto)
- [Publisher profile](https://clawhub.ai/user/oomol)
- [Dev.to homepage](https://dev.to)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [Skill icon](https://static.oomol.com/logo/third-party/devto.svg)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce Dev.to connector commands and schema-shaped JSON for read and write actions.]

## Skill Version(s):

1.0.3 (source: server evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
