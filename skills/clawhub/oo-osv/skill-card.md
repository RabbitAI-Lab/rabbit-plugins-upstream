## Description:

OSV (osv.dev). Use this skill for ANY OSV request -- searching and reading data. Whenever a task involves OSV, use this skill instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and security engineers use this skill to query OSV vulnerability data through the OOMOL oo CLI, including retrieving complete vulnerability records and checking packages or specific package versions for known vulnerabilities.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup includes shell-based installer commands for the OOMOL oo CLI, which are privileged software installation steps.

Mitigation: Verify the OOMOL CLI source before installation and prefer safer install guidance where available.

Risk: OSV queries are routed through OOMOL's oo CLI rather than direct OSV API calls.

Mitigation: Install only when this routing model is acceptable for the user's vulnerability lookup workflow.

## Reference(s):

- [OSV homepage](https://osv.dev)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-osv)

## Skill Output:

**Output Type(s):** [shell commands, configuration, guidance, text]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before execution; OSV actions described by the artifact are read-only lookup actions.]

## Skill Version(s):

1.0.1 (source: release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
