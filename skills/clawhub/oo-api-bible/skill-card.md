## Description:

API.Bible (scripture.api.bible) helps agents search and read Bible data through the OOMOL-connected API.Bible connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to retrieve verses, passages, chapters, Bible metadata, and scripture search results from API.Bible without calling the API directly.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include one-line remote installer commands for the oo CLI.

Mitigation: Review installer commands before execution and install the oo CLI only through a trusted, verifiable method.

Risk: Authentication and account-connection steps may open user account flows.

Mitigation: Run login or connection steps only after a command fails for that reason, and have the user confirm account access themselves.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-api-bible)
- [API.Bible Homepage](https://scripture.api.bible/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, API Calls, JSON, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON request or response examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live action schemas before constructing JSON payloads; API responses include data and execution metadata.]

## Skill Version(s):

1.0.3 (source: server evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
