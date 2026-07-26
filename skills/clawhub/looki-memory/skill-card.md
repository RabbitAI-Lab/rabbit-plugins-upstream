## Description: <br>
Access the user's digital personal memory to retrieve context and generate more personalized, data-driven responses. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[looki](https://clawhub.ai/user/looki) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and their assistants use this skill to retrieve Looki personal memory context, including profile details, moments, media, journals, highlights, and realtime events, so responses can be more personalized and grounded in the user's real-world history. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can expose highly private Looki wearable memory data, including places, people, media, journals, profile data, and realtime events. <br>
Mitigation: Install only when this level of personal memory access is intended, review outputs before sharing them, and avoid using the saved credentials on shared machines. <br>
Risk: The Looki API key is stored locally in ~/.config/looki/credentials.json and can grant account access if exposed. <br>
Mitigation: Treat the credentials file as sensitive, do not save the API key in agent memory or chat history, and remove the saved API key when agent access is no longer needed. <br>
Risk: Sending the API key to an unverified endpoint could disclose the credential. <br>
Mitigation: Validate the base URL with the Looki verification endpoint before first use and only send the API key in the X-API-Key header to the verified base URL. <br>


## Reference(s): <br>
- [Looki Memory on ClawHub](https://clawhub.ai/looki/skills/looki-memory) <br>
- [Looki endpoint verification API](https://open.looki.ai/api/v1/verify?endpoint={base_url}) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, configuration] <br>
**Output Format:** [Markdown documentation with JSON and bash examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Read-only Looki API requests with local credential setup, file download retry guidance, and a 60 requests per minute API-key rate limit.] <br>

## Skill Version(s): <br>
1.0.5 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
