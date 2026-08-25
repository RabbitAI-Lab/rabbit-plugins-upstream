## Description:

Converts long Markdown reports, research notes, industry analyses, strategy memos, white papers, retrospectives, and weekly reports into planned, editorially designed, self-contained HTML feature pages while preserving the source facts and conclusion strength.

This skill is ready for commercial/non-commercial use.

## Publisher:

[sensenova-skills](https://clawhub.ai/user/sensenova-skills)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and content teams use this skill when an agent needs to turn a substantive Markdown report or long document into a polished shareable HTML page. The workflow requires a design plan before HTML generation and emphasizes fact fidelity, domain-specific visual direction, responsive layout, and accessibility review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may be invoked by generic HTML-conversion wording even when the input is not a substantive report or long document.

Mitigation: Use it for report-like Markdown inputs and review the generated plan.md before accepting the HTML direction.

Risk: The workflow reshapes source material into an editorial page, which can unintentionally change emphasis or conclusion strength.

Mitigation: Review the plan.md and final HTML against the source report for fact fidelity, missing limitations, unsupported numbers, and overstated conclusions before sharing.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/sensenova-skills/skills/sn-md-to-html-report)
- [01 - Aesthetic Direction](artifact/references/01-aesthetic-direction.md)
- [02 - Layout and Content Design](artifact/references/02-layout-and-content-design.md)
- [03 - Design Contract](artifact/references/03-design-contract.md)
- [04 - Review Angles](artifact/references/04-review-angles.md)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Code]

**Output Format:** [Markdown planning guidance plus self-contained HTML code]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill directs the agent to create plan.md before producing a single-file HTML page with semantic HTML, inline CSS, responsive behavior, and accessibility checks.]

## Skill Version(s):

2026.8.19 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
