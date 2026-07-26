## Description: <br>
Skio (skio.com). Use this skill for ANY Skio request - searching and reading data. Whenever a task involves Skio, use this skill instead of calling the API directly. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and agents use this skill to read and export Skio orders, products, storefront users, and subscriptions through an OOMOL-connected account. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may require installing or using the oo CLI before Skio data can be read. <br>
Mitigation: Review the CLI installation step before running it and only perform setup when a command fails because the CLI, authentication, or Skio connection is missing. <br>
Risk: Future Skio connector actions labeled write or destructive could change or remove business data. <br>
Mitigation: Require explicit user confirmation of the target, payload, and effect before running any write or destructive action. <br>
Risk: The skill reads Skio business data through an OOMOL-connected account. <br>
Mitigation: Install and use it only when the user intends the agent to access Skio data through that connected account. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-skio) <br>
- [OOMOL publisher profile](https://clawhub.ai/user/oomol) <br>
- [oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [oo CLI install guide](https://cli.oomol.com/install-guide.md) <br>
- [Skio homepage](https://skio.com) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses live connector schemas before execution and returns Skio connector responses as JSON when actions are run.] <br>

## Skill Version(s): <br>
1.0.1 (source: server evidence and frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
