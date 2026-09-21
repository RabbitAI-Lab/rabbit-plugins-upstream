## Description:

Runs a multi-agent, double-blind A/B testing workflow that compares two AI models or agents across multiple rounds with coordinator, contestant, and judge roles.

This skill is ready for commercial/non-commercial use.

## Publisher:

[johnsmithfan](https://clawhub.ai/user/johnsmithfan)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, evaluators, and agent builders use this skill to compare two models or agents through repeated blind trials, rubric-based judging, anonymized presentation order, and a structured final report.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Blind evaluation can be compromised if contestant identities, model names, or anonymizer mappings are exposed to the judge.

Mitigation: Filter identity markers before judging, keep mappings private until the final reveal, and invalidate or rerun rounds where identity leaks occur.

Risk: Prompts, model outputs, reports, and terminal logs may contain sensitive or proprietary information.

Mitigation: Use controlled evaluation inputs, keep sensitive prompts and proprietary outputs out of the workflow unless storage and log access are governed, and review generated reports before sharing.

Risk: Script-driven normal mode contains placeholder execution paths and should not be treated as a reliable benchmark result by itself.

Mitigation: Use the documented agent workflow or implement and validate real subagent execution before relying on script-produced comparisons.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/johnsmithfan/skills/ab-test-agent-workflow-1-1-0)
- [Workflow guide](artifact/references/workflow_guide.md)
- [Rubric templates](artifact/references/rubric_templates.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown reports, JSON summaries, prompt templates, and optional shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Multi-round outputs can include contestant responses, anonymized judge scores, comments, winners, aggregate scores, and confidence notes.]

## Skill Version(s):

1.1.0 (source: SKILL.md frontmatter and artifact/_meta.json; release metadata version: 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
