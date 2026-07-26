## Description: <br>
Prepare Dataify builder requests for the airbnb.com scraper family rooted at airbnb_product_by-searchurl, including tool selection, saved parameter lookup, and generation of a scraperapi.dataify.com builder curl request using DATAIFY_API_TOKEN. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[dataify-server](https://clawhub.ai/user/dataify-server) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and automation users use this skill to prepare Dataify Airbnb scraper builder calls by choosing an available scraper tool, collecting parameter values, and producing an executable curl request. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: DATAIFY_API_TOKEN is required and could be exposed through shell history, profile edits, terminals, or logs. <br>
Mitigation: Treat the token as a secret, avoid committing or sharing token setup commands, and review generated commands before running them. <br>
Risk: User-provided spider parameters may include sensitive personal data sent to Dataify. <br>
Mitigation: Only include personal or sensitive data in spider_parameters when the user intends to send it to Dataify. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/dataify-server/skills/dataify-airbnb-product-by-searchurl) <br>
- [Dataify Dashboard](https://dashboard.dataify.com?utm_source=skill) <br>
- [Saved tool parameter catalog](references/tool-params.json) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown containing a curl command and brief setup guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires DATAIFY_API_TOKEN and user-provided scraper parameter values; generated requests target Dataify's builder endpoint.] <br>

## Skill Version(s): <br>
1.2.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
