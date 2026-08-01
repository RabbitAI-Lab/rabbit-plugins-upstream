## Description: <br>
This skill analyzes fixed-camera public-place image or video inputs to produce anonymized group-level facial-expression statistics, a 0-100 group emotion index, operational suggestions, safety warnings, and report links. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[18072937735](https://clawhub.ai/user/18072937735) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Operators and developers use this skill to analyze public-place camera footage from malls, exhibition halls, scenic areas, airports, museums, and theme parks. It returns group emotion distributions, region-level emotion indices, operational recommendations, safety-warning context, and historical report lookups for management review. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The security evidence says the skill sends video or video URLs to a remote service. <br>
Mitigation: Use only with legal authority, operator approval, posted public notice, and approved handling rules for camera footage and report data. <br>
Risk: The security evidence says reports are linked to an internally managed user identity and local database state may be created. <br>
Mitigation: Review local state before deployment, restrict access to report history, and define a deletion process for credentials, identities, and reports. <br>
Risk: The security evidence says backend tokens may be stored. <br>
Mitigation: Install only in controlled environments, rotate credentials as needed, and remove stored tokens when the skill is no longer in use. <br>
Risk: The skill supports public-place emotion analysis from camera footage, which can affect privacy and safety decisions. <br>
Mitigation: Use results as group-level decision support only, avoid individual decisions or automated intervention, and require human review for safety responses. <br>


## Reference(s): <br>
- [Skill API Documentation](references/api_doc.md) <br>
- [Skill Demo](https://lifeemergence.com/sample.html) <br>
- [ClawHub Skill Page](https://clawhub.ai/18072937735/skills/smyx-public-place-group-emotion-index-analysis) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, JSON, shell commands, guidance] <br>
**Output Format:** [Markdown or JSON analysis report with report links and optional saved output file] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs may include group emotion distributions, a 0-100 emotion index, region breakdowns, heatmap links, operational suggestions, safety suggestions, and historical report tables.] <br>

## Skill Version(s): <br>
1.0.7 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
