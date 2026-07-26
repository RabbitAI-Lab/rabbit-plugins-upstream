## Description: <br>
Code Handover Assistant helps agents inspect handed-over codebases and produce structured Chinese onboarding documents covering business context, architecture, execution flow, dependencies, risks, and next actions. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[chenxyzcyxpp](https://clawhub.ai/user/chenxyzcyxpp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill when receiving an unfamiliar codebase and needing a structured handover package. It guides repository inspection and produces formal Chinese onboarding documents for understanding the project, setting it up, reviewing risks, and planning first-day actions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may read many project files while inspecting a repository, which can surface sensitive private code in generated documentation. <br>
Mitigation: Run it only on the intended target path and review generated HANDOVER.md and QUICKSTART.md before sharing them. <br>
Risk: The skill may run local listing and search commands or delegate analysis on large repositories. <br>
Mitigation: Confirm the repository scope before execution and avoid using it on unrelated private workspaces. <br>
Risk: Generated handover guidance can contain incorrect or misleading interpretations of the codebase. <br>
Mitigation: Verify important claims against cited files and line references before using the documents for onboarding or operational decisions. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/chenxyzcyxpp/skills/code-handover-assistant) <br>
- [Publisher profile](https://clawhub.ai/user/chenxyzcyxpp) <br>
- [Anti-patterns reference](references/anti-patterns.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, guidance] <br>
**Output Format:** [Markdown documents, typically HANDOVER.md and QUICKSTART.md, with concise shell commands where useful] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs are intended for human review before sharing or relying on them for onboarding decisions.] <br>

## Skill Version(s): <br>
1.0.0 (source: ClawHub release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
