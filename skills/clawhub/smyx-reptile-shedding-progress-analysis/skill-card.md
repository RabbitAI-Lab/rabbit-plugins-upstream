## Description: <br>
Analyzes reptile enclosure images or videos to classify shedding phase, identify stuck-shed risk signals, and return care-oriented recommendations and report links. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[18072937735](https://clawhub.ai/user/18072937735) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External reptile keepers, breeders, and developers use this skill to submit reptile images, videos, or media URLs for shedding-stage analysis, stuck-shed risk screening, and history/report review. It is intended to support care decisions, not to provide veterinary diagnosis or prescribe treatment. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Reptile images, videos, or media URLs are sent to a third-party cloud service and report history is queried from that service. <br>
Mitigation: Use only media appropriate for third-party processing, avoid private household details, and confirm the cloud retention model is acceptable before installation. <br>
Risk: The skill creates or reuses an internal identity and stores service tokens in the workspace data directory. <br>
Mitigation: Run in a workspace where local token storage is acceptable and remove stored credentials when the skill is no longer needed. <br>
Risk: Outputs can influence reptile care decisions but are not veterinary diagnoses. <br>
Mitigation: Treat the analysis as care guidance and consult a reptile veterinarian for persistent stuck shed, eye-cap issues, injury, infection concerns, or other serious symptoms. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-reptile-shedding-progress-analysis) <br>
- [API documentation](references/api_doc.md) <br>
- [Skill demo](https://lifeemergence.com/sample.html) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown and JSON-like structured analysis text with report links and optional saved output files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May upload local media or submit media URLs to a third-party cloud API, poll for analysis results, and query cloud report history.] <br>

## Skill Version(s): <br>
1.0.5 (source: server release metadata; artifact SKILL.md frontmatter reports 1.0.6) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
