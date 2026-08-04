## Description: <br>
Provides sem semantic-diff detection, install-on-first-use, and fallback patterns. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[athola](https://clawhub.ai/user/athola) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill when building or modifying skills that consume git diff output. It guides agents to detect sem availability, offer user-approved installation when needed, and normalize sem or git diff output for downstream analysis. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The broad triggers may activate the skill in unrelated git or foundation discussions. <br>
Mitigation: Confirm that the task needs semantic diff guidance before applying the sem workflow. <br>
Risk: The skill can propose installing sem from Cargo, Homebrew, or a release binary. <br>
Mitigation: Only approve installation commands after deciding that sem is trusted and needed; otherwise use the documented git-diff fallback. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/athola/skills/nm-leyline-sem-integration) <br>
- [OpenClaw homepage](https://github.com/athola/claude-night-market/tree/master/plugins/leyline) <br>
- [sem project](https://github.com/Ataraxy-Labs/sem) <br>
- [sem Linux binary release](https://github.com/Ataraxy-Labs/sem/releases/latest/download/sem-x86_64-unknown-linux-gnu) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Markdown, Code, Shell commands, Configuration] <br>
**Output Format:** [Markdown with bash and JSON code blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes sem detection patterns, installation command options, git-diff fallback commands, and normalized entity schemas.] <br>

## Skill Version(s): <br>
1.9.17 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
