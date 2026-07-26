## Description: <br>
Security advisory feed package for OpenClaw-related threats and vulnerabilities. The upstream feed is updated daily; local automation is handled by clawsec-suite or the operator. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[davida-ps](https://clawhub.ai/user/davida-ps) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent operators use this skill to subscribe to a security advisory feed, check advisories against installed skills, and receive guidance about emerging agent-security threats. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Standalone installation downloads release artifacts and advisory data from external endpoints. <br>
Mitigation: Use the signed manifest and checksum verification workflow before installing, especially on production hosts. <br>
Risk: Advisory scope and applicability may not be limited to OpenClaw or to locally installed skills. <br>
Mitigation: Review advisory type, affected packages, severity, and exploitability context before taking action. <br>


## Reference(s): <br>
- [ClawHub skill listing](https://clawhub.ai/davida-ps/skills/clawsec-feed) <br>
- [ClawSec homepage](https://clawsec.prompt.security) <br>
- [Advisory feed](https://raw.githubusercontent.com/prompt-security/ClawSec/main/advisories/feed.json) <br>
- [Prompt Security](https://prompt.security) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, markdown, shell commands, configuration, JSON] <br>
**Output Format:** [Markdown guidance with inline bash commands and JSON advisory examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Advisory feed entries include severity, type, affected packages, recommended action, and optional exploitability context.] <br>

## Skill Version(s): <br>
0.0.11 (source: frontmatter, skill.json, CHANGELOG, server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
