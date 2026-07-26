## Description: <br>
Cyberimpact (cyberimpact.com). Use this skill for ANY Cyberimpact request -- reading, creating, updating, and deleting data. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, developers, and operators use this skill to let an agent inspect Cyberimpact connector schemas and run Cyberimpact actions for groups, members, and email templates through an OOMOL-connected account. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can create, update, replace, and delete Cyberimpact groups, members, and email templates, which may affect business contact data. <br>
Mitigation: Confirm the exact payload, target object, and expected effect with the user before approving write or destructive actions. <br>
Risk: Incorrect payloads can change member lists, group visibility, or template content in unintended ways. <br>
Mitigation: Fetch the live connector schema before building payloads and review the constructed JSON before execution. <br>


## Reference(s): <br>
- [Cyberimpact homepage](https://www.cyberimpact.com/) <br>
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-cyberimpact) <br>
- [OOMOL publisher profile](https://clawhub.ai/user/oomol) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline shell commands and JSON payload guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Directs the agent to inspect live connector schemas before constructing Cyberimpact action payloads.] <br>

## Skill Version(s): <br>
1.0.0 (source: frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
