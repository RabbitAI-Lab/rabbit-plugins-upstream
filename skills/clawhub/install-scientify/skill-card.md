## Description: <br>
Installs and sets up the Scientify research workflow automation plugin for OpenClaw, adding research-pipeline, literature-survey, idea-generation, arXiv tools, and workspace management. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[springleave](https://clawhub.ai/user/springleave) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Researchers and developers use this skill to install Scientify and enable OpenClaw workflows for literature surveys, research planning, generated implementation work, review, experiments, and research workspace management. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill instructs the agent to install Scientify without asking first. <br>
Mitigation: Require explicit user confirmation before installation and proceed only when the user intends to add Scientify and trusts the `scientify` package and publisher. <br>
Risk: The skill advertises high-impact research automation, including project deletion, paper downloads, generated code execution, and long-running experiments. <br>
Mitigation: Confirm before project deletion, paper downloads, generated code execution, or long-running experiments, and review and scan the skill before deployment. <br>


## Reference(s): <br>
- [Scientify package on npm](https://www.npmjs.com/package/scientify) <br>
- [Scientify GitHub project](https://github.com/tsingyuai/scientify) <br>
- [ClawHub skill page](https://clawhub.ai/springleave/skills/install-scientify) <br>
- [ClawHub publisher profile](https://clawhub.ai/user/springleave) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline shell commands, command descriptions, tool descriptions, and workflow guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May lead the agent to install an OpenClaw plugin and initiate paper downloads, generated code execution, project deletion, or long-running experiments after user confirmation.] <br>

## Skill Version(s): <br>
1.7.3 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
