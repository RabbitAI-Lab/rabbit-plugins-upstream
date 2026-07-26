## Description: <br>
gitload helps agents download files, folders, or entire GitHub repositories using the gitload CLI without cloning full git history. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[waldekmastykarz](https://clawhub.ai/user/waldekmastykarz) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill when they need to fetch selected files, folders, ZIP archives, or repository contents from GitHub without cloning full history. It also guides authenticated downloads for private repositories and rate-limit-sensitive access. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill invokes the external gitload-cli package and can write downloaded repository contents to local paths. <br>
Mitigation: Use a fresh working directory, prefer narrow output paths, and inspect downloaded code before running install, build, or execution commands. <br>
Risk: Private repository access may involve GitHub credentials or tokens. <br>
Mitigation: Prefer gh auth login, avoid putting real tokens directly in commands, and use fine-grained read-only tokens when a token is necessary. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/waldekmastykarz/skills/gitload) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include GitHub URLs, output paths, ZIP options, and authentication choices.] <br>

## Skill Version(s): <br>
1.0.1 (source: server-resolved release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
