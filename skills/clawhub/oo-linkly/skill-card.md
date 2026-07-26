## Description: <br>
Linkly (linklyhq.com). Use this skill for ANY Linkly request: reading, creating, updating, and deleting data. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to operate a connected Linkly account from an agent, including workspace discovery, link lookup, short-link creation, updates, and deletion. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can create or update Linkly links in a connected account. <br>
Mitigation: Review the exact action payload and intended effect with the user before approving write actions. <br>
Risk: The skill can delete Linkly short links. <br>
Mitigation: Confirm the target link and obtain explicit approval before running destructive deletion actions. <br>
Risk: Setup and recovery commands can initiate account login, connection, installation, or billing workflows. <br>
Mitigation: Use setup commands only after a command fails with the matching missing CLI, authentication, connection, or billing error. <br>


## Reference(s): <br>
- [Linkly homepage](https://linklyhq.com) <br>
- [oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-linkly) <br>
- [OOMOL publisher profile](https://clawhub.ai/user/oomol) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, API Calls, Configuration instructions, Guidance] <br>
**Output Format:** [Markdown with inline bash commands and JSON payload guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses live connector schemas before constructing action payloads.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata and skill frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
