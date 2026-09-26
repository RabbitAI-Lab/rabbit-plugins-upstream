## Description:

PixVerse C1 is a dLazy CLI-backed video generation skill for text-to-video, image-to-video, first/last-frame-to-video, and reference-to-video workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to invoke PixVerse C1 through the pinned dLazy CLI, sending prompts and optional media inputs to dLazy services and receiving generated media URLs or saved output files.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected local media files are sent to dLazy services for generation.

Mitigation: Use the skill only when users trust dLazy with the submitted content, and avoid sending sensitive media or prompts unless permitted.

Risk: The skill depends on a pinned npm CLI that stores or uses a dLazy API key.

Mitigation: Prefer npx for one-off use when avoiding a persistent global binary, protect the local configuration file, and rotate or revoke the API key from the dLazy dashboard when needed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-pixverse-c1)
- [dLazy CLI homepage](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Files, Guidance]

**Output Format:** [JSON responses with generated media URLs, optional saved files, and Markdown command guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports asynchronous task IDs, polling, dry-run cost estimates, and optional local save paths.]

## Skill Version(s):

1.2.21 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
