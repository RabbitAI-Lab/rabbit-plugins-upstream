## Description:

BoloForms (boloforms.com). Use this skill for ANY BoloForms request - reading, creating, and updating data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate BoloForms through an OOMOL-connected account, including listing documents and form responses, checking signing participants, and sending templates for signing after confirmation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions can involve unverified remote installer scripts with broad local execution power.

Mitigation: Review the installer source and prefer a signed, versioned, checksum-verified oo CLI installation before using the skill.

Risk: The send_template_for_signing action changes BoloForms state by starting a signing request.

Mitigation: Confirm the exact recipients, template, and payload with the user before allowing the action to run.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-boloforms)
- [BoloForms homepage](https://www.boloforms.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance]

**Output Format:** [Markdown instructions with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live oo connector schemas and returns oo CLI JSON responses when actions run.]

## Skill Version(s):

1.0.3 (source: release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
