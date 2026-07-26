## Description: <br>
DocsBot AI lets an agent search and read DocsBot AI data through the OOMOL docsbot_ai connector instead of calling the API directly. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and other agent users use this skill to list DocsBot teams and bots, inspect team or bot details, run semantic searches, and fetch reconstructed document text from DocsBot AI through an OOMOL-connected account. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: DocsBot searches and document fetches may expose DocsBot content to the agent. <br>
Mitigation: Install and use the skill only for accounts and tasks where the agent is allowed to access the connected DocsBot content. <br>
Risk: First-time setup may require installing or signing in to the oo CLI before DocsBot actions can run. <br>
Mitigation: Complete setup only after an auth or connection failure, and avoid repeating one-time login or connection steps during normal use. <br>


## Reference(s): <br>
- [DocsBot AI homepage](https://docsbot.ai) <br>
- [oo CLI](https://github.com/oomol-lab/oo-cli) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs are read-oriented DocsBot AI results returned through the oo CLI as JSON.] <br>

## Skill Version(s): <br>
1.0.1 (source: frontmatter and release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
