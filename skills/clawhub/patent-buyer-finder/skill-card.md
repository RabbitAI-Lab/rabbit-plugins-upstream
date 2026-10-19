## Description:

Identifies potential buyers or licensees for a patent using similar patents, citations, and active applicants, then explains the evidence for each lead.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ip930](https://clawhub.ai/user/ip930)

### License/Terms of Use:

MIT-0

## Use Case:

Patent owners, inventors, and technology transfer teams use this skill to identify companies that may be interested in acquiring or licensing a patent and to prioritize outreach using patent evidence.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Patent identifiers, search terms, and related technical or commercial context are sent to PatentMax/ip930.com.

Mitigation: Use only when external API sharing is acceptable; avoid unpublished confidential invention details unless that disclosure is authorized.

Risk: Changing the API host can send patent data to an untrusted service.

Mitigation: Do not set PATENTMAX_BASE_URL to an untrusted host.

Risk: Search results and trial credentials may be stored locally.

Mitigation: Restrict access to local PatentMax cache and result files, and remove them when no longer needed.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/ip930/skills/patent-buyer-finder)
- [PatentMax API platform](https://api.ip930.com/features/api-platform)
- [PatentMax search workflow](artifact/references/search-workflow.md)
- [PatentMax API reference](artifact/references/api-reference.md)

## Skill Output:

**Output Type(s):** [Text, CSV file]

**Output Format:** [Markdown summary and Excel-compatible UTF-8 CSV]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Ranked company leads with reasons and supporting patent numbers; does not verify purchase intent or provide contacts or valuations.]

## Skill Version(s):

1.0.0 (source: release evidence and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
