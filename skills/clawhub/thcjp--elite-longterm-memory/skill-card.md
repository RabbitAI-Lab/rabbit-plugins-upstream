## Description: <br>
Elite Longterm Memory guides AI agents through a six-layer long-term memory architecture that combines session state, vector retrieval, Git notes, curated archives, optional cloud backup, automatic fact extraction, and WAL-style persistence. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, teams, and workflow operators use this skill to guide agents in creating, recalling, maintaining, and troubleshooting persistent memory across session files, vector stores, Git notes, curated archives, and optional cloud backup. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill encourages agents to persist user context automatically across multiple memory stores. <br>
Mitigation: Use it only in workspaces where persistent memory is intended, and define explicit consent, review, redaction, retention, and deletion rules before relying on stored memories. <br>
Risk: Stored memories may include secrets or sensitive personal or business data. <br>
Mitigation: Avoid storing secrets or sensitive data, review memory writes before retention, and redact or delete inappropriate entries promptly. <br>
Risk: Optional cloud sync can send remembered context to an external service. <br>
Mitigation: Keep cloud sync disabled unless the operator understands what will be sent and has approved the destination and data-handling rules. <br>


## Reference(s): <br>
- [ClawHub listing](https://clawhub.ai/thcjp/skills/elite-longterm-memory) <br>
- [Skill homepage](https://skillhub.cn) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands, code and configuration snippets, and JSON examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May instruct the agent to create or update memory files and optional cloud-sync configuration.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release metadata; artifact frontmatter says 1.2.4) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
