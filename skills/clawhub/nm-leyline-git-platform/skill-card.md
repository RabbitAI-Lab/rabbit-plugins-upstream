## Description: <br>
Detects git forge (GitHub/GitLab/Bitbucket) and maps CLI commands cross-platform. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[athola](https://clawhub.ai/user/athola) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill before running forge-specific commands so they can detect GitHub, GitLab, or Bitbucket projects and choose platform-appropriate issue, pull request, merge request, discussion, and CI/CD commands. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill includes examples for commands that can modify remote repositories, issues, pull requests, merge requests, discussions, or collaborator-facing comments. <br>
Mitigation: Use remote write commands only for user-directed tasks, and verify the target repository, issue, PR/MR, API endpoint, and intended platform before execution. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/athola/skills/nm-leyline-git-platform) <br>
- [Metadata homepage](https://github.com/athola/claude-night-market/tree/master/plugins/leyline) <br>
- [Complete command mapping](modules/command-mapping.md) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Markdown, Shell commands, API calls, Configuration] <br>
**Output Format:** [Markdown reference guidance with inline shell commands, API examples, and command mapping tables] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes platform-specific terminology and fallbacks for GitHub, GitLab, and Bitbucket forge workflows.] <br>

## Skill Version(s): <br>
1.9.16 (source: ClawHub release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
