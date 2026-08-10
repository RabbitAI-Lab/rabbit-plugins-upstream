## Description:

fal.ai sync-lipsync v3 generates a new video where a speaker's lip movement is synchronized to supplied audio, supporting dubbing, localization, and virtual-presenter re-syncing.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, localization teams, and developers use this skill to run dLazy's hosted sync-lipsync-3 workflow for dubbing, localization, or re-syncing a speaker's lip movement in a video to supplied audio.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected video and audio may be sent to dLazy/fal.ai hosted services for processing.

Mitigation: Use only media approved for that hosted processing flow and review applicable service terms before submitting sensitive or regulated content.

Risk: Using dlazy login or dlazy auth set stores a dLazy API key in the local CLI configuration.

Mitigation: Prefer per-invocation DLAZY_API_KEY or pinned npx usage when appropriate, and rotate or revoke the key from the dLazy dashboard if exposure is suspected.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-sync-lipsync-3)
- [dLazy CLI source](https://github.com/dlazyai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance]

**Output Format:** [Markdown guidance with inline bash commands and JSON API results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return a hosted generated video URL, or an asynchronous generateId and task status when no-wait mode is used.]

## Skill Version(s):

1.3.7 (source: server release metadata; artifact frontmatter says 1.3.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
