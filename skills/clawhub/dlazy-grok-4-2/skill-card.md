## Description:

Provides text generation, dialogue Q&A, and logical reasoning through dLazy's hosted Grok 4.2 CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and agent users use this skill to call dLazy's hosted Grok 4.2 service for text generation, chat-style Q&A, and reasoning tasks from an agent workflow.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts, parameters, and selected local file inputs may be sent to dLazy hosted services.

Mitigation: Use only data appropriate for dLazy processing, and avoid passing sensitive local files unless upload to dLazy is intended.

Risk: The skill depends on an npm-distributed third-party CLI.

Mitigation: Prefer the pinned npx invocation for non-persistent use, and review the package or source before installing globally.

Risk: A dLazy API key is required for use.

Mitigation: Store keys in the documented CLI config or environment variable, and rotate or revoke keys if exposure is suspected.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-grok-4-2)
- [dlazyai publisher profile](https://clawhub.ai/user/dlazyai)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Guidance]

**Output Format:** [Text or JSON CLI result, often relayed as Markdown by the agent]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include asynchronous task status or hosted output URLs when the CLI returns them.]

## Skill Version(s):

1.3.12 (source: server release metadata; artifact frontmatter reports 1.3.4)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
