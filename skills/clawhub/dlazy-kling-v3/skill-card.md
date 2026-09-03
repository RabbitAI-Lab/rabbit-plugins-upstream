## Description:

Powerful video generation with Kling v3, supporting high-quality text-to-video and image-to-video workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to generate Kling v3 videos from text prompts and image inputs through the dLazy CLI and hosted API.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad trigger phrases can route generic video-generation requests to a paid third-party CLI.

Mitigation: Use the skill only for explicit dLazy/Kling v3 requests and consider dry-run review before submitting prompts, media, or paid jobs.

Risk: Prompts, media inputs, and generated outputs are processed by dLazy-hosted API and file services.

Mitigation: Avoid sending sensitive prompts or media unless uploading them to dLazy is acceptable for the user's use case.

Risk: Persistent API-key storage may create local credential exposure if config-file permissions are weaker than expected.

Mitigation: Prefer per-invocation DLAZY_API_KEY or npx where appropriate, and check permissions on ~/.dlazy/config.json when storing an API key locally.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-kling-v3)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Configuration, JSON, Files, Guidance]

**Output Format:** [Markdown guidance with bash commands and JSON command output; generated media is returned as hosted URLs or saved files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a dLazy API key; async mode can return a generateId for later polling.]

## Skill Version(s):

1.3.11 (source: server release metadata; artifact frontmatter reports 1.3.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
