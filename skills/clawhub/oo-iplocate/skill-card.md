## Description: <br>
This skill guides agents to use the OOMOL IPLocate connector for single, batch, and self IP intelligence lookups. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and external users use this skill to look up IP geolocation, ASN, privacy, hosting, company, and abuse data through their OOMOL-connected IPLocate account. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: IP addresses provided for lookup are sent to IPLocate through OOMOL. <br>
Mitigation: Use the skill only when the user expects an IPLocate lookup through their OOMOL-connected account and avoid submitting unrelated sensitive data. <br>
Risk: The skill depends on an OOMOL account, an IPLocate connection, and available billing credit. <br>
Mitigation: Run setup or billing commands only when connector commands fail with the matching authentication, connection, or credit error. <br>


## Reference(s): <br>
- [ClawHub IPLocate skill page](https://clawhub.ai/oomol/skills/oo-iplocate) <br>
- [IPLocate homepage](https://www.iplocate.io/) <br>
- [OOMOL CLI](https://github.com/oomol-lab/oo-cli) <br>
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses live connector schema inspection before constructing action payloads; connector responses are JSON.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release evidence and artifact metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
