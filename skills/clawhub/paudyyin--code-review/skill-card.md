## Description: <br>
Review code on two axes - Standards for code quality and Spec for requirements alignment - with multi-agent parallel review, visual review, and file-based handoffs. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[paudyyin](https://clawhub.ai/user/paudyyin) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineering teams use this skill to review code changes against code-quality standards and stated requirements. It supports task-level and branch-level review, optional multi-agent review, visual diff inspection, and structured report generation. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Broad activation triggers may start the review workflow when a user intended a lighter or unrelated review request. <br>
Mitigation: Narrow the activation triggers or require explicit invocation before installing for routine use. <br>
Risk: The workflow can create persistent local review artifacts, including annotation stores and generated reports. <br>
Mitigation: Require explicit output paths, review generated files before sharing, and gate or remove the record.md update behavior. <br>
Risk: The workflow can read repository diffs and history and can spawn review agents. <br>
Mitigation: Use it only in repositories where code-review agents are allowed to inspect diffs and history, and treat generated findings as advisory until reviewed. <br>


## Reference(s): <br>
- [Confidence Scoring Reference](artifact/references/confidence-scoring.md) <br>
- [ClawHub Skill Page](https://clawhub.ai/paudyyin/skills/code-review) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance, files] <br>
**Output Format:** [Markdown review findings with optional JSON and HTML review artifacts] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May read repository diffs and history, spawn review agents, and create local annotation or report files during visual review workflows.] <br>

## Skill Version(s): <br>
2.2.0 (source: frontmatter and release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
