## Description: <br>
Review Workflow orchestrates a code-change workflow for developers by collecting change context, reviewing diffs, proposing fixes, running validation checks, generating commit messages, and guiding Git operations. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[abeautifulsnow](https://clawhub.ai/user/abeautifulsnow) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers use this skill after making code changes to run a structured review and commit-preparation workflow. It captures change intent, classifies diffs, checks lint and dependency risks, produces review findings and fix proposals, validates changes, and prepares conventional commit guidance. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The workflow can inspect repository diffs and some untracked files while preparing reviews. <br>
Mitigation: Run it only in repositories where this inspection is intended, and review the generated findings before acting on them. <br>
Risk: The workflow may run local lint, test, and audit tools and may auto-format files. <br>
Mitigation: Review the working tree after execution and confirm any file modifications before committing. <br>
Risk: The workflow guides Git staging, commit, and push operations. <br>
Mitigation: Inspect staged files and generated commit messages, and confirm push commands before execution. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/abeautifulsnow/skills/review-workflow) <br>
- [Server-resolved GitHub provenance](https://github.com/Abeautifulsnow/skills/tree/main/review-workflow) <br>
- [Review Workflow skill definition](SKILL.md) <br>
- [Review preferences](references/review-preferences/SKILL.md) <br>
- [Code reviewer workflow](references/code-reviewer/SKILL.md) <br>
- [Parallel debugging workflow](references/parallel-debugging/SKILL.md) <br>
- [Git commit workflow](references/git-commit/SKILL.md) <br>
- [Security review guide](references/code-reviewer/references/security-review-guide.md) <br>
- [Common bugs checklist](references/code-reviewer/references/common-bugs-checklist.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown reports with inline shell commands, patch diffs, status summaries, and commit message suggestions] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include review findings, lint and dependency security results, test validation summaries, proposed fixes, and Git workflow commands.] <br>

## Skill Version(s): <br>
1.0.1 (source: ClawHub release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
