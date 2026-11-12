## Description:

Creates an ElevenLabs Instant Voice Clone from a clean voice sample for use with ElevenLabs text-to-speech.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use the skill to create a custom ElevenLabs voice from a clean recording for text-to-speech.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security summary says the documented `dlazy login` command's role in the advertised ElevenLabs workflow is unclear.

Mitigation: Inspect the linked CLI repository and confirm the voice-cloning command's behavior before installing it or sending a sample.

Risk: The skill says local audio samples are uploaded to dLazy media storage and requests are sent to its hosted API.

Mitigation: Review dLazy's data handling terms and submit only recordings you are permitted to share.

## Reference(s):

- [CLI repository (linked in skill metadata)](https://github.com/dlazy-ai/cli)
- [@dlazy/cli on npm](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy](https://dlazy.com)

## Skill Output:

**Output Type(s):** [JSON, Generated voice resource]

**Output Format:** [JSON response with result metadata and a hosted output URL]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [With --no-wait, the response can contain an asynchronous task ID before outputs are available.]

## Skill Version(s):

1.3.39 (source: server-resolved release metadata; artifact frontmatter lists 1.3.4)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
