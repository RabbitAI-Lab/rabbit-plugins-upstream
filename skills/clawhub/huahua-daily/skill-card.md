## Description:

HuaHuaDailyMCP lets agents query and analyze HuaHuaDaily fund holdings, market data, trades, quantitative context, and community data, and create App-confirmed trade or import requests while routing local files and large exports through the bundled CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[baiye1997](https://clawhub.ai/user/baiye1997)

### License/Terms of Use:

MIT-0

## Use Case:

External users and their configured agents use this skill to inspect sensitive HuaHuaDaily portfolio and market data, prepare fund analysis, and send trade or import requests that still require confirmation in the HuaHuaDaily App. The bundled CLI supports local screenshots, complete exports, large files, and diagnostics that should not be copied into model context.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can access sensitive portfolio, amount, cost, and return data through a HuaHuaDaily Agent Token.

Mitigation: Use a revocable least-privilege Agent Token, avoid exposing the token in chat or logs, and prefer the core profile unless the full tool surface is needed.

Risk: The security evidence flags unpinned live GitHub installation and broad dependency ranges for review.

Mitigation: Install only when the publisher and repository are trusted, and prefer a pinned release or commit in managed environments.

Risk: Some supported actions can create App-confirmed trade/import requests or perform direct community, report, or quant state changes.

Mitigation: Review these actions before execution, preserve idempotency IDs on retry, and rely on the HuaHuaDaily App confirmation flow for final trade or import writes.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/baiye1997/skills/huahua-daily)
- [README](README.md)
- [Portfolio and synchronization](references/portfolio.md)
- [Fund and market data](references/fund-market.md)
- [Trade requests and batch import](references/trade-import.md)
- [Quantitative analysis, replay, and snapshots](references/quant.md)
- [Community, JCTI, and personal reports](references/community-reports.md)
- [Date semantics and safety boundaries](references/date-safety.md)
- [CLI files and complete exports](references/cli-artifacts.md)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, configuration, guidance]

**Output Format:** [Markdown answers, JSON tool results, and shell-command or configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Large exports and local-file workflows are handled through CLI files; ordinary agent responses should summarize only the relevant results.]

## Skill Version(s):

4.1.4 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
