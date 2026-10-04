## Description:

Turns documents into explainer, report, or training videos through dLazy's hosted service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators, educators, and teams use this skill to turn documents into narrated explainer, report, or training videos.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Attached documents and prompts are sent to dLazy's hosted service.

Mitigation: Only send files approved for use with dLazy; avoid confidential content without organizational authorization.

Risk: Using the service requires a dLazy API key.

Mitigation: Store the key using the CLI's authentication flow or protected configuration, and revoke it if exposed.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-doc-to-video)
- [dLazy CLI source (tool reference, not verified skill provenance)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Text, Guidance]

**Output Format:** [Text responses with project updates from the dLazy service]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated video is handled by the hosted service; attached files are uploaded to dLazy.]

## Skill Version(s):

1.0.22 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
