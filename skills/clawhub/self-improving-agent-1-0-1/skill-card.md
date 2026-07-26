## Description: <br>
Captures learnings, errors, corrections, and feature requests so coding agents can log recurring issues and promote useful knowledge into project memory. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[pntrivedy](https://clawhub.ai/user/pntrivedy) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and agent users use this skill to capture command failures, user corrections, missing capabilities, outdated knowledge, and better recurring approaches in structured project memory. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Durable learning logs can capture conversation details, secrets, personal data, or customer data. <br>
Mitigation: Keep .learnings local unless reviewed, and redact secrets plus personal or customer data before retaining or sharing entries. <br>
Risk: Global always-on hooks can make learning capture apply to every prompt or command result. <br>
Mitigation: Avoid global hooks unless the scripts and scope have been reviewed and the user explicitly wants every prompt covered. <br>
Risk: Promoting entries into agent instructions or new skills can preserve incorrect, sensitive, or overly broad guidance. <br>
Mitigation: Require explicit human review before promoting entries into CLAUDE.md, AGENTS.md, Copilot instructions, or new skills. <br>


## Reference(s): <br>
- [Hook Setup Guide](artifact/references/hooks-setup.md) <br>
- [Entry Examples](artifact/references/examples.md) <br>
- [Agent Skills Specification](https://agentskills.io/specification) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration instructions, Guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and JSON configuration snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May guide creation or updates to .learnings markdown files, project memory files, hook settings, and reusable skill scaffolds.] <br>

## Skill Version(s): <br>
1.0.0 (source: ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
