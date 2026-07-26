## Description: <br>
Helps agents operate an awesome-poetize-open blog by drafting, publishing, updating or hiding posts, managing taxonomy, comments, media, translations, themes, analytics, SEO, and paid-article settings. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[leapya](https://clawhub.ai/user/leapya) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Blog owners, developers, and agent operators use this skill to manage an awesome-poetize-open blog through guided article workflows, administrative operations, and configuration commands. It is scoped to POETIZE blog management, not general-purpose writing or SEO consulting. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The POETIZE API key can grant broad blog administration access. <br>
Mitigation: Use a revocable least-privilege key, prefer secure environment injection, and protect any generated credential or config files. <br>
Risk: Publishing, hiding content, comment operations, SEO/theme changes, image uploads, and payment configuration can mutate a live blog. <br>
Mitigation: Require explicit confirmation for public posts and other state-changing actions, and use draft or preview flows before publishing. <br>
Risk: Local images and payment configuration files may contain sensitive or unintended content. <br>
Mitigation: Review file paths before upload or payment setup and only use payment configuration on a blog the operator owns. <br>
Risk: The optional eval dry-run can send skill text and test intent to a user-supplied LLM endpoint. <br>
Mitigation: Run eval only with explicit opt-in and confirm the destination host before any external transmission. <br>


## Reference(s): <br>
- [Poetize Blog Automation on ClawHub](https://clawhub.ai/leapya/skills/awesome-poetize-open-blog-automation) <br>
- [Strategy Playbook](references/strategy-playbook.md) <br>
- [Decision Matrix](references/decision-matrix.md) <br>
- [Creativity Workflow](references/creativity-workflow.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown, JSON briefs, shell commands, and configuration snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May produce local article/configuration files and guided command invocations for explicit POETIZE blog operations.] <br>

## Skill Version(s): <br>
2.1.8 (source: server release evidence and artifact frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
