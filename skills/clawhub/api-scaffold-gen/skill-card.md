## Description: <br>
Api Scaffold Gen is an API scaffolding agent skill for developers that generates project scaffolds, DDD and microservice templates, ORM and migration code, OpenAPI reverse-generation guidance, Docker and Kubernetes manifests, and CI/CD configurations. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, platform engineers, and technical leads use this skill to start or standardize API projects across Node.js, Python, Java, and Go stacks. It helps generate API scaffolds, DDD layers, microservice infrastructure templates, ORM models and migrations, WebSocket endpoints, deployment manifests, and CI/CD configuration for review and adaptation. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can produce code, Docker/Kubernetes manifests, and CI/CD files that may change application or infrastructure behavior. <br>
Mitigation: Treat all generated files as reviewable templates; run normal code review, tests, security scans, and deployment review before use. <br>
Risk: The security evidence notes unclear privacy and control guidance for remote LLM use and token requirements. <br>
Mitigation: Avoid sharing proprietary source, secrets, credentials, or sensitive infrastructure details unless the deployment path and data handling are acceptable. <br>
Risk: Generated scaffold choices can encode incorrect framework, database, or service configuration assumptions. <br>
Mitigation: Verify stack-specific settings such as ORM mappings, database URLs, service discovery, tracing, Kubernetes resources, and CI/CD credentials before execution. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/api-scaffold-gen) <br>
- [Skill homepage](https://skillhub.cn) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with command examples and generated project files or configuration templates] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include API scaffolds, ORM and migration files, Docker and Kubernetes manifests, CI/CD workflows, OpenAPI files, and microservice or WebSocket templates for user-selected stacks.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata and skill frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
