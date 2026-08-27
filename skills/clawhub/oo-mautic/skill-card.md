## Description:

Mautic helps agents read, create, update, and delete Mautic CRM data through an OOMOL-connected oo CLI connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to let an agent inspect Mautic connector schemas and perform approved CRM contact and segment operations through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Write actions can change Mautic CRM contact records or segment memberships.

Mitigation: Confirm the exact payload and expected effect with the user before running actions tagged as write.

Risk: Destructive actions can delete contacts or remove segment membership data.

Mitigation: Require explicit approval for the target contact or segment before running actions tagged as destructive.

Risk: The connector can access CRM data through the user's connected OOMOL account.

Mitigation: Install only when the user wants agent-managed Mautic access and use read actions directly only for get, list, or search tasks.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-mautic)
- [Mautic Homepage](https://mautic.org)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance, JSON]

**Output Format:** [Markdown with inline bash, PowerShell, text, and JSON snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill directs agents to inspect the live connector schema before building payloads and to request confirmation before write or destructive actions.]

## Skill Version(s):

1.0.0 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
