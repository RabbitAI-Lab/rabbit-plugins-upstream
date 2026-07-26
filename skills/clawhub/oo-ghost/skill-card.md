## Description: <br>
Ghost lets an agent operate a connected Ghost site through OOMOL's oo CLI connector, with documented actions for reading settings, authors, tags, posts, and pages. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, content operators, and agent users use this skill to retrieve public Ghost site settings and content through an authenticated OOMOL connection. The skill guides agents to inspect live connector schemas before running Ghost connector actions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Optional oo CLI installation guidance uses pipe-to-shell commands. <br>
Mitigation: Review the oo CLI installation method before running installer commands. <br>
Risk: Ghost connector actions may change or delete content when write or destructive actions are available. <br>
Mitigation: Require explicit confirmation of the target, payload, and expected effect before any action that changes or deletes Ghost content. <br>


## Reference(s): <br>
- [Ghost homepage](https://ghost.org) <br>
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [oo CLI install guide](https://cli.oomol.com/install-guide.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Connector actions return JSON responses from the oo CLI.] <br>

## Skill Version(s): <br>
1.0.0 (source: release evidence and skill metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
