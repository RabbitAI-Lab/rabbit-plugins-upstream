## Description:

Kuaimai ERP helps agents search and read Kuaimai ERP data through the OOMOL-connected oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operations users use this skill to inspect Kuaimai ERP products, SKUs, inventory, orders, sales stockouts, shops, and warehouses from an OOMOL-connected account. It is intended for read-oriented ERP workflows and session refresh guidance when the connector requires it.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review flags unsafe remote installer commands in the setup guidance.

Mitigation: Avoid pipe-to-shell installer commands unless the OOMOL installer is independently trusted and verified; prefer reviewed installation methods.

Risk: The security review says the session refresh action is account or session changing and under-disclosed.

Mitigation: Treat refresh_session as requiring explicit user approval before execution.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-kuaimai)
- [Kuaimai ERP Homepage](https://www.kuaimai.com/)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before action execution; command output is returned as JSON from the oo CLI.]

## Skill Version(s):

1.0.0 (source: server release metadata and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
