## Description: <br>
Wx Peitu turns Markdown long-form articles into WeChat-ready illustration packs, including HTML-generated PNG/JPEG assets and Lark Drive delivery guidance. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[edwardwason](https://clawhub.ai/user/edwardwason) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Content creators, editors, and publishing teams use this skill to convert WeChat long-form articles into consistent cover, body, divider, and back-cover illustrations. It is intended for article illustration workflows, not full article typesetting, video, pure image editing, or code editing. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Generated article-derived images may be saved to the Desktop and uploaded to Feishu/Lark Drive automatically. <br>
Mitigation: Use the confirmation-based flow for sensitive articles and disable the upload step when local-only output is required. <br>
Risk: The skill may call external photo APIs and use local Lark/Puppeteer subprocesses during delivery. <br>
Mitigation: Install and run it only in an environment where those services and local sessions are trusted and expected. <br>
Risk: Photo deduplication can keep cross-run state for image selection. <br>
Mitigation: Periodically clear the photo deduplication file if retaining cross-run state is not desired. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/edwardwason/skills/wx-peitu) <br>
- [Workflow Reference](references/workflow.md) <br>
- [Design System Reference](references/design-system.md) <br>
- [Quality Gates Reference](references/quality-gates.md) <br>
- [Assets Reference](references/assets.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance, files] <br>
**Output Format:** [Markdown guidance plus generated HTML, screenshot scripts, and PNG/JPEG image files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Generated illustrations are saved locally and may be uploaded to Feishu/Lark Drive through the user's local lark-cli session.] <br>

## Skill Version(s): <br>
7.4.0 (source: frontmatter, changelog, server evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
