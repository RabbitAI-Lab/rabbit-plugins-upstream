## Description: <br>
Analyzes InoProShop and CoDeSys Structured Text PLC code across 12 review dimensions and produces structured reports and issue lists. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[paudyyin](https://clawhub.ai/user/paudyyin) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
PLC engineers, controls engineers, and code reviewers use this skill to analyze or review InoProShop and CoDeSys Structured Text PLC files before handoff, documentation, quality audit, or production readiness review. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can suggest changes to safety-related PLC control logic. <br>
Mitigation: Treat findings and code snippets as advisory and require qualified controls or safety engineering review before deployment to equipment. <br>
Risk: Review results may be incomplete when users provide only part of a PLC project. <br>
Mitigation: Validate cross-file dependencies, global variables, and equipment-specific safety interlocks against the full PLC project before acting on recommendations. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/paudyyin/skills/plc-code-toolkit) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Guidance] <br>
**Output Format:** [Markdown report with prioritized issue tables and code snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Analyzes user-provided PLC source files and reports findings by selected review depth or dimension.] <br>

## Skill Version(s): <br>
1.1.0 (source: frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
