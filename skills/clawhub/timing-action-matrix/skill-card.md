## Description: <br>
Helps agents and teams assess whether a proposed action is paired with the right timing before committing to a high-stakes decision. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[deciqai](https://clawhub.ai/user/deciqai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, operators, and decision-support agents use this skill to separate action quality from timing conditions for launches, policy decisions, market entries, negotiations, and post-mortems. It guides the agent to map a decision into success, resistance, mistake, or disaster and produce a concrete next action or timing trigger. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The framework may be mistaken for authoritative advice in high-stakes historical, business, policy, or operational decisions. <br>
Mitigation: Treat outputs as decision-support guidance and independently verify claims, assumptions, and timing conditions before acting. <br>
Risk: A user or agent may collapse timing into intuition instead of checking concrete conditions, reducing the value of the matrix. <br>
Mitigation: Require at least three named timing conditions and mark each present, absent, or partial before selecting a quadrant. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/deciqai/skills/timing-action-matrix) <br>
- [deciqAI Timing-Action Matrix Metadata](https://www.deciqai.com/s/timing-action-matrix.json) <br>
- [deciqAI Timing-Action Matrix Page](https://www.deciqai.com/c/timing-action-matrix) <br>
- [Knowledge Skills Repository](https://github.com/deciqAI/knowledge-skills) <br>
- [Primary Sources](references/sources.md) <br>
- [D-Day Timing Decision Example](examples/d-day-timing-decision-june-1944.md) <br>
- [The Prince](https://www.gutenberg.org/ebooks/1232) <br>
- [The Alchemy of Finance](https://www.wiley.com/en-us/The+Alchemy+of+Finance-p-9780471042211) <br>
- [Forecast for Overlord](https://archive.org/details/forecastforoverl0000stag) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, markdown] <br>
**Output Format:** [Markdown decision worksheet with concise coaching prompts and checklist fields] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces advisory decision-support text; it does not execute code or access external systems.] <br>

## Skill Version(s): <br>
1.0.4 (source: server evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
