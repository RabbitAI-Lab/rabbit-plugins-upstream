## Description:

Generates a lip-synced video by aligning the speaker's mouth movement in an input video to a supplied audio track.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to run dLazy's hosted Sync Lipsync 3 video generation workflow for dubbing, localization, and re-syncing virtual presenters.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Local video and audio paths are uploaded to dLazy-hosted services for processing.

Mitigation: Only provide media intended for cloud processing and review the service terms before using sensitive content.

Risk: The skill installs or runs a third-party npm CLI.

Mitigation: Review the linked CLI source or npm package, prefer npx or an unprivileged local setup, and avoid running npm as administrator or root.

Risk: API keys are used for dLazy requests and may be stored in local CLI configuration or supplied through the environment.

Mitigation: Store keys only in the documented user config or per-invocation environment, and rotate or revoke keys from the dLazy dashboard when needed.

Risk: The documented sample output appears inconsistent with a video lip-sync workflow.

Mitigation: Validate the returned payload and saved media before using the result in downstream workflows.

## Reference(s):

- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)
- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-sync-lipsync-3)

## Skill Output:

**Output Type(s):** [shell commands, configuration, guidance]

**Output Format:** [Markdown with inline bash commands and JSON response examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return an asynchronous task identifier when no-wait mode is used; completed media results are returned as hosted URLs.]

## Skill Version(s):

1.3.13 (source: server release metadata; artifact frontmatter says 1.3.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
