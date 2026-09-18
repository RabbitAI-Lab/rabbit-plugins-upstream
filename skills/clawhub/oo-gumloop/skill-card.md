## Description:

Gumloop (gumloop.com). Use this skill for Gumloop requests that read, create, or update data through the OOMOL-connected oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to inspect Gumloop schemas, list workbooks and saved flows, retrieve run history and details, start saved flow runs, and stop active runs through their connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include direct remote installer execution.

Mitigation: Use a verified oo CLI installation path and review the installer before running it.

Risk: State-changing Gumloop actions can start or stop flow runs.

Mitigation: Require explicit user confirmation for the exact payload and target before running start_flow_run or kill_flow_run.

## Reference(s):

- [Gumloop homepage](https://www.gumloop.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-gumloop)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live action schemas before constructing Gumloop connector payloads.]

## Skill Version(s):

1.0.2 (source: server evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
