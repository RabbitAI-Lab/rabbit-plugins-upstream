## Description: <br>
This skill helps personal investors and entry-level analysts extract financial data from local Excel or PDF files and generate interactive HTML financial analysis reports with trend sparklines. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, personal investors, and entry-level analysts use this skill to turn a single Excel or PDF financial report into a readable HTML analysis with calculated metrics and trend visuals. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Financial reports can contain confidential business or investment data, and broad file-analysis triggers may expose unrelated content if invoked on the wrong files. <br>
Mitigation: Use the skill only with intended financial report files and avoid providing unrelated PDFs or spreadsheets. <br>
Risk: The local-processing privacy language may be misunderstood because the agent's LLM may still see content used during analysis. <br>
Mitigation: Treat opened financial content as visible to the active agent environment and follow the user's data-handling policies. <br>
Risk: Financial analysis and PDF extraction can be incorrect or incomplete when source data is malformed, scanned, or missing context. <br>
Mitigation: Review the source data, extracted values, calculated metrics, and generated report before relying on the output for investment or business decisions. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/finance-report-tool-free) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and generated HTML report files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May generate a local interactive HTML financial analysis report with trend sparklines from one Excel or PDF input file.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
