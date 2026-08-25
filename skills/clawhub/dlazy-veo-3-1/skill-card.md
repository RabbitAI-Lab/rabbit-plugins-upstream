## Description:

Generate high-quality cinematic videos with Google Veo 3.1 from text prompts, reference images, frame pairs, or video extension inputs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to invoke the dLazy CLI for Google Veo 3.1 video generation, including text-to-video, image-guided generation, frame-based generation, and video extension workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires a dLazy API key and may store it in a local CLI configuration file.

Mitigation: Prefer per-invocation DLAZY_API_KEY use when persistent local credential storage is not acceptable, and rotate or revoke keys from the dLazy dashboard when needed.

Risk: Prompts and selected local media files are sent to dLazy API and file-hosting endpoints for generation.

Mitigation: Confirm user intent before using this skill for generic video requests, and avoid submitting private files unless upload to dLazy is intended.

Risk: Server security evidence marks the release suspicious because the skill makes a stronger local file-permission claim than the inspected CLI package appears to enforce.

Mitigation: Review the CLI behavior before installation and use environment-scoped credentials in higher-risk environments.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-veo-3-1)
- [dLazy CLI homepage](https://github.com/dlazyai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Files, Guidance]

**Output Format:** [Markdown guidance with CLI commands and JSON result payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return hosted media URLs, asynchronous task identifiers, or downloaded video assets when --save is used.]

## Skill Version(s):

1.3.9 (source: server release metadata; artifact frontmatter: 1.3.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
