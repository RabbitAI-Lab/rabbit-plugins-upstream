## Description: <br>
Detects delivery packages in surveillance images or videos for inventory checks, package-count review, and unattended alerts at community stations, residential entrances, and office lobbies. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[18072937735](https://clawhub.ai/user/18072937735) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and operations teams use this skill to analyze surveillance images, videos, or media URLs for package presence, counts, locations, overdue pickup alerts, structured reports, and cloud report history. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Uploaded surveillance media, media URLs, user or tenant identifiers, and generated account tokens may be sent to and stored by the provider's cloud service. <br>
Mitigation: Use only with explicit consent for the media and identifiers involved, and confirm retention, access, and deletion terms with the publisher before deployment. <br>
Risk: The skill silently creates or reuses an internal user identity and stores returned tokens with limited user-facing control. <br>
Mitigation: Run in a controlled workspace, review local data and token storage before and after use, and prefer a release with explicit identity and token-handling controls. <br>
Risk: The skill contacts configured remote service endpoints for analysis and historical report lookup. <br>
Mitigation: Allowlist expected provider endpoints and avoid running the skill in environments where outbound media or report metadata transfer is not permitted. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-package-detection-analysis) <br>
- [Skill demo](https://lifeemergence.com/sample.html) <br>
- [Package detection API documentation](references/api_doc.md) <br>
- [Analysis API error-code documentation](skills/smyx_analysis/references/api_doc.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown or JSON-formatted structured analysis reports, with optional saved output files.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs may include package-detection results, report links, historical report lists, and user-facing status or error messages.] <br>

## Skill Version(s): <br>
1.0.10 (source: ClawHub release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
