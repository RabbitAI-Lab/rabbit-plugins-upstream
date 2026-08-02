## Description: <br>
Continuous self-improvement through structured reflection and memory. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[lokix94](https://clawhub.ai/user/lokix94) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent operators use this skill to help an AI agent periodically check whether reflection is due, review past lessons, and log new improvements into local memory. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Reflection logs can accidentally capture secrets, credentials, customer data, or sensitive internal details. <br>
Mitigation: Choose an appropriate local memory-file location and instruct agents not to log sensitive data. <br>
Risk: The README includes external GitHub clone and CLI symlink steps, but the artifact does not include the CLI implementation. <br>
Mitigation: Review the external repository's executable code separately before installing or running the CLI workflow. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/lokix94/skills/self-reflection-2) <br>
- [Server-Resolved GitHub Provenance](https://github.com/lokix94/peru-ai/tree/main/skills/self-reflection) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with shell command examples and JSON configuration snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May produce local Markdown reflection entries and JSON state/configuration files when the referenced CLI workflow is used.] <br>

## Skill Version(s): <br>
0.1.0 (source: ClawHub release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
