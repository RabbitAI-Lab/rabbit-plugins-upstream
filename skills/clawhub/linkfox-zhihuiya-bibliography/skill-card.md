## Description: <br>
Queries Zhihuiya patent bibliography records by patent ID or publication number and returns structured patent metadata such as titles, applicants, inventors, classifications, citations, priority claims, and abstracts. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[linkfox-ai](https://clawhub.ai/user/linkfox-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Patent researchers, IP analysts, and agents assisting them use this skill to retrieve bibliography metadata for a specific known patent ID or publication number. It is intended for factual patent metadata lookup, not broad patent search, legal status analysis, freedom-to-operate review, or valuation. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Patent identifiers and related request context are sent to LinkFox/Zhihuiya services. <br>
Mitigation: Use the skill only when the user or workspace policy permits sharing that request context with LinkFox/Zhihuiya. <br>
Risk: Full API responses are stored locally and may contain detailed patent metadata from the lookup. <br>
Mitigation: Review storage location, access controls, and retention expectations before using the skill in sensitive workspaces. <br>
Risk: The skill includes automatic feedback reporting to a separate LinkFox feedback endpoint. <br>
Mitigation: Review or disable feedback reporting before sensitive use, especially when user intent or result quality could reveal confidential context. <br>
Risk: Patent bibliography lookups consume LinkFox/Zhihuiya credits, and repeated lookups can increase cost. <br>
Mitigation: Keep requests to one patent at a time, use the 24-hour cache when appropriate, and obtain explicit user consent before multiple lookups. <br>


## Reference(s): <br>
- [ClawHub skill listing](https://clawhub.ai/linkfox-ai/skills/linkfox-zhihuiya-bibliography) <br>
- [Zhihuiya bibliography API reference](artifact/references/api.md) <br>
- [LinkFox API key and credits guide](https://skill.linkfox.com/linkfoxskills/guide.htm) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, JSON, shell commands, guidance] <br>
**Output Format:** [Markdown summaries and JSON API responses saved to local files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Single-patent requests; full responses are stored locally, with summarized stdout for large responses and optional inline full output.] <br>

## Skill Version(s): <br>
1.0.5 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
