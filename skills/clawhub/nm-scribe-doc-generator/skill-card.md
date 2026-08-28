## Description:

Generates or remediates documentation with human-quality writing.

This skill is ready for commercial/non-commercial use.

## Publisher:

[athola](https://clawhub.ai/user/athola)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and documentation authors use this skill to draft, revise, and quality-check Markdown documentation, docstrings, and technical prose. It emphasizes thesis-first structure, specific claims, low-boilerplate language, and review before applying major changes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad activation terms may cause the skill to engage on general writing or polishing requests.

Mitigation: Use it when an opinionated documentation-writing assistant is desired, and review proposed edits before applying them.

Risk: Documentation edits can accidentally change technical meaning or introduce misleading guidance.

Mitigation: Preserve the original technical intent, request approval for major restructuring or deletions, and verify commands, file paths, links, and version numbers.

Risk: The referenced Claude Code plugin and related skills are separate components.

Mitigation: Review those components independently before installing or relying on them.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/athola/skills/nm-scribe-doc-generator)
- [Publisher profile](https://clawhub.ai/user/athola)
- [Scribe plugin homepage](https://github.com/athola/claude-night-market/tree/master/plugins/scribe)
- [Generation guidelines](artifact/modules/generation-guidelines.md)
- [Quality gates](artifact/modules/quality-gates.md)
- [Remediation workflow](artifact/modules/remediation-workflow.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Markdown guidance, proposed edits, checklists, and inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May request user approval before major documentation restructuring or technical-content changes.]

## Skill Version(s):

1.9.19 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
