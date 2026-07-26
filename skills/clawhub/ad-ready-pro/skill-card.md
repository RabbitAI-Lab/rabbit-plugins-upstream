## Description: <br>
Generate professional advertising images from product URLs using the Ad-Ready pipeline on ComfyDeploy. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[pauldelavallaz](https://clawhub.ai/user/pauldelavallaz) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External advertisers, marketers, and developers use this skill to prepare campaign assets and run a ComfyDeploy pipeline that generates brand-aware advertising images from product URLs, product images, logos, optional reference ads, and funnel-stage prompts. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Product URLs, product images, logos, reference ads, and optional model or talent images are sent to ComfyDeploy and may involve fetching assets from third-party sites. <br>
Mitigation: Use a scoped ComfyDeploy API key where possible and avoid unreleased or confidential campaign assets unless third-party processing is approved. <br>
Risk: Auto-fetch mode can leave sensitive product or logo images in /tmp/ad-ready. <br>
Mitigation: Clean /tmp/ad-ready after auto-fetching sensitive images. <br>
Risk: Generated ads may be lower quality or less brand-consistent when product image, logo, brand profile, or style reference inputs are missing. <br>
Mitigation: Provide explicit product images and logos, select or create the correct brand profile, and include a suitable reference ad before generation. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/pauldelavallaz/skills/ad-ready-pro) <br>
- [Ad-Ready Patreon documentation](https://www.patreon.com/posts/from-product-to-149933468) <br>
- [ComfyDeploy deployment queue API endpoint](https://api.comfydeploy.com/api/run/deployment/queue) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Files, Guidance] <br>
**Output Format:** [Markdown guidance with bash commands; runtime output is generated image files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires COMFY_DEPLOY_API_KEY and sends selected or auto-fetched campaign assets to ComfyDeploy.] <br>

## Skill Version(s): <br>
1.0.0 (source: ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
