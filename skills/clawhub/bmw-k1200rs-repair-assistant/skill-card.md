## Description: <br>
BMW K1200RS motorcycle repair and diagnostic assistant that helps diagnose, maintain, troubleshoot, plan repairs, interpret symptoms, prepare workshop checklists, and cross-check procedures using the user's legally obtained BMW Repair Manual PDF and other user-provided evidence. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[levomm](https://clawhub.ai/user/levomm) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
External users and AI-assisted mechanics use this skill for BMW K1200RS diagnostic triage, maintenance planning, repair checklists, symptom interpretation, and manual-backed verification. It is intended as decision support and requires the user to verify exact factory specifications and procedures against their own authorized repair manual. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Incorrect or incomplete repair guidance could affect motorcycle safety or roadworthiness. <br>
Mitigation: Treat output as decision support, verify exact specifications and procedures against an authorized BMW Repair Manual, and use a qualified mechanic when uncertainty remains. <br>
Risk: Safety-critical systems such as brakes, steering, suspension, fuel, electrical, ABS, or throttle controls can create hazards if repaired incorrectly. <br>
Mitigation: Stop work and use a qualified technician for safety-critical uncertainty, then complete static checks, leak checks, fastener checks, brake checks, and cautious low-speed verification before normal riding. <br>
Risk: Factory values, wiring details, service limits, torque values, or procedures may be missing from the user's prompt. <br>
Mitigation: Ask the user for the relevant page, section, or short excerpt from their legally obtained BMW Repair Manual before giving specification-dependent guidance. <br>
Risk: Requests may involve copyrighted BMW manual material. <br>
Mitigation: Use short user-provided excerpts only when needed, paraphrase the rest, and avoid reconstructing full manual procedures, tables, diagrams, or chapters. <br>


## Reference(s): <br>
- [Manual Policy](references/manual-policy.md) <br>
- [ClawHub Skill Page](https://clawhub.ai/levomm/skills/bmw-k1200rs-repair-assistant) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Guidance] <br>
**Output Format:** [Markdown with structured diagnostic sections, checklists, and verification steps] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires user-provided repair manual excerpts or page references for exact factory specifications, torque values, service limits, wiring details, and procedures.] <br>

## Skill Version(s): <br>
1.0.0 (source: skill.json and ClawHub release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
