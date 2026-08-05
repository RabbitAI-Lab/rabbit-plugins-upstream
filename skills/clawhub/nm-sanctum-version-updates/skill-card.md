## Description: <br>
Bumps versions, updates changelogs, and coordinates version changes across files for releases. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[athola](https://clawhub.ai/user/athola) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and release engineers use this skill when preparing a release, bumping project versions, updating changelogs, and coordinating version references across project files. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Broad triggers such as version, release, changelog, semver, and bump could activate the workflow during routine discussion. <br>
Mitigation: Require explicit user intent before invoking the skill for release or version-bump work. <br>
Risk: The workflow can guide repository-wide edits to configuration files, changelogs, README files, and documentation. <br>
Mitigation: Preview planned changes with dry-run or diff output before applying edits, then review git status and diffs after changes. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/athola/skills/nm-sanctum-version-updates) <br>
- [ClawHub Publisher Profile](https://clawhub.ai/user/athola) <br>
- [OpenClaw Homepage](https://github.com/athola/claude-night-market/tree/master/plugins/sanctum) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and file-change summaries] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May guide edits to version-bearing configuration files, changelogs, README files, and release documentation.] <br>

## Skill Version(s): <br>
1.9.17 (source: ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
