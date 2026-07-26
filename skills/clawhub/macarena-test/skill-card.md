## Description: <br>
Security audit and threat model skill for OpenClaw gateway hosts that produces an OK/VULNERABLE report with evidence and fixes. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[misirov](https://clawhub.ai/user/misirov) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and operators use this skill to audit OpenClaw gateway configuration, exposure, local files, and installed skills or plugins, then receive a concise security report with findings and fixes. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill directs the agent to run an unbundled local collection script immediately without user consent. <br>
Mitigation: Review and approve the exact collect_verified.sh script and referenced files from a trusted source before running them. <br>
Risk: The skill handles security evidence that may include sensitive configuration or credential material. <br>
Mitigation: Run only from a trusted working directory and redact tokens, passwords, cookies, OAuth credentials, session contents, pairing codes, and auth headers before sharing results. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/misirov/skills/macarena-test) <br>


## Skill Output: <br>
**Output Type(s):** [markdown, shell commands, guidance] <br>
**Output Format:** [Markdown security report with evidence excerpts, findings, and fix guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires a verified local evidence bundle before producing the final report.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
