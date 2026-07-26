## Description: <br>
Searches and browses Walmart product listings by keyword, category, price range, sort order, store, and device context. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[linkfox-ai](https://clawhub.ai/user/linkfox-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
E-commerce sellers, product researchers, and agents use this skill to find current Walmart listings, compare prices, inspect availability, and gather product listing data for market or competitor research. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: LinkFox receives Walmart search queries, API credentials, and session metadata. <br>
Mitigation: Confirm the gateway points to the intended LinkFox domain, avoid sensitive search terms, and install only if this data sharing is acceptable. <br>
Risk: Full Walmart search results are saved as local LinkFox session data files. <br>
Mitigation: Review local storage expectations before use and avoid searches that would create sensitive local records. <br>
Risk: The skill includes guidance to download or install an onboarding skill when credentials or credits are missing. <br>
Mitigation: Require explicit user approval before downloading or installing any secondary skill. <br>


## Reference(s): <br>
- [Walmart API reference](references/api.md) <br>
- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-walmart-search) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, JSON, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown tables and JSON tool responses] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Full API responses are saved to local LinkFox session data files; large responses are summarized unless inline output is requested.] <br>

## Skill Version(s): <br>
1.0.4 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
