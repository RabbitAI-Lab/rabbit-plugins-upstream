## Description:

Convert static character images into vivid action videos with Jimeng Dream Actor.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to submit prompts and character media to the dLazy Jimeng Dream Actor service and receive generated media URLs or an async task ID.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected image or video files are processed by dLazy's hosted service.

Mitigation: Use the skill only when cloud processing is intended, avoid sensitive media unless appropriate, and run with --dry-run when possible before making a live request.

Risk: The dLazy API key may be stored in the local CLI configuration.

Mitigation: Check local config protection, prefer OS-user-restricted storage, and rotate or revoke the organization-scoped key if exposure is suspected.

Risk: Generation requests can consume dLazy credits.

Mitigation: Use --dry-run for cost estimates when available and resolve insufficient-balance errors through the dLazy credits dashboard.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/dlazyai/skills/dlazy-jimeng-dream-actor)
- [dLazy CLI Source](https://github.com/dlazyai/cli)
- [dLazy CLI npm Package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy Homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance]

**Output Format:** [Markdown guidance with shell commands and JSON responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return generated media URLs hosted on files.dlazy.com or an async task with generateId when --no-wait is used.]

## Skill Version(s):

1.3.7 (source: server release evidence; artifact frontmatter shows 1.3.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
