## Description: <br>
Retrieves structured Amazon product-detail data by ASIN, including title, images, bullet points, specifications, A+ content, price, ratings, reviews, and variants. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[linkfox-ai](https://clawhub.ai/user/linkfox-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, Amazon sellers, and marketplace researchers use this skill to look up current Amazon listing details by ASIN across supported marketplaces and present the returned product data in tables, summaries, and links. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: ASIN lookup parameters, optional ZIP or location fields, session metadata, and the LinkFox API key are sent to LinkFox services. <br>
Mitigation: Install and run the skill only when that data sharing is acceptable for the user's project and organization. <br>
Risk: The skill includes automatic feedback reporting behavior. <br>
Mitigation: Review or disable feedback reporting where possible before using the skill in sensitive workflows. <br>
Risk: Full API responses and cache files are persisted locally, which can expose product research data on shared machines or projects. <br>
Mitigation: Review the configured linkfox output and cache directories, restrict access, and remove saved responses that should not be retained. <br>


## Reference(s): <br>
- [API Reference](references/api.md) <br>
- [ClawHub Skill Page](https://clawhub.ai/linkfox-ai/skills/linkfox-amazon-product-detail) <br>
- [LinkFox Tool Gateway](https://tool-gateway.linkfox.com) <br>


## Skill Output: <br>
**Output Type(s):** [API Calls, JSON, Files, Markdown, Shell commands, Guidance] <br>
**Output Format:** [Markdown guidance with JSON API responses and saved response files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Queries accept ASIN batches of up to 40 items; the script caches identical requests for 24 hours and saves full responses under a linkfox session data directory.] <br>

## Skill Version(s): <br>
1.0.4 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
