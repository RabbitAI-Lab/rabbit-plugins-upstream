## Description: <br>
Generates professional recruitment job descriptions and role analyses from job details, with platform-oriented styles for HR and recruiting workflows. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[g620710](https://clawhub.ai/user/g620710) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Recruiters, HR teams, hiring managers, and founders use this skill to draft, optimize, or analyze job descriptions for hiring channels. It can produce role highlights, responsibilities, requirements, salary references, growth-positioning copy, and multi-channel variants from user-provided role details. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The security evidence reports that credentials and hiring inputs are sent to a public-IP HTTP backend with limited disclosure. <br>
Mitigation: Do not use confidential roles, internal hiring plans, compensation details, or reusable API keys unless the publisher documents HTTPS transport, backend operation, credential handling, and data retention. <br>
Risk: JD_API_USER_KEY is a secret used for API-backed generation and account operations. <br>
Mitigation: Store JD_API_USER_KEY as a secret, prefer a scoped service-specific key, and avoid using a general DeepSeek or reusable credential. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/g620710/skills/ai-jd-generator) <br>
- [Artifact skill instructions](artifact/SKILL.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, JSON, shell commands, guidance] <br>
**Output Format:** [Text or Markdown job-description content, with optional JSON output described by the skill documentation.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires python3 and the JD_API_USER_KEY credential for API-backed generation.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
