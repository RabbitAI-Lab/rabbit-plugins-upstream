## Description:

Compares the independent claims of two or three patents feature by feature and produces a comparison table showing shared features, differences, and relative claim breadth.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ip930](https://clawhub.ai/user/ip930)

### License/Terms of Use:

MIT-0

## Use Case:

Patent professionals and technical teams compare two or three patents' claims to prepare feature-by-feature tables for prosecution, invalidity preparation, or technical differentiation. The comparison does not determine infringement, equivalence, or inventiveness.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Patent numbers, search queries, and pasted technical descriptions are sent to an external PatentMax service, including potentially confidential pre-filing material.

Mitigation: Obtain approval for external processing and avoid entering confidential pre-filing details unless that processing is acceptable.

Risk: Patent retrieval and broader search features may incur API charges.

Mitigation: Explain the expected cost before requests and monitor API spending.

Risk: The service destination can be changed through configuration, and trial credentials or task data may be retained locally.

Mitigation: Keep the service URL unset or pinned to the official endpoint, and protect or clear data stored under ~/.patentmax as appropriate.

Risk: Feature similarity and claim-breadth comparisons can be mistaken for legal conclusions.

Mitigation: Treat comparisons as technical guidance and consult a patent professional for infringement, equivalence, or inventiveness assessments.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/ip930/skills/patent-claim-compare)
- [PatentMax API documentation](https://api.ip930.com/features/api-platform)
- [PatentMax API reference](references/api-reference.md)
- [PatentMax comparison workflow](references/tools.md)

## Skill Output:

**Output Type(s):** [CSV file, Text analysis]

**Output Format:** [UTF-8 BOM CSV comparison table and a concise Markdown summary]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Compares two or three patents, defaults to independent claims, and cites claim numbers for compared features.]

## Skill Version(s):

1.0.0 (source: release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
