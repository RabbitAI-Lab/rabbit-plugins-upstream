## Description: <br>
Moosend lets agents read, create, and update Moosend data through the OOMOL oo CLI connector. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to inspect mailing lists and subscribers, fetch subscribers by email, and add or update Moosend subscribers through an OOMOL-connected account. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The security review marked the submitted workspace suspicious because it appears to be a full application repository rather than a single scoped skill. <br>
Mitigation: Review the embedded operational skills and scripts before installing, especially admin actions, production deploys, external service credentials, and local config files. <br>
Risk: The skill can change Moosend state by adding or updating subscribers. <br>
Mitigation: Confirm the exact payload and expected effect with the user before running tagged write actions. <br>


## Reference(s): <br>
- [ClawHub Moosend skill page](https://clawhub.ai/oomol/skills/oo-moosend) <br>
- [OOMOL publisher profile](https://clawhub.ai/user/oomol) <br>
- [oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [Moosend homepage](https://www.moosend.com/) <br>
- [oo CLI install guide](https://cli.oomol.com/install-guide.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline shell commands and JSON payload examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Runs oo connector commands that return JSON responses with data and meta.executionId.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata and skill metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
