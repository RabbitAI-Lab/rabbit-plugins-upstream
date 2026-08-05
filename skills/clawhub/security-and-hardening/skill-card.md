## Description: <br>
Threat-model and harden applications against security vulnerabilities. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[paudyyin](https://clawhub.ai/user/paudyyin) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to threat-model applications and apply hardening patterns for input validation, authentication, authorization, SSRF, XSS, secrets, dependencies, and LLM-enabled features. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can steer agents toward security-sensitive code and configuration changes. <br>
Mitigation: Require human approval for authentication, authorization, CORS, file upload, external service, sensitive-data, permission, and rate-limit changes before applying them. <br>
Risk: Visible encoding or formatting corruption in the Chinese text may reduce readability. <br>
Mitigation: Review generated guidance against the readable examples and intended security controls before using it for production changes. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/paudyyin/skills/security-and-hardening) <br>
- [OWASP Top 10 for LLM Applications 2025](https://genai.owasp.org/llm-top-10/) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Markdown, Code, Shell commands, Configuration] <br>
**Output Format:** [Markdown guidance with TypeScript, JavaScript, shell, and configuration examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes checklists and approval gates for sensitive security changes] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
