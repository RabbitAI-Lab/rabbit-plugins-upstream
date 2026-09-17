## Description:

OpenGraph.io helps agents extract webpage metadata, retrieve raw HTML, and capture configurable screenshots through an OOMOL-connected OpenGraph.io account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, operators, and agents use this skill to run OpenGraph.io webpage metadata extraction, raw HTML retrieval, site scraping, and screenshot capture actions through the oo CLI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Fallback setup guidance may lead an agent to suggest remote installer execution for the oo CLI.

Mitigation: Install oo from a verified OOMOL source, check signatures or checksums where available, and avoid running setup commands from an elevated shell.

Risk: Connector requests can fail or behave unexpectedly if action schemas, authentication, connection state, or billing state are stale.

Mitigation: Inspect the live action schema before constructing payloads and use setup or billing steps only after a matching command failure.

## Reference(s):

- [ClawHub OpenGraph.io Skill](https://clawhub.ai/oomol/skills/oo-opengraph-io)
- [OpenGraph.io Homepage](https://www.opengraph.io)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, JSON, Configuration, Guidance]

**Output Format:** [Markdown guidance with bash command examples and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Responses include action data and an execution identifier when returned by the connector.]

## Skill Version(s):

1.0.3 (source: metadata frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
