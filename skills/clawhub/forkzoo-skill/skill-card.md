## Description: <br>
Adopt and manage GitHub-native digital pets that evolve daily with AI. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[levi-law](https://clawhub.ai/user/levi-law) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External users and developers use ForkZoo to adopt GitHub-hosted digital pets, check pet status and evolution history, trigger interactions, and browse community pets. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Adopting a pet uses GitHub repository and workflow authority to create a fork, enable GitHub Actions, trigger workflows, and publish a GitHub Pages site. <br>
Mitigation: Review the upstream ForkZoo repositories and workflow files first, and use the narrowest GitHub token scopes that satisfy the workflow. <br>
Risk: Status and interaction commands make live GitHub API calls using the configured GitHub token. <br>
Mitigation: Run the commands only against intended repositories and rotate or revoke the token if it is no longer needed. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/levi-law/skills/forkzoo-skill) <br>
- [ForkZoo Site](https://forkzoo.com) <br>
- [ForkZoo GitHub Organization](https://github.com/forkZoo) <br>
- [Original ForkMonkey Project](https://github.com/roeiba/forkMonkey) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Shell commands, Configuration guidance] <br>
**Output Format:** [Markdown guidance with bash commands and command-line output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires a GitHub token for adoption, status, and interaction workflows.] <br>

## Skill Version(s): <br>
1.0.0 (source: ClawHub release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
