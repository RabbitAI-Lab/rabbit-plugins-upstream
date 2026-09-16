## Description:

This skill helps agents search and read Cin7 Core account, customer, and product data through the OOMOL-connected `oo` CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, operators, and business users use this skill to inspect live Cin7 Core action schemas and read connected account, customer, and product data through the OOMOL `oo` CLI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Inline remote installer commands can execute unreviewed setup code.

Mitigation: Prefer a verified package or official installation flow, or review the installer before running it.

Risk: The allowed OOMOL CLI access is broader than the documented read-only Cin7 Core purpose.

Mitigation: Keep use limited to documented `cin7_core` schema and run actions, and watch for `oo` commands outside those actions.

## Reference(s):

- [Cin7 Core homepage](https://www.cin7.com/solutions/core/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-cin7-core)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before constructing requests; documented actions are read-oriented account, customer, and product operations.]

## Skill Version(s):

1.0.3 (source: skill frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
