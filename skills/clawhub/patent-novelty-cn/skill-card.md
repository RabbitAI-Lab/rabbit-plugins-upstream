## Description:

Analyzes a technical invention against prior patents and other public disclosures, then summarizes novelty findings and produces a downloadable Word report.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ip930](https://clawhub.ai/user/ip930)

### License/Terms of Use:

MIT-0

## Use Case:

Inventors, patent practitioners, and R&D teams use this skill to screen invention disclosures against prior art before filing or project review and to obtain a comparative novelty report. Findings are bounded by the search scope and are not a guarantee of patentability or a certified search report.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Invention descriptions and draft patents are sent to PatentMax for processing.

Mitigation: Submit confidential or restricted material only when organizational data-processing requirements allow it; omit unreleased trade secrets when approval is absent.

Risk: A custom service endpoint can redirect sensitive submissions.

Mitigation: Leave PATENTMAX_BASE_URL unset unless intentionally using a trusted endpoint.

Risk: Cached credentials and generated reports can remain on a shared computer.

Mitigation: Protect and clean up ~/.patentmax and generated DOCX or JSON reports after use on shared workspaces.

Risk: Submitting or resubmitting a paid search can incur charges.

Mitigation: Confirm the price and obtain user consent before submission; continue an existing operation rather than submitting it again.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/ip930/skills/patent-novelty-cn)
- [PatentMax API platform](https://api.ip930.com/features/api-platform)
- [Patent novelty workflow](artifact/references/workflow.md)
- [Preparing a technical disclosure](artifact/references/solution-guide.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Files]

**Output Format:** [Markdown findings, JSON task results, and a downloadable DOCX report]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Asynchronous report generation; the report can be downloaded when complete.]

## Skill Version(s):

1.1.2 (source: release metadata and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
