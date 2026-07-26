## Description: <br>
Designs email preference centers, frequency opt-down ladders, preference-to-suppression mappings, and a SEND N sub-item note for preference-center and frequency options. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[aaron-he-zhu](https://clawhub.ai/user/aaron-he-zhu) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Email marketers, lifecycle operators, and agent users use this skill to design subscriber-facing preference centers and opt-down paths that offer topic, cadence, and pause choices before a hard unsubscribe. The skill also maps each preference choice to ESP and consent-registry rules for downstream audit and handoff. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: ESP exports and consent data can contain sensitive subscriber preferences or suppression facts. <br>
Mitigation: Review ESP exports and consent data before sharing them, and confirm saved memory or consent-registry handoffs reflect the intended suppression rules. <br>
Risk: Incorrect preference-to-suppression mapping could cause sends that ignore subscriber topic, cadence, pause, or opt-out choices. <br>
Mitigation: Require every topic toggle, cadence tier, and pause option to map to an explicit ESP and consent-registry rule before using the output operationally. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/aaron-he-zhu/skills/preference-frequency-manager) <br>
- [Project homepage](https://github.com/aaron-he-zhu/aaron-marketing-skills) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, configuration, guidance] <br>
**Output Format:** [Markdown with structured preference-center specs, opt-down ladders, choice-to-rule mappings, SEND N sub-item notes, and handoff summaries] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May write reusable handoff summaries to memory paths when the agent host supports canonical state.] <br>

## Skill Version(s): <br>
19.0.0 (source: server release metadata and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
