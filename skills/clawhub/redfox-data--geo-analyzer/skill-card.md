## Description: <br>
GEO Analyzer analyzes brand visibility across Doubao, Kimi, and DeepSeek AI search results, measuring mentions, sentiment, citations, and competitor comparisons, then generating interactive HTML reports. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[redfox-data](https://clawhub.ai/user/redfox-data) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External brand marketers, product managers, content operators, and PR teams use this skill to measure brand visibility in AI search, compare competitor presence, evaluate sentiment, and guide GEO optimization work. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Brand, category, competitor, and question data are sent to RedFox-backed external search services. <br>
Mitigation: Use only information that is appropriate to share with those services, and verify the API key source, scope, expiration, and revocation path before running the skill. <br>
Risk: The generated HTML summary may say there are no negative evaluations even when negative sentiment exists. <br>
Mitigation: Review the detailed sentiment fields and raw report evidence before using the summary for decisions. <br>


## Reference(s): <br>
- [GEO Metrics Reference](references/geo-metrics.md) <br>
- [RedFoxHub](https://redfox.hk) <br>
- [RedFoxHub API Key Settings](https://redfox.hk/settings/api-keys?source=clawhub) <br>
- [ClawHub Skill Page](https://clawhub.ai/redfox-data/skills/geo-analyzer) <br>


## Skill Output: <br>
**Output Type(s):** [Text, HTML, JSON, Shell commands, Guidance] <br>
**Output Format:** [Text or Markdown summary with generated HTML and JSON report files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires REDFOX_API_KEY and sends brand, category, competitor, and question data to RedFox-backed external search services.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
