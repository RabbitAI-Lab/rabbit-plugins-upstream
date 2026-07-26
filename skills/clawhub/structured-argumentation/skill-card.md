## Description: <br>
一组模型上下文协议服务器，为大型语言模型提供认知增强工具。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[alinklab](https://clawhub.ai/user/alinklab) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent users use this skill to structure claims, premises, conclusions, objections, rebuttals, and synthesis when analyzing complex questions or competing arguments. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Persistent API key storage in a local .env file can expose the credential if the workspace is shared or committed. <br>
Mitigation: Only provide an API key for trusted workspaces, keep .env out of source control, and rotate the key if exposure is suspected. <br>
Risk: Tool inputs are transmitted to an external upstream service. <br>
Mitigation: Avoid sending sensitive claims, private documents, business data, or credentials unless the upstream service and retention policy are acceptable. <br>
Risk: The release under-discloses persistent API key storage, external data transmission, and inconsistent project identity signals. <br>
Mitigation: Review the skill behavior, publisher, and service terms before installing or using it in managed environments. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/alinklab/skills/structured-argumentation) <br>
- [XiaoBenYang service site](https://xiaobenyang.com) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance] <br>
**Output Format:** [Markdown or structured text summarizing upstream JSON results] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires an XBY_APIKEY value and sends tool inputs to the XiaoBenYang upstream service.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
