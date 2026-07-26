## Description: <br>
Faraday helps agents read Faraday account, dataset, scope, target, trait, and usage information through an OOMOL-connected account. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill when a task needs read-only Faraday account data retrieval through the OOMOL oo CLI, including listing or retrieving accounts, datasets, scopes, targets, traits, and usage statistics. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can read Faraday account, dataset, scope, target, trait, and usage information through the user's connected account. <br>
Mitigation: Install and use it only when the agent should access that Faraday information, and review requested account or object identifiers before execution. <br>
Risk: First-time setup may require installing or authenticating the oo CLI. <br>
Mitigation: Review the oo CLI installer before running it, and only run setup steps after a command fails with the matching installation, authentication, or connection error. <br>
Risk: Future connector versions could add write or destructive Faraday actions. <br>
Mitigation: Require explicit user confirmation for any action tagged write or destructive before executing it. <br>


## Reference(s): <br>
- [Faraday homepage](https://faraday.ai) <br>
- [oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [ClawHub Faraday skill](https://clawhub.ai/oomol/skills/oo-faraday) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, JSON, Guidance] <br>
**Output Format:** [Markdown with inline bash commands and JSON payloads] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses live connector schema inspection before building action payloads.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and SKILL.md metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
