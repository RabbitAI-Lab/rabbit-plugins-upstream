## Description:

Fast HeyGen lip-sync generation for syncing supplied audio with a supplied video through the dLazy hosted API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and content teams use this skill to ask an agent to run dLazy's HeyGen Lipsync Speed tool for rapid audio-to-video lip synchronization, optionally with captions, duration adjustment, background music removal, speech enhancement, async execution, and local result saving.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill depends on the external @dlazy/cli package and hosted dLazy API endpoints.

Mitigation: Confirm the package and publisher are trusted before use, prefer npx for non-persistent execution when appropriate, and review the pinned CLI version before installation.

Risk: Input video or audio files and generation parameters may be uploaded to dLazy services.

Mitigation: Avoid submitting sensitive media unless approved for the intended service, and ensure users understand that processing occurs through dLazy-hosted endpoints.

Risk: The dLazy API key is stored in local CLI configuration or supplied through an environment variable.

Mitigation: Protect the local config file, use environment-scoped credentials where appropriate, and rotate or revoke the API key from the dLazy dashboard if exposure is suspected.

Risk: The artifact documentation includes a mismatched --prompt example for a video/audio lip-sync tool.

Mitigation: Use the documented --video_url and --audio_url options, and run dlazy heygen-lipsync-speed -h before invoking the tool.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-heygen-lipsync-speed)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, JSON, Files, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return hosted output URLs, async task IDs, or saved local media files through the dLazy CLI.]

## Skill Version(s):

1.3.20 (source: ClawHub release evidence; artifact frontmatter lists 1.3.6)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
