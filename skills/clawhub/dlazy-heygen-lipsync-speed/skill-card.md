## Description:

HeyGen Lipsync Speed is a dLazy CLI skill for fast lip-sync generation from video and audio inputs through the dLazy hosted API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to run dLazy's HeyGen Lipsync Speed model from an agent workflow, supplying video and audio inputs and receiving generated media results or asynchronous task identifiers.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uploads provided video or audio paths to dLazy cloud services for processing.

Mitigation: Only provide media that is appropriate to process with dLazy, and review dLazy service terms before use.

Risk: Use requires a dLazy API key stored in local configuration or supplied per invocation.

Mitigation: Use `dlazy login`, `dlazy auth set`, or `DLAZY_API_KEY` according to your environment, and rotate or revoke keys from the dLazy dashboard when needed.

Risk: The skill depends on the third-party dLazy CLI and hosted API endpoints.

Mitigation: Prefer the pinned `npx @dlazy/cli@1.2.3` invocation when avoiding a global install, and review the CLI source before installing globally.

## Reference(s):

- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)
- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-heygen-lipsync-speed)

## Skill Output:

**Output Type(s):** [Shell commands, API Calls, JSON, Files, Guidance]

**Output Format:** [Markdown guidance with shell commands and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return hosted output URLs, downloaded result files when --save is used, or async task identifiers when --no-wait is used.]

## Skill Version(s):

1.3.18 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
