## Description:

Suno music generation model that supports inspiration mode with automatic lyrics and custom mode with manual lyrics, generating music with or without vocals.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to ask an agent to generate Suno music through the dLazy CLI, including vocal, instrumental, inspiration-mode, and custom-lyrics workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill runs an external npm CLI and depends on dLazy hosted services.

Mitigation: Use the pinned npx @dlazy/cli@1.2.3 invocation when avoiding a persistent global install, and install only after accepting the external CLI and hosted-service dependency.

Risk: Prompts, parameters, and explicitly provided media files are sent to dLazy services for generation.

Mitigation: Avoid sending sensitive content, and use a revocable API key scoped to the intended organization and generation workflow.

Risk: API keys may be stored in local CLI configuration.

Mitigation: Prefer revocable keys, rotate or revoke keys from the dLazy dashboard when no longer needed, and use DLAZY_API_KEY for per-invocation credentials when appropriate.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-suno-music)
- [dLazy CLI repository](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Files, Guidance]

**Output Format:** [CLI command guidance and JSON responses with generated media URLs; optional downloaded media files when --save is used.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a dLazy API key and sends prompts, parameters, and explicitly provided media files to dLazy hosted services.]

## Skill Version(s):

1.3.14 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
