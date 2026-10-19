## Description:

Helps assess a technical invention against prior art, comparing relevant publications and delivering a scoped novelty analysis and downloadable report.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ip930](https://clawhub.ai/user/ip930)

### License/Terms of Use:

MIT-0

## Use Case:

Inventors, researchers, and patent teams use this skill to compare invention disclosures or draft applications with patents and other public material before filing or project review. It summarizes the closest references and produces a Word report for internal assessment, not an official certified search or a patentability guarantee.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Unfiled or confidential invention details are sent to PatentMax/api.ip930.com for analysis.

Mitigation: Obtain permission before submitting sensitive material and redact nonessential secrets where possible.

Risk: Trial credentials, task metadata, reports, and JSON results may remain on the local device.

Mitigation: Protect and review files under ~/.patentmax and the chosen report output directory.

Risk: A paid search can incur charges and cannot establish that no undisclosed prior art exists.

Mitigation: Get explicit approval of cost before submitting; treat findings as scoped technical input and seek qualified professional review for formal decisions.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/ip930/skills/prior-art-search)
- [PatentMax API platform](https://api.ip930.com/features/api-platform)
- [Technical solution guide](references/solution-guide.md)
- [Prior-art search workflow](references/workflow.md)
- [Troubleshooting and quality guidance](references/faq.md)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, Files]

**Output Format:** [Markdown summary and downloadable DOCX report, with JSON task results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Report conclusions depend on the supplied invention details and the searched prior-art scope.]

## Skill Version(s):

1.1.2 (source: skill frontmatter and ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
