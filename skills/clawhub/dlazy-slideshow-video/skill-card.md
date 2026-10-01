## Description:

Turns slides and documents into narrated slideshow videos with voiceover and transitions using dLazy.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators, educators, and business users turn presentations, reports, and other documents into narrated explainer or training videos through the dLazy service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Attached documents and prompts are sent to an external dLazy service.

Mitigation: Only attach documents approved for external processing and review what the prompt discloses.

Risk: The external CLI requires a dLazy API key and may save it locally.

Mitigation: Review the CLI before installing and protect or rotate the API key as needed.

## Reference(s):

- [dLazy CLI repository (linked in skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Video generation guidance]

**Output Format:** [Streamed text from the dLazy CLI]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The hosted service produces narrated slideshow videos; attached local files are uploaded to dLazy storage.]

## Skill Version(s):

1.0.20 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
