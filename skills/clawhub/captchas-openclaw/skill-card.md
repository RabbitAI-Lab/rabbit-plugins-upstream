## Description: <br>
OpenClaw integration guidance for CAPTCHAS Agent API, including OpenResponses tool schemas and plugin tool registration. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[captchasco](https://clawhub.ai/user/captchasco) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and engineers use this skill to integrate CAPTCHAS Agent API checks into OpenClaw through OpenResponses tool schemas or OpenClaw plugin tool registration. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: CAPTCHAS API credentials could be exposed or misused if handled insecurely. <br>
Mitigation: Store CAPTCHAS_API_KEY securely and send it only as the required x-api-key header to the verified CAPTCHAS endpoint. <br>
Risk: Verification requests may include unnecessary personal, secret, or regulated data in challenge, token, domain, media, or signal fields. <br>
Mitigation: Send only the minimum data needed for verification and avoid personal, secret, or regulated data unless explicitly approved. <br>


## Reference(s): <br>
- [CAPTCHAS OpenClaw on ClawHub](https://clawhub.ai/captchasco/skills/captchas-openclaw) <br>
- [CAPTCHAS](https://captchas.co) <br>
- [CAPTCHAS Agent API endpoint](https://agent.captchas.co) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, configuration, code, API calls] <br>
**Output Format:** [Markdown with JSON and JavaScript code blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires CAPTCHAS_API_KEY and CAPTCHAS_ENDPOINT environment variables.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
