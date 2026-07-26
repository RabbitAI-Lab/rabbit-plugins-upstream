## Description: <br>
Get stock screener list data from Intellectia API with no authentication and summarize results. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[intellectiaai](https://clawhub.ai/user/intellectiaai) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers, analysts, and agent users use this skill to fetch Intellectia stock, ETF, or crypto screener rows, inspect query parameters, and summarize returned market-screening data. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Stock screener query filters are sent to Intellectia's API. <br>
Mitigation: Use only query values appropriate to share with the third-party API provider. <br>
Risk: The Python example depends on the optional requests package. <br>
Mitigation: Install dependencies from a trusted package index and review the environment before running examples. <br>
Risk: API rate limits or service availability can affect result retrieval. <br>
Mitigation: Reduce page size and use backoff or retry behavior when rate limits occur. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/intellectiaai/skills/intellectia-stock-screener) <br>
- [Intellectia stock screener API endpoint](https://api.intellectia.ai/gateway/v1/stock/screener-list) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, guidance] <br>
**Output Format:** [Markdown with API parameter descriptions, JSON response shape, cURL example, and Python requests example] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May summarize JSON responses returned by the Intellectia API.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
