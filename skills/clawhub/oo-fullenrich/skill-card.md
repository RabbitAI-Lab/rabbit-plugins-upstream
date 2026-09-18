## Description:

FullEnrich (fullenrich.com). Use this skill for any FullEnrich request, including searching and reading FullEnrich data through the OOMOL-connected oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to check FullEnrich workspace credit balance and perform company or person lookups through an OOMOL-connected FullEnrich account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup includes remote installer commands that pipe downloaded scripts directly into a shell.

Mitigation: Review the installer path and independently trust the OOMOL CLI installer before running those commands.

Risk: FullEnrich actions depend on an authenticated OOMOL-connected account and may expose business contact or enrichment data returned by the connector.

Mitigation: Run only the needed read action, inspect the live action schema before sending a payload, and handle returned data according to the workspace's data policies.

## Reference(s):

- [FullEnrich homepage](https://www.fullenrich.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-fullenrich)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return JSON data from FullEnrich connector actions when the oo CLI command is run.]

## Skill Version(s):

1.0.2 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
