## Description: <br>
Fetches web page content, cleans and formats it, optionally translates prose to Simplified Chinese, and saves it as an Obsidian Markdown note with frontmatter, tags, and source metadata. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[wufengsheng](https://clawhub.ai/user/wufengsheng) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, technical writers, and Obsidian users use this skill to capture technical documentation, blog posts, GitHub README pages, and related web content as organized Markdown notes. It supports user confirmation of the target path, optional Simplified Chinese translation, and index-page handling for multi-page documentation. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill fetches user-provided URLs and may use external fallback fetchers when the preferred local fetch path is unavailable. <br>
Mitigation: Avoid private or login-only pages unless the user is comfortable with the fallback service receiving the page URL or content. <br>
Risk: The skill writes Markdown files to an Obsidian destination selected during the workflow. <br>
Mitigation: Review the destination path before confirming, and rely on the skill's post-write readback check to verify frontmatter and source metadata. <br>
Risk: Large pages may be truncated before being saved. <br>
Mitigation: Use the generated truncation warning and original source URL to recover the full content when needed. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/wufengsheng/skills/url-to-obsidian) <br>
- [Publisher profile](https://clawhub.ai/user/wufengsheng) <br>
- [Obsidian note template reference](artifact/references/template.md) <br>


## Skill Output: <br>
**Output Type(s):** [markdown, files, shell commands, guidance] <br>
**Output Format:** [Markdown notes with YAML frontmatter, Obsidian callouts, source links, tags, and a short completion report] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May create one note or multiple notes depending on user-selected handling for index pages and subpages.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
