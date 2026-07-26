## Description: <br>
Npi Quality Gate is a conversational advisor for NPI gate reviews across EVT, DVT, PVT, and MP stages, using user-provided context to assess readiness, explain decision logic, identify missing information, and guide next steps without making final release decisions. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[duding-engicool](https://clawhub.ai/user/duding-engicool) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Manufacturing quality, NPI, and product engineering teams use this skill to discuss stage-gate readiness, unresolved issues, conditional release considerations, and common EVT/DVT/PVT/MP pitfalls based on the information they provide. It supports advisory evaluation and follow-up questions, while final approval and sign-off remain with responsible business owners. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Broad activation on common terms such as EVT, DVT, PVT, and MP may start gate-review guidance when the user is discussing those terms in another context. <br>
Mitigation: Confirm the current NPI stage, the user's specific question, and whether a gate-review readiness assessment is intended before evaluating. <br>
Risk: Users may over-rely on advisory readiness language as a substitute for formal release approval. <br>
Mitigation: State that final release, conditional release, and sign-off decisions must remain with the responsible owners and approval process. <br>
Risk: Incomplete or selectively shared project information can lead to misleading readiness guidance. <br>
Mitigation: Use only stage-relevant excerpts, mark missing critical information as needing follow-up, and ask one or two targeted questions before drawing a conclusion. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/duding-engicool/skills/skill-npi-quality-gate) <br>
- [Server-Resolved Source Repository](https://github.com/duding-engicool/skill-npi-quality-gate) <br>
- [Publisher Profile](https://clawhub.ai/user/duding-engicool) <br>
- [EVT Gate Checklist](references/gate-checklist-evt.md) <br>
- [DVT Gate Checklist](references/gate-checklist-dvt.md) <br>
- [PVT Gate Checklist](references/gate-checklist-pvt.md) <br>
- [MP Gate Checklist](references/gate-checklist-mp.md) <br>
- [NPI Gate Decision Matrix and Residual Issue Mechanism](references/decision-matrix.md) <br>
- [Residual Issue Tracking](references/issue-tracking.md) <br>
- [NPI Stage Pitfalls](references/stage-pitfalls.md) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, text, markdown] <br>
**Output Format:** [Conversational Markdown guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [No files, forms, formal reports, scripts, or final approval decisions are produced by the skill.] <br>

## Skill Version(s): <br>
0.1.0 (source: ClawHub release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
