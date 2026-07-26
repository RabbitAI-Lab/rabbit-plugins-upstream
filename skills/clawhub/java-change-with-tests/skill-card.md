## Description: <br>
Guides agent-assisted Java changes through minimal edits, targeted tests, command verification, and a PR-ready summary. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[tanerilyazov](https://clawhub.ai/user/tanerilyazov) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers use this skill when making Java feature, refactor, or bug-fix changes that need a small implementation plan, test evidence, and a reviewable pull request summary. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Build and test commands may execute code already present in the project. <br>
Mitigation: Use the skill in repositories you trust, review commands before execution, and run verification in an appropriate development environment. <br>
Risk: Agent-produced Java changes can still be incomplete or incorrect even when tests pass. <br>
Mitigation: Review the resulting diff, confirm the acceptance criteria, and require relevant unit or integration test evidence before merging. <br>


## Reference(s): <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, guidance] <br>
**Output Format:** [Markdown plan, file-change summary, command results, risks, and follow-ups.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes exact test commands and results when the agent runs verification.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
