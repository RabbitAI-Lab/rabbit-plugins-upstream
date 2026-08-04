## Description: <br>
Quickly open-source a local skill to GitHub and optionally clawhub.com, with slug pre-checks, safe fork creation, internal-info stripping, frontmatter normalization, license and README generation, git initialization, push support, and decision checkpoints. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[songhonglei](https://clawhub.ai/user/songhonglei) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and skill maintainers use this skill to prepare a local agent skill for public release by creating a separate cleaned copy, generating release files, and publishing through GitHub or optional hub channels. It is intended for workflows where human review is needed around licensing, sensitive content removal, and token handling. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The workflow can publish local files to external services. <br>
Mitigation: Inspect the copied fork and generated file list before running push or publish steps, and keep manual confirmation gates for external uploads. <br>
Risk: The workflow can use session tokens, stored tokens, or a configured token command. <br>
Mitigation: Prefer GitHub CLI or OS keychain token retrieval, avoid plaintext tokens in profile files, and revoke one-time tokens after use. <br>
Risk: Custom exclude patterns can delete files from the fork. <br>
Mitigation: Review any .osg-exclude patterns before execution and avoid broad patterns unless their effect is fully understood. <br>
Risk: Publishing to skillhub.cn is a separate external upload destination. <br>
Mitigation: Treat skillhub.cn publication as an independent release decision and verify the target, token, and uploaded content separately. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/songhonglei/skills/opensource-skill-to-github) <br>
- [GitHub repository](https://github.com/Songhonglei/opensource-skill-to-github) <br>
- [README](README.md) <br>
- [Open-source playbook](references/opensource_playbook.md) <br>
- [Strip checklist](references/strip_checklist.md) <br>
- [UGLIC quick reference](references/uglic_quickref.md) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Code, Configuration, Markdown] <br>
**Output Format:** [Markdown guidance with inline shell commands and generated project files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [The skill can guide file creation, shell execution, git operations, and optional external publishing steps that require human confirmation.] <br>

## Skill Version(s): <br>
1.0.16 (source: server release metadata, SKILL.md, and CHANGELOG.md; released 2026-07-30) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
