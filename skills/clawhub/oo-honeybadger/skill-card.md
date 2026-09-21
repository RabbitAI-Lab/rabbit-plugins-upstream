## Description:

Honeybadger helps an agent inspect live connector schemas and run Honeybadger check-in, deployment, Insights event, and exception reporting actions through the OOMOL oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, operators, and support engineers use this skill to report Honeybadger check-ins, deployments, Insights events, and exception notices from an OOMOL-connected account. The skill is suited for agent-assisted Honeybadger operations where schemas are checked before action payloads are built.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup instructions include remote shell and PowerShell installer commands without checksum or signature verification.

Mitigation: Review the OOMOL CLI installation path first, prefer verified official documentation with pinned releases or checksum/signature verification, and do not let an agent run the installer automatically.

Risk: Honeybadger write actions can create operational records such as check-ins, deployments, events, and exception notices.

Mitigation: Fetch the live connector schema, show the exact payload and expected effect to the user, and get confirmation before running any write action.

## Reference(s):

- [ClawHub Honeybadger skill page](https://clawhub.ai/oomol/skills/oo-honeybadger)
- [Honeybadger homepage](https://www.honeybadger.io)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with oo CLI shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before constructing action payloads; write actions require user confirmation.]

## Skill Version(s):

1.0.4 (source: release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
