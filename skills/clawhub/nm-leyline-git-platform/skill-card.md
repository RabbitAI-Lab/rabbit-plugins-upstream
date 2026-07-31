## Description: <br>
Detects git forge (GitHub/GitLab/Bitbucket) and maps CLI commands cross-platform. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[athola](https://clawhub.ai/user/athola) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to detect the active git forge and translate issue, pull request, merge request, CI/CD, discussion, and repository metadata operations across GitHub, GitLab, and Bitbucket. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may suggest forge commands that create, close, merge, approve, comment, or call APIs against repository resources. <br>
Mitigation: Confirm the target repository, account, platform, and intended action before running any suggested command or API request. <br>
Risk: Broad git-related activation can surface the skill during many repository conversations. <br>
Mitigation: Use its command mappings as references and execute only the commands that match the current hosted forge and user intent. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/athola/skills/nm-leyline-git-platform) <br>
- [metadata/clawdis homepage](https://github.com/athola/claude-night-market/tree/master/plugins/leyline) <br>
- [Complete Command Mapping](artifact/modules/command-mapping.md) <br>


## Skill Output: <br>
**Output Type(s):** [markdown, shell commands, API calls, configuration, guidance] <br>
**Output Format:** [Markdown with inline shell commands, API examples, tables, and configuration guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [No hidden execution or persistent behavior was identified in the artifact.] <br>

## Skill Version(s): <br>
1.9.17 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
