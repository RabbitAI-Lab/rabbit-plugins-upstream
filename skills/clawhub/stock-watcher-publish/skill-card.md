## Description:

Manage and monitor a local Chinese A-share watchlist, including add, remove, list, clear, and quote-summary actions using 10jqka structured quote data with HTML fallback.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xiaoxiaohuayu](https://clawhub.ai/user/xiaoxiaohuayu)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to maintain a local Chinese A-share watchlist and summarize current quote data from command-line utilities. It is for market monitoring and analysis, not investment advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The uninstall script can delete an arbitrary directory selected through STOCK_WATCHER_DATA_DIR.

Mitigation: Review uninstall.sh before running it, avoid pointing STOCK_WATCHER_DATA_DIR at important directories, and update the script to delete only a known watchlist file or validated app-owned directory with explicit confirmation.

Risk: 10jqka quote endpoints are not official public APIs and may change, block requests, or return delayed or unavailable data.

Mitigation: Treat quote output as monitoring data only, check source labels in summaries, and verify important market data with an authoritative source before acting on it.

## Reference(s):

- [Server-resolved GitHub repository](https://github.com/xiaoxiaohuayu/stock-watcher-publish)
- [ClawHub skill page](https://clawhub.ai/xiaoxiaohuayu/skills/stock-watcher-publish)
- [10jqka stock page endpoint](https://stockpage.10jqka.com.cn/{stock_code}/)
- [10jqka structured quote endpoint](https://quota-h.10jqka.com.cn/fuyao/common_hq_aggr/quote/v1/multi_last_snapshot)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Plain text and Markdown with shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Quote summaries are concise command-line text and may identify data source as API or HTML.]

## Skill Version(s):

0.1.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
