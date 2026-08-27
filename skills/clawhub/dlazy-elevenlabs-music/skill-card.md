## Description:

Generates 10-300 second original music from a natural-language prompt using the ElevenLabs music_v1 model through the dLazy CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to generate background music, ad music, and short-video soundtracks from text prompts. The skill invokes the dLazy hosted generation service through a pinned CLI and can return hosted result URLs or save generated media locally.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected inputs are sent to dLazy's hosted service for generation.

Mitigation: Use approved input data only and avoid sensitive prompts or files unless the dLazy service is trusted for the intended use.

Risk: The skill depends on a third-party pinned CLI package that handles authentication, hosted API calls, and generated media retrieval.

Mitigation: Review the dLazy CLI source or npm package before installation, use npx for non-persistent use when appropriate, and rotate or revoke the API key if exposure is suspected.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/dlazyai/skills/dlazy-elevenlabs-music)
- [dLazy CLI Homepage](https://github.com/dlazyai/cli)
- [@dlazy/cli npm Package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy Website](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Files, Guidance]

**Output Format:** [JSON response with hosted output URLs, optional saved media file, and concise guidance for authentication, balance, or generation errors.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a dLazy API key; prompts and selected inputs are sent to dLazy's hosted service; asynchronous runs may return a generateId for polling.]

## Skill Version(s):

1.3.8 (source: server release metadata; artifact frontmatter reports 1.3.4)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
