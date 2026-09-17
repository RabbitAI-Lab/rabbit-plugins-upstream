## Description:

Givebutter supports searching and reading Givebutter data through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to retrieve Givebutter campaigns, chapters, contacts, funds, recurring plans, and transactions through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup guidance includes remote installer commands for the oo CLI.

Mitigation: Install the oo CLI only from trusted OOMOL sources, and prefer a verified or package-manager installation path when available.

Risk: The skill routes broad Givebutter requests through an OOMOL-connected account.

Mitigation: Review the requested Givebutter action and payload before allowing account data access or changes.

## Reference(s):

- [ClawHub Givebutter Skill](https://clawhub.ai/oomol/skills/oo-givebutter)
- [Givebutter Homepage](https://givebutter.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May call Givebutter actions through the oo CLI and return JSON response data when requested.]

## Skill Version(s):

1.0.2 (source: frontmatter and server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
