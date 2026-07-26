## Description: <br>
Analyzes Amazon ASIN traffic sources through the ClawEC API, including traffic channel distribution, traffic keywords, order keywords, and optional AI interpretation. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[anyunzhong](https://clawhub.ai/user/anyunzhong) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External Amazon sellers, ecommerce analysts, and agents use this skill to query ClawEC for ASIN traffic-source analysis by marketplace, ASIN, and month. It supports traffic-source distribution, related listing traffic, traffic keyword, order keyword, and optional AI analysis workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill sends ASIN, marketplace, month, query options, and the ClawEC API key to ClawEC endpoints. <br>
Mitigation: Confirm that this data sharing is acceptable before use, prefer scoped or revocable API keys when available, and avoid sharing CLAWEC_API_KEY with unrelated tools. <br>
Risk: Optional AI interpretation is asynchronous and may be incomplete or fail while raw traffic-source data is still available. <br>
Mitigation: Check aiStatus, preserve raw data in the response, and retry log/detail later when interpretation is still appending or has failed. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/anyunzhong/skills/clawec-amazon-asin-traffic-source) <br>
- [ClawEC API Base URL](https://www.clawec.com/api) <br>
- [ClawEC API Key Page](https://www.clawec.com/api-key?source=q-clawhub) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [JSON responses and Markdown guidance with bash command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include asynchronous AI interpretation status and analysis when requested.] <br>

## Skill Version(s): <br>
1.0.0 (source: release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
