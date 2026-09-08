## Description:

Anthropic's latest Sonnet model for reasoning, code generation, complex tool orchestration, and text generation from text, image, and video inputs through the dLazy CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to invoke Claude Sonnet 5 through dLazy for text generation, coding assistance, reasoning, and multimodal prompts that include image or video references.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts, parameters, and selected local media files may be sent to dLazy cloud endpoints for processing.

Mitigation: Avoid sending sensitive data unless the dLazy service terms and account controls are acceptable for the use case.

Risk: The skill depends on a third-party npm CLI package and remote API endpoints.

Mitigation: Install only from trusted package sources, keep the API key scoped and revocable, and review the CLI source or package before global installation.

Risk: Authentication failures or exhausted credits can prevent task completion.

Mitigation: Use a revocable dLazy API key and confirm account credit availability before relying on the skill in a workflow.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-claude-sonnet-5)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [JSON response envelope with generated content or asynchronous task status; guidance may be Markdown with shell commands.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports prompt input plus optional image and video references; no-wait mode returns a generation identifier for later polling.]

## Skill Version(s):

1.2.16 (source: server release evidence; artifact frontmatter reports 1.2.7)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
