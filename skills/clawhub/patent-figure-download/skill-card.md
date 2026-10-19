## Description:

Downloads available Chinese patent abstract drawings by patent number or technology search and creates a browsable gallery and inventory.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ip930](https://clawhub.ai/user/ip930)

### License/Terms of Use:

MIT-0

## Use Case:

Patent researchers and presentation creators use this skill to collect Chinese patent abstract drawings and browse a gallery of figures, titles, and abstracts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Patent numbers, search topics, or technical descriptions are sent to PatentMax.

Mitigation: Avoid confidential invention details unless sharing them with PatentMax is acceptable.

Risk: The bundled client can make paid patent-search calls beyond figure downloads.

Mitigation: Review requested operations and likely charges before use, and monitor usage in PatentMax.

Risk: API credentials and trial or session state may be stored locally.

Mitigation: Review PATENTMAX_API_KEY and PATENTMAX_BASE_URL settings and protect local ~/.patentmax files.

## Reference(s):

- [PatentMax API reference](references/api-reference.md)
- [PatentMax search workflow](references/search-workflow.md)
- [PatentMax API platform](https://api.ip930.com/features/api-platform)

## Skill Output:

**Output Type(s):** [Files, Text]

**Output Format:** [HTML gallery, PNG drawings, CSV inventory, and brief text summary]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [One abstract drawing per available Chinese patent; not a complete figure set or full-text PDF.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
