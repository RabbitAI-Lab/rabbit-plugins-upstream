## Description: <br>
Compute a financial-independence (FIRE) target, estimate years to reach it from stated assumptions, and present a sensitivity grid plus ignored risks instead of a single false-precision answer. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[mohitagw15856](https://clawhub.ai/user/mohitagw15856) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to estimate a FIRE number and years-to-target from current savings, monthly contributions, annual spending, real-return assumptions, and withdrawal-rate assumptions. The skill is intended for educational planning estimates and highlights sensitivity, omitted risks, and professional-verification needs. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill asks for rough savings, contribution, and spending assumptions that may be sensitive. <br>
Mitigation: Install and use it only when comfortable sharing those assumptions with the agent session. <br>
Risk: FIRE outputs can be mistaken for personalized financial advice. <br>
Mitigation: Present results as educational estimates, label assumptions, and verify decisions with a qualified professional. <br>
Risk: The model omits factors such as sequence-of-returns risk, taxes, spending drift, and scenario-specific constraints. <br>
Mitigation: Include the ignored-risks list with each analysis and avoid presenting a single deterministic retirement date. <br>


## Reference(s): <br>
- [ClawHub skill listing](https://clawhub.ai/mohitagw15856/skills/fire-number) <br>
- [Publisher profile](https://clawhub.ai/user/mohitagw15856) <br>
- [Skill homepage](https://mohitagw15856.github.io/pm-claude-skills/skill/fire-number.html) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, guidance] <br>
**Output Format:** [Markdown FIRE analysis with assumptions, calculations, a sensitivity grid, ignored risks, and optional inline bash examples.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Treats outputs as educational planning estimates, not personalized financial advice.] <br>

## Skill Version(s): <br>
50.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
