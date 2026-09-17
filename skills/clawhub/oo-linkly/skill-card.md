## Description:

Operates Linkly through an OOMOL-connected account to read, create, update, and delete short links.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users with Linkly accounts use this skill to inspect connector schemas and manage Linkly short links from an agent workflow.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The optional one-time CLI installer commands execute remote shell or PowerShell installer code.

Mitigation: Use official package or release instructions where available, verify the source, and run installer commands only after review.

Risk: Write and destructive actions can change or delete Linkly short-link data.

Mitigation: Confirm the exact payload, target workspace, link identifier, and expected effect before approving write or delete operations.

Risk: The skill operates through OOMOL as the connector for the user's Linkly account.

Mitigation: Install and use the skill only when OOMOL is an acceptable connector for the account and review connection or authorization issues before retrying.

## Reference(s):

- [Linkly homepage](https://linklyhq.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline bash, PowerShell, text, and JSON snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands use the oo CLI and can return JSON responses from the Linkly connector.]

## Skill Version(s):

1.0.3 (source: server release metadata and SKILL.md frontmatter metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
