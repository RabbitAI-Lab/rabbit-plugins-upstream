## Description:

Runscope helps agents inspect live action schemas and retrieve Runscope account, bucket, test, environment, and test-result data through the OOMOL-connected oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to query Runscope API Monitoring resources through an OOMOL-connected account without handling raw Runscope tokens directly.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The first-time setup fallback documents piping a remote installer directly into a shell.

Mitigation: Do not let an agent run the installer automatically; install the oo CLI from a verified, versioned source after confirming files, permissions, and account connections.

Risk: Runscope read actions can return account, bucket, test, environment, and result data from the connected account.

Mitigation: Use the live action schema before each request and avoid exposing returned account or monitoring data beyond the user's intended task.

## Reference(s):

- [ClawHub Runscope skill page](https://clawhub.ai/oomol/skills/oo-runscope)
- [Runscope API Monitoring](https://www.blazemeter.com/api-monitoring)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration guidance, JSON]

**Output Format:** [Markdown guidance with shell commands and JSON connector responses.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector responses use a data object plus meta.executionId when actions run with --json.]

## Skill Version(s):

1.0.2 (source: server release metadata and skill frontmatter metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
