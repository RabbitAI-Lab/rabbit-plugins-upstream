## Description: <br>
Operates Paddle through an OOMOL-connected account so an agent can list, fetch, create, and update customers, products, and prices. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, operators, and support teams use this skill to let an agent manage Paddle catalog and customer workflows through OOMOL, including reading records and preparing confirmed create or update actions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Write actions can change Paddle customers, products, prices, archive state, or reactivation state. <br>
Mitigation: Confirm the exact JSON payload and expected effect with the user before running create or update actions. <br>
Risk: Connector commands depend on a working OOMOL sign-in, Paddle connection, permissions, credential freshness, and account billing state. <br>
Mitigation: Use the documented first-time setup or connection remediation steps only when a command fails with the matching authentication, scope, credential, app, or billing error. <br>
Risk: Paddle connector schemas may change over time. <br>
Mitigation: Inspect the live action schema with oo connector schema before constructing a payload. <br>


## Reference(s): <br>
- [ClawHub Paddle Skill](https://clawhub.ai/oomol/skills/oo-paddle) <br>
- [Paddle Homepage](https://www.paddle.com) <br>
- [oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [OOMOL CLI Install Guide](https://cli.oomol.com/install-guide.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses live connector schema inspection before payload execution; write actions require confirmation.] <br>

## Skill Version(s): <br>
1.0.0 (source: evidence release, metadata, and frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
