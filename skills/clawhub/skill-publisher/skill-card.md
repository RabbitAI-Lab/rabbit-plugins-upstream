## Description: <br>
Publishes SKILL.md-based Agent Skills to ClawHub and skills.sh through a workflow that validates metadata, prepares documentation, cleans release bundles, drafts release notes, and reports publication status. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[mebusw](https://clawhub.ai/user/mebusw) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and skill maintainers use this skill to move a local SKILL.md-based Agent Skill toward public release on ClawHub and skills.sh. It is intended for release preparation tasks such as validation, documentation refresh, release-note drafting, bundle cleanup, and publishing status reporting. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The workflow has broad release-oriented authority and can prepare files or commands that affect public skill publication. <br>
Mitigation: Run the workflow in dry-run mode first and review the validation report, generated files, cleanup log, and publish commands before executing a real release. <br>
Risk: The publishing namespace and generated install commands are hardcoded to the mebusw account, which may be wrong for other publishers. <br>
Mitigation: Use this workflow only for the mebusw namespace, or fork and update the publisher handle before publishing under a different account. <br>
Risk: A release bundle may expose secrets or unintended local files if cleanup results are not reviewed. <br>
Mitigation: Inspect the cleaned bundle and verify that credentials, dot-files, logs, and other non-release files were removed before publication. <br>


## Reference(s): <br>
- [Server-resolved source repository](https://github.com/mebusw/skill-publisher) <br>
- [ClawHub skill listing](https://clawhub.ai/mebusw/skills/skill-publisher) <br>
- [Publisher profile](https://clawhub.ai/user/mebusw) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance, command snippets, generated documentation files, release notes, cleanup logs, and publish summaries] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May create or update README.md, README.zh-cn.md, RELEASE_NOTES.md, and a cleaned release bundle when run outside dry-run mode.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
