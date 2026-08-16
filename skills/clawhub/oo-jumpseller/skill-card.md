## Description:

Jumpseller (jumpseller.com). Use this skill for ANY Jumpseller request - reading, creating, and updating data. Whenever a task involves Jumpseller, use this skill instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to manage Jumpseller store data through the OOMOL oo CLI connector, including store information, products, categories, customers, and orders. It supports read, search, create, and update workflows with confirmation required for state-changing actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can create or update Jumpseller products, categories, customers, and orders.

Mitigation: Review the exact payload and expected effect with the user before approving any write action.

Risk: The skill may require installing the OOMOL oo CLI before use.

Mitigation: Run the CLI installer only when the user trusts OOMOL's installation source and the tool is required for the requested workflow.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-jumpseller)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [Jumpseller homepage](https://jumpseller.com)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance, Configuration instructions]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [State-changing Jumpseller actions require user confirmation before execution.]

## Skill Version(s):

1.0.0 (source: release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
