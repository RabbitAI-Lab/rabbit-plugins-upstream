## Description: <br>
Bumps versions, updates changelogs, and coordinates version changes across files for releases. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[athola](https://clawhub.ai/user/athola) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and release maintainers use this skill when preparing a release or bumping a project version across configuration files, changelogs, and version references. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Broad triggers such as version, release, changelog, semver, and bump may activate the skill during ordinary release discussions. <br>
Mitigation: Confirm that the intended task is a release or version bump before applying the workflow. <br>
Risk: Version bump workflows can affect multiple configuration and documentation files. <br>
Mitigation: Review the dry run, git status, and diff before allowing edits or accepting proposed changes. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/athola/skills/nm-sanctum-version-updates) <br>
- [Sanctum plugin homepage](https://github.com/athola/claude-night-market/tree/master/plugins/sanctum) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline shell commands and release file-change summaries] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include proposed version edits, changelog updates, git status, and diff excerpts.] <br>

## Skill Version(s): <br>
1.9.16 (source: server release metadata; artifact frontmatter reports 1.9.8) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
