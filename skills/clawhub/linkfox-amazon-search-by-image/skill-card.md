## Description: <br>
Searches Amazon by image URL across eight marketplaces to find visually similar product listings, with optional Keepa-enriched product data. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[linkfox-ai](https://clawhub.ai/user/linkfox-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External agents, developers, Amazon sellers, and product researchers use this skill to find visually similar Amazon listings from a product image URL for comparison, sourcing, counterfeit review, and market discovery. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Image URLs, optional local image files, request metadata, and API-key-authenticated requests are sent to LinkFox. <br>
Mitigation: Use the skill only with data that is acceptable to share with LinkFox and avoid sensitive or private images unless sharing is intentional. <br>
Risk: Local image upload can make an image externally accessible. <br>
Mitigation: Confirm the image can be public before upload and treat uploaded image URLs as temporary external links. <br>
Risk: The skill can auto-send feedback or install onboarding support without clear user consent. <br>
Mitigation: Review and approve feedback submission or onboarding installation before allowing those actions. <br>
Risk: Cached or saved results may be written outside the documented location in some cases. <br>
Mitigation: Inspect generated LinkFox output directories after use and avoid running the skill in workspaces that cannot contain API result data. <br>


## Reference(s): <br>
- [Amazon image search API reference](artifact/references/api.md) <br>
- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-amazon-search-by-image) <br>
- [LinkFox skills guide](https://skill.linkfox.com/linkfoxskills/guide.htm) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, files] <br>
**Output Format:** [Markdown response with product tables, inline images, JSON summaries, and saved JSON result files when the script is used.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May call authenticated LinkFox APIs, upload local images to obtain public URLs, and cache or save API responses for later inspection.] <br>

## Skill Version(s): <br>
1.0.4 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
