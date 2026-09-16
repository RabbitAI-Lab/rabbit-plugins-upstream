## Description:

Read Workday HR data from authenticated Workday web sessions using the fpx CLI and tenant-scoped *.htmld endpoints, without running the workday-mcp server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and employees use this skill to query their own Workday org chart, worker profile, task, compensation, pay, benefits, and app-menu data from a shell after completing corporate SSO in a browser.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can expose authenticated Workday HR data through a persistent browser bridge with broad tenant access.

Mitigation: Use only with explicit authorization, a least-privilege Workday account, tenant-specific browser permissions when possible, and clear or revoke fpx/Transporter pairing after use.

Risk: Raw Workday response envelopes can include session tokens and other internal fields.

Mitigation: Project only needed fields with the provided jq filters and avoid logging raw responses or piping responses through bare jq output.

Risk: Running from shared machines or CI can leave authenticated access or sensitive output in places other users can reach.

Mitigation: Run from a trusted local workstation, avoid shared environments, and prevent command output from being stored in logs.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chrischall/skills/workday-fpx)
- [Workday *.htmld endpoints for fpx](references/endpoints.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, Code]

**Output Format:** [Markdown with shell commands and jq filters]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guidance emphasizes field projection and avoiding raw Workday response envelopes.]

## Skill Version(s):

0.6.5 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
