## Description:

This skill helps agents use dLazy's hosted fal.ai sync-lipsync v3 workflow to generate lip-synced video from an input video and audio track for dubbing, localization, and virtual presenter resynchronization.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users, creators, and developers use this skill to submit video and audio inputs through the dLazy CLI and receive lip-synced media for dubbing, localization, or virtual presenter workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Using the skill sends selected video files, audio files, and parameters to dLazy's hosted service.

Mitigation: Avoid submitting private media unless the user is comfortable uploading it to dLazy.

Risk: Running dlazy login or dlazy auth set stores an API key in the local dLazy CLI configuration.

Mitigation: Use per-invocation DLAZY_API_KEY when persistent local credentials are not desired, and rotate or revoke keys from the dLazy dashboard when needed.

Risk: A global CLI install persists @dlazy/cli on the system.

Mitigation: Use the pinned npx invocation when a non-persistent CLI execution is preferred.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-sync-lipsync-3)
- [Publisher profile](https://clawhub.ai/user/dlazyai)
- [dLazy CLI homepage](https://github.com/dlazyai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance, JSON]

**Output Format:** [Markdown guidance with bash commands and CLI JSON responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return generated media URLs or an asynchronous generateId for polling.]

## Skill Version(s):

1.3.8 (source: server release metadata; artifact frontmatter says 1.3.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
