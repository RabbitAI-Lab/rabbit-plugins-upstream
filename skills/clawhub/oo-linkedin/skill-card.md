## Description: <br>
Enables an agent to operate LinkedIn through an OOMOL-connected account, including member profile lookup, post creation, reshares, and post deletion with confirmation safeguards. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent users use this skill to manage a connected LinkedIn account through OOMOL for profile lookup, public posting, reshares, and explicit post deletion. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can publish LinkedIn posts or reshare existing posts. <br>
Mitigation: Confirm the exact content, target action, and intended effect with the user before running any write action. <br>
Risk: The skill can delete a LinkedIn post by raw post URN. <br>
Mitigation: Require explicit user approval for the exact post URN before running the destructive delete action. <br>
Risk: Authentication, connection, or missing-CLI failures may require setup steps. <br>
Mitigation: Run setup, login, or connection steps only after a command fails with the matching error. <br>


## Reference(s): <br>
- [ClawHub LinkedIn skill page](https://clawhub.ai/oomol/skills/oo-linkedin) <br>
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [LinkedIn homepage](https://www.linkedin.com) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses live connector schemas before constructing action payloads; write and destructive actions require user confirmation.] <br>

## Skill Version(s): <br>
1.0.2 (source: server evidence and frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
