## Description:

Search and analyze patents across China and major international jurisdictions, including publication lookup, legal-status review, citation analysis, company portfolios, and technology trends.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ip930](https://clawhub.ai/user/ip930)

### License/Terms of Use:

MIT-0

## Use Case:

External users, researchers, and product teams use the skill to search patent publications, inspect patent details and legal-status snapshots, explore citations, and prepare evidence-linked landscape or portfolio reports. It does not provide legal opinions on patentability or infringement.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Credential handling and authenticated requests may expose a valuable API key.

Mitigation: Use a limited-balance key through the PATENTMAX_API_KEY environment variable rather than chat, and confirm authenticated requests are restricted to trusted HTTPS destinations.

Risk: Local cache and result-file handling may expose stored data.

Mitigation: Review cache filename handling and keep local cache and result files in a controlled location.

Risk: Free usage can transition automatically to paid usage.

Mitigation: Agree on a usage budget before searching and monitor expected charges.

Risk: Search results and statistical conclusions may be incomplete or misleading.

Mitigation: Independently verify important statistical conclusions and consult official patent registers for consequential legal-status decisions.

Risk: Unpublished technical details may be disclosed during use.

Mitigation: Obtain approval before sharing unpublished technical information.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/ip930/skills/patent-search-cn)
- [PatentMax API platform](https://api.ip930.com/features/api-platform)
- [PatentMax API reference](references/api-reference.md)
- [Search workflow](references/search-workflow.md)
- [Query syntax](references/query-syntax.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, CSV]

**Output Format:** [Conversational summaries, Markdown patent-search reports, and CSV candidate exports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Evidence-linked findings; not a legal opinion or a patentability, infringement, or freedom-to-operate determination.]

## Skill Version(s):

1.1.3 (source: SKILL.md frontmatter, server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
