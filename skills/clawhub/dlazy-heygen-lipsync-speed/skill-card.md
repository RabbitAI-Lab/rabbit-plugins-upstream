## Description:

HeyGen Lipsync Speed provides fast lip-sync generation for video and audio inputs through the dLazy hosted API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and content teams use this skill to submit video and audio inputs to dLazy's hosted HeyGen Lipsync Speed model and receive lip-synced generated media. It is suited to workflows where rapid lip-sync generation is more important than local model execution.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses a dLazy API key and stores or accepts credentials for hosted API access.

Mitigation: Use the documented dLazy authentication flow, protect the local CLI config, and rotate or revoke the API key if compromise is suspected.

Risk: Video and audio inputs may be uploaded to dLazy-hosted media storage for processing.

Mitigation: Provide only media files intended for upload and avoid submitting sensitive or unauthorized content.

Risk: The skill depends on the @dlazy/cli npm package for execution.

Mitigation: Review the package or source before use and prefer npx or an isolated non-root environment over a global install.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-heygen-lipsync-speed)
- [dLazy CLI source link from metadata](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Files, Guidance]

**Output Format:** [Markdown guidance with bash commands and JSON API results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return hosted file URLs, async task IDs, or saved media assets.]

## Skill Version(s):

1.3.15 (source: evidence.json release.version; artifact frontmatter reports 1.3.6)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
