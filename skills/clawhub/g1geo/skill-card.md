## Description: <br>
g1geo helps agents use the official @g1geo/cli to monitor brand visibility in AI search, generate GEO content, manage reports, and submit publishing tasks across supported media platforms. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[mzoob](https://clawhub.ai/user/mzoob) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Marketing, content, and SEO/GEO teams use this skill through an agent to run g1geo CLI workflows for AI-search visibility analysis, content generation, report export, and multi-platform publishing. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can cause an agent to install or update a global npm CLI and then run authenticated account-level workflows. <br>
Mitigation: Require manual approval for global npm installation, authentication, and commands that publish, export, or submit tasks; review the exact CLI command before execution. <br>
Risk: Authenticated CLI use may view account-visible products and submit content publishing tasks. <br>
Mitigation: Use least-privileged accounts and product contexts, specify team and device context when publishing, and confirm content and destinations before submission. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/mzoob/skills/g1geo) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and CLI output summaries] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include account, product, report, export, and publishing task status when returned by the CLI.] <br>

## Skill Version(s): <br>
1.1.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
