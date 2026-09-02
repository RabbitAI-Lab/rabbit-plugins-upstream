## Description:

Helps AI-agent users, skill authors, maintainers, and teams create practical workflows, checklists, analysis, or implementation support for Humanizer-style productivity needs, including bug fixing, setup hardening, reliability improvements, and adjacent skill design.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kyro-ma](https://clawhub.ai/user/kyro-ma)

### License/Terms of Use:

MIT-0

## Use Case:

AI-agent users, skill authors, maintainers, and teams use this skill to turn Humanizer-style productivity demand into concrete workflows, checklists, plans, code changes, or decision support. It is intended for practical local workflows that clarify the requested outcome, produce a reusable artifact when useful, and validate the result against stated success criteria.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad automatic activation terms may route unrelated productivity, writing, editing, reviewing, or bug-fix prompts to this helper when the user did not intend to use it.

Mitigation: Narrow trigger terms or disable implicit invocation, and confirm intent before applying Humanizer-style workflow guidance to ambiguous requests.

Risk: The skill can produce workflow guidance, code changes, shell commands, or configuration suggestions that may be incorrect for the user's environment.

Mitigation: Review proposed changes before use, run local validation where applicable, and keep assumptions and remaining risks visible in the final output.

## Reference(s):

- [Skill release page](https://clawhub.ai/kyro-ma/skills/work-productivity-humanizer-remove-workflow-helper)
- [Publisher profile](https://clawhub.ai/user/kyro-ma)
- [Requirement plan](artifact/references/requirement-plan.md)
- [Humanizer demand signal](https://clawhub.ai/skills/humanizer)
- [Nano Banana Pro demand signal](https://clawhub.ai/skills/nano-banana-pro)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with optional code blocks, command snippets, checklists, workflow steps, and verification notes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs should state assumptions, limits, required inputs, remaining risks, and next steps when helpful.]

## Skill Version(s):

0.20260829.40354 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
