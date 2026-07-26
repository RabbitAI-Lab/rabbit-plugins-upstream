## Description: <br>
Vet ClawHub skills for security and utility before installation. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[eddygk](https://clawhub.ai/user/eddygk) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and engineers use this skill to evaluate ClawHub skills before installation by combining automated scan findings with manual review guidance for security and practical utility. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill reads local skill artifacts and can guide scanner execution over files selected by the user. <br>
Mitigation: Review requested shell commands and paths before running them, especially when private files or remote sources are involved. <br>
Risk: Scanner findings and utility judgments can be incomplete because the artifact describes regex-based scanning plus manual review. <br>
Mitigation: Use scanner results as triage input and complete a manual review before installing a skill. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/eddygk/skills/skill-vetting) <br>
- [Malicious patterns and false positives](references/patterns.md) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, markdown, code] <br>
**Output Format:** [Markdown guidance with shell commands and scanner output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [The scanner can report file and line findings with severity levels; human review remains required.] <br>

## Skill Version(s): <br>
1.1.0 (source: ClawHub server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
