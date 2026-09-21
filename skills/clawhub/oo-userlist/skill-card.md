## Description:

Userlist (userlist.com). Use this skill for ANY Userlist request: reading, creating, and updating data through the OOMOL oo CLI instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to inspect Userlist connector schemas, create events, create or update users, companies, and relationships, and send transactional messages from an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup can ask an agent to run remote install scripts for the oo CLI.

Mitigation: Review the setup path before installation and prefer verified official packages or documented manual installation steps.

Risk: Write actions can create events, update Userlist records, or send transactional messages.

Mitigation: Fetch the live action schema and confirm the exact payload and intended effect before allowing write actions to run.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-userlist)
- [Userlist Homepage](https://userlist.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Configuration guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector responses include JSON data and metadata such as an executionId.]

## Skill Version(s):

1.0.4 (source: server release evidence and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
