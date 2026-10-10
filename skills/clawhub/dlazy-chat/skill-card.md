## Description:

Chat with dLazy's hosted sandbox agent to run skills and continue project-scoped conversations across multiple turns.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and other dLazy users start or continue project conversations with a hosted agent, discover available skills and projects, and optionally attach reference files.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and files attached with --files are sent to dLazy's hosted service.

Mitigation: Share only material you intend to send to dLazy; review attachments before upload.

Risk: The CLI stores an API key locally for authenticated requests.

Mitigation: Protect local CLI configuration and rotate or revoke the key if exposed.

Risk: Broad chat requests may unintentionally route conversations to the hosted agent.

Mitigation: Request dLazy chat explicitly when you intend to use the service.

Risk: Using the skill requires installing or running a third-party CLI package.

Mitigation: Review the pinned CLI package before installing when supply-chain risk matters.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-chat)
- [dLazy CLI package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy CLI source listed in skill metadata](https://github.com/dlazy-ai/cli)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Conversational text streamed to the terminal]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Project-scoped multi-turn responses; content depends on the selected hosted skill.]

## Skill Version(s):

1.2.29 (source: server-resolved ClawHub release; artifact frontmatter says 1.2.8)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
