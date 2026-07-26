## Description: <br>
Send emails via Google Apps Script when traditional SMTP ports are blocked. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[rishikreddyl](https://clawhub.ai/user/rishikreddyl) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and agent operators use this skill to send automated email over HTTPS when SMTP ports are blocked, after deploying their own Google Apps Script relay and configuring token-based access. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: An agent can send email through a public Google Apps Script relay as the user's account, with access controlled by a shared token. <br>
Mitigation: Use only with a Google account approved for automated email, require an HTTPS Apps Script URL, store a long random token as a secret, and rotate it if exposed. <br>
Risk: The relay code is referenced by the artifact but not included, so the deployed Google Apps Script behavior may differ from the skill documentation. <br>
Mitigation: Inspect or supply the Google Apps Script relay code before deployment and confirm that it enforces the expected token check. <br>
Risk: Automated sending can reach unintended recipients or exceed acceptable volume. <br>
Mitigation: Add recipient allowlists, rate limits, or per-send approval before allowing an agent to send messages. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/rishikreddyl/skills/openclaw-email-bypass) <br>
- [Google Apps Script Email Bypass Setup Guide](references/setup.md) <br>
- [OpenClaw Email Bypass Usage Examples](references/examples.md) <br>
- [Google Apps Script](https://script.google.com) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Code, Configuration instructions, Guidance] <br>
**Output Format:** [Markdown with inline bash and Python examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires python3, the requests package, GOOGLE_SCRIPT_URL, and GOOGLE_SCRIPT_TOKEN; sends email requests to a user-managed Google Apps Script relay.] <br>

## Skill Version(s): <br>
0.1.2 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
