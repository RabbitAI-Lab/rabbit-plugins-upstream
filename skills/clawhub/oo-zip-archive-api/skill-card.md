## Description:

Zip Archive API helps agents operate archiveapi.com through the OOMOL oo CLI to compress publicly accessible files into ZIP archives and extract public archives through transit storage.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and agents use this skill to inspect Zip Archive API action schemas, compress publicly accessible files into ZIP archives, and extract public archives through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Extract operations can create extracted files through transit storage.

Mitigation: Confirm the exact payload and intended effect with the user before running the write-tagged extract_archive action.

Risk: The skill depends on the OOMOL oo CLI, a signed-in OOMOL account, a connected Zip Archive API account, and available billing credit.

Mitigation: Install and connect the service only when needed, and resolve auth, connection, scope, credential, or billing errors before retrying.

Risk: Connector input contracts may change over time.

Mitigation: Fetch the live connector schema before each action and build payloads to match the returned schema.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-zip-archive-api)
- [Zip Archive API homepage](https://archiveapi.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, API Calls, JSON, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before actions and routes credentials through OOMOL-managed connections.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
