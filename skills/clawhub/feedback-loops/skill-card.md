## Description: <br>
Helps agents diagnose feedback-driven systems by mapping reinforcing and balancing loops, delays, stocks, flows, leverage points, interventions, and falsifiers. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[deciqai](https://clawhub.ai/user/deciqai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Employees, external users, and agents use this skill to analyze organizational, market, supply-chain, and technology dynamics where feedback loops, delays, or bullwhip effects may cause overshoot, oscillation, collapse, or growth flywheels. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Confidential business situations may become persistent if real case notes are appended to local skill files. <br>
Mitigation: Keep confidential case details out of skill source files unless persistence is intended and approved. <br>
Risk: Feedback-loop analysis can become misleading when the system variable, causal loops, delays, or falsifier are vague. <br>
Mitigation: Use the skill's verification checks to name the system and variable, map at least one loop with delays, and state an observable falsifier. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/deciqai/skills/feedback-loops) <br>
- [Primary sources](references/sources.md) <br>
- [Forrester's Beer Distribution Game and Sterman's 1989 Measurement](examples/forresters-beer-distribution-game-stermans-1989-measurement.md) <br>
- [AI Capex Boom Feedback-Loop Example](examples/ai-capex-boom-reinforcing-and-balancing-loops-2024-2026.md) <br>
- [Sterman 1989, Management Science](https://doi.org/10.1287/mnsc.35.3.321) <br>
- [Lee, Padmanabhan, and Whang 1997, Management Science](https://doi.org/10.1287/mnsc.43.4.546) <br>
- [Meadows, Leverage Points](https://donellameadows.org/archives/leverage-points-places-to-intervene-in-a-system/) <br>
- [IEA Electricity 2024](https://www.iea.org/reports/electricity-2024) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Markdown, Text] <br>
**Output Format:** [Markdown diagnosis template with structured text sections] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May ask follow-up questions before producing a one-case feedback-loop diagnosis.] <br>

## Skill Version(s): <br>
1.0.5 (source: ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
