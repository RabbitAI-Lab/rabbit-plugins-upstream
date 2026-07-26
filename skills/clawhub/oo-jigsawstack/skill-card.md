## Description: <br>
JigsawStack (jigsawstack.com). Use this skill for JigsawStack requests that search, read, summarize, translate, or check text through an OOMOL-connected account. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to operate JigsawStack through the oo CLI for AI web search, search suggestions, summarization, translation, spam checks, and profanity checks. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: User text, queries, or provider-accessible document references may be sent to the JigsawStack connector. <br>
Mitigation: Review payloads before running connector actions and avoid sending secrets or sensitive data unless the user has approved that use. <br>
Risk: First-time oo CLI installation, login, or account connection steps can modify the local environment or require account authorization. <br>
Mitigation: Run setup commands only after a matching failure and get user approval before installation, login, or connection actions. <br>


## Reference(s): <br>
- [JigsawStack homepage](https://jigsawstack.com) <br>
- [oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [oo CLI install guide](https://cli.oomol.com/install-guide.md) <br>
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-jigsawstack) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, JSON, Guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and JSON connector responses] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Connector responses include data and meta.executionId when actions are run with --json.] <br>

## Skill Version(s): <br>
1.0.1 (source: ClawHub release metadata and SKILL.md metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
