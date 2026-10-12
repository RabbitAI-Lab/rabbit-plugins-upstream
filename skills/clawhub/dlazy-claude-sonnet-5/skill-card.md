## Description:

Uses the dLazy hosted Claude Sonnet 5 service to generate text and code from prompts with optional image and video inputs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and other users can generate written answers and code using a hosted model, optionally providing images or videos for context.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected local media files may be sent to dLazy's hosted service.

Mitigation: Avoid sending sensitive content or local files unless their upload is approved.

Risk: The CLI may store an API key locally.

Mitigation: Protect local credentials and rotate or revoke the key if it is exposed.

Risk: Installing the third-party CLI introduces a software supply-chain dependency.

Mitigation: Review the linked CLI source and package before installation; use the pinned npx command for one-off use if a global install is unnecessary.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-claude-sonnet-5)
- [dLazy CLI source (linked by skill metadata; skill import provenance unavailable)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Text, Code, Guidance]

**Output Format:** [JSON response containing generated content]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Asynchronous requests may return a task ID for later retrieval.]

## Skill Version(s):

1.2.30 (source: ClawHub release; skill frontmatter lists 1.2.7)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
