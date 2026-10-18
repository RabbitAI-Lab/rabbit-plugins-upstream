## Description:

Helps scholars revise Chinese and English academic manuscripts for clearer, more natural prose using local style checks, cleanup, revision guidance, and integrity checks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[docsor1212](https://clawhub.ai/user/docsor1212)

### License/Terms of Use:

MIT-0

## Use Case:

Scholars and academic writers use this skill to find formulaic phrasing, clean up manuscript artifacts, plan revisions, and check that numbers, citation identifiers, and terminology survive editing. It supports self-review rather than authorship detection or decisions about disclosure obligations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Read/write/Bash access can change manuscripts passed to the skill.

Mitigation: Pass only intended files, retain the originals, and review edits and reports before using the revised manuscript.

Risk: Heuristic style scores or experimental PDF extraction can give incomplete or misleading results.

Mitigation: Treat scores as writing feedback, inspect PDF extraction quality, and manually verify facts and citation details.

Risk: Style revisions do not resolve authorship or required AI-use disclosure.

Mitigation: Follow applicable institutional and journal disclosure policies; do not use the skill to conceal AI assistance.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/docsor1212/skills/paper-rewriter)
- [Workflow and best practices](references/best_practices.md)
- [Honest boundaries of style scoring](references/honest_boundaries.md)
- [PDF extraction confidence](references/pdf_confidence.md)
- [Academic integrity and disclosure](references/compliance.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Shell commands, Guidance]

**Output Format:** [Revised manuscript text, revision plans, and Markdown or JSON reports; optional HTML reports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Local files and reports; integrity checks flag changed numbers, identifiers, or terminology. Style scores do not establish authorship.]

## Skill Version(s):

3.9.0 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
