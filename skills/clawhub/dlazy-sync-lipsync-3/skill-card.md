## Description:

Guides an agent to synchronize a speaker's lip movements in a video with supplied audio using dLazy's hosted lip-sync service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to produce lip-synced video for dubbing, localization, and virtual presenters.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installing the third-party CLI runs external software on the user's machine.

Mitigation: Review the package before installing; use the pinned npx invocation if a persistent global binary is unnecessary.

Risk: Local video and audio supplied to the service are uploaded to dLazy.

Mitigation: Only submit media that is appropriate to upload to this cloud service.

Risk: The documented example command and sample output may not match the video lip-sync workflow.

Mitigation: Check the CLI help and confirm output type before relying on the examples.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-sync-lipsync-3)
- [dLazy CLI homepage](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance]

**Output Format:** [Markdown with shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The CLI returns a JSON response with a generated media URL; the result can optionally be saved locally.]

## Skill Version(s):

1.3.26 (source: ClawHub release; artifact frontmatter lists 1.3.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
