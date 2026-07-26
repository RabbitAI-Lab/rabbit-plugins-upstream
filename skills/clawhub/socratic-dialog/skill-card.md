## Description: <br>
Reasoning rigor and anti-sycophancy guard for high-stakes decisions that anchors questions to operational definitions, cross-examines assumptions, and checks faithfulness before synthesis. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[monikazapisekstudio](https://clawhub.ai/user/monikazapisekstudio) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, developers, designers, and product teams use this skill to slow down ambiguous or high-stakes reasoning, define key terms, challenge unsupported agreement, and keep long-session decisions consistent. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill intentionally adds questioning and friction, which can slow simple tasks or direct-answer workflows. <br>
Mitigation: Enable it for high-stakes, ambiguous, or strategically loaded reasoning; avoid it for simple lookups, routine edits, and tight-latency tasks. <br>
Risk: The dialogue can stall when key terms or missing evidence are not supplied. <br>
Mitigation: After repeated decomposition without progress, surface the missing variable, ask for an external anchor, or mark any assumption as low confidence. <br>
Risk: Users may treat structured reasoning support as an autonomous product, budget, technical, or contractual decision. <br>
Mitigation: Present tradeoffs and contradictions clearly, then ask the user to make or confirm the final decision. <br>


## Reference(s): <br>
- [Socratic Dialogue on ClawHub](https://clawhub.ai/monikazapisekstudio/skills/socratic-dialog) <br>
- [Methodology - Socratic Dialogue](references/methodology-socratic-dialogue.md) <br>
- [Agent Skills open standard](https://agentskills.io) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Guidance] <br>
**Output Format:** [Markdown conversational responses with clarifying questions, confidence notes, retractions, and fixed-parameter summaries.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Reasoning-only output; no tool, network, or file access is required at runtime.] <br>

## Skill Version(s): <br>
0.1.3 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
