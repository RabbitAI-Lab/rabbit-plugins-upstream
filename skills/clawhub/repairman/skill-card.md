## Description: <br>
General household repairman assistant for diagnosing appliances, electronics, plumbing, electrical circuits, furniture, and small vehicle issues, with repair steps, safety warnings, DIY versus professional recommendations, and cost estimates. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[bettermen](https://clawhub.ai/user/bettermen) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Household users use this skill to triage common repair problems, compare self-check, DIY, and professional repair options, and produce practical repair guidance or reports. It is most appropriate for low-risk troubleshooting and planning, with hazardous work escalated to qualified professionals. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may provide under-scoped DIY guidance for hazardous electrical, chemical, gas-adjacent, or vehicle brake work. <br>
Mitigation: Use it only as a high-level troubleshooting aid for hazardous cases, and prefer licensed professionals for electrical wiring, gas leaks or gas-line work, microwave or high-voltage repairs, chemical drain cleaners, refrigerant work, and vehicle braking systems. <br>
Risk: Repair advice can be unsafe if the user's symptoms omit critical context such as live power, leaking gas, high work areas, or corrosive chemicals. <br>
Mitigation: Collect key safety context before giving steps, require disconnecting power, gas, or water where applicable, and stop at emergency instructions or professional referral when P0 safety conditions appear. <br>


## Reference(s): <br>
- [ClawHub listing](https://clawhub.ai/bettermen/skills/repairman) <br>
- [Appliance fault reference](references/appliance-faults.md) <br>
- [Plumbing and electrical reference](references/plumbing-electrical.md) <br>
- [Furniture repair reference](references/furniture-fix.md) <br>
- [Repair report template](references/repair-template.md) <br>
- [Safety guide](references/safety-guide.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, guidance] <br>
**Output Format:** [Markdown repair guidance with optional HTML report output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include diagnostic questions, step-by-step repair options, safety warnings, tool and parts checklists, cost estimates, and professional-repair recommendations.] <br>

## Skill Version(s): <br>
1.0.1 (source: evidence.release.version and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
