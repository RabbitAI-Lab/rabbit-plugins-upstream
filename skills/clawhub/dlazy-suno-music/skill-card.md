## Description:

Suno music generation model. Supports inspiration mode (auto lyrics) and custom mode (manual lyrics), generating music with or without vocals.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and creators use this skill to generate music from prompts, with options for automatic or custom lyrics, vocals, and instrumental tracks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and media provided for generation are sent to dLazy's hosted services, and generated assets are hosted there.

Mitigation: Submit only prompts or media you intend to share with dLazy.

Risk: Login stores the API key locally, and generation can consume account credits.

Mitigation: Use a revocable key, use the environment-variable option if you do not want the CLI to save the key, and use --dry-run to preview requests and cost.

## Reference(s):

- [dLazy CLI source (metadata link)](https://github.com/dlazy-ai/cli)
- [dLazy CLI on npm](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy](https://dlazy.com)
- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-suno-music)

## Skill Output:

**Output Type(s):** [Audio, JSON]

**Output Format:** [Generated music assets and their URLs in a JSON response; optionally saved as local files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generation may be asynchronous; the command can return a task identifier before the audio is ready.]

## Skill Version(s):

1.3.35 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
