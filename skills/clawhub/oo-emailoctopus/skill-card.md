## Description:

EmailOctopus enables agents to read, create, update, and delete EmailOctopus campaigns, mailing lists, and contacts through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate EmailOctopus from an agent, including listing and retrieving campaigns, mailing lists, and contacts, and creating, updating, or deleting list contacts after appropriate confirmation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup asks users to run a mutable remote installer directly in a shell.

Mitigation: Review the oo CLI installation path before use, prefer a versioned official release or package-manager install, and verify checksums or signatures when available.

Risk: Write and destructive actions can change or delete EmailOctopus contact data.

Mitigation: Confirm the exact action, target, payload, and expected effect with the user before running write or delete commands.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-emailoctopus)
- [OOMOL Publisher Profile](https://clawhub.ai/user/oomol)
- [EmailOctopus Homepage](https://emailoctopus.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)
- [OOMOL EmailOctopus Connection](https://console.oomol.com/app-connections?provider=emailoctopus)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Agent commands should fetch live action schemas before execution and require explicit user confirmation for write or destructive EmailOctopus actions.]

## Skill Version(s):

1.0.3 (source: server release metadata and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
