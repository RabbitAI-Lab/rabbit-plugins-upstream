## Description:

TikHub (tikhub.io). Use this skill for ANY TikHub request - searching and reading data. Whenever a task involves TikHub, use this skill instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to inspect TikHub connector action schemas, run read-oriented TikHub searches and data retrieval through an OOMOL-connected account, and review TikHub endpoint pricing, metadata, account, and quota information.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Fallback setup may run a remote oo CLI installer script that has not been verified in the evidence.

Mitigation: Review the CLI installation path first and prefer installation from trusted OOMOL documentation with verification.

Risk: TikHub account information, API key metadata, usage data, or endpoint invocations may expose sensitive or billable activity.

Mitigation: Run only intended TikHub actions, inspect each live action schema before constructing payloads, and confirm scope-sensitive account or endpoint invocation requests.

## Reference(s):

- [TikHub homepage](https://tikhub.io/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-tikhub)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, Guidance, Text]

**Output Format:** [Markdown guidance with oo CLI commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Actions should be preceded by live schema inspection; connector responses include data and meta.executionId.]

## Skill Version(s):

1.0.4 (source: server release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
