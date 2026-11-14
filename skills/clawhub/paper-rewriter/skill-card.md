## Description:

A bilingual academic writing toolkit that checks style, cleans mechanical artifacts, supports guided revision, and checks whether key terms and numeric details survive editing.

This skill is ready for commercial/non-commercial use.

## Publisher:

[docsor1212](https://clawhub.ai/user/docsor1212)

### License/Terms of Use:

MIT-0

## Use Case:

Researchers and scholars use it to review and revise bilingual academic prose, clean formatting residue, and check edits for changes to numbers, identifiers, and terminology. Its style signals are for writing feedback, not authorship judgments or disclosure decisions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The style checks are heuristic and can miss fluent model-generated text or flag legitimate academic phrasing; their scores do not establish who wrote a passage.

Mitigation: Treat reports as prompts for author review, not as authorship evidence or a basis for disclosure decisions. Follow applicable journal and institutional disclosure rules.

Risk: The security assessment is benign with medium confidence and reports partial inspection and gaps in terminology and numeric preservation checks.

Mitigation: Review proposed edits and integrity results yourself, with particular attention to numbers, identifiers, and terminology.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/docsor1212/skills/paper-rewriter)
- [Honest boundaries](references/honest_boundaries.md)
- [Compliance guidance](references/compliance.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Analysis, Guidance, Shell commands]

**Output Format:** [Revised academic prose, style and integrity reports, revision plans, and optional Markdown, HTML, or CSV reports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs are for author review; style signals do not establish authorship, and generated edits require human review.]

## Skill Version(s):

5.10.0 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
