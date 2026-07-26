## Description: <br>
Implements hub-and-spoke lazy loading to minimize token usage in large skills. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[athola](https://clawhub.ai/user/athola) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and skill authors use this skill to design modular, multi-workflow agent skills that load only the relevant guidance for the current task and token budget. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill provides developer guidance for composing modular skills, so incorrect adoption could lead to missing or misleading module guidance in downstream skills. <br>
Mitigation: Review the generated or modified skill structure and scan it before deployment. <br>
Risk: Installing the full companion plugin experience may add agents, hooks, commands, or extra configuration beyond this documentation-only artifact. <br>
Mitigation: Review downstream modules and companion Night Market plugin components separately before enabling them. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/athola/skills/nm-leyline-progressive-loading) <br>
- [Leyline plugin homepage](https://github.com/athola/claude-night-market/tree/master/plugins/leyline) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, markdown, code, shell commands, configuration] <br>
**Output Format:** [Markdown guidance with inline code, shell examples, and configuration snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Documentation-only guidance for progressive module selection and token-budgeted loading.] <br>

## Skill Version(s): <br>
1.9.16 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
