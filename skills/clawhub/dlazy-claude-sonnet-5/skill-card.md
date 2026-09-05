## Description:

Provides access to Claude Sonnet 5 through the dLazy CLI for text generation, reasoning, coding, and prompt workflows with optional image and video inputs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and agents use this skill to invoke dLazy-hosted Claude Sonnet 5 for text generation, coding assistance, reasoning, and multimodal prompt tasks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The dLazy API key may be stored in local CLI configuration and has account value if exposed.

Mitigation: Prefer per-invocation DLAZY_API_KEY or a private config directory with restrictive permissions, and rotate or revoke keys that may have been exposed.

Risk: Prompts and local media files passed to the skill are sent to dLazy-hosted services.

Mitigation: Only pass prompts, images, videos, or files that are appropriate to send to the hosted dLazy API and media storage.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/dlazyai/skills/dlazy-claude-sonnet-5)
- [Publisher Profile](https://clawhub.ai/user/dlazyai)
- [dLazy CLI Source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm Package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy Homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [JSON response containing generated outputs, with agent-facing guidance and shell commands in Markdown.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return asynchronous task metadata when invoked with no-wait mode; generated output URLs may be hosted by dLazy.]

## Skill Version(s):

1.2.14 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
