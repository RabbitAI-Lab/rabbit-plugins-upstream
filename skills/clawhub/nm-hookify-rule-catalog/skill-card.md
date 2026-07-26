## Description: <br>
Browse hookify rule catalog. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[athola](https://clawhub.ai/user/athola) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent users use this skill to browse Hookify rule categories and install pre-built rules into a project as templates or local .claude rule files. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Broad triggers and rule-installation behavior can modify future agent behavior by adding .claude rule files. <br>
Mitigation: Review the exact destination and rule contents before any write, and install only rules intentionally requested by the user. <br>
Risk: The packaged artifact does not include the referenced rule files or installer script. <br>
Mitigation: Treat catalog entries as guidance unless the referenced files are present in the target project or obtained from a trusted source. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/athola/skills/nm-hookify-rule-catalog) <br>
- [Hookify homepage metadata](https://github.com/athola/claude-night-market/tree/master/plugins/hookify) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown instructions with inline shell commands, rule identifiers, and rule-file paths] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May create or instruct creation of local .claude Hookify rule files when the user requests installation.] <br>

## Skill Version(s): <br>
1.9.16 (source: ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
