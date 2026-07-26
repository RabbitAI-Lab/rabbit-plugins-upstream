## Description: <br>
Screens a company or patent list against public patent data and produces a quick IP due-diligence report with portfolio overview, quality indicators, technology distribution, and risk warnings. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[golngod](https://clawhub.ai/user/golngod) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, analysts, and diligence teams use this skill to perform an initial patent portfolio screen for a company or patent-number list before deeper IP review. It summarizes patent counts, technology areas, legal-status signals, quality indicators, and risk warnings from public patent data. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The company names or patent numbers entered by the user are sent to PatentsView for lookup. <br>
Mitigation: Use only inputs appropriate for public patent-data lookup, and avoid including confidential deal context or sensitive internal analysis in the query. <br>
Risk: The skill provides quick screening, not legal advice or a complete patent valuation. <br>
Mitigation: Treat the report as triage output and have qualified IP professionals validate conclusions before relying on it for legal, investment, or transaction decisions. <br>
Risk: Public patent data can be delayed, incomplete, or interpreted incorrectly by simplified heuristics. <br>
Mitigation: Verify important patent status, ownership, citation, and expiration findings against authoritative records before taking action. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/golngod/skills/ip-quick-screen) <br>
- [USPTO PatentsView API](https://api.patentsview.org/patents/query) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, JSON, guidance] <br>
**Output Format:** [Markdown report with a structured JSON summary] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Chinese-language report output; broad company searches are capped to the first 100 patents.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
