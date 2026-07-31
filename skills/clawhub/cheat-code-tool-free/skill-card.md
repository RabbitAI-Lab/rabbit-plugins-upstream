## Description: <br>
This skill helps an AI agent query an external knowledge service for structured technical documents, API information, domain knowledge, and standards when its built-in knowledge may be incomplete or outdated. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and individual agent users use this skill to supplement an AI agent's answer with external structured knowledge for recent technical documentation, API specifications, standards, and domain-specific questions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill sends lookup requests to a third-party knowledge service and may expose sensitive prompts or private context if used broadly. <br>
Mitigation: Use it only for explicit external lookup requests and do not send secrets, private documents, credentials, or regulated data. <br>
Risk: The skill requires a KNOWLEDGE_TOKEN and includes examples that display or configure the token in shell environments. <br>
Mitigation: Keep the token in a local secret store or environment manager, never echo or commit it, rotate it if exposed, and limit access to trusted agent sessions. <br>
Risk: The artifact requests broad read, write, exec, glob, and grep tools without a clearly bounded need for all local permissions. <br>
Mitigation: Run with the minimum tool permissions needed for knowledge lookup and remove exec or write access unless the publisher documents a specific bounded workflow. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/thcjp/skills/cheat-code-tool-free) <br>
- [Publisher Profile](https://clawhub.ai/user/thcjp) <br>
- [Artifact Skill Definition](artifact/SKILL.md) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration, API Calls] <br>
**Output Format:** [Markdown with inline shell commands and JSON examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [The artifact describes single-query use with optional configuration through KNOWLEDGE_TOKEN, KNOWLEDGE_ENDPOINT, KNOWLEDGE_TIMEOUT, and KNOWLEDGE_MAX_RESULTS.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
