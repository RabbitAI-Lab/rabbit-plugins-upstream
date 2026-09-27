## Description:

Reviews UTF-8 text or Markdown with deterministic PIPL and data-export rule packs, returning source evidence, matched rules, framework coverage levels, cited provisions, and Markdown or JSON reports for human compliance review.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yottameta](https://clawhub.ai/user/yottameta)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, compliance reviewers, and legal operations teams use this skill to check privacy policies, data-processing clauses, and personal-information compliance text for observable PIPL and data-export coverage gaps. It is a rule-based review aid for reproducible reports and CI gates, not legal advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Reports can be mistaken for legal advice or a final compliance determination.

Mitigation: Use findings as review aids and require qualified human review before relying on conclusions.

Risk: Installer choices such as global installation or an implicit target directory can overwrite an existing skill folder.

Mitigation: Install a reviewed or pinned version, prefer an explicit --agent or --dir target, and back up any existing yotta-compliance folder first.

Risk: mapping_only framework labels can be misread as completed GDPR, HIPAA, SOC2, PCI-DSS, ISO27001, or China MLPS reviews.

Mitigation: Treat mapping_only labels only as topic mappings and do not claim certification or independent framework review from them.

Risk: Deterministic text matching can miss paraphrases, negated statements, non-UTF-8 inputs, PDFs, docx files, or image-only content.

Mitigation: Convert source material to UTF-8 text or Markdown and manually review low-confidence findings, absences, and uncovered areas.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/yottameta/skills/yotta-compliance)
- [yotta-compliance homepage](https://github.com/YottaMeta/yotta-compliance)
- [Coverage reference](references/coverage.md)
- [Report format reference](references/report-format.md)
- [Rule authoring reference](references/rule-authoring.md)
- [Personal Information Protection Law official text](https://www.npc.gov.cn/npc/c2/c30834/202108/t20210820_313088.html)
- [CAC cross-border data transfer provisions](https://www.cac.gov.cn/2024-03/22/c_1712776611775634.htm)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Shell commands, Guidance]

**Output Format:** [Markdown report or stable JSON contract, with CLI commands for review, rules listing, rule inspection, rule validation, and CI gating.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Deterministic local output for UTF-8 text or Markdown inputs; reports go to stdout unless --out is set, and the review path does not use network access or model calls.]

## Skill Version(s):

0.1.0 (source: server release metadata, SKILL.md frontmatter, package.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
