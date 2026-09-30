## Description:

Guides an agent to generate a lip-synced video from a source video and audio using dLazy's hosted sync-lipsync-3 service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators, localization teams, and developers use this skill to synchronize a speaker's lip movements in a video with supplied audio for dubbing and virtual presenters.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected video and audio files are uploaded to dLazy's hosted service.

Mitigation: Only submit media you are authorized to share and review the service terms before use.

Risk: Using a third-party CLI requires trusting its code and handling a dLazy API key.

Mitigation: Review the CLI before installing, prefer the pinned on-demand npx command, and revoke keys when no longer needed.

Risk: The skill's --prompt example and image/png sample output do not match its stated video workflow.

Mitigation: Check the CLI help for supported flags and confirm the actual response before using the generated media.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-sync-lipsync-3)
- [dLazy CLI source (listed in skill metadata; not verified release provenance)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands]

**Output Format:** [Markdown with command examples and JSON response guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated videos are returned as hosted links or saved locally; asynchronous requests return a task ID.]

## Skill Version(s):

1.3.23 (source: ClawHub release; artifact frontmatter states 1.3.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
