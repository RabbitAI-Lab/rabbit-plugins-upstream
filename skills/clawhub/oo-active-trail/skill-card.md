## Description: <br>
ActiveTrail (activetrail.com). Use this skill for any ActiveTrail request, including reading, creating, updating, and deleting data through the OOMOL ActiveTrail connector. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to operate ActiveTrail through an OOMOL-connected account for contact, group, membership, and account balance tasks. It helps agents inspect the live connector schema, build JSON payloads, and run read, write, or destructive ActiveTrail actions with appropriate confirmation. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Write and destructive actions can modify or remove ActiveTrail contacts and groups. <br>
Mitigation: Confirm the exact target, payload, and intended effect with the user before approving write actions, and require explicit approval before destructive actions. <br>
Risk: First-time setup may involve running an external oo CLI installer. <br>
Mitigation: Run the installer only when the oo command is missing and only after confirming that the user trusts OOMOL's installation source. <br>


## Reference(s): <br>
- [ClawHub ActiveTrail skill page](https://clawhub.ai/oomol/skills/oo-active-trail) <br>
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [ActiveTrail homepage](https://www.activetrail.com/) <br>
- [OOMOL oo CLI install guide](https://cli.oomol.com/install-guide.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration guidance, JSON] <br>
**Output Format:** [Markdown guidance with oo CLI commands and JSON payload or response examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Responses may include connector schema lookup commands, connector run commands, JSON payloads, and confirmation guidance for write or destructive operations.] <br>

## Skill Version(s): <br>
1.0.1 (source: server evidence and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
