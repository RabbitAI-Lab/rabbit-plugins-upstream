## Description: <br>
Through a fixed camera in a reptile enclosure, the system continuously captures 24-hour video and uses motion-detection techniques to count hourly activity volume, producing circadian activity reports and disruption alerts. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[18072937735](https://clawhub.ai/user/18072937735) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External keepers, reptile facility operators, and developers use this skill to analyze fixed-camera reptile enclosure video, compare observed activity against species circadian baselines, and produce structured rhythm reports with non-diagnostic guidance. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Video files or video URLs are sent to external lifeemergence.com/open.lifeemergence.com services for analysis. <br>
Mitigation: Review the footage before use, avoid sensitive household imagery, and use the skill only when external processing is acceptable. <br>
Risk: The skill can create or reuse an internal identity and local workspace data may retain an identity database with service tokens. <br>
Mitigation: Review local workspace storage and token-handling expectations before installation, especially in shared or regulated environments. <br>
Risk: Circadian analysis can be misleading when observation data is incomplete or environmental context is missing. <br>
Mitigation: Require fixed-camera footage covering at least 24 hours, IR night vision, species rhythm baseline, light schedule, and relevant physiological context before relying on alerts. <br>
Risk: The skill provides animal-welfare guidance but is not a veterinary diagnostic tool. <br>
Mitigation: Treat reports as activity-based screening support and consult a reptile veterinarian when abnormalities persist or health signs accompany rhythm changes. <br>


## Reference(s): <br>
- [API Interface Documentation](artifact/references/api_doc.md) <br>
- [Skill Demo](https://lifeemergence.com/sample.html) <br>
- [ClawHub Skill Page](https://clawhub.ai/18072937735/skills/smyx-reptile-circadian-activity-analysis) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, JSON, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown or JSON analysis report with optional saved file output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Reports include hourly activity arrays, peak activity windows, rhythm consistency scores, alert levels, recommended checks, disclaimers, and report links when available.] <br>

## Skill Version(s): <br>
1.0.8 (source: server release metadata; artifact frontmatter reports 1.0.6) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
