## Description: <br>
Analyzes Amazon ASIN traffic-source composition and exposure distribution across organic search, ads, recommendations, and period-over-period keyword changes using LinkFox SIF data. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[linkfox-ai](https://clawhub.ai/user/linkfox-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External Amazon sellers, ecommerce analysts, and agent users use this skill to inspect ASIN traffic-source mix, compare competing ASINs, and summarize current versus previous-period exposure and keyword changes. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill requires a LinkFox API key and sends ASIN or product traffic queries to LinkFox services. <br>
Mitigation: Use a scoped key where available, avoid submitting sensitive ASIN lists unless authorized, and confirm the user accepts LinkFox data sharing before API calls. <br>
Risk: API calls consume LinkFox credits. <br>
Mitigation: Tell the user when a request will spend credits, rely on the script's cache for repeated identical requests, and ask before running high-frequency or exploratory queries. <br>
Risk: Full API responses are stored locally and cached. <br>
Mitigation: Review the local linkfox output and cache directories for sensitive data, apply workspace retention controls, and delete cached responses when they are no longer needed. <br>
Risk: The skill can auto-send feedback externally and references an external onboarding-skill download path. <br>
Mitigation: Review or disable automatic feedback behavior before deployment and approve any onboarding download path before use. <br>


## Reference(s): <br>
- [SIF-ASIN API Reference](artifact/references/api.md) <br>
- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-sif-asin-summary) <br>
- [LinkFox skill documentation](https://skill.linkfox.com/) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, JSON, Shell commands, Files, Guidance] <br>
**Output Format:** [Markdown analysis with tables and summaries, plus saved JSON API responses from the helper script.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [The helper script can cache results for 24 hours and saves full responses locally while summarizing large responses in stdout.] <br>

## Skill Version(s): <br>
1.0.5 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
