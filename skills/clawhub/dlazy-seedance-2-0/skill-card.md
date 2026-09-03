## Description:

Seedance 2.0 helps agents invoke dLazy's hosted ByteDance video generation model for text-to-video, first/last-frame video, and multimodal reference-based video generation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to generate short videos through the dLazy CLI from prompts, reference images, videos, audio, or first/last frames.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses a third-party CLI to call a hosted video-generation service.

Mitigation: Review the @dlazy/cli source before global installation or use the pinned npx command for on-demand execution.

Risk: Prompts and referenced image, video, or audio files may be uploaded to dLazy endpoints for inference and storage.

Mitigation: Only provide media and prompts that are appropriate to upload to dLazy, and review generated hosted URLs before sharing.

Risk: The CLI stores or accepts a dLazy API key for authenticated requests.

Mitigation: Treat the key as a credential, prefer scoped organization keys, and rotate or revoke it from the dLazy dashboard when needed.

## Reference(s):

- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)
- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-seedance-2-0)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance, JSON, Files]

**Output Format:** [Markdown guidance with CLI commands and JSON result payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return hosted media URLs or download generated assets when --save is used.]

## Skill Version(s):

1.3.10 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
