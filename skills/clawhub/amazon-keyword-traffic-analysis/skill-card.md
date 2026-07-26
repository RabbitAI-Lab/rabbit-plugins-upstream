## Description: <br>
Use when user asks for keyword expansion or ad keyword filtering; single keyword analysis or keyword deep dive; whether a keyword is worth bidding on; which keywords drive traffic to an ASIN; ASIN keyword health, keyword traffic changes, or why an ASIN changed under a keyword. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[apiclaw](https://clawhub.ai/user/apiclaw) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External marketplace operators, analysts, and agent users use this skill to perform ZooData-backed Amazon keyword expansion, single-keyword analysis, reverse-ASIN keyword review, and ASIN keyword-traffic diagnosis. It helps frame directional keyword and traffic decisions while requiring seller-side evidence before final budget, bid, profitability, or conversion conclusions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill requires a ZooData API key for endpoint access. <br>
Mitigation: Provide the key through ZOODATA_API_KEY and keep it scoped to trusted agent sessions. <br>
Risk: The bundled CLI exposes broader ZooData product, market, pricing, and review commands beyond the keyword workflows. <br>
Mitigation: Use the documented Amazon keyword and ASIN traffic workflows unless the broader CLI behavior is intentionally needed. <br>
Risk: Keyword and traffic outputs can be mistaken for final conversion, profitability, bid, or budget decisions. <br>
Mitigation: Treat ZooData-derived conclusions as directional until seller-side ABA Search Query Performance or ads performance evidence is provided. <br>


## Reference(s): <br>
- [Skill README](artifact/README.md) <br>
- [ZooData API Reference](artifact/references/reference.md) <br>
- [Execution Guide](artifact/references/execution-guide.md) <br>
- [Keyword Expansion Scenario](artifact/references/scenarios-expand.md) <br>
- [Single Keyword Analysis Scenario](artifact/references/scenarios-keyword-analysis.md) <br>
- [Reverse ASIN Keyword Analysis Scenario](artifact/references/scenarios-reverse-asin.md) <br>
- [Keyword Traffic Diagnosis Scenario](artifact/references/scenarios-keyword-traffic-diagnosis.md) <br>
- [ClawHub Skill Page](https://clawhub.ai/apiclaw/skills/amazon-keyword-traffic-analysis) <br>
- [ZooData API Keys](https://zoodata.ai/en/api-keys) <br>
- [ZooData Pricing](https://zoodata.ai/en/pricing) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown reports with concise findings, data notes, API usage notes, and bounded recommendations] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires ZOODATA_API_KEY and uses ZooData keyword and ASIN traffic endpoints; conclusions remain bounded by available market, ASIN observation, and seller-provided evidence.] <br>

## Skill Version(s): <br>
0.1.2 (source: release evidence and frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
