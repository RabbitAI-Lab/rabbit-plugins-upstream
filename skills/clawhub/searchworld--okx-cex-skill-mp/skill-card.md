## Description:

Helps agents search, install, update, remove, and verify AI trading skills from the OKX Skills Marketplace using the okx CLI or limited MCP alternatives.

This skill is ready for commercial/non-commercial use.

## Publisher:

[searchworld](https://clawhub.ai/user/searchworld)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to browse and manage marketplace skills for trading assistants, including installation, updates, downloads, removal, and signature verification.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installing marketplace skills can add third-party instructions to local agent environments with broad agent permissions.

Mitigation: Review each skill's SKILL.md before installation and install only from trusted publishers.

Risk: Mutable installation paths, npm or npx execution, and force-install behavior can weaken source and signature assurance.

Mitigation: Use pinned package versions, avoid elevated privileges, and do not use --force unless the package source and contents have been independently verified.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/searchworld/skills/okx-cex-skill-mp)
- [OKX homepage](https://www.okx.com)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with CLI commands and configuration guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include JSON-output options when the skill directs use of okx command flags.]

## Skill Version(s):

1.4.6 (source: server evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
