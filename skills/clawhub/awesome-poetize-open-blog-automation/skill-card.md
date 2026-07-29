## Description: <br>
Helps an agent operate an awesome-poetize-open blog by drafting and publishing posts, updating or hiding content, managing taxonomy, comments, themes, analytics, SEO, image uploads, translations, and paid-article payment settings. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[leapya](https://clawhub.ai/user/leapya) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External developers and blog operators use this skill to automate routine management of an awesome-poetize-open blog, including article drafting, draft-first publishing, content maintenance, taxonomy and comment management, analytics review, SEO configuration, and payment setup when explicitly requested. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The POETIZE API key is a high-privilege blog administration credential. <br>
Mitigation: Use framework secret storage or protected environment variables, prefer a revocable least-privilege key, and avoid committing local credential files or generated config files containing secrets. <br>
Risk: Publishing, hiding posts, changing SEO, comments, themes, taxonomy, sitemap settings, image uploads, and payment configuration can mutate a live blog. <br>
Mitigation: Require explicit confirmation with the concrete target and action, preview new articles as drafts when visibility is unspecified, and run smoke tests before first write actions in a new environment. <br>
Risk: Local Markdown and HTML image references may be uploaded to the configured blog during publishing. <br>
Mitigation: Review every local image path before publishing and stop on missing or unintended image files instead of dropping or guessing them. <br>
Risk: Paid publishing and payment-plugin configuration can affect monetization behavior. <br>
Mitigation: Only configure payment on a POETIZE instance the user controls, require an explicit monetization request, and fail closed when payment checks are unavailable. <br>
Risk: The optional evaluation dry run can send the skill text and a test intent to a user-supplied OpenAI-compatible endpoint. <br>
Mitigation: Run evaluation only with explicit opt-in and a confirmed destination host; keep credential handling separate from the dry-run path. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/leapya/skills/awesome-poetize-open-blog-automation) <br>
- [Strategy playbook](references/strategy-playbook.md) <br>
- [Decision matrix](references/decision-matrix.md) <br>
- [Creativity workflow](references/creativity-workflow.md) <br>
- [awesome-poetize-open project reference](https://github.com/LeapYa/awesome-poetize-open) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown, JSON briefs, environment configuration, and shell commands for the bundled POETIZE CLI] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May create or update blog content and configuration through the configured POETIZE API after explicit confirmation for state-changing actions.] <br>

## Skill Version(s): <br>
2.2.0 (source: server release metadata and skill frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
