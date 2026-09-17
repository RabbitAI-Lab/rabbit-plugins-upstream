## Description:

Benzinga (benzinga.com). Use this skill for Benzinga requests involving searching and reading data through the OOMOL Benzinga connector instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to retrieve Benzinga market data through an OOMOL-connected account, including analyst ratings, earnings calendar entries, consensus ratings, price targets, and news channel lists.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include remote installer commands that can execute code on the user's machine.

Mitigation: Install the oo CLI only from reviewed official instructions, verify the installer source, and avoid running pasted installer commands blindly.

Risk: The skill relies on OOMOL as the broker for Benzinga access.

Mitigation: Use the skill only when comfortable with OOMOL-mediated credential handling and connect Benzinga intentionally through the OOMOL account.

Risk: Live connector schemas and credentials may be unavailable, expired, or missing required scopes.

Mitigation: Inspect the action schema before each payload and perform login or connection repair only after an auth or connection error.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-benzinga)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [Benzinga Homepage](https://www.benzinga.com/)
- [OOMOL CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill instructs the agent to inspect live connector schemas before execution and to return connector results from the oo CLI.]

## Skill Version(s):

1.0.3 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
