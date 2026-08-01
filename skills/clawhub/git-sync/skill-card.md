## Description: <br>
git-sync normalizes and publishes skill code to Gitee and GitHub, creates ZIP install packages, and updates related release indexes and manifests. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ldxs001](https://clawhub.ai/user/ldxs001) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and skill maintainers use git-sync to package a ClawHub skill, compare version metadata, scan and redact sensitive content, update manifests and README output, and push releases to configured Gitee and GitHub remotes. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may perform automated Git commits and pushes to configured Gitee and GitHub remotes. <br>
Mitigation: Review the target skill, configured remotes, generated report, and package outputs before sharing or retrying pushes. <br>
Risk: The skill may change global Git credential storage to plaintext store and use stored credentials. <br>
Mitigation: Use it only in an environment where that credential behavior is acceptable; prefer SSH keys or a secure credential manager. <br>
Risk: Skipping the sensitive information scan can allow secrets to be packaged or pushed. <br>
Mitigation: Do not use --skip-scan unless the skill has been independently checked for secrets. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/ldxs001/skills/git-sync) <br>
- [git-sync complete usage guide](artifact/references/guide.md) <br>
- [git-sync complete reference manual](artifact/references/reference.md) <br>
- [git-sync permissions guide](artifact/references/permissions.md) <br>
- [git-sync FAQ](artifact/references/faq.md) <br>
- [git-sync changelog](artifact/references/changelog.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, files] <br>
**Output Format:** [Markdown or terminal text reports with shell commands, plus generated ZIP and HTML files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May produce Git commits and pushes, sanitized package artifacts, manifests, README updates, and an HTML package index.] <br>

## Skill Version(s): <br>
2.36.0 (source: server release metadata; artifact frontmatter and changelog show 2.9.2) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
