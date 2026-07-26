## Description: <br>
Cloud memory for AI agents. Store, search, and recall context across sessions. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[aerialcombat](https://clawhub.ai/user/aerialcombat) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and agent operators use this skill to connect agents to a persistent cloud memory service for storing, searching, recalling, bootstrapping, and deleting selected context across sessions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Selected agent context is sent to and retained by the external ctxly.app service. <br>
Mitigation: Use the skill only when external persistent memory is intended, periodically review stored memories, and delete memories that should no longer persist. <br>
Risk: Secrets, regulated data, or sensitive personal information could be stored if users save inappropriate memory content. <br>
Mitigation: Do not store secrets, regulated data, or sensitive personal information; use dedicated secret storage for credentials and sensitive values. <br>
Risk: The CTXLY_API_KEY grants access to the memory service. <br>
Mitigation: Store the API key in a protected configuration or environment secret and rotate it if exposure is suspected. <br>
Risk: Tweet-based verification can publish a public association if performed without review. <br>
Mitigation: Require human approval before any public tweet-based verification flow. <br>


## Reference(s): <br>
- [MyMemory.bot on ClawHub](https://clawhub.ai/aerialcombat/skills/cloud-memory) <br>
- [Ctxly service homepage](https://ctxly.app) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, configuration] <br>
**Output Format:** [Markdown with inline bash code blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Provides curl examples, environment variable setup, endpoint descriptions, storage recommendations, and rate-limit guidance.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
