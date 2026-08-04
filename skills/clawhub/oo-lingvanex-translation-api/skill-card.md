## Description: <br>
Lingvanex Translation API helps an agent translate text, detect input language, and list supported Lingvanex languages through an OOMOL-connected account. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and external users can use this skill to route Lingvanex translation, language detection, and supported-language lookup requests through the OOMOL connector flow. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Text submitted for translation or language detection is processed by an external Lingvanex connector through OOMOL. <br>
Mitigation: Avoid using the skill with confidential, regulated, or private text unless that third-party processing is acceptable for the deployment. <br>
Risk: Connector authentication or connection state may be missing, expired, or lack required scope. <br>
Mitigation: Use the documented first-time setup steps only after a command returns an authentication or connection error. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-lingvanex-translation-api) <br>
- [Lingvanex Translation API homepage](https://lingvanex.com/products/translationapi/) <br>
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration guidance] <br>
**Output Format:** [Markdown with inline shell commands and JSON payload guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Connector responses are returned as JSON with data and meta.executionId fields.] <br>

## Skill Version(s): <br>
1.0.0 (source: release evidence and skill metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
