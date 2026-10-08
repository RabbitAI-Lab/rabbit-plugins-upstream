## Description:

Synthesize spoken audio from text using Doubao TTS through the dLazy CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and other users can turn text into spoken audio with selectable language, voice, and speech speed through the dLazy CLI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Text prompts and selected local files may be sent to the third-party dLazy service, which hosts generated outputs.

Mitigation: Review prompts and selected files for sensitive information before sending them to dLazy.

Risk: Installing the third-party CLI may leave a global executable, and login can save an API key locally.

Mitigation: Review the CLI before installing, use the documented pinned npx invocation to avoid a persistent global binary, and safeguard or revoke stored credentials as needed.

Risk: The artifact's output example describes an image rather than synthesized speech.

Mitigation: Verify the actual audio result and file format instead of relying on the example.

## Reference(s):

- [dLazy CLI repository (listed in skill metadata; release provenance unavailable)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Audio, JSON]

**Output Format:** [Hosted audio asset URL or downloaded audio file, with a JSON CLI response]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [An asynchronous request can return a task ID for later status checks; the artifact's sample output shows an image, not audio.]

## Skill Version(s):

1.3.25 (source: ClawHub release; artifact frontmatter lists 1.3.4)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
