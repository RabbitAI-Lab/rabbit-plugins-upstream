## Description: <br>
Boost developer productivity with Gitai: An AI-powered Git automation tool that analyzes code changes and generates semantic Conventional Commits instantly. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[leandrosilvaferreira](https://clawhub.ai/user/leandrosilvaferreira) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and engineers use this skill to run a local Gitai CLI workflow that analyzes repository changes, generates Conventional Commit messages, and can commit or push changes when explicitly requested. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can commit repository changes and can push them to a remote branch. <br>
Mitigation: Review the diff and generated commit message before permitting a commit, and allow push only after confirming the target branch and remote. <br>
Risk: The configured Gitai provider may send code changes or summaries to an external AI service. <br>
Mitigation: Use only AI providers approved for the repository contents, and avoid sensitive repositories unless the configured provider is approved for that code. <br>
Risk: The workflow depends on a preinstalled and configured local gitai CLI. <br>
Mitigation: Check that `gitai` is available and `~/.gitai` exists before use; stop and ask the user to install or configure Gitai if either prerequisite is missing. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/leandrosilvaferreira/skills/gitai-skill) <br>
- [Gitai skill repository](https://github.com/leandrosilvaferreira/gitai-skill) <br>
- [Gitai skill issues](https://github.com/leandrosilvaferreira/gitai-skill/issues) <br>
- [Node.js](https://nodejs.org/) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Guidance, Configuration] <br>
**Output Format:** [Markdown with inline bash code blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces agent guidance for checking prerequisites, invoking gitai, reviewing generated commit messages, and optionally pushing changes.] <br>

## Skill Version(s): <br>
1.0.2 (source: ClawHub release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
