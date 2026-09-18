## Description:

Userlist connector skill for reading, creating, and updating Userlist data through the OOMOL-connected oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to inspect Userlist action schemas and run OOMOL-connected Userlist connector actions for users, companies, relationships, events, and transactional messages.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Write actions can create or update Userlist users, companies, relationships, events, and transactional messages.

Mitigation: Confirm the target, payload, and intended effect before running create_event, push_company, push_relationship, push_user, or send_message actions.

Risk: The setup guidance includes remote installer commands using curl-to-shell or PowerShell invoke-expression patterns.

Mitigation: Use those installer commands only after independently trusting and verifying the OOMOL installer source, or install the oo CLI through a trusted platform-specific path.

## Reference(s):

- [ClawHub Userlist skill page](https://clawhub.ai/oomol/skills/oo-userlist)
- [Userlist homepage](https://userlist.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance, Configuration]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses oo CLI connector schemas before constructing action payloads; write actions can change Userlist records.]

## Skill Version(s):

1.0.3 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
