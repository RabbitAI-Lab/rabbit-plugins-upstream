## Description: <br>
Analyzes pet carrier videos or video URLs through configured APIs to estimate resting respiratory rate, compare it with a >40 bpm alert threshold, and return a non-diagnostic monitoring report for transport risk awareness. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[18072937735](https://clawhub.ai/user/18072937735) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to analyze videos of pets in airline carriers or cargo transport, producing respiratory-rate monitoring results, threshold alerts, and report links without making a disease diagnosis. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Pet videos may be uploaded to configured cloud services for analysis. <br>
Mitigation: Use only media that the user is willing to send to the configured lifeemergence.com services, and avoid submitting sensitive or unnecessary footage. <br>
Risk: The skill can silently reuse or create account-linked identity records and query cloud history. <br>
Mitigation: Review whether account-linked history lookup is acceptable before installation, and avoid invoking history-list workflows when identity reuse is not desired. <br>
Risk: Authentication tokens may be stored locally. <br>
Mitigation: Inspect and delete the workspace data database and smyx-api-key.txt after use if persistent local credentials are not acceptable. <br>


## Reference(s): <br>
- [Pet carrier respiratory rate API documentation](references/api_doc.md) <br>
- [Skill usage demo](https://lifeemergence.com/sample.html) <br>
- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-pet-carrier-respiratory-rate-analysis) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, json, shell commands, guidance] <br>
**Output Format:** [Markdown and JSON analysis reports with optional report links and command-line status text] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs may include respiratory-rate estimates, threshold alerts, non-diagnostic guidance, history tables, and links to generated reports.] <br>

## Skill Version(s): <br>
1.0.6 (source: server release metadata; artifact frontmatter lists 1.0.7) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
