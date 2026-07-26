## Description: <br>
Searches the MPSTATS Ozon Russia database by Russian keyword or SKU and returns product identity fields such as product ID, title, brand, seller, image URL, and product page URL. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[linkfox-ai](https://clawhub.ai/user/linkfox-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External marketplace analysts, e-commerce operators, and agent users can use this skill to find or reverse-lookup Ozon Russia products before deciding whether to run deeper product, brand, seller, category, or trend analysis. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill makes LinkFox API calls that may consume account credits. <br>
Mitigation: Confirm the search parameters and expected credit use before running calls, especially when retrying or changing keywords. <br>
Risk: Full search responses are stored locally and may include product, seller, or session-related metadata. <br>
Mitigation: Review the saved JSON location and handle those files according to the workspace's data retention and sharing requirements. <br>
Risk: The security scan notes remote onboarding-skill installation guidance and feedback submission to a separate LinkFox service. <br>
Mitigation: Review those behaviors before deployment and require user approval for installing additional skills or sending feedback where policy requires consent. <br>


## Reference(s): <br>
- [MPSTATS Ozon Product Search API Reference](artifact/references/api.md) <br>
- [ClawHub Skill Page](https://clawhub.ai/linkfox-ai/skills/linkfox-mpstats-ozon-product-search) <br>
- [Publisher Profile](https://clawhub.ai/user/linkfox-ai) <br>
- [LinkFox Tool Gateway Product Search Endpoint](https://tool-gateway.linkfox.com/mpstats/ozon/productSearch) <br>
- [LinkFox Feedback API](https://skill-api.linkfox.com/api/v1/public/feedback) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with JSON parameters, shell command examples, and JSON response summaries or saved response files.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Full API responses are saved to local JSON files; small responses may also be printed inline, while larger responses are summarized.] <br>

## Skill Version(s): <br>
1.0.5 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
