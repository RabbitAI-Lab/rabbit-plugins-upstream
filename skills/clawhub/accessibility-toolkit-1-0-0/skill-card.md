## Description: <br>
Friction-reduction patterns for agents helping humans with disabilities through voice-first workflows, smart home templates, and efficiency automation. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[stavrostsamadias](https://clawhub.ai/user/stavrostsamadias) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
External users, caregivers, and accessibility-focused developers use this skill to help agents reduce manual effort for humans with physical disabilities through voice-first workflows, smart home templates, batch operations, and failure recovery patterns. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Smart home examples can affect physical security when applied to locks, doors, alarms, or similar high-impact devices. <br>
Mitigation: Adapt templates with explicit confirmations or strict allowlists before enabling high-impact actions. <br>
Risk: Conversation-history audits can expose private history if run without user consent or clear boundaries. <br>
Mitigation: Get consent first, set privacy limits, and avoid mining conversation history beyond the stated accessibility task. <br>
Risk: Example access codes or recovery instructions can encourage unsafe handling of secrets. <br>
Mitigation: Replace access-code examples with placeholders or secret storage before deployment. <br>
Risk: Medication reminders and other care-related routines may be treated as authoritative if copied directly. <br>
Mitigation: Keep human review and confirmation for medical routines and other high-impact assistance. <br>


## Reference(s): <br>
- [Apple Accessibility](https://www.apple.com/accessibility/) <br>
- [Home Assistant Accessibility](https://www.home-assistant.io/docs/accessibility/) <br>
- [Apple Human Interface Guidelines: Accessibility](https://developer.apple.com/design/human-interface-guidelines/accessibility) <br>
- [ClawHub skill page](https://clawhub.ai/stavrostsamadias/skills/accessibility-toolkit-1-0-0) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, markdown, code, configuration] <br>
**Output Format:** [Markdown guidance with YAML and code examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes templates and checklists that should be adapted before use.] <br>

## Skill Version(s): <br>
1.0.0 (source: SKILL.md frontmatter, package.json, server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
