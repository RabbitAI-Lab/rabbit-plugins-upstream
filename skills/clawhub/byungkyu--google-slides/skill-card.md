## Description: <br>
Google Slides API integration with managed OAuth for creating presentations, adding slides, inserting content, and managing slide formatting. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[byungkyu](https://clawhub.ai/user/byungkyu) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to call Google Slides through Maton-managed OAuth, including creating presentations, managing slides, inserting text or images, and applying formatting changes. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill uses Maton-managed OAuth to access a connected Google Slides account or workspace. <br>
Mitigation: Install only after confirming trust in Maton, connect the least-privileged Google account practical, and review requested access before authorizing the connection. <br>
Risk: Create, update, and delete requests can change presentations, slides, and slide content. <br>
Mitigation: Require explicit user approval before write operations and confirm the target presentation, resource, and intended effect before execution. <br>
Risk: MATON_API_KEY grants access to the integration and could be misused if exposed. <br>
Mitigation: Store MATON_API_KEY as a secret, do not include it in logs or shared prompts, and avoid using it in untrusted projects. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/byungkyu/skills/google-slides) <br>
- [Google Slides API overview](https://developers.google.com/slides/api/reference/rest) <br>
- [Presentations API](https://developers.google.com/slides/api/reference/rest/v1/presentations) <br>
- [Pages API](https://developers.google.com/slides/api/reference/rest/v1/presentations.pages) <br>
- [BatchUpdate API](https://developers.google.com/slides/api/reference/rest/v1/presentations/batchUpdate) <br>
- [Maton](https://maton.ai) <br>


## Skill Output: <br>
**Output Type(s):** [text, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with API endpoint examples and inline bash, Python, JavaScript, and JSON snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires network access and MATON_API_KEY for live API calls.] <br>

## Skill Version(s): <br>
1.0.4 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
