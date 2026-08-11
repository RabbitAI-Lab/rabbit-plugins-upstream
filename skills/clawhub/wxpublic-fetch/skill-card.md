## Description:

从微信公众号抓取指定公众号和日期范围内的文章，并将文章内容和图片保存为本地 Markdown 文件。

This skill is ready for commercial/non-commercial use.

## Publisher:

[xiongweixp](https://clawhub.ai/user/xiongweixp)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to retrieve WeChat Official Account articles for a named account and date range, save the converted Markdown locally, and continue analysis or summarization from the saved files.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Sensitive account names, date ranges, credentials, or article URLs may be exposed to external services during use.

Mitigation: Review sensitivity before installation and execution; use environment variables, limited or revocable credentials, and avoid running on sensitive article URLs unless the disclosure is acceptable.

Risk: Large date ranges can trigger many paginated requests and may increase service cost.

Mitigation: Require explicit user confirmation before continuing with date ranges longer than 60 days, as described by the skill behavior.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/xiongweixp/skills/wxpublic-fetch)
- [wxpub service site](https://wxpub.aibana.art)
- [anything-md conversion service](https://anything-md.doocs.org/)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown files plus a concise text summary of saved paths and failures]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Creates a local images directory for downloaded article images and records saved Markdown paths for follow-up analysis.]

## Skill Version(s):

1.0.8 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
