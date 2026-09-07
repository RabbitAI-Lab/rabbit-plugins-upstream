## Description:

Tongyi Wanxiang 2.7 video model supports text-to-video, first/last-frame-to-video, and reference-to-video generation through the dLazy CLI and hosted API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to ask an agent to generate Wan 2.7 videos from text prompts, reference images or videos, first and last frames, and optional audio through dLazy's cloud service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts, parameters, and referenced media files are sent to dLazy's hosted API and media storage.

Mitigation: Use the skill only for content you are comfortable processing through dLazy's cloud service and avoid sending sensitive media unless the service terms and controls meet your requirements.

Risk: The skill depends on a third-party CLI and API key stored in local configuration or supplied through an environment variable.

Mitigation: Prefer the pinned npx invocation when practical, protect the dLazy API key, and rotate or revoke the key when access is no longer needed.

Risk: Generated media may be returned as hosted URLs or asynchronous task identifiers rather than immediate local files.

Mitigation: Use the documented save and status commands when a local artifact or completion check is required.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-wan2-7)
- [dLazy homepage](https://dlazy.com)
- [dLazy CLI project page](https://github.com/dlazy-ai/cli)
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Files, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON response examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return hosted result URLs, asynchronous task identifiers, or save generated media to a local path when requested.]

## Skill Version(s):

1.3.12 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
