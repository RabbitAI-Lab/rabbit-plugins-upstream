## Description:

Converts static character images into vivid action videos with Jimeng Dream Actor.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to call the dLazy CLI/API to turn supplied character images, prompts, and optional media references into generated action-video output.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected media may be uploaded to dLazy-hosted services for generation.

Mitigation: Confirm the media is appropriate for external processing before invoking the skill.

Risk: Generation may be billable or fail when the dLazy account has insufficient credits.

Mitigation: Use --dry-run or confirm intent before billable generation, and direct the user to the dLazy credits dashboard if the service reports insufficient balance.

Risk: Authentication uses a dLazy API key that may be stored in the local CLI configuration.

Mitigation: Use the documented login or auth flow, keep the config file restricted to the OS user, and rotate or revoke keys from the dLazy dashboard when needed.

Risk: The skill depends on the external @dlazy/cli package and hosted dLazy endpoints.

Mitigation: Review the package/source and prefer npx or the pinned install command in sensitive environments.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-jimeng-dream-actor)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy website](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Files, Guidance]

**Output Format:** [Markdown guidance with CLI commands and JSON result payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return hosted generated media URLs or save the generated asset when --save is used.]

## Skill Version(s):

1.3.17 (source: server release metadata; artifact frontmatter reports 1.3.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
