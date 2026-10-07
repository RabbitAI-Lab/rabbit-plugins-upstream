## Description:

Audits source code for comprehension cost and change risk, producing an evidence-backed, red/amber/green clean-code report and interactive checklist.

This skill is ready for commercial/non-commercial use.

## Publisher:

[elisabeth15501](https://clawhub.ai/user/elisabeth15501)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to review their own agent-skill scripts or other source code for readability and maintainability, with file-and-line evidence and prioritized findings. It does not edit the code under audit or replace a correctness or security review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The audit reads selected source files and writes a local report and checklist that may contain sensitive project details.

Mitigation: Choose only code you intend the agent to read, and review the local report and checklist before sharing them.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/elisabeth15501/skills/skill-clean-audit)
- [Clean code audit sample (English)](references/clean_code_audit_sample.en.md)
- [Code smells crosswalk](references/smells_crosswalk.md)
- [FAQ (English)](references/faq.en.md)

## Skill Output:

**Output Type(s):** [Markdown report, HTML checklist, Guidance]

**Output Format:** [Local Markdown report with file-and-line findings and an interactive HTML checklist]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Chinese or English output; optional metric hints do not determine severity.]

## Skill Version(s):

1.3.0 (source: skill frontmatter and ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
