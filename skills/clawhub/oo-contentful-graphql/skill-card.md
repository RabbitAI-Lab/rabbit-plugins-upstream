## Description:

Helps agents search and read Contentful GraphQL data through OOMOL's connected Contentful GraphQL connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to inspect the Contentful GraphQL connector schema and run read-oriented GraphQL queries against a specified Contentful space and environment through the oo CLI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup guidance includes one-line remote installer commands that can execute changing code on the user's machine.

Mitigation: Review OOMOL's installer delivery path before installation; prefer an official package manager or a downloaded, version-pinned installer with checksum or signature verification.

Risk: Connector use depends on a signed-in OOMOL account and a valid Contentful GraphQL connection.

Mitigation: Run authentication, connection, or billing setup only after a command fails with the matching error, and avoid handling raw Contentful tokens locally.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-contentful-graphql)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI Install Guide](https://cli.oomol.com/install-guide.md)
- [Contentful](https://www.contentful.com)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses the oo CLI to inspect connector schemas and run actions; command results may include JSON responses with execution metadata.]

## Skill Version(s):

1.0.3 (source: server release metadata and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
