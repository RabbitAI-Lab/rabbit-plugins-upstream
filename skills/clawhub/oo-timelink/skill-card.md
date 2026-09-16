## Description:

timelink (timelink.io). Use this skill for ANY timelink request: searching and reading Timelink data through the OOMOL-connected oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to inspect Timelink clients, companies, projects, services, users, tokens, active time entries, and time entries from an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup path includes remote installer commands for the oo CLI.

Mitigation: Review installer snippets before use and prefer a trusted, verified release channel for installing the oo CLI.

Risk: The skill operates against Timelink data through an authenticated OOMOL-connected account.

Mitigation: Confirm authentication, connection status, billing state, and any state-changing action before execution.

## Reference(s):

- [timelink homepage](https://timelink.io)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-timelink)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before constructing action payloads.]

## Skill Version(s):

1.0.3 (source: server release metadata and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
