## Description:

Ambee lets agents geocode locations and retrieve current, forecast, and historical air-quality data through an OOMOL-connected Ambee account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to search Ambee location data and retrieve current, forecast, or historical air-quality readings by place or coordinates through their connected OOMOL account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Fallback setup includes remote installer commands that pipe network scripts into a shell.

Mitigation: Review the installer path before use and prefer a verified, pinned, or signed oo CLI installation source before running Ambee lookups.

Risk: Authentication, connection, or billing failures can prevent Ambee lookups from running.

Mitigation: Perform login, connection, or recharge steps only after matching command failures, and rely on OOMOL server-side credential handling instead of handling raw Ambee tokens.

## Reference(s):

- [Ambee homepage](https://www.getambee.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schema inspection before action execution; Ambee action responses are JSON.]

## Skill Version(s):

1.0.3 (source: server release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
