## Description:

Enables agents to inspect Shotstack action schemas, retrieve render details, and submit video, image, or audio render jobs through an OOMOL-connected Shotstack account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to inspect Shotstack action schemas, submit Shotstack render jobs through an OOMOL-connected account, and retrieve render status or output details.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Submitting a render_edit payload can affect the user's Shotstack account or billing.

Mitigation: Confirm the exact payload and expected effect with the user before running the write action.

Risk: The skill depends on an OOMOL-connected Shotstack account and one-time oo CLI or authentication setup.

Mitigation: Only perform setup after an auth or connection failure, and proceed only when the user trusts OOMOL and intends to connect Shotstack.

## Reference(s):

- [Shotstack homepage](https://shotstack.io)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-shotstack)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, JSON]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May submit Shotstack render jobs after user confirmation and return render IDs, status, output URLs, and execution metadata.]

## Skill Version(s):

1.0.0 (source: server release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
