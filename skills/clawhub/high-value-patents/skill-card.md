## Description:

Screens a technology area or company patent portfolio for potentially high-value patents and explains each selection using visible indicators such as maintenance duration, citations, ranking, and claim breadth.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ip930](https://clawhub.ai/user/ip930)

### License/Terms of Use:

MIT-0

## Use Case:

External patent analysts and businesses use the skill to shortlist potentially valuable patents in a technology area or company portfolio, review the reasons for each selection, and export a preliminary screening list. It is not a formal patent valuation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Credential-protection and cache-path weaknesses could expose keys or valuable files.

Mitigation: Do not paste paid API keys into chat, and wait for the credential-redirect and cache-path fixes before using valuable keys or files.

Risk: Retrying a timed-out patent lookup could result in unintended charges.

Mitigation: Set a spending limit and check charges before retrying a timed-out lookup.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/ip930/skills/high-value-patents)
- [PatentMax API platform](https://api.ip930.com/features/api-platform)
- [PatentMax API documentation](https://api.ip930.com)

## Skill Output:

**Output Type(s):** [Analysis, Files, Text]

**Output Format:** [UTF-8 CSV patent shortlist with a concise conversational summary]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The shortlist is ranked by visible screening indicators, includes a reason for each selection, and is a preliminary screen rather than a formal valuation.]

## Skill Version(s):

1.0.1 (source: SKILL.md frontmatter, server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
