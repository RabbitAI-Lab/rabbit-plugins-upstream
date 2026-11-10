## Description:

Helps shoppers assess product risks and value by grading evidence, checking safety records and complaints, and comparing ownership costs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhashushu](https://clawhub.ai/user/zhashushu)

### License/Terms of Use:

MIT

## Use Case:

External shoppers can use the skill to evaluate a product category or model against official safety records, independent tests, and user reports. It produces an evidence-graded comparison and a recommendation that includes price and lifetime-cost considerations when reliable data is available.

### Deployment Geography for Use:

China (mainland-focused shopping and regulatory sources)

## Known Risks and Mitigations:

Risk: The security scan was partial because some local references could not be resolved, so evidence about those references is incomplete.

Mitigation: Review unresolved references and inspect the skill source before installation.

Risk: Installation guidance uses an unpinned npx skills command.

Mitigation: Use it only when the installer source is trusted, and verify and pin a trusted release before installation.

Risk: Missing incident records or independent measurements do not establish that a product is safe.

Mitigation: Show source dates, evidence grades, and unknowns, and keep recommendation strength within the available evidence.

## Reference(s):

- [Evidence grading and source credibility guide](references/source-credibility.md)
- [ClawHub release page](https://clawhub.ai/zhashushu/skills/bilei)
- [CCTV News article cited by the README](https://content-static.cctvnews.cctv.com/snow-book/index.html?item_id=12967278106578155767)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, Guidance]

**Output Format:** [Chinese Markdown report with evidence grades, cited links, comparison tables, and calculated cost metrics]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Recommendations reflect available evidence; missing or uncertain data is identified explicitly.]

## Skill Version(s):

1.0.7 (source: SKILL.md frontmatter, release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
