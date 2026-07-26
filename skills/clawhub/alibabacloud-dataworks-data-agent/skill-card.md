## Description: <br>
Interact with DataWorks Data Agent for conversational data analysis, session lifecycle management, and artifact download. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[sdk-team](https://clawhub.ai/user/sdk-team) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and data engineers use this skill to operate Alibaba Cloud DataWorks Data Agent sessions through aliyun CLI for conversational data querying, session history, artifact retrieval, token usage checks, and cancellation. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Prompts, dataset context, and attached files are sent to Alibaba Cloud DataWorks Data Agent. <br>
Mitigation: Review each prompt, dataset identifier, and file path before use; do not attach secrets, credential files, personal data, or regulated datasets unless the organization has approved that cloud transfer. <br>
Risk: The skill can issue cloud API calls through an aliyun CLI profile. <br>
Mitigation: Use a profile with only the documented DataWorks Data Agent permissions and confirm the intended action before creating, prompting, loading, listing, downloading, checking token usage, or cancelling sessions. <br>
Risk: Downloaded artifacts depend on paths returned by the cloud service and may contain sensitive analysis output. <br>
Mitigation: List artifacts first, download only expected artifact paths, and handle returned content according to organizational data handling rules. <br>


## Reference(s): <br>
- [DataWorks Data Agent API Reference](artifact/references/api-reference.md) <br>
- [DataWorks Data Agent Examples](artifact/references/examples.md) <br>
- [RAM Policies](artifact/references/ram-policies.md) <br>
- [ClawHub skill page](https://clawhub.ai/sdk-team/skills/alibabacloud-dataworks-data-agent) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline aliyun CLI commands and JSON parameter examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May reference session IDs, artifact paths, token usage, and downloaded analysis artifact content returned by DataWorks Data Agent.] <br>

## Skill Version(s): <br>
0.0.1-beta.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
