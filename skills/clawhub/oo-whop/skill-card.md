## Description: <br>
Operates Whop through an OOMOL-connected account by inspecting connector schemas and running read-only Whop actions with the oo CLI. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, developers, and operators use this skill to read Whop authorized users, companies, memberships, and products from an OOMOL-connected Whop account. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can read data available through the user's connected Whop account, including broad list queries. <br>
Mitigation: Confirm the company, product, membership, or user scope before list queries and request only the data needed for the task. <br>
Risk: First-time recovery may install the oo CLI or require OOMOL sign-in and a Whop connection. <br>
Mitigation: Run setup steps only after the matching command failure and let the user authorize installation, sign-in, or account connection. <br>
Risk: Connector input schemas can change over time, which can make guessed payloads fail or query the wrong fields. <br>
Mitigation: Fetch the live action schema with `oo connector schema` before building each action payload. <br>


## Reference(s): <br>
- [Whop homepage](https://whop.com) <br>
- [oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [oo CLI install guide](https://cli.oomol.com/install-guide.md) <br>
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-whop) <br>


## Skill Output: <br>
**Output Type(s):** [shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline bash commands and JSON payload guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires live connector schema inspection before constructing action payloads.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release and skill metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
