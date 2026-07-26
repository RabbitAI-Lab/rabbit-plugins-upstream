## Description: <br>
Export Clawdbot skills as standalone, deployable microservices. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[macstenk](https://clawhub.ai/user/macstenk) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and engineers use Skill Exporter to package an existing Clawdbot skill as an independent FastAPI microservice for Docker, Railway, or Fly.io deployment. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The exporter can overwrite or delete files in the selected output directory. <br>
Mitigation: Run it with a fresh empty output directory, avoid existing projects or home directories, and review generated files before deploying. <br>
Risk: Generated services may include permissive CORS, copied scripts, dependencies, deployment settings, and optional LLM environment variables that need review before exposure. <br>
Mitigation: Review the generated API, CORS and auth settings, copied scripts, requirements, deployment configs, and .env.example before running or deploying the service. <br>


## Reference(s): <br>
- [Skill Exporter on ClawHub](https://clawhub.ai/macstenk/skills/skill-exporter) <br>


## Skill Output: <br>
**Output Type(s):** [Code, Files, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Generated project files with terminal next steps] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces a FastAPI wrapper, Docker and deployment configuration, requirements, environment examples, copied skill scripts, and optional LLM client code.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
