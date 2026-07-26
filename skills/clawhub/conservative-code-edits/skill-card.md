## Description: <br>
Guides agents to make minimal, task-focused code edits while preserving existing architecture, behavior, style, and shared-code boundaries. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[addxing](https://clawhub.ai/user/addxing) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and coding agents use this skill when modifying existing projects where preserving architecture, behavior, style, and shared foundational code is more important than broad refactoring or opportunistic cleanup. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may cause an agent to request confirmation before larger architectural, shared-code, or core-logic edits. <br>
Mitigation: Use explicit user authorization when broader changes are intended, and keep the impact scope visible before proceeding. <br>
Risk: A conservative editing posture can leave unrelated cleanup, refactoring, or latent issues untouched. <br>
Mitigation: Track unrelated improvements separately and address them in dedicated tasks when they are in scope. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/addxing/skills/conservative-code-edits) <br>
- [Server-resolved GitHub provenance](https://github.com/addxing/conservative-code-edits) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Text] <br>
**Output Format:** [Markdown instructions and decision rules] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [No external tools, credentials, or commands are required by the skill itself.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
