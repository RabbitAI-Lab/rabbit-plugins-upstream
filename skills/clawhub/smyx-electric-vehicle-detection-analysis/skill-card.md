## Description: <br>
Detects electric motorcycles and e-bikes in restricted areas from images or video streams, counts suspected parking or driving violations, and returns alerts and management recommendations. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[18072937735](https://clawhub.ai/user/18072937735) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Security, facilities, and operations teams use this skill to analyze surveillance images, uploaded video, or media URLs for suspected e-bike violations in parks, communities, campuses, parking areas, roads, and other restricted zones. Developers and agents can also use it to retrieve prior detection reports and present structured summaries for human review. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill sends images, videos, or media URLs to a remote service for cloud processing. <br>
Mitigation: Use only with media approved for the service operator and confirm retention, jurisdiction, and account-boundary requirements before deployment. <br>
Risk: The skill silently creates or reuses a remote identity and stores session tokens in the workspace data directory. <br>
Mitigation: Run it in an isolated workspace, restrict access to local data files, and remove or rotate stored tokens after use when policy requires it. <br>
Risk: Detection outputs may be incorrect or incomplete for safety and enforcement decisions. <br>
Mitigation: Treat reports as decision-support material and require human review before taking action on alleged violations. <br>


## Reference(s): <br>
- [Electric Vehicle Detection API Documentation](artifact/references/api_doc.md) <br>
- [SMYX Analysis API Documentation](artifact/skills/smyx_analysis/references/api_doc.md) <br>
- [Skill Demo](https://lifeemergence.com/sample.html) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, JSON, Files] <br>
**Output Format:** [Markdown-formatted text or JSON detection reports, with optional saved output file] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Reports may include vehicle counts, suspected violation levels, warnings, management suggestions, export links, or historical report lists.] <br>

## Skill Version(s): <br>
9.9.11 (source: ClawHub release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
