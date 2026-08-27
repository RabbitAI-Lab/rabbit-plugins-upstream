## Description:

Orchestrates multi-domain review (code, arch, tests, security) in a single pass

This skill is ready for commercial/non-commercial use.

## Publisher:

[athola](https://clawhub.ai/user/athola)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineering teams use this skill to run comprehensive pre-release or multi-domain code reviews, selecting relevant review domains and consolidating findings into an action plan.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill directs the agent to run a local deferred-capture script for backlog findings without clear confirmation or storage details.

Mitigation: Before deployment, inspect scripts/deferred_capture.py, confirm what data it writes, and require explicit approval or disable deferred capture when persistence is not desired.

Risk: Multi-domain review orchestration can produce incorrect or misleading findings if synthesized outputs are accepted without review.

Mitigation: Require reviewers to validate findings against cited evidence, file paths, and project tests before acting on recommendations.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/athola/skills/nm-pensive-unified-review)
- [Pensive plugin homepage](https://github.com/athola/claude-night-market/tree/master/plugins/pensive)
- [Review workflow core](artifact/modules/review-workflow-core.md)
- [Output format templates](artifact/modules/output-format-templates.md)
- [Quality checklist patterns](artifact/modules/quality-checklist-patterns.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown review report with findings, evidence appendix, action items, and optional shell command snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May coordinate multiple review domains and preserve deferred backlog findings when the project supports that workflow.]

## Skill Version(s):

1.9.19 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
