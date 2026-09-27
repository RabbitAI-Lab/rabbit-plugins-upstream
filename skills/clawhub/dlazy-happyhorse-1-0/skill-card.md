## Description:

Happy Horse 1.0 video model covers text-to-video, first-frame-to-video, reference-to-video, and video editing, automatically routing each selected mode to the matching sub-model.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to call the dLazy Happy Horse 1.0 hosted video-generation service for text-to-video, image/reference-to-video, and video-editing workflows through the dLazy CLI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The dLazy CLI stores an API key locally for authenticated requests.

Mitigation: Use the per-invocation DLAZY_API_KEY environment variable or rotate and revoke saved keys from the dLazy dashboard when access should change.

Risk: Prompts and explicitly provided media files are sent to dLazy's hosted API and media storage.

Mitigation: Only submit content appropriate for the third-party dLazy service and review the service terms before sending sensitive media.

Risk: A global CLI install persists a third-party executable on the system.

Mitigation: Use the pinned npx invocation when a non-persistent CLI execution path is preferred.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/dlazyai/skills/dlazy-happyhorse-1-0)
- [dLazy CLI Source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm Package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy Homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance, JSON]

**Output Format:** [Markdown guidance with shell commands and JSON response examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return hosted media URLs, asynchronous task identifiers, or saved local assets when the CLI --save option is used.]

## Skill Version(s):

1.3.20 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
