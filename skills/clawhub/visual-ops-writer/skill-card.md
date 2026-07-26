## Description: <br>
图文运营创作器 helps content operators, brand teams, skill developers, bloggers, and editors rewrite articles, generate Skill promotion articles, add illustrations, and run article quality checks. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[if530770](https://clawhub.ai/user/if530770) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External content operators, brand teams, skill developers, bloggers, and editors use this skill to create operations articles, rewrite reference articles, produce Skill promotion copy, add generated illustrations, and review article quality before publication. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill fetches supplied links and images, which can expose private or untrusted content. <br>
Mitigation: Use trusted, public URLs when possible and review fetched material before using generated output. <br>
Risk: The skill may send prompts and reference images to RedFox for image generation. <br>
Mitigation: Avoid sensitive or proprietary content unless approved, and use a scoped, revocable REDFOX_API_KEY configured as an environment variable. <br>
Risk: Security evidence reports disabled TLS verification for URL and image fetching. <br>
Mitigation: Treat network fetches as higher risk until fixed; use trusted networks and sources, or avoid link/image-fetch workflows for sensitive work. <br>
Risk: Security evidence notes under-disclosed credential handling. <br>
Mitigation: Do not paste API keys into chat, prompts, logs, or output files; rotate the key if exposure is suspected. <br>


## Reference(s): <br>
- [Core workflow](references/core_workflow.md) <br>
- [Writing framework](references/writing-framework.md) <br>
- [Article type templates](references/article-type-templates.md) <br>
- [Persona matrix](references/persona-matrix.md) <br>
- [Image decision rules](references/image-decision-rules.md) <br>
- [Link rewrite guide](references/link-rewrite-guide.md) <br>
- [Prompt templates](references/prompt-templates.md) <br>
- [Error handling](references/error-handling.md) <br>
- [ClawHub skill page](https://clawhub.ai/if530770/skills/visual-ops-writer) <br>
- [RedFox API keys](https://redfox.hk/settings/api-keys?source=clawhub) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, JSON, Files, Guidance] <br>
**Output Format:** [Markdown article with embedded image links, JSON validation report, local article/report files, and conversational guidance.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Image generation requires REDFOX_API_KEY; without it, the skill can still produce text and may skip images or use placeholders.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata and user changelog) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
