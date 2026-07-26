## Description: <br>
Create presentations, documents, social posts, and websites using Gamma's AI API. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[mrgoodb](https://clawhub.ai/user/mrgoodb) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and external users use this skill to have an agent submit content to Gamma's API and return generated presentations, documents, social posts, or webpages. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill submits user-provided content to Gamma's external API. <br>
Mitigation: Use it only when Gamma processing is acceptable for the content, and avoid confidential or regulated data unless approved. <br>
Risk: The artifact mentions storing a Gamma API key in a local text file. <br>
Mitigation: Prefer an environment variable or secret manager, and avoid storing API keys in version-controlled files. <br>


## Reference(s): <br>
- [Gamma Developer Documentation](https://developers.gamma.app) <br>
- [Gamma Public API Base URL](https://public-api.gamma.app/v1.0) <br>
- [ClawHub Skill Page](https://clawhub.ai/mrgoodb/skills/gamma-presentations) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Configuration, API Calls] <br>
**Output Format:** [Markdown with inline bash and JSON examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Returns Gamma generation IDs, polling guidance, generated Gamma URLs, and optional export instructions.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
