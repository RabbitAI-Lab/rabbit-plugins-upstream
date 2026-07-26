## Description: <br>
Audits agent and skill code for sensitive information exposure, API key leaks, injection risks, permission issues, and related security concerns with AI-assisted findings and fix suggestions. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[g620710](https://clawhub.ai/user/g620710) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and security reviewers use this skill to review agent, skill, or repository code before release or installation, with findings focused on secrets, injection risks, permissions, data exposure, and AI-agent-specific issues. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The security evidence reports a suspicious verdict because the documentation promises local or static scanning, but the bundled script sends supplied code to a remote HTTP audit API. <br>
Mitigation: Do not submit proprietary code, secrets, credentials, regulated data, or private repositories unless the endpoint, transport security, retention policy, and publisher trust have been reviewed; prefer local-only tools for sensitive reviews. <br>
Risk: The release license evidence and bundled LICENSE.txt do not agree. <br>
Mitigation: Confirm the authoritative license for this release before rendering or publishing the public card. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/g620710/skills/agent-security-audit) <br>
- [AI Agent security checklist](references/security_checklist.md) <br>
- [Publisher profile](https://clawhub.ai/user/g620710) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown or JSON audit reports with command examples and remediation guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires python3 and SECURITY_API_USER_KEY for the bundled SaaS audit command; avoid submitting sensitive code unless the remote endpoint, transport security, retention policy, and vendor trust are acceptable.] <br>

## Skill Version(s): <br>
1.2.4 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
