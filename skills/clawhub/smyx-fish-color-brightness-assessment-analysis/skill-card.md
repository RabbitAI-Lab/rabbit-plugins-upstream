## Description: <br>
Assesses ornamental fish image or video inputs for color brightness by extracting calibrated HSV color signals, comparing species-specific baselines, and returning vibrancy scores, trends, alerts, and reports. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, developers, and aquarium operators use this skill to analyze ornamental fish side images or videos, estimate body color vibrancy against species-specific baselines, and review current or historical assessment reports. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Media may be sent to a configured cloud service for analysis. <br>
Mitigation: Use only media that the user is authorized to process, avoid sensitive local paths, and confirm cloud processing is acceptable before deployment. <br>
Risk: The skill can create or reuse local user identities and session tokens, and can query cloud history. <br>
Mitigation: Review the workspace data directory before and after use, avoid shared workspaces for sensitive sessions, and delete local data if persistent account linkage is not desired. <br>
Risk: Poor calibration, missing white reference, low segmentation confidence, or missing species baseline can make color scores unreliable. <br>
Mitigation: Require side-view high-resolution inputs with a white or gray reference, treat unreliable signals as non-scored results, and keep recommendations non-diagnostic. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-fish-color-brightness-assessment-analysis) <br>
- [API Documentation](references/api_doc.md) <br>
- [Skill Demo](https://lifeemergence.com/sample.html) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, JSON, shell commands, guidance] <br>
**Output Format:** [Structured text, Markdown tables, and JSON report content] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs may include HSV color metrics, species baseline comparisons, vibrancy scores, trends, alert levels, recommended actions, report links, and historical report listings.] <br>

## Skill Version(s): <br>
1.0.5 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
