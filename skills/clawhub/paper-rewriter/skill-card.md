## Description:

Helps scholars revise Chinese and English academic prose through style self-checks, mechanical cleanup, guided rewriting, and checks that facts and citations remain intact.

This skill is ready for commercial/non-commercial use.

## Publisher:

[docsor1212](https://clawhub.ai/user/docsor1212)

### License/Terms of Use:

MIT-0

## Use Case:

Scholars and academic editors use this skill to identify stiff or templated prose, clean writing artifacts, and revise manuscripts for clarity while checking that numbers, references, and protected terminology remain unchanged.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Running the local scripts reads supplied documents and can write cleaned files or reports to chosen paths.

Mitigation: Review input and output paths before running, and retain the original draft.

Risk: A style score may be mistaken for proof of authorship or used to avoid required AI-use disclosure.

Mitigation: Treat scores as writing self-checks only; follow institutional or journal disclosure requirements.

Risk: Revisions may change numbers, citations, or specialized terminology.

Mitigation: Run the integrity check against the original and review flagged changes before using the revision.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/docsor1212/skills/paper-rewriter)
- [English style guide](references/style_guide_en.md)
- [Chinese style guide](references/style_guide_zh.md)
- [Academic integrity and disclosure guidance](references/compliance.md)
- [Examples](references/examples.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance, Files]

**Output Format:** [Revised prose and guidance; optional plain-text, Markdown, HTML, JSON, or CSV reports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Optional before-and-after comparison and integrity verdict; reports are heuristic self-checks, not authorship determinations.]

## Skill Version(s):

1.5.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
