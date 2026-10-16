## Description:

Helps agents read and manage an authorized Bilibili account's videos, articles, and anthologies through OOMOL.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

People managing a connected Bilibili account can use this skill to inspect profiles and content, review engagement, and create, edit, or remove videos, articles, and anthologies.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup fallback suggests running unverified remote installer scripts.

Mitigation: Review official installation instructions, pin and verify the CLI release, and do not allow automatic execution of remote installers.

Risk: Publishing, editing, or deleting Bilibili content can change or permanently remove account data.

Mitigation: Check the exact target and payload with the user and obtain explicit approval before write or delete actions.

## Reference(s):

- [Bilibili skill release on ClawHub](https://clawhub.ai/oomol/skills/oo-bilibili)
- [OOMOL CLI installation guide](https://cli.oomol.com/install-guide.md)
- [Bilibili](https://www.bilibili.com)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Text or Markdown summaries and action guidance; JSON results from connector commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Write and delete actions can change or permanently remove account content.]

## Skill Version(s):

1.0.0 (source: skill frontmatter and ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
