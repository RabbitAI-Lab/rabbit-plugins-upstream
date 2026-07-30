## Description: <br>
Generate and edit video with Seedance through RunAPI. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[runapi-ai](https://clawhub.ai/user/runapi-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, developers, and agents use this skill to create, edit, or transform video with Seedance through RunAPI. It guides one-off CLI generation and SDK integration for application or backend workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill uses RunAPI account credentials for video generation. <br>
Mitigation: Confirm trust in RunAPI before installation and prefer RUNAPI_API_KEY or saved CLI configuration over interactive browser authentication for agent and headless runs. <br>
Risk: Generated file URLs are temporary and are not durable storage. <br>
Mitigation: Download generated videos or other returned files to storage you control within 7 days. <br>
Risk: Using the CLI as a production integration layer can create brittle application behavior. <br>
Mitigation: Use the RunAPI SDK integration path for apps, backends, workers, libraries, and production workflows. <br>


## Reference(s): <br>
- [RunAPI Seedance model overview](https://runapi.ai/models/seedance.md) <br>
- [RunAPI Seedance homepage](https://runapi.ai/models/seedance) <br>
- [ByteDance provider comparison](https://runapi.ai/providers/bytedance.md) <br>
- [RunAPI model catalog](https://runapi.ai/models.md) <br>
- [RunAPI CLI skill](https://github.com/runapi-ai/cli-skill) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, code, configuration] <br>
**Output Format:** [Markdown with inline shell commands and SDK package guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May direct agents to use the runapi CLI for one-off generation or RunAPI SDK packages for application integration.] <br>

## Skill Version(s): <br>
0.2.10 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
