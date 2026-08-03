## Description: <br>
Helps an agent create, list, update, delete, draft, and publish Markdown blog posts through a local REST API. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External creators and developers use this skill to let an agent manage blog posts through authenticated REST endpoints, including drafting, publishing, updating, listing, and deleting Markdown content. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill gives an agent authority to publish, update, and delete blog posts, which could change public content or remove posts unintentionally. <br>
Mitigation: Create drafts by default and require confirmation of the exact title, slug, and action before publishing, updating, or deleting content. <br>
Risk: The skill relies on a blog API key for authenticated requests. <br>
Mitigation: Use a least-privilege API key, keep it out of public files and logs, and rotate it immediately if exposed. <br>
Risk: The artifact references setup commands and platform files that should not be executed blindly. <br>
Mitigation: Inspect the actual scripts and platform files before running setup commands, especially in shared or production environments. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/blog-writer-tool-free) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with REST API examples and shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes blog API request examples, setup guidance, draft and publish workflow guidance, and API key handling notes.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release metadata; artifact frontmatter lists 1.0.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
