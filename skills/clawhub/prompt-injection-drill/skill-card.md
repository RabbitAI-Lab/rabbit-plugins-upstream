## Description:

Generates eight prompt-injection drill cases and expected-behavior checks for pre-launch testing of an agent's system prompt.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhaoxinghua09-cell](https://clawhub.ai/user/zhaoxinghua09-cell)

### License/Terms of Use:

MIT-0 (release metadata); artifact states MIT for code only and reserves rights to documentation and theory

## Use Case:

Developers and security reviewers use the generated cases to check whether an agent respects its system instructions before deployment. The checklist supports human assessment; it does not test the agent automatically.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated attack strings could be mistaken for instructions to the agent.

Mitigation: Treat them only as test inputs and assess the agent's responses against the expected behaviors.

Risk: The optional output path can write to a location the user did not intend.

Mitigation: Review the path supplied to --out before running the drill.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/zhaoxinghua09-cell/skills/prompt-injection-drill)
- [Publisher homepage](https://zhaoxinghua09-cell.github.io/lgd-hub/)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON]

**Output Format:** [Markdown drill checklist on stdout or in a file; optional JSON wrapper on stdout]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Eight fixed attack cases with expected behaviors; accepts an inline or file-based system prompt and can write to a chosen output path.]

## Skill Version(s):

1.0.2 (source: ClawHub release metadata; artifact frontmatter says 1.1.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
