## Description: <br>
Git助手免费版 helps developers with common Git workflows, merge-conflict resolution, commit-message checks, safety checklists, and reusable configuration templates. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill in an agent to receive Git operation guidance, conflict-resolution steps, commit-message validation, safety checks, and configuration templates for everyday version-control tasks. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Plaintext credential storage guidance can expose repository credentials. <br>
Mitigation: Avoid the plaintext credential-helper store and prefer an OS-backed credential manager or platform token workflow. <br>
Risk: Hard reset recovery commands can discard local work if used on the wrong commit or branch. <br>
Mitigation: Create a backup branch or stash before following reset --hard guidance, and verify the target commit first. <br>
Risk: Generated .gitignore templates can overwrite existing ignore rules. <br>
Mitigation: Review and merge generated .gitignore content instead of blindly replacing an existing file. <br>
Risk: Global Git configuration changes can affect unrelated repositories. <br>
Mitigation: Review each global configuration command before execution and prefer repository-local configuration when appropriate. <br>
Risk: Push guidance can send changes to an unintended remote. <br>
Mitigation: Check remote URLs and branch targets before any push operation. <br>


## Reference(s): <br>
- [Git助手免费版 ClawHub page](https://clawhub.ai/thcjp/skills/git-helper-tool-free) <br>
- [Publisher profile](https://clawhub.ai/user/thcjp) <br>
- [Detailed reference](artifact/references/detail.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with bash, YAML, JSON, and plain-text examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes step-by-step Git guidance, safety checklist output, execution logs, and reusable configuration templates; commands should be reviewed before execution.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release metadata; artifact frontmatter lists 1.0.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
