## Description: <br>
Orchestrates a phased workflow for creating Spring Boot and Vue full-stack projects, including requirements, UI design, frontend development, backend integration, testing, and optional Chinese thesis writing. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[tanboku](https://clawhub.ai/user/tanboku) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and students use this skill to coordinate an agent-assisted Spring Boot 3.x, Vue 3, Vite, and MySQL project build from initial idea through implementation and acceptance testing. It can also guide optional Redis, Alipay sandbox payment, AI chat, and Chinese graduation-paper deliverables when the user selects those components. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill asks users to provide high-value secrets such as MySQL root passwords and API keys in chat. <br>
Mitigation: Use placeholders in chat, store real values in environment variables or untracked local secrets files, and prefer a least-privilege database user instead of root credentials. <br>
Risk: The skill generates runnable frontend and backend code through multiple subskills, which can introduce insecure configuration or unreviewed dependencies. <br>
Mitigation: Review, scan, and test generated code before deployment, with particular attention to authentication, CORS, payment callbacks, AI API configuration, and dependency versions. <br>
Risk: The activation wording is broad and may trigger project generation when the user only intends a discussion. <br>
Mitigation: Confirm the user's intent and requested scope before starting the phased build workflow or collecting configuration details. <br>


## Reference(s): <br>
- [Server-resolved GitHub provenance](https://github.com/Tanboku/springboot-vue-builder) <br>
- [ClawHub skill listing](https://clawhub.ai/tanboku/skills/springboot-vue-builder) <br>
- [ClawHub publisher profile](https://clawhub.ai/user/tanboku) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Markdown, Code, Shell commands, Configuration] <br>
**Output Format:** [Markdown with inline code blocks and generated project files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Coordinates staged outputs including Product-Spec.md, UI-Prompts.md, frontend and backend project code, startup commands, and optional thesis.md.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
