## Description: <br>
PromptLayer lets agents search and read PromptLayer prompt templates, logged requests, tables, sheets, and rows through the OOMOL oo CLI connector. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to retrieve PromptLayer prompt templates, inspect logged requests, and list PromptLayer table data from an authenticated workspace without calling the PromptLayer API directly. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill connects to a PromptLayer workspace through OOMOL's connector. <br>
Mitigation: Install only after confirming trust in OOMOL and comfort with connecting the target PromptLayer workspace through its connector. <br>
Risk: Future connector schemas could introduce write or destructive actions not present in this release. <br>
Mitigation: Review the live connector schema before execution and confirm any write or destructive action with the user before running it. <br>


## Reference(s): <br>
- [PromptLayer skill page](https://clawhub.ai/oomol/skills/oo-promptlayer) <br>
- [OOMOL publisher profile](https://clawhub.ai/user/oomol) <br>
- [PromptLayer homepage](https://promptlayer.com/) <br>
- [oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [oo CLI install guide](https://cli.oomol.com/install-guide.md) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, JSON, Guidance] <br>
**Output Format:** [Markdown with inline shell commands and JSON connector responses] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Read-only PromptLayer get and list actions; payloads are expected to match the live connector schema.] <br>

## Skill Version(s): <br>
1.0.0 (source: release evidence and skill metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
