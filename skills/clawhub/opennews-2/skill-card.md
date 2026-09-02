## Description: <br>
Crypto news search, AI ratings, trading signals, and real-time updates via the OpenNews 6551 API. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[infra403](https://clawhub.ai/user/infra403) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and agents use this skill to query OpenNews/6551 crypto news, filter articles by keyword, coin, source, or category, and inspect AI ratings, summaries, and trading signals. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill sends the OPENNEWS_TOKEN and news queries to the OpenNews/6551 API at https://ai.6551.io. <br>
Mitigation: Use a dedicated, revocable OPENNEWS_TOKEN scoped to this service and avoid sharing broader credentials. <br>
Risk: AI ratings, summaries, and trading signals may be unavailable for some articles or may be unsuitable as sole trading guidance. <br>
Mitigation: Check returned rating status and review article context before using results in market analysis or trading decisions. <br>


## Reference(s): <br>
- [OpenNews skill page](https://clawhub.ai/infra403/opennews-2) <br>
- [6551 token page](https://6551.io/mcp) <br>
- [OpenNews API base URL](https://ai.6551.io) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline shell commands and JSON API examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses curl commands authenticated with OPENNEWS_TOKEN; example workflows may pipe API JSON to jq.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release metadata and package.json) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
