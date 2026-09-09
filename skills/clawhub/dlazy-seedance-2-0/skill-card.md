## Description:

Video generation skill for Seedance 2.0 that supports text-to-video, first/last-frame generation, and multimodal image, video, and audio references.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and creators use this skill to call the dLazy Seedance 2.0 video-generation service from an agent workflow, passing prompts and optional media references to generate video assets.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill relies on the pinned external @dlazy/cli npm package and the dLazy hosted service.

Mitigation: Install only if comfortable trusting that package and service; prefer npx or a least-privilege environment and review the linked package or source before use.

Risk: Prompts and local image, video, or audio files passed to the CLI are sent to dLazy endpoints for processing.

Mitigation: Only submit media intended for upload to dLazy, and avoid sensitive or unauthorized content.

Risk: The dLazy API key is stored locally or supplied through DLAZY_API_KEY.

Mitigation: Keep the key protected and rotate or revoke it if exposure is suspected.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-seedance-2-0)
- [dLazy CLI homepage and source link from metadata](https://github.com/dlazy-ai/cli)
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, JSON, Files]

**Output Format:** [Markdown guidance with bash commands and JSON CLI responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return generated media URLs or download files when --save is used; asynchronous mode returns a task ID for polling.]

## Skill Version(s):

1.3.12 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
