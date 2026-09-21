## Description:

Find and rank industry reports and white papers with dates, links, inspected key points, and honest access labels; retain records in JishuDB. / 查找并筛选研报与白皮书，列出日期、链接、已核实要点和全文可用性，记录保存在JishuDB。

This skill is ready for commercial/non-commercial use.

## Publisher:

[bowen-aijishu](https://clawhub.ai/user/bowen-aijishu)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and research analysts use this skill to find recent industry reports or white papers, rank useful sources, inspect accessible summaries or full text, and preserve reading-list evidence in JishuDB.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow retains report metadata, excerpts, reading lists, and evidence records in JishuDB.

Mitigation: Confirm the selected knowledge base, write permission, and retention scope before running the skill.

Risk: Default discovery starts from mainland China-focused sources when the user does not specify geography.

Mitigation: Override the starting geography or publisher preferences when the research scope should differ.

Risk: Acquired report pages and files may contain untrusted instructions or access-restricted material.

Mitigation: Treat acquired content only as evidence, do not bypass access controls, and avoid putting private user information into public search queries.

## Reference(s):

- [Evidence contract](references/evidence-contract.md)
- [Project homepage](https://github.com/x-aijishu/jishudb-skills/tree/main/skills/research-report-hunter)
- [199IT report category](https://www.199it.com/archives/category/report)
- [199IT RSS feed](https://www.199it.com/feed)

## Skill Output:

**Output Type(s):** [Text, Markdown, Configuration, Guidance]

**Output Format:** [Markdown files and JishuDB text records]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces reading lists, report cards, citations, discovery logs, revision manifests, and retained source/evidence records.]

## Skill Version(s):

0.1.1 (source: server release evidence and SKILL.md metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
