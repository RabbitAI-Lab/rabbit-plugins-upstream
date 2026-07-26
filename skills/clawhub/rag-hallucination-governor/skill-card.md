## Description: <br>
Rag Hallucination Governor helps delivery and technical teams diagnose production RAG hallucinations from symptoms, metrics, or retrieval logs and produce root-cause analysis, tuning advice, and governance steps. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[william202404](https://clawhub.ai/user/william202404) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, delivery engineers, and technical PMs use this skill to triage inaccurate or fabricated RAG answers, tune retrieval thresholds and Top-K behavior, and plan knowledge-base or architecture remediation. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Sensitive production logs may be exposed if users paste them into the agent unnecessarily. <br>
Mitigation: Avoid pasting sensitive production logs unless needed, and redact confidential values before use. <br>
Risk: The skill may activate unexpectedly in broad RAG troubleshooting conversations. <br>
Mitigation: Narrow trigger terms if accidental activation would be disruptive. <br>


## Reference(s): <br>
- [Server-resolved GitHub source](https://github.com/william202404/tob-skills/tree/main/rag-hallucination-governor) <br>
- [ClawHub skill release](https://clawhub.ai/william202404/skills/rag-hallucination-governor) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Guidance] <br>
**Output Format:** [Markdown diagnostic report] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Structured report with symptom classification, root-cause analysis, tuning advice, architecture recommendations, and immediate repair steps.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata; artifact frontmatter lists 1.0.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
