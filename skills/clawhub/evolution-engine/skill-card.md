## Description: <br>
Evolution Engine helps an AI agent learn from explicit corrections, reflect on important work, maintain layered local memory, and track whether repeated mistakes decline over time. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent users use this skill to give an AI coding or productivity assistant a persistent local correction-and-reflection workflow so it can reuse confirmed preferences and project patterns across sessions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill stores durable interaction-derived memory in local files, which can preserve preferences, corrections, or project context longer than expected. <br>
Mitigation: Review stored memory regularly, avoid saving sensitive data, and keep a clear process for exporting, disabling, or deleting the memory directory. <br>
Risk: The manifest requests command execution even though the artifact describes the skill as pure Markdown guidance. <br>
Mitigation: Install with least privilege where possible and review any proposed shell commands before execution. <br>
Risk: Incorrectly learned memories or over-broad rules can affect future agent behavior across sessions or projects. <br>
Mitigation: Require explicit user confirmation before promoting rules, keep project and domain namespaces separate, and archive or remove mistaken memories when found. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/evolution-engine) <br>
- [Publisher profile](https://clawhub.ai/user/thcjp) <br>
- [Clawdis homepage](https://skillhub.cn) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance, configuration] <br>
**Output Format:** [Markdown guidance with structured local-memory file conventions] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces correction records, reflection notes, memory rules, metrics summaries, and maintenance guidance for local files under the skill's memory directory.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
