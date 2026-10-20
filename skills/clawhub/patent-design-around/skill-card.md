## Description:

Helps engineers explore preliminary patent design-around options by breaking down independent claims, considering feature changes, and checking alternatives against patent search results; it does not provide legal advice.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ip930](https://clawhub.ai/user/ip930)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use the skill to examine a patent's independent claims, explore ways to remove or materially change technical features, and review patents relevant to alternative approaches. The resulting ideas are preliminary and should be assessed by a patent professional before business or product decisions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review flags API-key handling and cache-path weaknesses that warrant review before installation.

Mitigation: Use a dedicated spending-limited API key supplied through the environment rather than chat, set a task budget, and prefer a version that confines cache paths, validates cached patent identity, restricts authenticated redirects, and protects saved credentials.

Risk: Confidential invention details included in external patent queries could be disclosed to the search service.

Mitigation: Keep confidential invention details out of external queries.

## Reference(s):

- [PatentMax search workflow](artifact/references/search-workflow.md)
- [PatentMax query syntax](artifact/references/query-syntax.md)
- [PatentMax tools reference](artifact/references/tools.md)
- [PatentMax API reference](artifact/references/api-reference.md)
- [PatentMax service](https://api.ip930.com)
- [ClawHub skill listing](https://clawhub.ai/ip930/skills/patent-design-around)

## Skill Output:

**Output Type(s):** [Analysis, Guidance, Files, CSV]

**Output Format:** [Excel-compatible CSV design-around ideas table with a brief explanatory response]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Initial suggestions with patent search results for alternatives; not legal advice and not an infringement determination.]

## Skill Version(s):

1.0.1 (source: frontmatter; server release 1.0.1)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
