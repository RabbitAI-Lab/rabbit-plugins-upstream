## Description: <br>
Searches Kalodata TikTok Shop livestream leaderboards and retrieves detailed metrics for a selected livestream by livestreamId. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[linkfox-ai](https://clawhub.ai/user/linkfox-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and agents use this skill to browse TikTok Shop livestream rankings by market, date range, language, and currency, then inspect one selected livestream's revenue, viewers, duration, GPM, and product count. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill makes authenticated external API calls and relies on environment-provided gateway and authorization settings. <br>
Mitigation: Install and run it only when external API access is acceptable, review the gateway URL, and constrain API key exposure through environment controls. <br>
Risk: The skill stores complete API responses locally, which may preserve sensitive or task-specific data in the workspace. <br>
Mitigation: Avoid sending sensitive prompts or identifiers, review generated linkfox data files, and clean retained responses according to local data handling policy. <br>
Risk: The evidence security summary flags under-scoped network, persistence, and external-install behavior. <br>
Mitigation: Treat external onboarding or skill-install instructions as requiring separate manual review before use. <br>


## Reference(s): <br>
- [Kalodata-TikTok直播搜索与详情 API Reference](artifact/references/api.md) <br>
- [ClawHub Skill Page](https://clawhub.ai/linkfox-ai/skills/linkfox-kalodata-tiktok-livestream) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown summaries with JSON API responses and saved JSON data files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Scripts save complete API responses under the local linkfox session data directory and may print either full JSON or a compact summary depending on response size.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
