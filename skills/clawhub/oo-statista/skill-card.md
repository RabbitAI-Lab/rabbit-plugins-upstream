## Description: <br>
Statista enables agents to search Statista data and retrieve statistics through an OOMOL-connected Statista account. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to search Statista statistics, Consumer Insights, and Market Insights, then retrieve chart data and metadata for Statista statistic identifiers. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Statista searches or statistic identifiers may be sent through the OOMOL/Statista connector. <br>
Mitigation: Review the requested query or identifier before execution and avoid sending sensitive or unnecessary information. <br>
Risk: First-time setup can require installing the oo CLI or starting an account login flow. <br>
Mitigation: Run installer or login commands only when the corresponding command failure occurs and after reviewing the setup step. <br>
Risk: Future Statista connector actions could add write or destructive behavior. <br>
Mitigation: Confirm the exact payload and expected effect with the user before running any action tagged write or destructive. <br>


## Reference(s): <br>
- [Statista homepage](https://www.statista.com) <br>
- [oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [oo CLI install guide](https://cli.oomol.com/install-guide.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell command examples and JSON connector payloads or responses.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses live connector schemas before constructing payloads; listed actions are read-only, while future write or destructive actions require user confirmation.] <br>

## Skill Version(s): <br>
1.0.0 (source: evidence.release.version and artifact metadata.version) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
