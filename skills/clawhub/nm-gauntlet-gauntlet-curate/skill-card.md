## Description: <br>
Audits the DSA problem bank for coverage gaps and proposes new YAML entries. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[athola](https://clawhub.ai/user/athola) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers maintaining the Gauntlet DSA problem bank use this skill to audit category coverage against the manifest and prepare human-reviewed YAML proposal reports for missing problems. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Generated problem proposals may be inaccurate, duplicative, or poorly aligned with the existing DSA problem bank. <br>
Mitigation: Review the generated report before merging any proposal and validate proposed entries against the Gauntlet problem schema. <br>
Risk: Using the skill outside the intended Gauntlet plugin repository may produce misleading coverage analysis. <br>
Mitigation: Confirm the local workspace contains the Gauntlet problem bank before running the suggested analysis commands. <br>
Risk: Direct edits to problem-bank YAML files could bypass the intended review process. <br>
Mitigation: Keep output as a proposal report and require human approval before applying any YAML changes. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/athola/skills/nm-gauntlet-gauntlet-curate) <br>
- [Gauntlet plugin homepage](https://github.com/athola/claude-night-market/tree/master/plugins/gauntlet) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown report with YAML snippets and inline shell command blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Human review is required before any proposed YAML entries are merged.] <br>

## Skill Version(s): <br>
1.9.17 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
