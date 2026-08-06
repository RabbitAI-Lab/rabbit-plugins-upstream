## Description:

Use when search or investigation could run forever. Set an explicit good-enough threshold first, then stop at the first option that clears it.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tjboudreaux](https://clawhub.ai/user/tjboudreaux)

### License/Terms of Use:

MIT-0

## Use Case:

Agents and developers use this skill to make bounded, reversible decisions when search or option comparison could otherwise consume excessive time, tools, or context. It helps set explicit good-enough criteria before evaluating options and stop once an adequate option is found.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may be over-applied to high-stakes, irreversible, or correctness-critical decisions where stopping at a sufficient-looking option is inappropriate.

Mitigation: Use it only for reversible or low-stakes choices; keep tests, security checks, migrations, data-loss risks, and similar correctness gates outside its satisficing workflow.

Risk: The skill can stop useful investigation too early if the aspiration level is unclear or created after seeing candidate options.

Mitigation: State concrete pass/fail criteria before searching, and clarify the requirement first when the aspiration level cannot be stated.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/tjboudreaux/skills/thinking-bounded-rationality)
- [ClawHub publisher profile](https://clawhub.ai/user/tjboudreaux)

## Skill Output:

**Output Type(s):** [guidance, text, markdown]

**Output Format:** [Markdown or plain text decision summary]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Structured decision output with aspiration criteria, search status, selected option, residual risk, and next spend.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
