## Description:

ElevenLabs eleven_v3 text-to-speech with 12 curated multilingual voices and stability, similarity, and style controls for dubbing, audiobooks, and character dialogue.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and creators use this skill to synthesize speech for dubbing, audiobooks, and character dialogue, selecting a multilingual voice and tuning stability, similarity, and style.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Submitted text and generation settings are sent to dLazy for cloud processing, and use may consume paid credits.

Mitigation: Send only content approved for the service, review its pricing and data terms, and use a revocable API key; set DLAZY_API_KEY to avoid storing the key in CLI configuration.

## Reference(s):

- [dLazy CLI project page](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Audio, JSON]

**Output Format:** [Generated speech audio returned with a JSON result containing hosted output URLs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Asynchronous requests may initially return a task ID instead of an audio URL.]

## Skill Version(s):

1.3.33 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
