## Description:

APIVoid helps agents run reputation checks for domains, IP addresses, and URLs, verify email addresses or domains, and retrieve account usage information.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to ask an agent for APIVoid-powered domain, IP, URL, email, and account checks without handling raw credentials directly.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Fallback setup guidance includes remote installer commands that could execute unreviewed code.

Mitigation: Review the skill before installing, and use an official, pinned, or separately downloaded and inspected OOMOL installer path before running setup commands.

## Reference(s):

- [ClawHub APIVoid Skill](https://clawhub.ai/oomol/skills/oo-api-void)
- [APIVoid Homepage](https://www.apivoid.com/)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL oo CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands return JSON from the APIVoid connector when run with --json.]

## Skill Version(s):

1.0.2 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
