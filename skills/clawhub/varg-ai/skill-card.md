## Description: <br>
Generate AI videos, images, speech, and music with varg for videos, animations, talking characters, slideshows, product showcases, social content, or single-asset generation. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[securityqq](https://clawhub.ai/user/securityqq) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, creators, and agent users use this skill to generate media assets and composed videos through varg cloud rendering or local rendering workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill handles API credentials and account sign-in. <br>
Mitigation: Set VARG_API_KEY through the user's shell or a secret manager, avoid pasting raw keys into agent context, and do not commit .env or credential files. <br>
Risk: The skill can consume paid API credits or direct the user to checkout flows. <br>
Mitigation: Confirm estimated cost, available balance, and user intent before full renders, purchases, or checkout-session creation. <br>
Risk: Cloud rendering submits TSX code and media inputs to varg services. <br>
Mitigation: Review render code, prompts, and media files before submission, especially when project or user-provided files are included. <br>
Risk: The artifact includes self-update guidance. <br>
Mitigation: Require explicit user confirmation before updating the skill and re-read changed files before using updated instructions. <br>
Risk: Setup and rendering workflows may create or modify local project files. <br>
Mitigation: Review generated files such as examples, credentials, .env additions, and render outputs before committing or sharing them. <br>


## Reference(s): <br>
- [Varg homepage](https://varg.ai) <br>
- [ClawHub skill page](https://clawhub.ai/securityqq/skills/varg-ai) <br>
- [Cloud Render Mode](references/cloud-render.md) <br>
- [Local Render Mode](references/local-render.md) <br>
- [varg API Reference (v2)](references/gateway-api.md) <br>
- [Model Catalog](references/models.md) <br>
- [Component Reference](references/components.md) <br>
- [Recipes & Patterns](references/recipes.md) <br>
- [Prompt Engineering Guide](references/prompting.md) <br>
- [Common Errors & Debugging](references/common-errors.md) <br>
- [BYOK](references/byok.md) <br>
- [Complete Templates](references/templates.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands, TSX code, and JSON snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May guide agents to create render files, configure credentials, submit cloud jobs, or run local rendering commands.] <br>

## Skill Version(s): <br>
2.0.8 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
