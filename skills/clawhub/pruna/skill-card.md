## Description: <br>
Use when installing the full Pruna generative media suite, including guides, tools, and workflows in one package. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[pruna-ai](https://clawhub.ai/user/pruna-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, creators, and agent operators use this skill to install the full Pruna generative media suite and route work to the appropriate guide, API, tool, or workflow skill. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Dependent skills may call external Pruna or Replicate APIs with user credentials and generate billable media. <br>
Mitigation: Review the dependent skills before use, scope API keys appropriately, and confirm user intent before paid API calls. <br>
Risk: The umbrella release installs a broad media-generation suite, so behavior depends on the selected guide, tool, or workflow skill. <br>
Mitigation: Install only the needed dependent skills when possible and review each selected skill's requirements before execution. <br>


## Reference(s): <br>
- [Pruna dashboard](https://dashboard.pruna.ai/) <br>
- [ClawHub skill page](https://clawhub.ai/pruna-ai/skills/pruna) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline shell commands and configuration guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Installs and coordinates dependent Pruna skills; dependent skills may use API credentials and local media tooling.] <br>

## Skill Version(s): <br>
1.0.8 (source: server release metadata and SKILL.md metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
