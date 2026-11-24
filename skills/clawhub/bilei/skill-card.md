## Description:

An evidence-graded shopping advisor that checks product risks, evaluates sources and manufacturers, and compares price trade-offs before making a recommendation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhashushu](https://clawhub.ai/user/zhashushu)

### License/Terms of Use:

MIT-0

## Use Case:

External consumers use the skill when choosing a product or evaluating whether a particular product is worth its price. It checks public safety and recall information, grades source quality, examines manufacturer claims, and compares costs to provide an evidence-based recommendation or explain when the evidence is insufficient.

### Deployment Geography for Use:

China-focused; official standards, recall, and certification checks use Chinese sources.

## Known Risks and Mitigations:

Risk: The security scan had medium confidence and partial coverage; it also flags an unpinned installer and network and file-write capabilities.

Mitigation: Review the installer before running it, allow only the access needed for the task, and verify recommendations against the cited primary sources.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/zhashushu/skills/bilei)
- [Source credibility guide](artifact/references/source-credibility.md)
- [Manufacturer audit guide](artifact/references/manufacturer-audit.md)
- [Source blocklist guide](artifact/references/source-blocklist.md)
- [CCTV News: 3·15 Gala report on GEO poisoning](https://content-static.cctvnews.cctv.com/snow-book/index.html?item_id=12967278106578155767)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, Guidance]

**Output Format:** [Markdown report with evidence grades, comparison tables, source links, and purchase checks.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Recommendation strength is limited by the available evidence; prices and source records reflect the time of the query.]

## Skill Version(s):

4.3.10 (source: release evidence, SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
