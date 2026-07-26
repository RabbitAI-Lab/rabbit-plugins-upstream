## Description: <br>
JotForm API integration with managed OAuth for creating forms, managing submissions, accessing form data, and managing webhooks through Maton. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[byungkyu](https://clawhub.ai/user/byungkyu) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and external users use this skill to interact with JotForm forms, submissions, webhooks, and account data through Maton's managed OAuth proxy. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: MATON_API_KEY can grant access to connected JotForm data if exposed. <br>
Mitigation: Install only when Maton is trusted, store MATON_API_KEY securely, and avoid sharing terminal output that prints the key. <br>
Risk: Requests may target the wrong JotForm account when multiple connections exist. <br>
Mitigation: Use the Maton-Connection header when multiple accounts are connected and confirm the intended connection before making requests. <br>
Risk: Create, update, and delete operations can modify forms, submissions, webhooks, or connections. <br>
Mitigation: Confirm the exact target resource and intended effect with the user before approving write or delete operations. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/byungkyu/skills/jotform) <br>
- [JotForm API Overview](https://api.jotform.com/docs/) <br>
- [JotForm User Forms](https://api.jotform.com/docs/#user-forms) <br>
- [JotForm Form Submissions](https://api.jotform.com/docs/#form-id-submissions) <br>
- [JotForm Webhooks](https://api.jotform.com/docs/#form-id-webhooks) <br>
- [Maton](https://maton.ai) <br>
- [Maton Settings](https://maton.ai/settings) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration instructions, API Calls, Guidance] <br>
**Output Format:** [Markdown with inline bash, Python, JavaScript, HTTP, and JSON examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires network access and MATON_API_KEY; write operations should be confirmed with the user before execution.] <br>

## Skill Version(s): <br>
1.0.5 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
