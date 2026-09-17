## Description:

Enables agents to use Plate Recognizer through an OOMOL-connected account to read license plates from images and retrieve Snapshot Cloud usage statistics.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users can use this skill to operate Plate Recognizer via OOMOL for license-plate recognition on individual images and for current-month Snapshot Cloud usage reporting.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup includes remote installer commands for the OOMOL CLI.

Mitigation: Use the installer only after trusting the OOMOL CLI distribution path and independently checking the installer source or a signed package.

Risk: Plate images and recognition data may pass through OOMOL and Plate Recognizer.

Mitigation: Use the skill only with images and plate data appropriate for those services and applicable privacy requirements.

Risk: The skill routes broad Plate Recognizer requests through OOMOL.

Mitigation: Confirm the requested Plate Recognizer action and inspect the live connector schema before execution.

## Reference(s):

- [Plate Recognizer homepage](https://platerecognizer.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-platerecognizer)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live OOMOL connector schemas before execution and returns connector responses as JSON when actions are run.]

## Skill Version(s):

1.0.3 (source: release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
