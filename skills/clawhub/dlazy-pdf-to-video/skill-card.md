## Description:

Helps turn PDFs and other documents into narrated explainer, training, or presentation videos through dLazy's hosted service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators, educators, and teams use this skill to turn supplied PDFs or other documents into narrated explainer, report, courseware, or training videos.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and attached documents may be sent to dLazy's hosted service.

Mitigation: Review documents for sensitive content and confirm the hosted-service terms before uploading.

Risk: The CLI may store an API key locally.

Mitigation: Protect local credentials and rotate or revoke the key through dLazy when needed.

Risk: A global CLI install persists on the user's system.

Mitigation: Use the version-pinned npx option when a persistent global install is not wanted.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-pdf-to-video)
- [dLazy CLI homepage (release metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Text, Guidance, Shell commands]

**Output Format:** [Conversational text and project-based video creation guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Video generation uses dLazy's hosted service and requires an API key.]

## Skill Version(s):

1.0.25 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
