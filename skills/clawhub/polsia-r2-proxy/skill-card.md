## Description: <br>
Upload and manage files through Polsia's Cloudflare R2 proxy with authenticated API requests. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[agentlevier](https://clawhub.ai/user/agentlevier) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to upload and manage user-selected files through Polsia's Cloudflare R2 proxy with authenticated requests. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Files uploaded through the skill are sent to Polsia's external Cloudflare R2 proxy. <br>
Mitigation: Use the skill only for files intended to be stored through that service and confirm the user trusts Polsia before uploading sensitive content. <br>
Risk: POLSIA_API_KEY is required for authenticated requests and functions as a credential. <br>
Mitigation: Store the API key in a protected environment variable or secret manager, avoid logging it, and do not commit it to source control. <br>


## Reference(s): <br>
- [Polsia R2 proxy API](https://polsia.com/api/proxy/r2) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, code, shell commands, configuration] <br>
**Output Format:** [Markdown] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires POLSIA_API_KEY for authentication and describes upload requirements, response metadata, allowed file types, and size limits.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
