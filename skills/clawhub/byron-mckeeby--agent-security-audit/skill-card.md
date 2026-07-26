## Description: <br>
A defensive checklist for strengthening AI-agent prompt-injection handling when processing external content. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[byron-mckeeby](https://clawhub.ai/user/byron-mckeeby) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and security reviewers use this skill to audit AI-agent workflows that ingest external content and to plan prompt-injection defenses, content sanitization, detection, and memory-write controls. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Example shell commands may modify files or write to privileged log paths if copied directly. <br>
Mitigation: Run examples only on copies of data, review every command, and adjust paths and permissions intentionally. <br>
Risk: The promotional external link is not vetted security guidance. <br>
Mitigation: Treat the link as publisher-provided promotional content and rely on internal security review for implementation decisions. <br>
Risk: Checklist controls may be incomplete for a specific agent architecture. <br>
Mitigation: Validate the proposed patterns against the target agent's trust boundaries, tools, memory behavior, and logging requirements. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/byron-mckeeby/skills/agent-security-audit) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Markdown, Code, Shell commands, Configuration] <br>
**Output Format:** [Markdown with checklist items and example bash and nginx code blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes defensive checklist guidance; code blocks are examples and should be reviewed before use.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
