## Description:

Screens public FDA adverse-event reports for potential drug–event safety signals using disproportionality measures and optional corroborating sources.

This skill is ready for commercial/non-commercial use.

## Publisher:

[medstatstar](https://clawhub.ai/user/medstatstar)

### License/Terms of Use:

MIT

## Use Case:

Drug-safety professionals and clinical-trial methodologists use the skill to screen public adverse-event data, review drug–event disproportionality, and prioritize signals for expert follow-up. Its findings do not establish causation or support treatment decisions on their own.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Routine public drug and event queries send a stable hashed machine identifier to publisher-operated endpoints without clear user disclosure.

Mitigation: Use only public, non-confidential queries and proceed only if this data flow is acceptable.

Risk: Endpoint overrides may send queries to an unexpected service.

Mitigation: Review CT_SEARCH_ENDPOINT and CT_SEARCH_ENDPOINT_STREAM settings before use.

Risk: Optional bug-report submission may transmit diagnostic information.

Mitigation: Inspect the displayed report and approve submission only after reviewing its contents.

Risk: Spontaneous adverse-event reports can yield biased signals that do not establish causation.

Mitigation: Corroborate findings against clinical evidence and product labels with qualified drug-safety review; do not use signals alone to guide care.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/medstatstar/skills/ct-safety)
- [Project homepage (skill metadata; import provenance unavailable)](https://github.com/medstatstar/ct-safety)
- [Safety signal methods](references/methods.md)
- [Evidence hierarchy and claim boundaries](references/evidence-hierarchy.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Files]

**Output Format:** [Markdown summaries and optional HTML, XLSX, and JSON reports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Detailed retrieval requires explicit confirmation; generated reports go to the selected output directory.]

## Skill Version(s):

0.10.1 (source: skill frontmatter and ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
