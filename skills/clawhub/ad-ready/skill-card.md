## Description: <br>
Generate advertising images automatically from a product URL and brand profile. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[pauldelavallaz](https://clawhub.ai/user/pauldelavallaz) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External marketers, creative teams, and developers use this skill to turn ecommerce product URLs, brand profiles, and funnel objectives into ad-ready product images. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Product URLs, images, logos, model photos, reference ads, brand choices, and briefs may be sent to external services. <br>
Mitigation: Review before installing, use only public product URLs, avoid internal or private links, and do not submit confidential campaign assets. <br>
Risk: Generated ads can closely copy a person's likeness or protected traits without built-in consent controls. <br>
Mitigation: Use model and reference images only when the publisher has rights and consent for the intended commercial ad use. <br>
Risk: Reference ads or brand assets may introduce rights and reuse concerns. <br>
Mitigation: Provide logos and reference ads only when they are authorized for the campaign, and leave optional reference inputs empty unless explicitly needed. <br>


## Reference(s): <br>
- [Ad-Ready ClawHub Release](https://clawhub.ai/pauldelavallaz/skills/ad-ready) <br>
- [Campaign Brief Prompt](configs/Brief_Generator/brief_prompt.json) <br>
- [Product-to-Ads Master Prompts](configs/Product_to_Ads/) <br>
- [Reference Analyzer Prompt](configs/Reference_Analyzer/reference_analysis_prompt.txt) <br>


## Skill Output: <br>
**Output Type(s):** [Files, Shell commands, Configuration instructions, API Calls] <br>
**Output Format:** [PNG image file with CLI status text and Markdown command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires a ComfyDeploy API key and may send product URLs, product images, logos, model images, reference images, brand choices, and briefs to external AI services.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
