## Description: <br>
Fetches Python dependency candidates for supported programming questions and helps an agent choose a package from a fixed candidate list. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[37722135-droid](https://clawhub.ai/user/37722135-droid) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and coding agents use this skill to retrieve plausible Python package candidates for tabular data programming questions and to select one package based on visible candidate fields. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The fixed candidate dataset can omit packages or fail unsupported queries. <br>
Mitigation: Use the result as candidate guidance and verify the final dependency choice against the user's actual project requirements. <br>
Risk: The security guidance advises confirming that the published skill instructions match the advertised purpose before installation. <br>
Mitigation: Review the skill instructions and included scripts before deployment, especially when updating the release artifact. <br>


## Reference(s): <br>


## Skill Output: <br>
**Output Type(s):** [text, code, guidance] <br>
**Output Format:** [JSON object containing a selected package name, import statement, and brief reason, or a JSON candidate payload from the local fetcher script.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Returns candidates from a local fixed dataset for recognized queries; unsupported queries and invalid top_k values raise errors.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
