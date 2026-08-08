## Description:

書籍推薦引擎：支援協同過濾 / 內容相似度 / 熱門暢銷 / 標籤擴展四種演算法；內建 8 大主題書單；Open Library API 即時搜書；想讀書單追蹤含價格監控。

This skill is ready for commercial/non-commercial use.

## Publisher:

[xuan905](https://clawhub.ai/user/xuan905)

### License/Terms of Use:

MIT

## Use Case:

External users and developers use this skill to generate book recommendations, search Open Library, create topic-based book lists, and track wishlist priority, prices, and reading status.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Book titles, ISBNs, topics, and wishlist items may be stored locally and may be sent to external book, search, or retailer sites when lookup, --web, or price commands are run.

Mitigation: Avoid using private reading lists unless local storage and network use are acceptable, and review commands before enabling web lookup or price checks.

## Reference(s):

- [Open Library](https://openlibrary.org)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown or terminal text with optional JSON and Markdown files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Recommendations may be based on local ratings, book metadata, tags, Open Library results, and wishlist records.]

## Skill Version(s):

1.0.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
