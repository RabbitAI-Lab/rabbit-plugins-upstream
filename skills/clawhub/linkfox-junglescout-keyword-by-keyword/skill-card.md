## Description: <br>
Expands a single Amazon seed keyword into related keywords with search volume, trend, PPC bid, ranking difficulty, and competition metrics across 10 marketplaces. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[linkfox-ai](https://clawhub.ai/user/linkfox-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External sellers, marketplace operators, and developers use this skill to research Amazon keyword expansion, long-tail opportunities, PPC bid signals, and keyword competition from a seed keyword. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Amazon keyword queries and a LinkFox API key are sent to LinkFox endpoints. <br>
Mitigation: Confirm the target marketplace and keyword before running the API call, and avoid sensitive or confidential search terms. <br>
Risk: The skill can consume paid LinkFox credits during API use. <br>
Mitigation: Tell the user when a query may incur credit costs and avoid automatic retries, paging, or parameter changes without user confirmation. <br>
Risk: Full API responses may be saved in local linkfox output and cache directories. <br>
Mitigation: Review or clean the generated linkfox output and cache directories after use, especially on shared workspaces. <br>


## Reference(s): <br>
- [Jungle Scout keyword expansion API reference](artifact/references/api.md) <br>
- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-junglescout-keyword-by-keyword) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, JSON, Shell commands, Guidance] <br>
**Output Format:** [Markdown summaries and tables, with full API responses persisted as JSON files when the helper script is used.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May call LinkFox endpoints, consume paid credits, and cache full responses locally for reuse.] <br>

## Skill Version(s): <br>
1.0.5 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
