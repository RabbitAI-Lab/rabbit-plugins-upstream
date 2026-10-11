## Description:

Helps agents use dLazy's hosted VideoRetalk service to synchronize a speaker's lips in a video with a new voice track, with an optional reference face for multi-person videos.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers can align a person's mouth movements in a video with a new spoken audio track, optionally identifying the intended face in a multi-person scene.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Provided video, audio, and optional face images are uploaded to dLazy's hosted service.

Mitigation: Upload only media you are authorized and comfortable sharing with the external service.

Risk: A dLazy API key is stored locally for authenticated requests.

Mitigation: Treat the key as a credential; rotate or revoke it if exposed.

Risk: The skill uses an external CLI, which may be installed globally.

Mitigation: Review the CLI before use and choose the documented npx option if a global installation is unwanted.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-videoretalk)
- [dLazy CLI source (listed in skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Configuration guidance]

**Output Format:** [Markdown guidance and CLI JSON containing a generated media URL]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The hosted result can be downloaded to a local path using --save.]

## Skill Version(s):

1.3.27 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
