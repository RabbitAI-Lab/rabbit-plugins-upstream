## Description:

Zendesk (zendesk.com). Use this skill for ANY Zendesk request: reading, creating, and updating data through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and support operators use this skill to let an agent retrieve Zendesk tickets, users, and organizations, and to create, reply to, or update tickets through the oo CLI after the account connection is configured.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include unverified remote installer commands that can execute changing external code on a user's machine.

Mitigation: Prefer installing the oo CLI through a verified, pinned, or signed method before using the skill.

Risk: Write actions can create, reply to, or update Zendesk tickets.

Mitigation: Confirm the exact payload and intended effect with the user before running Zendesk write actions.

## Reference(s):

- [ClawHub Zendesk skill page](https://clawhub.ai/oomol/skills/oo-zendesk)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [Zendesk homepage](https://www.zendesk.com)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Agent should inspect the live connector schema before building action payloads.]

## Skill Version(s):

1.0.3 (source: server release metadata and skill frontmatter metadata.version)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
