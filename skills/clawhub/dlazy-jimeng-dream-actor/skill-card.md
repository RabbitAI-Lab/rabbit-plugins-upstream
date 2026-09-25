## Description:

Convert static character images into vivid action videos with Jimeng Dream Actor.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to call the dLazy Jimeng Dream Actor cloud service from an agent workflow, supplying prompts and image or video references to generate action-video outputs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected local media files are sent to dLazy cloud endpoints, and generated outputs are hosted by dLazy.

Mitigation: Use only media approved for dLazy processing and avoid submitting sensitive content unless the user has authorization for that cloud service.

Risk: Authentication can store a dLazy API key in a local CLI configuration file.

Mitigation: Use the documented login or key-setting flow, protect the local user account, and rotate or revoke the key from the dLazy dashboard when access should end.

Risk: A global installation runs a third-party npm CLI on the user's machine.

Mitigation: Prefer the pinned npx command for on-demand use, or review the pinned npm package and source before installing globally.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-jimeng-dream-actor)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Files, Guidance]

**Output Format:** [Markdown instructions with CLI commands and JSON result payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return hosted file URLs or an asynchronous generateId; the CLI can save generated assets locally when requested.]

## Skill Version(s):

1.3.20 (source: server release evidence; artifact frontmatter reports 1.3.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
