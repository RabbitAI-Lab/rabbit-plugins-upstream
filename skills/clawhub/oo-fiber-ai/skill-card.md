## Description: <br>
Fiber AI (fiber.ai). Use this skill for Fiber AI requests involving searching and reading data through the OOMOL connector instead of calling the API directly. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and external users use this skill to let an agent query Fiber AI account information, rate limits, organization credits, and reference datasets through an OOMOL-connected account. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may install or rely on the OOMOL CLI when the command is not available. <br>
Mitigation: Review the OOMOL CLI installer before first use and install it only from the documented OOMOL URL. <br>
Risk: Future Fiber AI actions could write, overwrite, or remove data if such actions are added to the connector. <br>
Mitigation: Require explicit user confirmation of the exact payload and expected effect before approving any action tagged write or destructive. <br>
Risk: Connector calls depend on account connection state, scopes, credentials, and billing status. <br>
Mitigation: Use the documented recovery paths for authentication, connection scope, expired credentials, app readiness, and insufficient credit errors. <br>


## Reference(s): <br>
- [Fiber AI homepage](https://fiber.ai) <br>
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-fiber-ai) <br>
- [OOMOL publisher profile](https://clawhub.ai/user/oomol) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Guides the agent to inspect the live connector schema before running Fiber AI actions.] <br>

## Skill Version(s): <br>
1.0.1 (source: frontmatter and release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
