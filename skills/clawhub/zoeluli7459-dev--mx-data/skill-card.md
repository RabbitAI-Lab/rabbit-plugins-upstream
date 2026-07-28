## Description: <br>
A股数据结构化 helps agents query Eastmoney MX for exact, time-sensitive market and company data and return structured financial results. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zoeluli7459-dev](https://clawhub.ai/user/zoeluli7459-dev) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and finance-oriented users can use this skill when an agent needs current or historical A-share market data, company fundamentals, shareholder information, executive information, capital-flow data, or structured financial tables from Eastmoney MX. It is intended for data lookup and structuring, not news interpretation, screening workflows, watchlist management, or simulated trading. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Financial lookup query text is sent to Eastmoney MX with the configured MX_APIKEY. <br>
Mitigation: Avoid including confidential portfolio strategy, proprietary research intent, or other sensitive information in query text unless that data use is approved. <br>
Risk: Generated Excel, text, and raw JSON result files may remain on local storage after the lookup. <br>
Mitigation: Use a controlled MX_OUTPUT_DIR for sensitive work and review, retain, or delete generated files according to the user's data-handling policy. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/zoeluli7459-dev/skills/mx-data) <br>
- [Result Fields Reference](artifact/references/result-fields.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, files, JSON] <br>
**Output Format:** [Markdown terminal preview with generated Excel, text description, and raw JSON file paths] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires MX_APIKEY. Generated result files are written under MX_OUTPUT_DIR or the default ~/.codex/skills-output/mx_data/output path.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
