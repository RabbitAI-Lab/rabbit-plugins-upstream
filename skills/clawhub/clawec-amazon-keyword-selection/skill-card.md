## Description: <br>
Uses the ClawEC API to run Amazon keyword product research using search volume, purchase rate, supply-demand ratio, and blue ocean index, with optional AI interpretation. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[anyunzhong](https://clawhub.ai/user/anyunzhong) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Amazon sellers, ecommerce operators, and developers use this skill to submit ClawEC keyword research requests, retrieve logs and details, and summarize high-potential keyword opportunities for supported Amazon marketplaces. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Searches and log lookups are sent to ClawEC under the user's account. <br>
Mitigation: Use only a CLAWEC_API_KEY intended for this service and avoid submitting keywords or account data that should not be shared with ClawEC. <br>
Risk: Keyword opportunity scores and optional AI interpretation may be incomplete or unsuitable as the sole basis for business decisions. <br>
Mitigation: Review returned search volume, purchase rate, supply-demand ratio, blue ocean index, and AI analysis against independent marketplace evidence before acting. <br>
Risk: Polling log details can retrieve prior search records associated with the configured API key. <br>
Mitigation: Protect the API key as an account credential and run the helper only in environments where account search history access is appropriate. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/anyunzhong/skills/clawec-amazon-keyword-selection) <br>
- [ClawEC API base](https://www.clawec.com/api) <br>
- [ClawEC API key page](https://www.clawec.com/api-key?source=q-clawhub) <br>
- [ClawEC Amazon keyword research search endpoint](https://www.clawec.com/api/aigc/ec/amazon/keyword_research/search) <br>
- [ClawEC Amazon keyword research logs endpoint](https://www.clawec.com/api/aigc/ec/amazon/keyword_research/search/logs) <br>
- [ClawEC Amazon keyword research detail endpoint](https://www.clawec.com/api/aigc/ec/amazon/keyword_research/search/log/detail) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown summaries with JSON API responses and shell command snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include keyword opportunity tables, ClawEC log IDs, polling status, and optional AI analysis.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
