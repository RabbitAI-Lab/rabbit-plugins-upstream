## Description: <br>
Build a complete, production-ready masterplan for a new project or system from scratch, including websites, web apps, mobile apps, local AI assistants, desktop apps, backend/API services, browser extensions, and CLI tools. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[anjasta-tarigan](https://clawhub.ai/user/anjasta-tarigan) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, product builders, and project teams use this skill to turn a vague new-project idea into a researched, implementation-ready markdown masterplan before writing code. It guides a topic-by-topic interview, validates technical choices with live research, audits production readiness, and writes the final plan to the project workspace. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill writes a masterplan to docs/masterplan/masterplan.md and could overwrite existing planning content if run in a repository that already has that file. <br>
Mitigation: Before running in a workspace with existing docs/masterplan content, check whether masterplan.md already exists or ask the agent to preview and confirm the write target. <br>
Risk: The resulting plan depends on current web research and user answers; stale or incomplete inputs can lead to misleading architecture recommendations. <br>
Mitigation: Require the agent to verify major technical choices during the session and flag any recommendation it cannot validate from current sources. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/anjasta-tarigan/skills/masterplan-builder) <br>
- [Interview topics](artifact/references/interview-topics.md) <br>
- [Production-readiness standards](artifact/references/production-standards.md) <br>
- [Masterplan document structure](artifact/references/masterplan-template.md) <br>
- [Planning and governance gap checklist](artifact/references/gap-checklist.md) <br>


## Skill Output: <br>
**Output Type(s):** [Markdown, Files, Guidance, Configuration] <br>
**Output Format:** [Markdown masterplan written to docs/masterplan/masterplan.md, with concise chat guidance after file creation] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [The masterplan covers architecture, features, data model, security, reliability, costs, roadmap, adaptive behavior, and production-readiness checks.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
