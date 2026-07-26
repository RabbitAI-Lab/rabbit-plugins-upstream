## Description: <br>
Helps agents upload images and chunked videos to Shopee MediaSpace for authorized stores through LinkFox gateway scripts. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[linkfox-ai](https://clawhub.ai/user/linkfox-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External developers and commerce operators use this skill to upload product images and video parts for authorized Shopee stores, then retrieve Shopee media URLs for listing workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill makes Shopee-related network calls through LinkFox services and may contact a separate feedback service. <br>
Mitigation: Review the intended outbound services, configured API keys, and feedback data before using the skill with a real store. <br>
Risk: The skill persists complete API responses as local result files. <br>
Mitigation: Confirm where response files are stored, restrict access to the workspace, and delete files that contain sensitive store or media data when they are no longer needed. <br>
Risk: The skill depends on separate Shopee store authorization setup. <br>
Mitigation: Install and complete the required authorization skill before use, and stop if dependency checks report missing authorization. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-shopee-store-media-space) <br>
- [Local API reference](references/api.md) <br>
- [Shopee MediaSpace API documentation](https://open.shopee.com/documents/v2/v2.media_space.init_video_upload?module=91&type=1) <br>


## Skill Output: <br>
**Output Type(s):** [text, JSON, shell commands, files, guidance] <br>
**Output Format:** [Markdown guidance with shell commands and JSON API responses or response summaries] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Scripts write complete API responses under the current workspace and may print full JSON or a summary depending on response size.] <br>

## Skill Version(s): <br>
1.0.3 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
