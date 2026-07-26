## Description: <br>
Builds, validates, and confirms ChatMOSP MSR and KMC parameters, including database lookup, gas entropy calculation, interaction-parameter conversion, and missing-parameter handling. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[sanyangye](https://clawhub.ai/user/sanyangye) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and researchers using ChatMOSP use this skill to assemble, complete, validate, and confirm MSR or KMC simulation parameters before handing them to companion calculation skills. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Missing parameters may trigger companion literature lookup and generated simulation files after confirmation. <br>
Mitigation: Review literature-derived or defaulted parameters and generated-file plans before confirming the workflow. <br>
Risk: Language-routing labels in the artifact may be confusing. <br>
Mitigation: Check that the selected language file and response language match the user's latest message before relying on the skill. <br>
Risk: Literature-derived interaction parameters may be converted between KMC and MSR formats under a default assumption. <br>
Mitigation: Check the original literature before using converted MSR interaction values. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/sanyangye/skills/chatmosp-parameter-builder) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, configuration, guidance] <br>
**Output Format:** [Markdown parameter summaries with JSON-oriented configuration values] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires explicit user confirmation before calculation and keeps MSR and KMC parameter sets separate.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
