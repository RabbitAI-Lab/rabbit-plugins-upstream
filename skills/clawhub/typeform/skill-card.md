## Description: <br>
Typeform API integration with managed OAuth for creating forms, managing responses, and accessing insights. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[byungkyu](https://clawhub.ai/user/byungkyu) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operators use this skill to connect an agent to a Typeform account through Maton, list and manage forms, retrieve responses, and inspect Typeform insights. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill uses Maton as an OAuth proxy for Typeform API actions, so requests depend on the intended Typeform connection and a protected MATON_API_KEY. <br>
Mitigation: Use the intended Typeform connection, set the Maton-Connection header when multiple connections exist, and keep MATON_API_KEY out of logs and shared outputs. <br>
Risk: Create, update, and delete actions can change forms, responses, or related Typeform resources in the connected account. <br>
Mitigation: Confirm the target resource and intended effect with the user before allowing any write or delete request to run. <br>


## Reference(s): <br>
- [ClawHub Typeform skill](https://clawhub.ai/byungkyu/skills/typeform) <br>
- [Typeform API Overview](https://www.typeform.com/developers/get-started) <br>
- [Typeform Forms API](https://www.typeform.com/developers/create/reference/retrieve-forms) <br>
- [Typeform Responses API](https://www.typeform.com/developers/responses/reference/retrieve-responses) <br>
- [Typeform Workspaces API](https://www.typeform.com/developers/create/reference/retrieve-workspaces) <br>
- [Maton](https://maton.ai) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline HTTP paths, JSON examples, Python and JavaScript snippets, and shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires network access and MATON_API_KEY; write operations should be confirmed with the user before execution.] <br>

## Skill Version(s): <br>
1.0.5 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
