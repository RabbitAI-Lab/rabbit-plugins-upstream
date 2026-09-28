## Description:

Selects a dLazy audio model to generate speech, music, or sound effects from user requests.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to generate voiceovers, dialogue, music, and sound effects through dLazy's hosted audio models.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installing or running the pinned dLazy CLI introduces third-party code.

Mitigation: Review the pinned @dlazy/cli package and its linked source before installing, especially in sensitive environments.

Risk: Prompts and supplied files are sent to dLazy's hosted service.

Mitigation: Avoid sending sensitive inputs unless approved for the service.

Risk: Login or manual authentication saves an API key locally.

Mitigation: Use the per-invocation DLAZY_API_KEY environment variable when local key storage is unsuitable.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-audio-generate)
- [dLazy CLI source (linked in skill metadata; release provenance unavailable)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance, Text]

**Output Format:** [Text guidance and CLI JSON results with audio URLs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results can link to hosted speech, music, or sound effects.]

## Skill Version(s):

1.3.23 (source: ClawHub release metadata; artifact frontmatter lists 1.3.7)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
