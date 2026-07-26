## Description: <br>
Searches 1688 by product image and returns visually similar supplier listings with prices, minimum order quantities, sales, seller badges, and trade metrics. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[linkfox-ai](https://clawhub.ai/user/linkfox-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External sourcing teams and agents use this skill to find visually similar products on 1688 from a public image URL, local uploaded image, Base64 image, or returned image ID. It helps compare supplier listings by price, minimum order quantity, monthly sales, repurchase rate, seller badges, and trade score. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Local product images may be uploaded to a publicly reachable URL for search. <br>
Mitigation: Use non-sensitive images, confirm the user is comfortable with public upload before searching local files, and treat generated image URLs as temporary shared data. <br>
Risk: Search requests are sent through LinkFox/1688 services using configured credentials and gateway endpoints. <br>
Mitigation: Verify LINKFOX_AGENT_API_KEY or LINKFOXAGENT_API_KEY and the gateway configuration before use, and avoid entering credentials into untrusted prompts. <br>
Risk: Full API responses are persisted locally and may contain detailed search results. <br>
Mitigation: Review where response files are written, keep them out of shared workspaces when results are sensitive, and delete saved files when no longer needed. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-1688-search-by-image) <br>
- [1688 image search API reference](references/api.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, JSON, Files, Shell commands, Guidance] <br>
**Output Format:** [Markdown summaries and tables with saved JSON response files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Large responses are summarized while full API responses are saved under the LinkFox session data directory; product results may include inline image URLs.] <br>

## Skill Version(s): <br>
1.0.4 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
