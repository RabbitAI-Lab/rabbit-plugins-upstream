## Description:

Kuaidi100 (kuaidi100.com) helps agents read, create, update, and delete Kuaidi100 logistics data through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate Kuaidi100 logistics workflows through an OOMOL-connected account, including tracking, carrier detection, price and time estimates, pickup order quotes, order creation, order lookup, and cancellations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup guidance can run remote installer scripts directly on the user's machine.

Mitigation: Prefer installing the oo CLI manually from a trusted source or verifying the installer before execution.

Risk: Write and cancellation actions can change or cancel Kuaidi100 pickup orders.

Mitigation: Check the exact payload and effect with the user before approving write actions, and require explicit approval for destructive cancellation actions.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-kuaidi100)
- [Kuaidi100 Homepage](https://www.kuaidi100.com/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands inspect live connector schemas before action payloads; write and destructive actions require user confirmation.]

## Skill Version(s):

1.0.4 (source: server evidence and frontmatter metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
