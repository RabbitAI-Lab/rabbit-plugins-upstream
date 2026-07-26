## Description: <br>
Queries Zhihuiya patent citation data for a single patent and returns the cited patent documents and non-patent literature referenced during the patent application process. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[linkfox-ai](https://clawhub.ai/user/linkfox-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Patent analysts, external users, and developers use this skill to look up the patent and non-patent references cited by one supplied patent ID or publication number. It is suited for citation review and prior-art reference discovery when the user accepts the API credit cost and local response storage. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Patent identifiers, full API responses, cache data, and session metadata may be written locally. <br>
Mitigation: Use the skill only in workspaces where this local persistence is acceptable, review retention needs, and remove stored LinkFox response files when they are no longer needed. <br>
Risk: Feedback content may be sent to LinkFox services when the skill reports functionality issues or user sentiment. <br>
Mitigation: Review the feedback behavior before deployment and avoid sending confidential user content through feedback unless that disclosure is approved. <br>
Risk: The onboarding fallback references an unpinned helper-skill download. <br>
Mitigation: Install helper material only from a verified source and prefer pinned or reviewed release artifacts before using the onboarding fallback. <br>
Risk: Each patent lookup can consume LinkFox credits, and repeated or multi-patent queries can increase cost. <br>
Mitigation: Keep the one-patent-per-request limit, confirm user consent before additional lookups, and rely on the 24-hour cache for identical requests when appropriate. <br>


## Reference(s): <br>
- [API reference](artifact/references/api.md) <br>
- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-zhihuiya-patent-forward-citation) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, JSON, shell commands, guidance] <br>
**Output Format:** [Markdown summaries and tables, plus persisted JSON API responses] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires LINKFOX_AGENT_API_KEY or LINKFOXAGENT_API_KEY; each request is limited to one patent, and identical requests may be cached for 24 hours.] <br>

## Skill Version(s): <br>
1.0.5 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
