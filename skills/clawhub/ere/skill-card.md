## Description:

ERE refines LLM-generated English and Portuguese (pt-BR) text into more natural editorial prose while preserving facts, entities, numbers, dates, and quotes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[rickkbarbosa](https://clawhub.ai/user/rickkbarbosa)

### License/Terms of Use:

MIT

## Use Case:

Developers, editors, and content teams use this skill to refine AI-generated articles, documentation, summaries, and other prose into publishable English or Portuguese (pt-BR) text. It supports profile-based refinement and optional quality analysis while preserving source facts and quoted material.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Refined output can drift from the source text despite preservation rules, especially around factual claims.

Mitigation: Review the refined output against the original before publishing and verify facts, entities, numbers, dates, and quotes.

Risk: The documented /tmp examples can expose private or sensitive text on shared systems.

Mitigation: Use a private working directory and restricted file permissions for original and refined analysis files.

## Reference(s):

- [ERE architecture reference](references/ERE.md)
- [AI writing pattern catalog](references/patterns.md)
- [Writing principles](references/writing-principles.md)
- [Portuguese writing principles](references/portuguese-writing-principles.md)
- [ClawHub skill page](https://clawhub.ai/rickkbarbosa/skills/ere)

## Skill Output:

**Output Type(s):** [Text, Markdown, Analysis, Shell commands]

**Output Format:** [Refined prose or Markdown, with optional quality metrics and diff summaries.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Preserves facts, entities, numbers, dates, and literal quotes; optional helper commands analyze local text files.]

## Skill Version(s):

1.4.0 (source: SKILL.md frontmatter, manifest.json, release.json, and server release metadata; released 2026-08-23)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
