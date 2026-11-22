## Description:

This shopping-advisor skill compares products using graded public evidence, source-quality checks, manufacturer and after-sales audits, and price-versus-risk calculations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhashushu](https://clawhub.ai/user/zhashushu)

### License/Terms of Use:

MIT

## Use Case:

Consumers comparing products use this skill to review product safety and quality evidence, check manufacturers and after-sales responsibility, compare lifetime costs and resale value, and get a purchase recommendation grounded in available sources.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security assessment flags an unpinned installer.

Mitigation: Review the installer source and pin the version before running it.

Risk: The update checker is outside the stated shopping-advisor purpose.

Mitigation: Review its network behavior and disable the optional check if it is not needed.

Risk: The security guidance reports a cost-calculation issue that could affect product comparisons.

Mitigation: Check calculation inputs and independently verify cost results before relying on them for a purchase.

Risk: The security assessment is incomplete, with one component unscanned and static tool-misuse analysis degraded.

Mitigation: Review unassessed files and supervise web or tool actions before use.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/zhashushu/skills/bilei)
- [Manufacturer and Supply Chain Audit](references/manufacturer-audit.md)
- [Source Credibility and Manipulation Checks](references/source-credibility.md)
- [Source Blocklist](references/source-blocklist.md)
- [CCTV News: AI model manipulation report](https://content-static.cctvnews.cctv.com/snow-book/index.html?item_id=12967278106578155767)

## Skill Output:

**Output Type(s):** [Analysis, Guidance, Markdown]

**Output Format:** [Markdown report with evidence-graded findings, comparison tables, and price calculations]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Product- and requirement-specific; includes a ranked comparison, buying checks, and a recommendation or a no-reliable-option conclusion.]

## Skill Version(s):

4.3.8 (source: SKILL.md frontmatter, ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
