## Description: <br>
Manage received (inbound) emails and attachments via Resend API. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[mjrussell](https://clawhub.ai/user/mjrussell) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and operators use this skill to help an agent inspect inbound Resend emails, retrieve attachment metadata, and review configured domains when answering email-related questions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can give an agent read access to inbound email content and attachments through RESEND_API_KEY. <br>
Mitigation: Use a dedicated read-only API key and avoid retrieving full message bodies or attachments unless needed. <br>
Risk: Domain commands may reveal configured domains and DNS records. <br>
Mitigation: Run domain lookups only when that information is required and avoid sharing command output unnecessarily. <br>
Risk: The skill depends on the third-party resend CLI package. <br>
Mitigation: Install only if you trust that package and include it in normal dependency review. <br>


## Reference(s): <br>
- [Resend](https://resend.com) <br>
- [ClawHub Skill Page](https://clawhub.ai/mjrussell/skills/resend) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, JSON, guidance] <br>
**Output Format:** [Markdown with inline shell commands and optional JSON command output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires the resend CLI and RESEND_API_KEY.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
