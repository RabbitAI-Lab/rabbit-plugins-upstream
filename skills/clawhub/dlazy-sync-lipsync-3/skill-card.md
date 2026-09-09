## Description:

fal.ai sync-lipsync v3 generates a new video whose speaker lip movement matches a provided audio track, supporting dubbing, localization, and virtual presenter re-sync workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to ask an agent to run dLazy's hosted sync-lipsync-3 service against input video and audio for dubbing, localization, and lip-sync repair. The workflow requires dLazy authentication and sends selected media inputs to the hosted API.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Media files and request parameters are sent to dLazy's hosted service for processing.

Mitigation: Only upload media the user is comfortable sending to the service, and review dLazy terms before using sensitive content.

Risk: The skill depends on a pinned external CLI and stores or reads a dLazy API key.

Mitigation: Prefer npx or an unprivileged account in high-trust environments, review the @dlazy/cli package or source before installation, and rotate or revoke API keys if exposure is suspected.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-sync-lipsync-3)
- [Publisher profile](https://clawhub.ai/user/dlazyai)
- [dLazy homepage](https://dlazy.com)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, API Calls, Files, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON result examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return hosted media URLs or an asynchronous task identifier; --save can download the generated result to a local file.]

## Skill Version(s):

1.3.14 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
