## Description:

Helps an agent use dLazy's hosted VideoRetalk service to synchronize a person's lip movements in a video with a supplied voice recording, optionally selecting a face with a reference image.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to make a talking-person video match a new voice recording, with an optional reference image to select a face when several people appear.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installing an external CLI and storing or passing a dLazy API key exposes credentials to the service workflow.

Mitigation: Review the CLI before installation, protect the API key, and rotate or revoke it if compromised.

Risk: Video, audio, and reference images supplied as local files are uploaded to dLazy-hosted services.

Mitigation: Only submit media you are authorized to share, and check the service terms before uploading sensitive content.

Risk: Generation may consume paid credits, and documentation examples conflict with the listed flags and output type.

Mitigation: Check the available credits and CLI help, use the dry run where appropriate, and verify returned media before relying on it.

## Reference(s):

- [ClawHub Video Retalk release](https://clawhub.ai/dlazyai/skills/dlazy-videoretalk)
- [dLazy CLI repository (artifact metadata link)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance, JSON]

**Output Format:** [Markdown instructions and JSON CLI response with a generated media URL]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can save the generated file locally; asynchronous requests return a task ID for later status checks.]

## Skill Version(s):

1.3.29 (source: server release; artifact frontmatter lists 1.3.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
