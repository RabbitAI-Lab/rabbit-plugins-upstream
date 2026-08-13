## Description:

Fetches articles from WeChat, Xiaohongshu, Douban, and Zhihu, uploads article images to Aliyun OSS, extracts keywords with an optional LLM workflow, and archives results to an Obsidian knowledge base with optional Notion sync.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ajayhao](https://clawhub.ai/user/ajayhao)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to collect supported Chinese-platform articles, preserve article content as Markdown or Notion records, and keep image assets accessible through Aliyun OSS. It supports URL-based fetching as well as HTML or MHTML offline input for archiving workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Article images are uploaded to Aliyun OSS as part of normal operation.

Mitigation: Use a dedicated bucket with least-privilege PutObject/GetObject credentials and confirm users have rights to archive the target content.

Risk: Optional LLM keyword extraction sends up to the first 12000 characters of article text to the configured LLM endpoint.

Mitigation: Leave LLM credentials unset for local word-frequency fallback, or configure only an approved provider and model for the data being processed.

Risk: Cookie files may be used for WeChat or Zhihu anti-scraping fallbacks.

Mitigation: Keep cookie files narrowly scoped, rotate them regularly, and prefer low-risk accounts for cookie-based scraping.

Risk: Optional Notion archiving writes article metadata and content to a Notion database.

Mitigation: Grant the Notion integration access only to the intended database and review database sharing permissions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/ajayhao/skills/article-fetcher)
- [Project homepage](https://github.com/AjayHao/article-fetcher)
- [README](artifact/README.md)
- [Changelog](artifact/CHANGELOG.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Files, Configuration guidance]

**Output Format:** [Terminal status text, Obsidian Markdown files with YAML frontmatter, and optional Notion page records]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May write local Markdown files, upload images to Aliyun OSS, and optionally send article text to the configured LLM endpoint for keyword extraction.]

## Skill Version(s):

1.3.6 (source: server release metadata, SKILL.md metadata, README, CHANGELOG)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
