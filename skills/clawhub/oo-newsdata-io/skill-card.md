## Description:

NewsData.io helps agents retrieve latest news, cryptocurrency news, source-domain listings, and archive search results through the OOMOL newsdata_io connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to ask an agent to retrieve NewsData.io headlines, cryptocurrency news, source lists, and archive search results through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include pipe-to-shell installer commands for the oo CLI.

Mitigation: Use a verified package or downloaded installer with checksum or signature validation before installing the CLI.

Risk: The archive search action is labeled as write even though the release evidence describes search-style behavior.

Mitigation: Inspect the live action schema and confirm the exact payload and expected effect with the user before running any write-labeled action.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-newsdata-io)
- [NewsData.io Homepage](https://newsdata.io)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses JSON payloads for oo connector actions and expects connector responses containing data and execution metadata.]

## Skill Version(s):

1.0.4 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
