## Description:

Operate Shotstack through an OOMOL-connected account to inspect render status, retrieve output URLs, and submit asynchronous media render jobs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to work with Shotstack render workflows through an OOMOL-connected account. It helps agents inspect live connector schemas, check render status and output URLs, and submit render jobs after user confirmation for write actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup guidance includes remote installer commands for the oo CLI.

Mitigation: Avoid running remote installer commands unless the installation source has been independently trusted and verified.

Risk: Shotstack payloads and responses are routed through OOMOL.

Mitigation: Use the skill only when that routing is acceptable for the data and workflow involved.

Risk: The render_edit action can create asynchronous media render jobs.

Mitigation: Confirm the exact payload and expected effect with the user before allowing the write action.

## Reference(s):

- [ClawHub Shotstack skill page](https://clawhub.ai/oomol/skills/oo-shotstack)
- [Shotstack homepage](https://shotstack.io)
- [oo CLI](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [Text, Shell commands, JSON responses, Configuration guidance]

**Output Format:** [Markdown with inline shell commands and JSON response summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Write actions require confirmation of the exact payload and expected effect before execution.]

## Skill Version(s):

1.0.2 (source: server release metadata and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
