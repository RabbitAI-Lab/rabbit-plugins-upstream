## Description: <br>
Analyzes fixed-camera public-place images or videos to produce anonymized group emotion distributions, a 0-100 group emotion index, operational suggestions, safety-warning guidance, and report links. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[18072937735](https://clawhub.ai/user/18072937735) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External operators and developers use this skill to analyze public-place camera footage for group-level emotion trends in malls, exhibition halls, scenic areas, museums, airports, and similar venues. It supports operational planning and human-reviewed safety awareness, not individual identification or automated action against people. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Public-place images or videos may be sent to external services for analysis. <br>
Mitigation: Use only footage you are authorized to process, provide clear public notice, and confirm retention rules before deployment. <br>
Risk: The skill can create or reuse persistent local or remote identity and token state linked to report history. <br>
Mitigation: Review account, token, and local storage behavior before installation and limit access to users who should see cloud-stored report history. <br>
Risk: Group emotion scores can be misused for individual decisions, automated interventions, discriminatory service, or differential pricing. <br>
Mitigation: Use only anonymous aggregate results, keep safety outputs human-reviewed, and do not use the score to identify, track, price, or treat individuals differently. <br>
Risk: Low face visibility, short time windows, or small samples can make the group emotion index unreliable. <br>
Mitigation: Follow the documented minimum-sample rule, do not publish an index when fewer than five faces are detected, and label camera or sampling limitations in reports. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/18072937735/skills/smyx-public-place-group-emotion-index-analysis) <br>
- [API Documentation](artifact/references/api_doc.md) <br>
- [Skill Demo](https://lifeemergence.com/sample.html) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown or JSON structured analysis report with report links] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May write results to a requested file; history queries return cloud report records.] <br>

## Skill Version(s): <br>
1.0.6 (source: server release metadata; artifact frontmatter says 1.0.5) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
