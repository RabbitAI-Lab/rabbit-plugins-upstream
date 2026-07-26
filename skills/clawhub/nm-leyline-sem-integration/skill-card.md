## Description: <br>
Provides sem semantic-diff detection, install-on-first-use, and fallback patterns. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[athola](https://clawhub.ai/user/athola) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers building or modifying skills that consume git diff output use this skill to add semantic-diff detection, optional sem installation, and normalized git-diff fallback behavior. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Broad activation terms can cause the skill to trigger when semantic-diff guidance is not needed. <br>
Mitigation: Review the trigger terms before installation and narrow them if accidental invocation would interrupt the workflow. <br>
Risk: Install-on-first-use guidance can involve package-manager commands or downloading a sem binary. <br>
Mitigation: Review the proposed install command and source before running it, or decline installation and use the documented git-diff fallback path. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/athola/skills/nm-leyline-sem-integration) <br>
- [Clawdis homepage](https://github.com/athola/claude-night-market/tree/master/plugins/leyline) <br>
- [sem CLI repository](https://github.com/Ataraxy-Labs/sem) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration] <br>
**Output Format:** [Markdown guidance with shell command examples and JSON schema examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes primary sem paths and git-diff fallback patterns for agent workflows.] <br>

## Skill Version(s): <br>
1.9.16 (source: ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
