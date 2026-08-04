## Description: <br>
Automates CI/CD pipeline setup and helps configure build, test, quality gate, and deployment workflows. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to set up or modify CI/CD pipelines, automate quality gates, configure test runners, and prepare deployment-related automation. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill requests command execution and may touch CI/CD or deployment-related files while its scope and safety boundaries are vague. <br>
Mitigation: Install only in repositories where CI/CD automation is intended, and require explicit confirmation before running commands or changing build and deployment configuration. <br>
Risk: The skill discusses API keys, credentials, and external services in deployment workflows. <br>
Mitigation: Do not expose secrets in prompts, logs, or generated files; confirm any external service calls and credential use before execution. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/ci-cd-and-automation) <br>
- [SkillHub homepage](https://skillhub.cn) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline code blocks, shell commands, configuration snippets, and JSON examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May propose CI/CD file changes or command execution; review before applying to deployment repositories.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and artifact frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
