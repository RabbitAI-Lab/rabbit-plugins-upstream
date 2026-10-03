## Description:

Guides employees in reading Workday HR data through their signed-in browser session using the fpx CLI, without running an MCP server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Employees use this skill to retrieve their accessible Workday profiles, organization details, tasks, pay, and benefits from a signed-in browser session for shell-based workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Sensitive HR information may pass through persistent third-party browser and CLI tooling.

Mitigation: Use only if organizational policy permits this access method, on a managed private machine; revoke extension pairing when finished.

Risk: Raw responses may expose confidential HR records or session tokens in terminal output and logs.

Mitigation: Request only necessary fields, project results before display, and avoid raw dumps and terminal or file logging.

## Reference(s):

- [Workday endpoint recipes](references/endpoints.md)
- [ContextMint Bridge extension releases](https://github.com/nullnet-app/contextmint-bridge/releases)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance]

**Output Format:** [Markdown with shell commands and jq filters]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Field-selected results; avoid exposing raw Workday response envelopes.]

## Skill Version(s):

1.1.5 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
