## Description:

Tongyi VideoRetalk lip-syncs a talking-person video to a supplied voice audio track, with an optional reference face image for selecting the target person in multi-face videos.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to create a new video where a speaker's mouth movements match replacement speech audio. It is suited for cloud-hosted lip-sync generation workflows that can send selected video, audio, and optional face-reference media to dLazy services.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected video, audio, and optional face-reference media are uploaded to dLazy's hosted service for processing.

Mitigation: Use only media intended for cloud processing, avoid unrelated private files, and confirm user consent for any likeness or voice material.

Risk: The skill depends on running the dLazy npm CLI with API credentials.

Mitigation: Prefer npx or an isolated install, use a revocable API key, and avoid exposing environment secrets to the CLI session.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/dlazyai/skills/dlazy-videoretalk)
- [dLazy Publisher Profile](https://clawhub.ai/user/dlazyai)
- [dLazy CLI Source](https://github.com/dlazy-ai/cli)
- [@dlazy/cli npm Package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy Homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, Guidance, JSON, Files]

**Output Format:** [Markdown guidance with bash command examples and JSON CLI responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The dLazy CLI may return hosted media URLs, save generated assets locally, or return an asynchronous task identifier for later polling.]

## Skill Version(s):

1.3.16 (source: server release metadata; artifact frontmatter reports 1.3.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
