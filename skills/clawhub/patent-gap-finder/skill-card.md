## Description:

Analyzes patent-search counts across a technology's problems and technical approaches to identify candidate white spaces for R&D and patent planning.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ip930](https://clawhub.ai/user/ip930)

### License/Terms of Use:

MIT-0

## Use Case:

Researchers, engineers, and patent-planning teams use the skill to compare patent counts for problem-by-approach combinations, check sparse results, and prioritize candidate research or filing opportunities.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Patent searches may disclose sensitive R&D descriptions, search terms, or patent numbers to PatentMax/ip930.com.

Mitigation: Avoid trade secrets and unpublished invention details unless third-party processing is acceptable.

Risk: The skill can automatically create and store a local trial API key, and searches may incur charges after free allowances.

Mitigation: Review credential handling, use a dedicated or test key where possible, and obtain approval for the search count and estimated cost.

Risk: A custom API endpoint can receive authenticated requests.

Mitigation: Do not set PATENTMAX_BASE_URL unless the destination is trusted.

Risk: Low patent counts may reflect incomplete keywords or unpublished applications rather than a viable invention opportunity.

Mitigation: Recheck promising gaps with synonyms and assess technical feasibility and market demand independently.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/ip930/skills/patent-gap-finder)
- [PatentMax API](https://api.ip930.com)
- [Search query syntax](references/query-syntax.md)
- [Search workflow](references/search-workflow.md)

## Skill Output:

**Output Type(s):** [Files, Text, Guidance]

**Output Format:** [UTF-8 CSV matrix and conversational summary]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes per-cell patent counts, checked candidate gaps, and cautions about technical feasibility and market demand.]

## Skill Version(s):

1.0.0 (source: ClawHub release and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
