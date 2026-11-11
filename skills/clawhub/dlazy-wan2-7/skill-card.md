## Description:

Tongyi Wanxiang 2.7 video generation for text-to-video, first/last-frame-to-video, and reference-to-video workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to generate videos from text prompts, first and last frames, or reference images and videos through dLazy's hosted service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security scan could not verify the referenced CLI package or establish how its login flow relates to video generation; coverage is incomplete and confidence is medium.

Mitigation: Review the CLI authentication flow and dLazy service details before installing or entering credentials.

Risk: Prompts and local reference media are sent to dLazy-hosted services, so submitted material may leave the user's environment.

Mitigation: Submit only prompts and assets you are authorized to share with dLazy, and review the service terms.

## Reference(s):

- [ClawHub release](https://clawhub.ai/dlazyai/skills/dlazy-wan2-7)
- [dLazy service](https://dlazy.com)
- [dLazy CLI package on npm](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Video, JSON]

**Output Format:** [Hosted video asset URLs with JSON result or asynchronous task metadata]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can return a task ID when asynchronous mode is requested.]

## Skill Version(s):

1.3.38 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
