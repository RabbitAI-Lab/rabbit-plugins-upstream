## Description: <br>
Skill Lifecycle records skill usage, identifies low-frequency or retirement candidates, and supports archiving and restoring OpenClaw skills. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[jijinbao-code](https://clawhub.ai/user/jijinbao-code) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and OpenClaw users use this skill to monitor skill activity, identify low-use or retirement candidates, and manually archive or restore skills while preserving metadata. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Archive and restore commands move skill directories in the user's OpenClaw workspace. <br>
Mitigation: Review the target skill name before running archive or restore commands, and use the restore workflow if an archived skill needs to be returned to the active skills directory. <br>


## Reference(s): <br>
- [Skill Lifecycle release page](https://clawhub.ai/jijinbao-code/skills/skill-lifecycle) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Markdown, JSON, Guidance] <br>
**Output Format:** [Markdown instructions with Bash commands; scripts produce JSONL/JSON usage records and a Markdown retirement report.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Archive and restore commands move skill directories under the configured OpenClaw skills and skills-archive paths.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
