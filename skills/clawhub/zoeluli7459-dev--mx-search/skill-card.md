## Description: <br>
Retrieves source-backed China A-share financial news, announcements, research reports, policy updates, trading rules, market events, event explanations, and impact-analysis context through Eastmoney MX search. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zoeluli7459-dev](https://clawhub.ai/user/zoeluli7459-dev) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and external users use this skill when they need current or source-backed China A-share finance information before analysis, especially for news, announcements, research reports, policy updates, trading rules, event timelines, or impact explanations. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Finance search queries are sent to the configured Eastmoney MX endpoint. <br>
Mitigation: Install only when Eastmoney MX search is intended, configure MX_APIKEY deliberately, and avoid sending unnecessary sensitive query details. <br>
Risk: Returned finance sources can be sparse, conflicting, or interpretive. <br>
Mitigation: Cite source names and dates, separate retrieved facts from inference, and prefer official announcements, exchange disclosures, company filings, and policy texts for factual claims. <br>
Risk: Search results are saved locally for audit and may contain user query context. <br>
Mitigation: Set MX_OUTPUT_DIR to an appropriate storage location when saved TXT/JSON outputs need controlled retention. <br>


## Reference(s): <br>
- [mx-search Result Fields](artifact/references/result-fields.md) <br>
- [Eastmoney MX news-search endpoint](https://mkapi2.dfcfs.com/finskillshub/api/claw/news-search) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, files, guidance] <br>
**Output Format:** [Markdown guidance with shell commands, terminal text, and saved TXT/JSON result files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires MX_APIKEY; MX_OUTPUT_DIR can redirect saved search outputs.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
