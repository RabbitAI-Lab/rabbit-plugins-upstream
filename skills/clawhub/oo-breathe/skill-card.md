## Description:

Breathe lets agents search and read Breathe HR account, employee, department, and location data through an OOMOL-connected Breathe account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Agents use this skill to fulfill Breathe HR data requests by retrieving account, employee, department, and location information through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup includes remote installer commands that download scripts for shell execution.

Mitigation: Prefer an official signed or checksum-verified oo CLI installation path and review the installer before execution.

Risk: The skill accesses Breathe HR account and employee data through a connected account.

Mitigation: Use the skill only with trusted OOMOL and Breathe connections, and keep account permissions limited to the intended read-only use.

## Reference(s):

- [Breathe homepage](https://www.breathehr.com/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-breathe)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Responses may include connector JSON results with execution metadata.]

## Skill Version(s):

1.0.2 (source: server release metadata and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
