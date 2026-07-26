## Description: <br>
Helps agents reverse-search US Amazon niches and keywords by filtering historical opportunity metrics such as market size, growth, competition, price tiers, demographics, product features, and review themes. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[linkfox-ai](https://clawhub.ai/user/linkfox-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Amazon sellers, e-commerce operators, and agents use this skill to turn selection criteria such as low competition, growth, price gaps, demographics, and review pain points into concrete US Amazon niche or keyword candidates. <br>

### Deployment Geography for Use: <br>
Global; data coverage is limited to the United States Amazon marketplace. <br>

## Known Risks and Mitigations: <br>
Risk: The skill sends the LinkFox API key, query parameters, session metadata, and Amazon opportunity results to LinkFox-controlled endpoints. <br>
Mitigation: Install and run it only when the user trusts LinkFox with that data, and verify LINKFOX_TOOL_GATEWAY is unset or points to the official LinkFox gateway before use. <br>
Risk: Full API responses and cache files can be saved in local linkfox data directories. <br>
Mitigation: Monitor the generated linkfox data and cache folders, avoid running from sensitive working directories, and delete stored results when they are no longer needed. <br>
Risk: Successful searches consume LinkFox credits, including empty-result searches. <br>
Mitigation: Warn the user before use, avoid repeated automatic retries or broadening without consent, and rely on the 24-hour cache for repeated identical queries. <br>
Risk: Feedback behavior can send user context to a separate feedback endpoint. <br>
Mitigation: Require explicit user consent before submitting feedback or downloading and installing the separate onboarding skill. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-amazon-opportunity-search-by-metrics) <br>
- [API reference](artifact/references/api.md) <br>
- [LinkFox Skills](https://skill.linkfox.com/) <br>


## Skill Output: <br>
**Output Type(s):** [Markdown, JSON, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with JSON API parameters, shell command examples, and saved JSON API responses.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires a LinkFox API key; writes full API responses and a 24-hour cache under a linkfox data directory.] <br>

## Skill Version(s): <br>
1.0.4 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
