## Description: <br>
ByteRover helps agents use the `brv` CLI to retrieve, search, curate, review, and sync project memory stored in `.brv/context-tree`. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[byteroverinc](https://clawhub.ai/user/byteroverinc) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use ByteRover to maintain long-term project memory, retrieve relevant decisions and patterns, and store new context for future work. It supports local search, LLM-backed query and curation, review of pending memory changes, local version control, optional cloud sync, and history inspection. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The security review says ByteRover asks agents to use an LLM-backed memory tool too broadly, which can persist or transmit project and user context without tight consent boundaries. <br>
Mitigation: Use ByteRover only for intentional project-memory workflows, prefer local `brv search` when synthesis is unnecessary, and avoid storing secrets or personal data. <br>
Risk: `brv query` and `brv curate` send query text, curation text, and included file contents to the configured LLM provider. <br>
Mitigation: Review content before using LLM-backed commands, limit file attachments to necessary project-scoped files, and use local search for sensitive or simple lookups. <br>
Risk: Cloud sync can upload stored project knowledge to ByteRover's cloud service when remote version-control commands are used. <br>
Mitigation: Use local version-control workflows unless sync is intended, and only connect providers or run cloud sync after confirming what content may be processed or uploaded. <br>


## Reference(s): <br>
- [ByteRover ClawHub Listing](https://clawhub.ai/byteroverinc/skills/byterover) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and JSON examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Some commands can produce structured JSON output when requested.] <br>

## Skill Version(s): <br>
3.3.0 (source: ClawHub release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
