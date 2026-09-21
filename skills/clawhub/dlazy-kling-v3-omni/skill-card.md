## Description:

Generates Kling v3 Omni videos from text prompts and optional image or video inputs through the dLazy CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to ask an agent to generate short Kling v3 Omni videos from prompts and reference media through dLazy's hosted service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires a dLazy API key and may save it in local CLI configuration.

Mitigation: Use the documented dLazy authentication flow, restrict local config access to the OS user, and rotate or revoke the key from the dLazy dashboard when needed.

Risk: Prompts and supplied media files are uploaded to dLazy-hosted services for generation.

Mitigation: Avoid sending confidential or restricted media unless the user has approved use of dLazy's hosted service for that content.

Risk: The agent installs or invokes the pinned third-party @dlazy/cli package.

Mitigation: Confirm trust in dLazy and the pinned @dlazy/cli package before installation or execution.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-kling-v3-omni)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [JSON, Files, Guidance]

**Output Format:** [JSON response with generated media URLs or async task status; optional downloaded asset file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a dLazy API key; prompts and any supplied media are sent to dLazy-hosted services.]

## Skill Version(s):

1.3.17 (source: server release evidence; artifact frontmatter lists 1.3.4)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
