## Description: <br>
Use this skill for Tremendous requests that read, create, or update data through the OOMOL-connected Tremendous connector. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Agents and operators use this skill to work with a connected Tremendous account: create reward orders, generate reward links, and read campaigns, funding sources, organizations, orders, products, and rewards. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Reward orders and redemption links can have financial or recipient-impacting effects. <br>
Mitigation: Require explicit user approval of the exact payload and intended effect before creating orders or links. <br>
Risk: Connected Tremendous account data may include sensitive order, reward, funding, or organization information. <br>
Mitigation: Install and use the skill only for intended Tremendous account operations, and avoid exposing connector responses beyond the user-authorized task. <br>


## Reference(s): <br>
- [Tremendous homepage](https://www.tremendous.com) <br>
- [oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-tremendous) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and JSON connector responses] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Write actions require explicit user confirmation before execution.] <br>

## Skill Version(s): <br>
1.0.0 (source: frontmatter and release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
