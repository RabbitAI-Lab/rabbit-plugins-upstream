## Description:

Use this skill to read, create, and update JobNimbus data through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and business operators use this skill to let an agent inspect live JobNimbus action schemas, then list, retrieve, create, or update contacts and jobs through the oo CLI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup may run installer scripts from OOMOL endpoints before using the connector.

Mitigation: Install only after trusting OOMOL's installer endpoint; prefer manually downloading and verifying the oo CLI installer before running it.

Risk: Write actions can create or update JobNimbus contacts and jobs.

Mitigation: Confirm the exact target, payload, and expected effect with the user before executing write actions.

## Reference(s):

- [JobNimbus homepage](https://www.jobnimbus.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [OOMOL JobNimbus connection](https://console.oomol.com/app-connections?provider=jobnimbus)

## Skill Output:

**Output Type(s):** [Shell commands, API Calls, Configuration instructions, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Responses from connector runs are JSON objects containing data and meta.executionId.]

## Skill Version(s):

1.0.4 (source: server release metadata and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
