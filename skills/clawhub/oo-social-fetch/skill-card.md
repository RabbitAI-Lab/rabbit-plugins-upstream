## Description:

Social Fetch enables agents to search and read Social Fetch data through the OOMOL `social_fetch` connector instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to retrieve Social Fetch account status, credit or billing state, and public social profiles or channels through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The connector can read account and billing information from the connected Social Fetch account.

Mitigation: Install and use the skill only when the user trusts OOMOL and Social Fetch with that account and billing information.

Risk: First-time setup or reconnection commands may change authentication state or service connections.

Mitigation: Run install, login, or connection steps only when needed to set up the oo CLI or recover from an authentication or connection failure.

## Reference(s):

- [Social Fetch homepage](https://www.socialfetch.dev)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before execution and returns Social Fetch connector responses as JSON when actions run.]

## Skill Version(s):

1.0.0 (source: skill metadata and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
