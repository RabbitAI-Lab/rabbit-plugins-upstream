## Description:

Chat with dLazy's project-scoped sandbox agent to run skills across multiple turns and continue existing projects.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and other dLazy users can start or resume project-based conversations with a hosted agent to complete multi-turn tasks using available skills.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad chat requests could invoke dLazy without clear intent.

Mitigation: Use explicit dLazy wording and confirm the intended service before invoking the skill.

Risk: Prompts and attached files are sent to dLazy's hosted service.

Mitigation: Review prompts and files before sending; avoid attaching sensitive material unless appropriate for that service.

Risk: The CLI uses or stores a local dLazy API key.

Mitigation: Protect the key and revoke it if it may have been exposed.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-chat)
- [dLazy CLI repository (listed in metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Guidance]

**Output Format:** [Streamed conversational text; content varies by selected skill]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Project-scoped conversations can preserve context across turns.]

## Skill Version(s):

1.2.24 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
