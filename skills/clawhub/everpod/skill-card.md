## Description:

Helps an agent connect to Everpod to start and check cloud pods, set up a developer pod, or guide a move to a managed OpenClaw pod.

This skill is ready for commercial/non-commercial use.

## Publisher:

[everpod](https://clawhub.ai/user/everpod)

### License/Terms of Use:

MIT-0

## Use Case:

Owners and developers use this skill to have an agent create or check Everpod cloud pods, prepare a developer pod, or guide migration of an OpenClaw agent to a managed pod.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: An Everpod API key grants access to pod details and can start new pods.

Mitigation: Keep the key private and revoke it when no longer needed.

Risk: A migration archive may contain personal memory, notes, workspace files, skills, and scheduled-job details.

Mitigation: Review the archive before uploading and exclude passwords and API keys.

Risk: Creating a pod can lead to a paid monthly subscription.

Mitigation: Start pods only on owner request; the owner reviews the price and completes payment themselves.

## Reference(s):

- [Everpod API documentation](https://everpod.ai/docs/api)
- [Everpod skill on ClawHub](https://clawhub.ai/everpod/skills/everpod)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Files]

**Output Format:** [Markdown guidance and optional ZIP archive for migration]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May provide pod status and payment or setup links; migration archives require owner review.]

## Skill Version(s):

1.1.1 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
