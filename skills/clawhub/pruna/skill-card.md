## Description:

Use when installing the full Pruna generative media suite -- all guides, tools, and workflows in one package.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pruna-ai](https://clawhub.ai/user/pruna-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to install and navigate the Pruna generative media suite, including media prompting guides, API helpers, model tools, and multi-step media workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Unpinned install commands may install changing third-party skill code.

Mitigation: Prefer a reviewed or pinned installer version where possible, and scan the installed skills before deployment.

Risk: Running associated media workflows may use paid API keys and local media tools.

Mitigation: Provide API tokens only when intentionally running the relevant workflows, and review generated shell commands before execution.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/pruna-ai/skills/pruna)
- [Pruna dashboard](https://dashboard.pruna.ai/)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration]

**Output Format:** [Markdown with inline bash code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May reference required API tokens and local media tools for downstream Pruna workflows.]

## Skill Version(s):

1.0.13 (source: server release evidence and artifact metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
