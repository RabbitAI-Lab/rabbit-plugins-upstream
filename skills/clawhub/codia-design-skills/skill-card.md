## Description: <br>
Create, edit, enhance, convert, and manage images, design resources, and visual assets with Codia Design Skills and the Codia Open API. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[codia-ai](https://clawhub.ai/user/codia-ai) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and other agent users use this skill pack to route Codia design, image, PDF, SVG, account, and billing-related requests through the local Codia CLI and Codia Open API. It supports workflows such as generating campaign or product assets, converting images or PDFs into editable design data or PPTX, removing backgrounds, describing images, checking credits, and managing usage settings. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can use an authenticated Codia CLI to upload selected images, PDFs, URLs, and prompts to Codia APIs for processing. <br>
Mitigation: Ask for explicit user confirmation before uploading sensitive documents or private images, and only process files or URLs the user has selected for the task. <br>
Risk: The skill can read account and usage data and can change billing-related auto-recharge settings. <br>
Mitigation: Require explicit user confirmation before enabling or changing auto-recharge, recharge thresholds, recharge amounts, monthly limits, or other billing-related settings. <br>
Risk: Public URLs and callback URLs can expose data outside the local workspace or make files accessible to Codia services. <br>
Mitigation: Confirm user intent before using public URLs or callback URLs, and report API errors or validation failures directly instead of treating missing or invalid downloads as successful. <br>


## Reference(s): <br>
- [Codia Open API documentation](https://codia.ai/api-reference#description/introduction) <br>
- [Codia Design Skills on ClawHub](https://clawhub.ai/codia-ai/skills/codia-design-skills) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline shell commands, local file paths, returned URLs, task IDs, compact result summaries, and API error messages when relevant] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May produce or report downloaded images, SVG files, PPTX files, editable design JSON, account usage data, credit balances, and billing setting summaries through the authenticated Codia CLI.] <br>

## Skill Version(s): <br>
0.1.4 (source: frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
