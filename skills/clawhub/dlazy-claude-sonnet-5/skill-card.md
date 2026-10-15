## Description:

Uses the dLazy CLI to request hosted Claude Sonnet 5 text generation for reasoning, coding, and agent workflows, with optional image and video inputs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and other agent users submit prompts, optionally with images or video, to dLazy's hosted service for text generation, reasoning, and coding assistance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and supplied media may be sent to dLazy's hosted service.

Mitigation: Review prompts and media before submission, and avoid sharing sensitive material without authorization.

Risk: Logging in stores a dLazy API key locally.

Mitigation: Protect local credentials and rotate or revoke the key from the dLazy dashboard if necessary.

Risk: Installing the third-party CLI globally leaves it on the system.

Mitigation: Use the pinned on-demand command `npx @dlazy/cli@1.2.3` if a persistent global install is unwanted.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-claude-sonnet-5)
- [dLazy CLI package (skill metadata)](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy CLI homepage (skill metadata; import provenance unavailable)](https://github.com/dlazy-ai/cli)

## Skill Output:

**Output Type(s):** [Text, Code, Guidance]

**Output Format:** [Text or structured JSON returned by the CLI]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Optional asynchronous task identifier; output may require polling.]

## Skill Version(s):

1.2.31 (source: ClawHub release; artifact frontmatter says 1.2.7)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
