## Description: <br>
Analyzes Amazon keywords through the ClawEC API, including ABA keyword analysis, keyword mining, keyword trends, and optional AI interpretation. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[anyunzhong](https://clawhub.ai/user/anyunzhong) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External sellers, ecommerce operators, and agents use this skill to submit Amazon keyword research requests to ClawEC, retrieve result logs, and summarize ABA data, keyword mining results, trends, and optional AI analysis. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill sends submitted keywords and result lookups to clawec.com using a ClawEC API key. <br>
Mitigation: Use an API key with appropriate account limits and submit only keyword data intended for ClawEC processing. <br>
Risk: Keyword searches and optional AI interpretation may consume ClawEC credits or quota. <br>
Mitigation: Confirm account limits and selected analysis options before running searches or polling for AI interpretation. <br>
Risk: AI interpretation is asynchronous and can fail or time out while raw keyword data remains available. <br>
Mitigation: Check response status, business codes, and aiStatus before presenting results, and fall back to raw data when AI interpretation is unavailable. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/anyunzhong/skills/clawec-amazon-keyword-search) <br>
- [ClawHub Publisher Profile](https://clawhub.ai/user/anyunzhong) <br>
- [ClawEC API Base](https://www.clawec.com/api) <br>
- [ClawEC API Key Page](https://www.clawec.com/api-key?source=q-clawhub) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell commands and JSON API responses] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs may include ABA data, keyword suggestions, trend data, ClawEC response envelopes, point usage details, and optional AI-generated analysis.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
