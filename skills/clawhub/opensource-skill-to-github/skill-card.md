## Description: <br>
Quickly open-source a local skill to GitHub and optionally ClawHub by guiding slug checks, copy-based cleanup, metadata normalization, license and README generation, git setup, push, and optional publishing. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[songhonglei](https://clawhub.ai/user/songhonglei) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and skill maintainers use this agent skill to prepare a local skill for public release through a guided, copy-based workflow. It helps coordinate cleanup, documentation, license selection, git initialization, GitHub push, and optional ClawHub publication. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The workflow handles GitHub and hub publishing credentials and can read tokens from environment variables, a profile file, a shell command, or the GitHub CLI. <br>
Mitigation: Prefer a trusted keychain command or GitHub CLI token source, avoid storing personal access tokens in profile files, and revoke any temporary token after use. <br>
Risk: The skill writes persistent local profile data for author and credential-source configuration. <br>
Mitigation: Review the profile path and contents before use, keep profile permissions restricted, and avoid placing secrets directly in the profile. <br>
Risk: Cleanup and exclude behavior can remove files from the copied fork before publication. <br>
Mitigation: Run the workflow only on copied forks, inspect any .osg-exclude file and scan report, and review generated changes before pushing or publishing. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/songhonglei/skills/opensource-skill-to-github) <br>
- [Open-source playbook](references/opensource_playbook.md) <br>
- [Strip checklist](references/strip_checklist.md) <br>
- [UGLIC quick reference](references/uglic_quickref.md) <br>
- [README template](references/readme_template.md) <br>
- [Precedents](references/precedents.md) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, configuration, markdown, code] <br>
**Output Format:** [Markdown guidance with inline shell commands and generated or modified project files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires user confirmation at publishing, license, cleanup, credential, and slug decision points.] <br>

## Skill Version(s): <br>
1.0.14 (source: server release evidence and artifact SKILL.md) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
