## Description: <br>
Neosoul Decision Agent provides structured decision support with local layered memory for learning user risk preferences, decision-framework preferences, domain weights, decision reviews, proactive decision detection, and confidence labeling. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this agent skill to analyze product, technical architecture, business strategy, and personal decisions with structured tradeoff analysis informed by local decision memory. The skill is intended for decision support and does not make final decisions for the user. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Persistent decision preferences under ~/decision-making/ can expose or retain sensitive decision history. <br>
Mitigation: Review stored memory files periodically, avoid recording third-party sensitive information, and delete or restrict access to entries that are no longer needed. <br>
Risk: Server security evidence flags inconsistent API, callback, and command-execution claims. <br>
Mitigation: Review the skill before installing and approve or block API, callback, or command-execution behavior that is outside the local decision-memory directory. <br>
Risk: Decision recommendations can be misleading if learned preferences are wrong, stale, or based on incomplete context. <br>
Mitigation: Treat outputs as advisory, verify assumptions and confidence labels, and keep final decisions with the user. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/neosoul-decision-agent) <br>


## Skill Output: <br>
**Output Type(s):** [Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown with structured analysis, inline shell commands, configuration steps, and local file paths] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May create, read, and update local decision-memory files under ~/decision-making/ when executed by an agent.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release metadata; artifact frontmatter says 1.0.1) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
