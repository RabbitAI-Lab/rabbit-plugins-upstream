## Description: <br>
Simple command-line snippet manager. Use it to save and reuse complex commands. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[gumadeiras](https://clawhub.ai/user/gumadeiras) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and command-line users use this skill to save, search, execute, and optionally sync reusable pet CLI snippets. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Saved snippets can contain sensitive commands or secrets. <br>
Mitigation: Review snippets before reuse and avoid storing passwords, tokens, or other secrets in pet snippets. <br>
Risk: pet exec can execute saved commands on the local machine. <br>
Mitigation: Inspect the selected command before execution and run only snippets that match the intended action. <br>
Risk: pet sync can upload snippet contents to GitHub Gist. <br>
Mitigation: Use pet sync only when the user intentionally wants snippet contents uploaded under that GitHub account's visibility and access settings. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/gumadeiras/skills/pet) <br>
- [ClawHub publisher profile](https://clawhub.ai/user/gumadeiras) <br>


## Skill Output: <br>
**Output Type(s):** [shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires the local pet CLI.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
