## Description: <br>
Publish content directly to WordPress sites via the REST API with Gutenberg block support, category selection, SEO tag generation, preview workflows, and scheduled publishing. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[asif2bd](https://clawhub.ai/user/asif2bd) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and content teams use this skill to prepare, preview, publish, update, schedule, and verify WordPress posts or pages from Markdown or HTML while preserving Gutenberg block structure. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can change a live WordPress site by publishing, updating, deleting, uploading media, and creating categories or tags. <br>
Mitigation: Install only for WordPress sites you control, default to draft and preview workflows, and require explicit confirmation before any publish, update, delete, upload, category, or tag operation. <br>
Risk: WordPress application passwords are used for API authentication and can be exposed if pasted into shell history, chat logs, or shared output. <br>
Mitigation: Use a least-privilege WordPress application password, avoid passing it directly on the command line, and rotate it after use or if exposure is suspected. <br>
Risk: A mistyped or untrusted site URL could send credentials or content to the wrong WordPress endpoint. <br>
Mitigation: Verify the WordPress site URL before connecting and test authentication against the intended site before any write operation. <br>


## Reference(s): <br>
- [Gutenberg Blocks Reference](references/gutenberg-blocks.md) <br>
- [WordPress REST API Handbook](https://developer.wordpress.org/rest-api/) <br>
- [WordPress Core Blocks Reference](https://developer.wordpress.org/block-editor/reference-guides/core-blocks/) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, markdown, code, shell commands, configuration] <br>
**Output Format:** [Markdown guidance with Python examples, shell commands, configuration steps, and Gutenberg-formatted content snippets.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Prompts users to start with draft and preview workflows before publishing or scheduling changes to a WordPress site.] <br>

## Skill Version(s): <br>
0.1.0 (source: ClawHub server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
