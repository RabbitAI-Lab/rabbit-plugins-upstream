## Description: <br>
ClawdChat browses Moltbook public feeds, extracts high-value posts and comments, filters low-quality content, and produces a daily Markdown analysis report about AI agent community topics, solutions, and trends. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[lucasyao1985](https://clawhub.ai/user/lucasyao1985) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers, analysts, and agent operators use this skill to summarize public Moltbook discussions into recurring questions, solution patterns, and daily community trend reports. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill uses browser automation against Moltbook and may encounter rate limits, dynamic page changes, or selector drift. <br>
Mitigation: Run at a modest cadence, respect retry and wait guidance, and update the selector reference when page structure changes. <br>
Risk: Generated reports and optional raw scraped data are stored locally under ~/myassistant/chat/moltbook-daily/ and may contain copied public discussion content. <br>
Mitigation: Review or clean that directory periodically, especially on shared or synced machines. <br>
Risk: Community summaries can include spam, unverifiable claims, or overgeneralized consensus from public posts. <br>
Mitigation: Use the provided spam filters and verification checks, and review conclusions before relying on them for decisions. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/lucasyao1985/skills/clawdchat) <br>
- [Moltbook](https://moltbook.com) <br>
- [Moltbook selector reference](references/selectors.md) <br>
- [Moltbook spam filtering rules](references/spam-rules.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance, configuration] <br>
**Output Format:** [Markdown daily reports with concise status text and optional structured raw data files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Writes reports under ~/myassistant/chat/moltbook-daily/ and may optionally retain raw scraped data in a raw/ subdirectory.] <br>

## Skill Version(s): <br>
1.0.0 (source: ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
