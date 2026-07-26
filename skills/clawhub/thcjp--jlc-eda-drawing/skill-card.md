## Description: <br>
Jlc Eda Drawing helps agents act as circuit-design copilots for JLC EDA / EasyEDA by planning schematic architecture, choosing parts, drawing PCB-ready schematics, and validating electrical design assumptions. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, engineers, and electronics designers use this skill to create or revise EasyEDA/JLC EDA schematics and PCB-ready circuit blocks with real parts, labeled nets, and documented verification. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may propose local command execution for EasyEDA automation while the referenced bridge script and reference files are absent from the artifact. <br>
Mitigation: Review any bridge package, script, or command before running it, especially when working on important design files. <br>
Risk: Circuit-design output can be incomplete or electrically unsuitable for safety, mains-voltage, battery-charging, RF, high-current, or precision-analog work. <br>
Mitigation: Require qualified engineering review of component ratings, footprints, nets, isolation, ERC/DRC results, and documented assumptions before fabrication or deployment. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/jlc-eda-drawing) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown with code snippets and command proposals] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include assumptions, verification notes, real-part selections, substitutions, and electrical risks that need review.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
