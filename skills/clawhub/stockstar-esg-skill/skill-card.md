## Description: <br>
Queries ESG ratings and score details for A-share and Hong Kong-listed companies from StockStar, covering Miotech, China Securities Index, and SynTao Green Finance ratings. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[stockstar1996](https://clawhub.ai/user/stockstar1996) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, analysts, and agents use this skill to search listed companies, retrieve ESG ratings and E/S/G score details, compare up to five stocks, and browse provider rating lists when explicitly requested. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Company names, stock codes, and ESG lookup terms are sent to public StockStar and search suggestion endpoints. <br>
Mitigation: Use the skill only when the user is comfortable sending those lookup terms to the configured public data providers. <br>
Risk: Ambiguous ESG conversations may not be about listed securities. <br>
Mitigation: Confirm the intended company or stock before running the skill when the request is ambiguous. <br>
Risk: ESG ratings may be incomplete, stale, unavailable, or differ across rating providers. <br>
Mitigation: Report provider names and rating dates with the results, and avoid filling missing provider fields with invented values. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/stockstar1996/skills/stockstar-esg-skill) <br>
- [StockStar ESG data source](https://esg.stockstar.com) <br>
- [StockStar ESG detail endpoint](https://esg.stockstar.com/esg/pjdetail/{stock_code}) <br>
- [Stock search suggestion endpoint](https://q.ssajax.cn/info/handler/xsuggesthandler.ashx?) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, guidance] <br>
**Output Format:** [Markdown summaries and tables derived from JSON command output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [The underlying CLI can emit JSON for agent parsing; the skill instructs the agent to summarize results rather than present raw JSON.] <br>

## Skill Version(s): <br>
1.0.0 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
