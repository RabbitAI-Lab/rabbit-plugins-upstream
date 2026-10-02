## Description:

Generates eight prompt-injection drill scenarios and expected-behavior checks for pre-launch testing of an agent's system prompt.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhaoxinghua09-cell](https://clawhub.ai/user/zhaoxinghua09-cell)

### License/Terms of Use:

MIT (Python code only); documentation and theoretical text: all rights reserved

## Use Case:

Developers and security reviewers use this skill to prepare adversarial prompt examples and expected responses for manual pre-launch testing of an agent's system prompt.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: System prompts supplied for testing may contain sensitive instructions or information.

Mitigation: Supply only prompts you intend to test and review generated output before sharing it.

Risk: Drill examples contain adversarial instructions that could be mistaken for operational requests.

Mitigation: Use the examples only as test inputs and compare agent responses against the expected-behavior checklist.

Risk: A remote installation command may fetch an unverified source.

Mitigation: Confirm the remote source and release before running an installation command.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/zhaoxinghua09-cell/skills/prompt-injection-drill)
- [Publisher homepage](https://zhaoxinghua09-cell.github.io/lgd-hub/)

## Skill Output:

**Output Type(s):** [Markdown, JSON, Text]

**Output Format:** [Markdown drill checklist or JSON containing the checklist; optionally writes a Markdown file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Eight fixed attack categories with expected behaviors; testing and pass/fail review are manual.]

## Skill Version(s):

1.0.3 (source: ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
