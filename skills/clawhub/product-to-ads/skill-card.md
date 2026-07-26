## Description: <br>
Generate professional advertising images from product URLs using the Ad-Ready pipeline on ComfyDeploy, with optional brand profiles, model or talent inputs, funnel-stage targeting, and multi-format output. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[pauldelavallaz](https://clawhub.ai/user/pauldelavallaz) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External users and marketing or creative teams use this skill to turn a product URL and authorized product, logo, brand, and optional talent assets into ad-ready campaign images. The skill supports funnel-stage creative direction and platform-oriented aspect ratios for commercial advertising workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may preserve or analyze faces, bodies, ethnicity, and exact poses for commercial ad imagery. <br>
Mitigation: Use model, talent, and reference images only when clear consent and commercial usage rights are documented; otherwise use product-only generation or licensed synthetic assets. <br>
Risk: Product URLs and image assets may be sent to ComfyDeploy during generation. <br>
Mitigation: Use public product pages and assets that the user has rights to share; avoid confidential product pages, private media, and unapproved customer data. <br>
Risk: Reference ads, logos, and brand assets can create likeness, trademark, or campaign-copying concerns. <br>
Mitigation: Use logos, brand assets, and reference ads only when the user has the required rights and has explicitly requested that style or asset use. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/pauldelavallaz/skills/product-to-ads) <br>
- [Skill documentation](artifact/SKILL.md) <br>
- [Campaign brief prompt configuration](artifact/configs/Brief_Generator/brief_prompt.json) <br>
- [Funnel-stage master prompts](artifact/configs/Product_to_Ads/) <br>
- [Reference analyzer prompt](artifact/configs/Reference_Analyzer/reference_analysis_prompt.txt) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Configuration, Files] <br>
**Output Format:** [Markdown guidance with inline shell commands and generated image file outputs] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires a ComfyDeploy API key and may upload product, logo, model, or reference images to ComfyDeploy.] <br>

## Skill Version(s): <br>
1.4.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
