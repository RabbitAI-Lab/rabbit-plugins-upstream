## Description: <br>
Selects optimal sources for tool calls, balancing accuracy with token cost for research tasks and citation decisions. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[athola](https://clawhub.ai/user/athola) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to decide when citations or source checks are warranted and when a concise uncertainty note is sufficient. It supports research and factual-response workflows that need to balance verification value against token cost. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The guidance may under-source legal, security, compliance, or current factual claims if used as the only citation policy. <br>
Mitigation: Apply stricter sourcing and review requirements for high-stakes or time-sensitive claims. <br>
Risk: Agents may make incorrect sourcing decisions when balancing verification value against token cost. <br>
Mitigation: Review outputs before deployment and require source checks when accuracy materially affects user decisions. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/athola/skills/nm-conserve-smart-sourcing) <br>
- [Conserve plugin homepage](https://github.com/athola/claude-night-market/tree/master/plugins/conserve) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Markdown, Text] <br>
**Output Format:** [Markdown guidance with decision tables and examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Documentation-only guidance; no executable output.] <br>

## Skill Version(s): <br>
1.9.16 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
