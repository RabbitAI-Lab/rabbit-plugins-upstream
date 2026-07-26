## Description: <br>
Jungle Scout keyword Share of Voice analysis returns brand visibility share across the first three pages of Amazon search results, split by organic, sponsored, and combined presence, along with 30-day exact search volume, median PPC bid, and top-three ASIN click and conversion data across 10 marketplaces. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[linkfox-ai](https://clawhub.ai/user/linkfox-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and e-commerce operators use this skill to analyze Amazon keyword competitive structure, brand Share of Voice, sponsored versus organic visibility, PPC bid context, and top ASIN click and conversion performance. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Jungle Scout query parameters and API credentials are shared with LinkFox's gateway. <br>
Mitigation: Install only when this data sharing is acceptable, keep API keys appropriately scoped and rotated, and avoid setting LINKFOX_TOOL_GATEWAY to an untrusted host. <br>
Risk: Full API responses and cached data can be stored locally in linkfox output and cache directories. <br>
Mitigation: Clean the linkfox output and cache directories when data is sensitive, and avoid running the skill in shared workspaces without reviewing stored files. <br>
Risk: The release includes feedback reporting behavior and remote onboarding installation guidance that deserve review before deployment. <br>
Mitigation: Review or disable feedback behavior as appropriate and inspect any remote onboarding or installation steps before use. <br>


## Reference(s): <br>
- [Jungle Scout Share of Voice API Reference](references/api.md) <br>
- [ClawHub Skill Page](https://clawhub.ai/linkfox-ai/skills/linkfox-junglescout-keyword-share-of-voice) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, JSON, shell commands, configuration guidance] <br>
**Output Format:** [Markdown summaries with saved JSON response files and optional inline JSON output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [The script writes full responses to a linkfox session data directory, uses a 24-hour local cache by default, and prints a compact summary when responses exceed 8 KB unless inline output is requested.] <br>

## Skill Version(s): <br>
1.0.5 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
