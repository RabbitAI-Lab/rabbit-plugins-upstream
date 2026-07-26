## Description: <br>
Implementation of the Dynamic Ethical Entity Personality (D.E.E.P.) v2 Framework. The cognitive architecture for agentic sovereignty and partnership. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[dacptn](https://clawhub.ai/user/dacptn) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and agent operators use this skill to structure persistent local personality memory, align required personality files, synchronize selected Markdown fields into a JSON vault, and run the advertised action check before critical actions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill stores and consolidates persistent local personality memory, which could contain secrets or sensitive personal details if users place them in memory/personality/. <br>
Mitigation: Review memory/personality/ and soul_vault.json periodically, and avoid storing secrets or sensitive personal details there. <br>
Risk: The advertised triple-check is not a meaningful safety gate by itself. <br>
Mitigation: Verify the safety-check implementation and review critical actions independently before relying on the check result. <br>


## Reference(s): <br>
- [Personality Template](artifact/personality_template.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and JSON CLI output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires Python >=3.8 and writes local personality state under memory/personality/ when the sync command is run.] <br>

## Skill Version(s): <br>
2.2.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
