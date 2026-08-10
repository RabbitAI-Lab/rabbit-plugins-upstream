## Description: <br>
Analyzes fixed-camera public-place image or video inputs to produce anonymous group-level emotion distributions, a 0-100 group emotion index, operational suggestions, public-safety advisory signals, and report links. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[18072937735](https://clawhub.ai/user/18072937735) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External operators, developers, and venue analytics teams can use this skill to analyze authorized mall, exhibition, scenic-area, airport, museum, or theme-park footage for anonymous aggregate emotion trends. The outputs support customer-satisfaction monitoring, service-layout optimization, and human-reviewed safety awareness. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Public-camera media and group emotion analysis may involve sensitive public-place data and affected bystanders. <br>
Mitigation: Use only footage the operator is authorized to analyze, post clear public notice, provide a contact path, and retain only aggregate metrics for a limited period. <br>
Risk: The skill sends analysis requests to the publisher's cloud service and can query cloud-hosted historical reports. <br>
Mitigation: Review the publisher, cloud endpoint configuration, data handling terms, and retention controls before using production footage. <br>
Risk: The skill creates or reuses an internal account identity and stores tokens locally. <br>
Mitigation: Run it in an isolated workspace, protect local data directories, rotate or remove tokens when access is no longer needed, and avoid sharing the workspace with untrusted users. <br>
Risk: Emotion-index results can be misleading when samples are small, occluded, low quality, or interpreted as individual emotion judgments. <br>
Mitigation: Treat outputs as aggregate advisory signals, require human review for interventions, enforce minimum sample handling, and do not use results for individual pricing, discrimination, identity tracking, or automated enforcement. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-public-place-group-emotion-index-analysis) <br>
- [Skill demo](https://lifeemergence.com/sample.html) <br>
- [Public place group emotion API documentation](artifact/references/api_doc.md) <br>
- [Analysis API documentation](artifact/skills/smyx_analysis/references/api_doc.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown and JSON structured analysis report] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include group emotion distributions, group emotion index, region breakdowns, recommendations, historical report tables, and report export links.] <br>

## Skill Version(s): <br>
1.0.8 (source: frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
