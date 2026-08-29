## Description:

Unpaywall helps agents retrieve DOI metadata and search open-access articles by title through the OOMOL oo CLI connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to look up Unpaywall open-access article metadata by DOI or title while relying on OOMOL-managed credentials.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill depends on the OOMOL oo CLI and an OOMOL-connected Unpaywall account.

Mitigation: Install, authenticate, or reconnect only when the connector command fails for that specific reason.

Risk: Payloads can drift from the live connector contract.

Mitigation: Fetch the live action schema with `oo connector schema` before running a connector action.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-unpaywall)
- [Unpaywall Homepage](https://unpaywall.org/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector responses are JSON data returned by the oo CLI.]

## Skill Version(s):

1.0.0 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
