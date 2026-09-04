## Description:

PixVerse C1 is a dLazy video-generation skill for text-to-video, image-to-video, first/last-frame-to-video, and reference-to-video workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to ask an agent to generate short videos through the dLazy PixVerse C1 CLI, with optional reference images, first and last frames, resolution, aspect ratio, duration, audio generation, async polling, and local save options.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts, parameters, and selected local media files are sent to third-party dLazy services for generation.

Mitigation: Review prompts and file inputs before use, and avoid sending sensitive or restricted media unless approved for the dLazy service.

Risk: The dLazy CLI can store an API key in the local user configuration.

Mitigation: Use the DLAZY_API_KEY environment variable for per-invocation authentication when persistent local key storage is not desired, and rotate or revoke keys from the dLazy dashboard as needed.

Risk: Generation can consume account credits and may fail when the account balance is insufficient.

Mitigation: Use --dry-run for payload and cost checks before calling the API, and confirm account credit availability for expected workloads.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/dlazyai/skills/dlazy-pixverse-c1)
- [dLazy CLI Source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm Package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy Homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, JSON, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with shell commands and JSON result envelopes containing generated media URLs or async task identifiers.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return hosted media URLs from files.dlazy.com; with --save it can download generated assets to a local path.]

## Skill Version(s):

1.2.13 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
