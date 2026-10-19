## Description:

Guides deep research and checks references against source material and citation registries before they are used in a report.

This skill is ready for commercial/non-commercial use.

## Publisher:

[docsor1212](https://clawhub.ai/user/docsor1212)

### License/Terms of Use:

MIT-0

## Use Case:

Researchers, writers, and developers use the skill to investigate questions, fact-check claims, and review bibliographies before citing them. It produces evidence-graded research reports and flags references that need human review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Optional judging services may receive claim and evidence text, including sensitive drafts or medical material.

Mitigation: Keep remote judging and local Ollama judging disabled for sensitive content unless you trust the destination and explicitly accept the disclosure.

Risk: Live GitHub installs may differ from the reviewed ClawHub release; server-resolved GitHub import provenance is unavailable.

Mitigation: Use the reviewed ClawHub artifact when release provenance matters.

## Reference(s):

- [Cite Holmes on ClawHub](https://clawhub.ai/docsor1212/skills/cite-holmes)
- [Report template and citation schema](artifact/references/report-template.md)
- [Citation verification details](artifact/references/verification-details.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Data files]

**Output Format:** [Research reports and citation-verification results in Markdown; optional JSON, BibTeX, RIS, and CSV exports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports distinguish verified, partial, unreachable, invalid, and unchecked references; uncertain results require human review.]

## Skill Version(s):

4.4.0 (source: skill frontmatter and ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
