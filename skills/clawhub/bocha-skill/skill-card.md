## Description: <br>
Searches the web using the Bocha AI Search API, optimized for Chinese-language content, with support for web pages, images, news, and summaries. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ypw757](https://clawhub.ai/user/ypw757) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
External users and developers use this skill to route Chinese and English search requests through Bocha, returning current web, image, news, and summary results for agent workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Search queries are sent to Bocha using the user's BOCHA_API_KEY. <br>
Mitigation: Use only with queries approved for third-party search services, and avoid sensitive or confidential prompts unless that use is explicitly permitted. <br>
Risk: The artifact includes an unsafe credential example in PUBLISH.md. <br>
Mitigation: Do not use or copy the example key; users should create and manage their own Bocha API key and rotate any copied or exposed credential. <br>
Risk: Broad routing may send Chinese or explicit search requests to a third-party provider unexpectedly. <br>
Mitigation: Review the routing behavior before enabling the skill and invoke Bocha search only when third-party search is intended. <br>
Risk: publish.sh can interactively authenticate to ClawHub and publish with the user's account. <br>
Mitigation: Run publish.sh only from a trusted checkout when publishing is intended, and protect any ClawHub token used during login. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/ypw757/skills/bocha-skill) <br>
- [Bocha Open Platform](https://open.bocha.cn/) <br>
- [Bocha API Documentation](https://bocha-ai.feishu.cn/wiki/RXEOw02rFiwzGSkd9mUcqoeAnNK) <br>
- [OpenClaw Docs](https://docs.openclaw.ai) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, JSON, API Calls] <br>
**Output Format:** [Markdown search results with an embedded raw JSON block] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires BOCHA_API_KEY and Node.js; accepts query, count, freshness, and summary controls.] <br>

## Skill Version(s): <br>
1.0.0 (source: ClawHub release metadata and scripts/package.json) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
