## Description:

Video Retalk helps agents run dLazy's Tongyi VideoRetalk lip-sync service to regenerate a talking-person video so the speaker's mouth movements match a supplied voice audio track, with optional reference-face targeting when multiple faces appear.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to generate lip-synced videos through the dLazy CLI by providing a person video and replacement voice audio. It is useful for dubbing or matching an existing talking-person video to new speech.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill depends on the dLazy npm CLI and hosted service.

Mitigation: Use the pinned on-demand `npx @dlazy/cli@1.2.3` invocation when possible and install only if the dLazy CLI and service are trusted.

Risk: Selected video, audio, and optional face reference files are sent to dLazy's hosted service.

Mitigation: Pass only files needed for the task and avoid unrelated private or sensitive media.

Risk: The dLazy API key grants access to the user's dLazy organization.

Mitigation: Protect the API key, use local configuration or environment variables carefully, and rotate or revoke the key if exposure is suspected.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-videoretalk)
- [dLazy CLI homepage](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Files, Guidance]

**Output Format:** [Markdown with inline bash commands and JSON result objects]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return generated media URLs or save downloaded result assets when the CLI save option is used.]

## Skill Version(s):

1.3.14 (source: server release metadata; artifact frontmatter says 1.3.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
