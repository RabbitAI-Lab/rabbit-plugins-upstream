## Description: <br>
Analyzes driver videos to identify unsafe driving behaviors and produce structured safety reports. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Drivers, fleet reviewers, safety trainers, or agents acting for them use this skill to submit driving videos or URLs for unsafe-behavior analysis and retrieve structured reports or report history. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Driver videos, faces, license plates, location clues, report history, and account identifiers may be sent to a remote lifeemergence.com service. <br>
Mitigation: Use only with explicit consent, avoid confidential or unnecessary footage, and install only when the remote service is trusted for this data. <br>
Risk: The skill may create or reuse a local identity and store service tokens in the workspace data directory. <br>
Mitigation: Run it in a trusted workspace, protect the data directory, and remove or rotate stored tokens when the skill is no longer needed. <br>
Risk: Historical report lookup can expose prior analysis records associated with the resolved account identity. <br>
Mitigation: Limit history queries to authorized users and review returned reports before sharing them. <br>
Risk: Driving-safety analysis output is educational guidance and may be incomplete or inaccurate for operational decisions. <br>
Mitigation: Treat results as supplemental safety review material and validate important findings with qualified reviewers or established safety processes. <br>


## Reference(s): <br>
- [API documentation](references/api_doc.md) <br>
- [Analysis API error codes](skills/smyx_analysis/references/api_doc.md) <br>
- [Skill demo](https://lifeemergence.com/sample.html) <br>
- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-drive-analysis) <br>
- [Publisher profile](https://clawhub.ai/user/smyx-sunjinhui) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, JSON, shell commands, guidance] <br>
**Output Format:** [Markdown text with embedded JSON or structured analysis content; optional output file when requested.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Can include report links returned by the remote service; supports basic, standard, and json detail modes.] <br>

## Skill Version(s): <br>
1.0.7 (source: server release metadata; artifact frontmatter says 1.0.11) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
