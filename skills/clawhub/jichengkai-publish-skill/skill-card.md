## Description: <br>
Prepare, safety-review, version, commit, and publish local Codex skills through a GitHub-backed release flow and ClawHub CLI. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[jichengkai](https://clawhub.ai/user/jichengkai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and skill publishers use this skill to prepare local Codex skills for GitHub-backed release, run a pre-publish safety review, manage versioning and commits, and publish through the ClawHub CLI or optional GitHub Actions automation. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Publishing, GitHub, and GitHub Actions steps can push code or publish a public skill if run against the wrong target or account. <br>
Mitigation: Confirm the skill path, repository owner, release command, and authentication state before running state-changing commands. <br>
Risk: The skill includes defaults tailored to the publisher's GitHub identity. <br>
Mitigation: Change the owner, repository, and validator path to the installer's own environment before using the workflow for another publisher. <br>
Risk: Tokens, API keys, SSH keys, and other credentials could be exposed if included in a target skill or automation workflow. <br>
Mitigation: Run the included pre-publish scanner, inspect executable scripts manually, and keep ClawHub and GitHub credentials in local auth or repository secrets rather than source files. <br>


## Reference(s): <br>
- [Publishing Flow](references/publishing.md) <br>
- [Security Review](references/security-review.md) <br>
- [ClawHub Skill Page](https://clawhub.ai/jichengkai/skills/jichengkai-publish-skill) <br>
- [Publisher Profile](https://clawhub.ai/user/jichengkai) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands, configuration snippets, code review findings, and concise release notes] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May propose state-changing GitHub or ClawHub commands only after target path, authentication state, and publish details are clear.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
