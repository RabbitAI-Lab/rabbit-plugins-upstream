## Description:

HeyGen Lipsync Speed is a fast lip-sync skill for generating synchronized video from video and audio inputs through the dLazy hosted API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users invoke this skill to run the dLazy HeyGen Lipsync Speed model from an agent workflow, supplying video and audio inputs and receiving generated lip-sync media results.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill invokes a pinned npm CLI dependency and depends on that package to perform API calls.

Mitigation: Review the @dlazy/cli package provenance or source before installation in sensitive environments, and run npm or the CLI without elevated privileges.

Risk: Video, audio, and related prompt parameters are sent to dLazy hosted services for processing.

Mitigation: Only pass media files and content that are approved for upload to dLazy, and confirm that this SaaS processing model fits the user's privacy and compliance requirements.

Risk: The CLI stores or uses a dLazy API key for authenticated requests.

Mitigation: Use per-invocation DLAZY_API_KEY where persistent local storage is undesirable, and rotate or revoke keys through the dLazy dashboard when access should change.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/dlazyai/skills/dlazy-heygen-lipsync-speed)
- [Publisher Profile](https://clawhub.ai/user/dlazyai)
- [dLazy CLI Homepage](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm Package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Files, Guidance]

**Output Format:** [Markdown guidance with CLI commands and JSON responses containing generated media URLs; optional downloaded files when --save is used.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires npm or npx, a dLazy API key, and network access to api.dlazy.com and files.dlazy.com.]

## Skill Version(s):

1.3.14 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
