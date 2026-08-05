## Description: <br>
Analyzes fixed-camera video of an elderly person's water-cup area to count cup pickup events, estimate drinking-frequency patterns, and produce directional dehydration-risk reminders for caregivers. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[18072937735](https://clawhub.ai/user/18072937735) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External caregivers, family members, elder-care operators, and developers use this skill to analyze living-room or kitchen camera video for water-cup pickup frequency, long no-drink intervals, and report history. It provides behavioral statistics and reminders, not medical diagnosis. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Sensitive in-home footage or video URLs may be sent to the LifeEmergence cloud service for analysis. <br>
Mitigation: Use only footage you own or are authorized to process, obtain explicit consent from the monitored person or guardian, and prefer minimal, stable camera views focused on the cup area. <br>
Risk: The skill may create or reuse persistent backend identity records for report access and history queries. <br>
Mitigation: Review local and backend identity/token handling before deployment, avoid exposing identifiers in user-facing output, and separate report access by user or care setting. <br>
Risk: Cup pickup count is an indirect proxy for drinking and may be inaccurate when cups are empty, shared, moved by another person, or outside the fixed camera view. <br>
Mitigation: Treat results as directional caregiver reminders, combine them with personal baselines and human follow-up, and avoid using the output as a medical diagnosis. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/18072937735/skills/smyx-elderly-drinking-frequency-analysis) <br>
- [Publisher Profile](https://clawhub.ai/user/18072937735) <br>
- [Skill Demo](https://lifeemergence.com/sample.html) <br>
- [API Interface Documentation](references/api_doc.md) <br>
- [SMYX Analysis API Documentation](skills/smyx_analysis/references/api_doc.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown text with structured JSON report content, analysis status messages, history-report tables, and report links.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May write the returned report text to a local output file when invoked with --output; cloud APIs return JSON used to build the report.] <br>

## Skill Version(s): <br>
1.0.6 (source: server release evidence; artifact frontmatter reports 1.0.8) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
