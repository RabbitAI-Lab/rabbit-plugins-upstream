## Description: <br>
Mattermost skill for reading Mattermost teams, channels, posts, and user data, and creating posts through an OOMOL-connected account. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Employees, external users, and developers use this skill to let an agent retrieve Mattermost team, channel, post, and current-user information, and to draft or create Mattermost posts after confirmation. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can read Mattermost content visible to the connected account. <br>
Mitigation: Install only for Mattermost accounts whose accessible teams, channels, and posts are appropriate for agent-assisted retrieval. <br>
Risk: The create_post action can publish content to Mattermost. <br>
Mitigation: Require exact user confirmation of the target channel and post payload before running create_post. <br>
Risk: First-time setup may require installing the oo CLI from a remote installer. <br>
Mitigation: Review the oo CLI installer before running first-time setup. <br>


## Reference(s): <br>
- [Mattermost homepage](https://mattermost.com) <br>
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-mattermost) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline bash and JSON command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Reads Mattermost data and can create posts through the OOMOL mattermost connector.] <br>

## Skill Version(s): <br>
1.0.1 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
