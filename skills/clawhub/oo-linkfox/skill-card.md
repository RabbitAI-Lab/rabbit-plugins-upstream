## Description:

LinkFox helps agents use the OOMOL-connected LinkFox connector to inspect schemas and run actions for marketplace research, product analysis, advertising data, account reports, and IP or policy risk checks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to access LinkFox through an OOMOL-connected account for commerce research, product discovery, marketplace analytics, advertising reports, reviews, patent research, translations, and controlled write actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup guidance includes remote installer scripts that can be piped directly into a shell.

Mitigation: Review the oo CLI installation path first, prefer official installer documentation, verify checksums or signatures when available, and require explicit approval before executing any remote script.

Risk: Some actions can change LinkFox or connected commerce account state.

Mitigation: Confirm the exact payload and intended effect with the user before running write actions, and require explicit approval before any destructive action.

Risk: The skill can access connected marketplace, advertising, and account data.

Mitigation: Use the live action schema before each request and limit payloads to the minimum account, product, report, or marketplace data needed for the task.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-linkfox)
- [LinkFox Homepage](https://www.linkfox.com/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce LinkFox connector responses as JSON when actions are run.]

## Skill Version(s):

1.0.3 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
