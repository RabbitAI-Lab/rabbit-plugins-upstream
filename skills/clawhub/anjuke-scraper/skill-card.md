## Description:

Anjuke Scraper collects Anjuke/58 rental listings and details, extracts broker contact information, resolves community coordinates through Amap, calculates distance to a target place, and generates a filtered Excel comparison table.

This skill is for research and development only.

## Publisher:

[shiqixiangxiang-collab](https://clawhub.ai/user/shiqixiangxiang-collab)

### License/Terms of Use:

MIT

## Use Case:

External developers and users evaluating rentals use this skill to configure and run a local scraping pipeline for a chosen Chinese city, keyword, budget, and target location. The pipeline helps compare rental listings by distance, rent, address, contact details, and related housing attributes.

### Deployment Geography for Use:

China

## Known Risks and Mitigations:

Risk: The skill automates a Chrome profile with active login cookies.

Mitigation: Use a dedicated Chrome profile that contains only the site sessions needed for the task.

Risk: The skill saves local files containing housing-search details, addresses, broker names, and phone numbers.

Mitigation: Keep the output directory private and delete intermediate files when they are no longer needed.

Risk: Scraped contact data can carry site-terms and privacy obligations.

Mitigation: Check the target site terms and applicable privacy obligations before using the scraped contact data.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/shiqixiangxiang-collab/skills/anjuke-scraper)
- [README](artifact/README.md)
- [Skill definition](artifact/SKILL.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, files, guidance]

**Output Format:** [Markdown instructions with bash commands and local JSON, HTML, and Excel files produced by the pipeline]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The pipeline writes intermediate JSON/HTML files and a filtered Excel workbook to the configured output directory.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
