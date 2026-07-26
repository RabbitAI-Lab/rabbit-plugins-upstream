## Description: <br>
Queries weekly and monthly 1688 product bestseller rankings to help users discover wholesale products, compare suppliers, and research sourcing opportunities. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[linkfox-ai](https://clawhub.ai/user/linkfox-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External sellers, sourcing teams, and commerce researchers use this skill to query 1688 bestseller data, filter product and supplier attributes, and present product-ranking results for wholesale sourcing decisions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill sends 1688 query parameters, API-authenticated requests, and session metadata headers to LinkFox services. <br>
Mitigation: Use it only when users are comfortable sharing those request details with LinkFox, and avoid submitting sensitive sourcing plans or confidential product identifiers. <br>
Risk: The artifact includes automatic feedback reporting behavior for quality, dissatisfaction, praise, or improvement opportunities. <br>
Mitigation: Review or disable feedback reporting when explicit consent is required before secondary network calls. <br>
Risk: The artifact includes onboarding behavior that may install a helper skill when authentication or credit issues occur. <br>
Mitigation: Require user approval before downloading or installing helper skill content, and review the helper source before use. <br>


## Reference(s): <br>
- [1688 Product Billboard API Reference](artifact/references/api.md) <br>
- [ClawHub Skill Page](https://clawhub.ai/linkfox-ai/skills/linkfox-dld-product-billboard) <br>
- [LinkFox Skill Guide](https://skill.linkfox.com/linkfoxskills/guide.htm) <br>
- [LinkFox Account and Credits](https://os.linkfox.com/) <br>


## Skill Output: <br>
**Output Type(s):** [API Calls, JSON, Markdown, Files, Guidance] <br>
**Output Format:** [Markdown tables and JSON summaries, with full API responses saved as JSON files when the script is used.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Can include product links, shop links, image URLs, pagination guidance, and error guidance; API use consumes 9 credits per call.] <br>

## Skill Version(s): <br>
1.0.5 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
