## Description: <br>
Prepare Claw skills for public release by validating structure, security, portability, documentation, testing, git hygiene, and metadata. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[acastellana](https://clawhub.ai/user/acastellana) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and skill maintainers use this skill to prepare Claw skills for public release, including audits for structure, security, portability, documentation, testing, git hygiene, and metadata. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The toolkit can modify and publish skill repositories. <br>
Mitigation: Review changes with git diff before publishing and run it only in the intended public skill repository. <br>
Risk: Forced publishing or running publish.sh from a directory with private files can expose unintended content. <br>
Mitigation: Avoid --force unless the target directory contains only intended public skill content. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/acastellana/skills/skill-publisher-claw-skill) <br>
- [README](artifact/README.md) <br>
- [Versioning Guide](artifact/docs/versioning.md) <br>
- [Deprecation Process](artifact/docs/deprecation.md) <br>
- [README Quality Guide](artifact/docs/readme-quality.md) <br>
- [Claw Docs](https://docs.clawd.bot) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, markdown, code, shell commands, configuration] <br>
**Output Format:** [Markdown guidance with inline bash commands, templates, and checklist content] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes shell scripts that can audit, fix, scaffold, score, analyze, validate links, generate changelogs, and publish skill repositories.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release evidence; artifact changelog lists 1.0.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
