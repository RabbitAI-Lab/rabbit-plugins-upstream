## Description:

Helps AI-agent users, skill authors, maintainers, and teams turn Nano Banana Pro-style workflow demand into practical artifacts, checklists, analysis, code changes, or decision support.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kyro-ma](https://clawhub.ai/user/kyro-ma)

### License/Terms of Use:

MIT-0

## Use Case:

External agent users, skill authors, maintainers, and teams use this skill to convert demand for Nano Banana Pro-style workflows into practical plans, templates, checklists, implementation support, and verification notes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill allows implicit invocation and has broad generic trigger terms, so it may activate for unrelated requests.

Mitigation: Review activation scope before installing and narrow invocation to explicit Nano Banana Pro workflow requests.

Risk: Workflow outputs may include implementation advice, code, shell commands, or configuration that could be incomplete for the user's environment.

Mitigation: Review generated artifacts before use, scan code changes, and validate outputs against the stated success criteria.

## Reference(s):

- [Requirement Plan](references/requirement-plan.md)
- [ClawHub Skill Page](https://clawhub.ai/kyro-ma/skills/work-productivity-nano-banana-workflow-helper)
- [Nano Banana Pro Demand Signal](https://clawhub.ai/skills/nano-banana-pro)
- [Nano PDF Demand Signal](https://clawhub.ai/skills/nano-pdf)
- [Nano Banana Pro SegmentFault Topic](https://segmentfault.com/t/nano-banana-pro)
- [GitHub Issue Demand Signal](https://github.com/petter-arch/iamp.ai/issues/3)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown or text with optional code blocks, shell commands, checklists, templates, and configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs should state assumptions, validation checks, and remaining risks when helpful.]

## Skill Version(s):

0.20260904.60001 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
