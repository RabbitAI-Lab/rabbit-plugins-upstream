## Description:

Higgsfield AI (higgsfield.ai). Use this skill for ANY Higgsfield AI request: reading, creating, and updating data through the OOMOL-connected oo CLI instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to operate Higgsfield AI from an agent session, including submitting image or video generation requests, checking request status, and cancelling queued requests.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup includes remote shell installer commands that execute code from OOMOL-controlled endpoints.

Mitigation: Review the setup source before installation, prefer a documented and verifiable oo CLI install path, and only run installer commands when the user trusts the endpoint.

Risk: Generation submission and cancellation actions can change Higgsfield AI account state or consume credits.

Mitigation: Confirm the exact action, payload, and expected effect with the user before running write or cancellation commands.

## Reference(s):

- [Higgsfield AI homepage](https://higgsfield.ai/)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-higgsfield-ai)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance, JSON]

**Output Format:** [Markdown with inline shell commands and JSON payloads or responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses oo connector schemas before actions and returns connector responses that may include request data and execution metadata.]

## Skill Version(s):

1.0.2 (source: release evidence and SKILL.md metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
