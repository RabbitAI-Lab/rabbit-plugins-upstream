## Description: <br>
Encharge (encharge.io). Use this skill for Encharge requests that read, create, or update data through the OOMOL `oo` CLI connector. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operators use this skill to inspect the Encharge connector schema and run Encharge actions through an OOMOL-connected account, including sending transactional email after user confirmation. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can send transactional email through the connected Encharge account. <br>
Mitigation: Review the recipient, subject, body, and complete payload before approving any write action. <br>
Risk: Broad Encharge routing language could be mistaken for permission to perform automatic writes. <br>
Mitigation: Treat the routing language as tool-selection guidance and require explicit user confirmation before actions that change Encharge state. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-encharge) <br>
- [oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [Encharge](https://encharge.io) <br>


## Skill Output: <br>
**Output Type(s):** [shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline shell commands and JSON payload guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses live connector schema inspection before constructing action payloads.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and skill metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
