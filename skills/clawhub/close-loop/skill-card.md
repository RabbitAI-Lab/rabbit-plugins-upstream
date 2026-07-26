## Description: <br>
End-of-session workflow for shipping changes, consolidating memory, applying self-improvements, and preparing publishable outputs with safety gates. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[clarezoe](https://clawhub.ai/user/clarezoe) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to close a coding session with clean repository state, scoped memory updates, and a consolidated human-readable and machine-readable wrap report. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can make local repository changes such as commits, file placement fixes, task cleanup, scoped rule updates, and memory writes. <br>
Mitigation: Use dry-run mode first in sensitive repositories, review proposed actions, and rely on the skill's evidence, confidence, retention, dedupe, and sensitive-data filters before persisting memory. <br>
Risk: Push, deploy, publish, and auto-post actions could affect external systems if allowed by policy. <br>
Mitigation: Confirm project policy and require explicit approval or preapproval before allowing pushes, deployments, publishing, or posting. <br>
Risk: Session memory could retain incorrect, stale, or sensitive information. <br>
Mitigation: Keep memory writes scoped to high-signal facts with traceable provenance, reject secrets and sensitive personal data, and mark contradictions as needs-review instead of overwriting active memory. <br>


## Reference(s): <br>
- [ClawHub Close Loop skill page](https://clawhub.ai/clarezoe/skills/close-loop) <br>
- [Memory Frameworks](references/memory-frameworks.md) <br>
- [Session Wrap Report Template](assets/templates/wrap-report-template.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, JSON, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown report with an embedded machine-readable JSON block] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include commit status, push/deploy status, memory write records, applied findings, publish queue items, blocked items, and KPIs.] <br>

## Skill Version(s): <br>
2.3.6 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
