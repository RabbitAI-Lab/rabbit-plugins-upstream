## Description:

Helps graduate students survey patents for thesis proposals, producing a sourced patent table and a draft of the patent-related research background.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ip930](https://clawhub.ai/user/ip930)

### License/Terms of Use:

MIT-0

## Use Case:

Graduate students and researchers use this skill to find and organize relevant patents by technical approach, document publication numbers and sources, and draft the patent section of a thesis proposal.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Research topics and patent search terms are sent to PatentMax.

Mitigation: Do not submit unpublished inventions, formulas, source code or trade secrets unless you accept that transfer.

Risk: The skill automatically creates and stores a trial API key and may retain local caches.

Mitigation: Protect your API key and review or remove ~/.patentmax if you do not want the trial key or caches to persist.

Risk: A changed API base URL can send requests to an unintended host.

Mitigation: Leave PATENTMAX_BASE_URL unset or point it only to the legitimate PatentMax host.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/ip930/skills/thesis-patent-survey)
- [Patent search workflow](references/search-workflow.md)
- [Query syntax](references/query-syntax.md)
- [PatentMax API reference](references/api-reference.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Files]

**Output Format:** [UTF-8 CSV tables and Markdown prose]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes publication numbers, source references, search scope and date; does not determine patentability or cover unpublished applications.]

## Skill Version(s):

1.0.1 (source: release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
