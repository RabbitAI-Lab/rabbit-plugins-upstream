## Description: <br>
Queries LinkFox SIF data to analyze traffic keywords for a single Amazon ASIN, including organic rank, ad rank, search volume, traffic share, click concentration, conversion rate, and weekly or monthly time windows. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[linkfox-ai](https://clawhub.ai/user/linkfox-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External Amazon sellers and e-commerce analysts use this skill to reverse-look up traffic keywords for a specific ASIN and inspect ranking, advertising, search-volume, and conversion-related metrics. Developers can also use it to run the bundled Python helper against the LinkFox SIF API and review saved JSON responses. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill sends ASIN and keyword queries to LinkFox's paid SIF API and uses API credentials. <br>
Mitigation: Install only when LinkFox API use is intended, use a scoped API key, and keep LINKFOX_TOOL_GATEWAY unset or pinned to a trusted LinkFox endpoint. <br>
Risk: The skill stores full LinkFox API responses and cache files locally, which may contain sensitive product research data. <br>
Mitigation: Review the saved linkfox response and cache directories and delete them periodically when the data is sensitive. <br>
Risk: The skill includes automatic feedback reporting behavior and can direct users toward a separate onboarding skill when authentication or balance issues occur. <br>
Mitigation: Review or disable feedback reporting before deployment, and install the separate onboarding skill only after explicitly trusting its source and package. <br>


## Reference(s): <br>
- [SIF-ASIN API Reference](references/api.md) <br>
- [ClawHub Skill Page](https://clawhub.ai/linkfox-ai/skills/linkfox-sif-asin-keywords) <br>


## Skill Output: <br>
**Output Type(s):** [API Calls, Analysis, Markdown, JSON, Shell commands, Files, Guidance] <br>
**Output Format:** [Markdown tables and summaries, JSON API responses, and saved local JSON files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Queries one ASIN per request; large responses are summarized on stdout while full responses are saved locally.] <br>

## Skill Version(s): <br>
1.0.5 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
