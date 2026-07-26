## Description: <br>
Operate HeyReach through an OOMOL-connected account to read, create, and update campaign, lead, list, account, tag, and outreach statistics data using the oo CLI. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and operators use this skill to manage HeyReach outreach workflows from an agent through an OOMOL-connected account, including reading campaigns, leads, tags, lists, LinkedIn accounts, and outreach statistics, and creating empty lead or company lists. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill lets an agent operate a user's OOMOL-connected HeyReach account through the oo CLI. <br>
Mitigation: Install and use it only when the user is comfortable granting that account access, and keep one-time login or connection setup user-driven. <br>
Risk: The create_empty_list action changes HeyReach state by creating a lead or company list. <br>
Mitigation: Fetch the live action schema first, then confirm the exact payload and expected effect with the user before running the write action. <br>
Risk: Setup, connection, credential, scope, and billing recovery steps can affect account access or costs. <br>
Mitigation: Run setup or billing steps only after the matching command failure or explicit user approval. <br>


## Reference(s): <br>
- [HeyReach homepage](https://www.heyreach.io) <br>
- [oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [oo CLI install guide](https://cli.oomol.com/install-guide.md) <br>
- [ClawHub HeyReach skill](https://clawhub.ai/oomol/skills/oo-heyreach) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and JSON payloads] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include oo connector schema and oo connector run commands; connector results are JSON.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and skill frontmatter metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
