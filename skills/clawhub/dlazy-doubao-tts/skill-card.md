## Description:

Synthesize text into natural-sounding speech with Doubao TTS through the dLazy service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to turn supplied text into spoken audio with a choice of language and voice through dLazy's Doubao TTS service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Submitted text and generated audio are handled by the hosted dLazy service.

Mitigation: Review the service terms and avoid submitting sensitive text unless its external processing is acceptable.

Risk: The CLI needs an API key, which can be stored in local configuration.

Mitigation: Protect the local configuration or pass DLAZY_API_KEY for individual invocations; rotate the key if exposed.

Risk: Installing and invoking an external CLI can incur service charges.

Mitigation: Review the pinned npm package before installation and invoke the skill explicitly to avoid unintended credit use.

## Reference(s):

- [dLazy CLI source (linked in skill metadata; not verified import provenance)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Audio file links]

**Output Format:** [CLI commands and JSON responses with hosted result URLs or task status]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Optional local download with --save; asynchronous tasks can require polling.]

## Skill Version(s):

1.3.28 (source: server release metadata; skill frontmatter lists 1.3.4)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
