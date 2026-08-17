## Description:

Tool Use helps an agent define OpenAI-style function schemas, translate user intent into structured tool calls, dispatch registered local tools, and collect execution results.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qq435912743](https://clawhub.ai/user/qq435912743)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent builders use this skill to turn existing commands or Python functions into registered tools, generate function-calling schemas, validate call arguments, execute selected tools, and capture results for agent workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Registered tools can execute local shell commands or Python functions, and model-generated values may be interpolated into command templates.

Mitigation: Use only trusted registries and reviewed arguments; keep command templates narrow and avoid passing unreviewed model output directly to dispatch.

Risk: The documented validation and confirmation safeguards are stronger than the dispatcher implementation.

Mitigation: Review the registry and command behavior before installation or use, and add external validation, confirmation, or sandboxing for sensitive tools.

Risk: The learner feature can persist usage notes, preferences, and failure details in learned_patterns.json.

Mitigation: Avoid recording secrets or sensitive user data, and review the learning file before sharing or publishing skill artifacts.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/qq435912743/skills/tool-use)
- [ClawHub publisher profile](https://clawhub.ai/user/qq435912743)

## Skill Output:

**Output Type(s):** [text, JSON, code, shell commands, configuration, guidance]

**Output Format:** [JSON files and text/Markdown guidance with shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Dispatch results may include stdout/stderr text; learning commands may update learned_patterns.json.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
