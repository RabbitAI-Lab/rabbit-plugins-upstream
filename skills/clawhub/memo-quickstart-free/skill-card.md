## Description: <br>
Provides a local, zero-dependency memory quickstart for agents using a three-layer memory structure, TF-IDF search, and a write-ahead logging workflow. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent users use this skill to add simple local conversation memory, store preferences and decisions, and retrieve memories without a cloud service or API key. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill stores local conversation memory and may persist sensitive project or user context. <br>
Mitigation: Use it only in workspaces where local memory is acceptable, and do not store secrets, credentials, regulated data, or confidential content. <br>
Risk: The skill requests command execution and recommends installing a global npm package that server evidence could not verify from the registry. <br>
Mitigation: Independently verify the package source and contents before running the global install or any generated memory CLI commands. <br>
Risk: The optional callback_url parameter can disclose processed data to an external endpoint. <br>
Mitigation: Avoid callback URLs unless the endpoint is trusted and approved for the data being processed. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/memo-quickstart-free) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Configuration, JSON] <br>
**Output Format:** [Markdown with inline shell commands and JSON examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces local memory workflow guidance and CLI-oriented examples for storing, searching, and maintaining memory files.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
