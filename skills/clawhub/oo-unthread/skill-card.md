## Description:

Unthread helps agents operate Unthread through the OOMOL-connected oo CLI for account reading, creation, listing, updates, and deletion.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and support teams use this skill to manage Unthread external customer accounts through OOMOL's connector workflow. It supports reading account data and performing confirmed create, update, and delete actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions can execute remote installer scripts directly during oo CLI installation.

Mitigation: Review the setup path before installing, prefer a verified and versioned release or package manager, and avoid piping remote scripts directly into a shell.

Risk: Write and destructive Unthread account actions can change or permanently delete customer account data.

Mitigation: Inspect the live action schema, confirm exact payloads and effects before write actions, and require explicit approval before delete actions.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-unthread)
- [OOMOL Publisher Profile](https://clawhub.ai/user/oomol)
- [Unthread Homepage](https://unthread.io/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, Guidance, JSON]

**Output Format:** [Markdown guidance with shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [State-changing actions require user confirmation; destructive delete actions require explicit approval.]

## Skill Version(s):

1.0.3 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
