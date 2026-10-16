## Description:

Helps plan technology routes and patent portfolios, including design-around options, filing priorities, timing, and budgets.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ip930](https://clawhub.ai/user/ip930)

### License/Terms of Use:

MIT-0

## Use Case:

Patent and R&D teams use this skill to compare technical directions and plan patent filings, budgets, and timelines. Its recommendations are technical and business guidance, not legal opinions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Confidential inventions, plans, budgets, and strategy submitted to the reporting service may be exposed outside the user's environment.

Mitigation: Review information before submission and use only a trusted environment; avoid supplying sensitive details unless their external processing is approved.

Risk: An overridden service endpoint could receive credentials and patent strategy submissions.

Mitigation: Do not set PATENTMAX_BASE_URL unless the destination is intentionally trusted.

Risk: Trial or API credentials and generated reports may remain on disk.

Mitigation: Protect the local credential store and generated DOCX/JSON files, and remove them under the organization's retention policy.

Risk: Patent coverage and design-around recommendations may miss unpublished applications or be mistaken for legal clearance.

Mitigation: Treat results as technical and commercial guidance, account for the publication window, and obtain a qualified patent professional's review before legal or filing decisions.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/ip930/skills/patent-portfolio-strategy)
- [PatentMax API platform](https://api.ip930.com/features/api-platform)
- [Business context guide](references/context-guide.md)
- [Workflow](references/workflow.md)
- [FAQ](references/faq.md)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, JSON, Files]

**Output Format:** [Markdown guidance and JSON progress/results; downloadable Word (DOCX) report]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Report covers route comparisons, filing priorities and timing, and patent risks; generated reports remain on disk.]

## Skill Version(s):

1.1.2 (source: skill frontmatter and ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
