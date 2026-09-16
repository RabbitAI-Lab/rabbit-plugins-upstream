## Description:

Operates Honeybadger through an OOMOL-connected account to report check-ins, deployments, Insights events, and exception notices.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operations teams use this skill to submit Honeybadger monitoring reports through an OOMOL-connected account. It helps agents inspect live action schemas, construct JSON payloads, and run Honeybadger reporting actions through the oo CLI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security summary says the skill presents Honeybadger reporting actions as safe reads even though the available report actions submit monitoring data.

Mitigation: Treat every report_* action as a write and confirm the exact payload and expected effect with the user before execution.

Risk: The security guidance flags remote pipe-to-shell installer commands as unsafe unless independently verified.

Mitigation: Avoid running the installer commands directly from the skill; verify the installer source and integrity or use a reviewed installation method before installing the oo CLI.

Risk: The skill acts through the user's connected Honeybadger account.

Mitigation: Install and use it only when the user accepts that the agent can submit Honeybadger monitoring data through that account.

## Reference(s):

- [Honeybadger Homepage](https://www.honeybadger.io)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)
- [Honeybadger Skill on ClawHub](https://clawhub.ai/oomol/skills/oo-honeybadger)
- [Honeybadger Icon](https://static.oomol.com/logo/third-party/Honeybadger.svg)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before building requests; Honeybadger report actions submit data through the connected account.]

## Skill Version(s):

1.0.3 (source: server evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
