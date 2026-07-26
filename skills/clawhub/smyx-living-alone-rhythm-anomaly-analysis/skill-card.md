## Description: <br>
Analyzes indoor night video from a fixed camera to detect lights-off timing and early-morning movement, compare them against a 7-14 day personal baseline, and produce a sleep-rhythm anomaly reminder for a person living alone. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[18072937735](https://clawhub.ai/user/18072937735) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External caregivers, family members, community workers, and developers use this skill to analyze consented night video for deviations from an individual sleep-rhythm baseline. It supports structured reports and follow-up reminders, not medical diagnosis. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill processes highly sensitive indoor night video through cloud services. <br>
Mitigation: Use only with explicit consent from the monitored person or authorized guardian, confirm where video is sent, and avoid submitting footage unless the cloud processing path is acceptable. <br>
Risk: Historical reports and export links may expose sensitive health, behavior, or home-environment information. <br>
Mitigation: Limit access to report links, define retention expectations before deployment, and periodically remove reports that are no longer needed. <br>
Risk: The skill silently creates or reuses local identity and token state. <br>
Mitigation: Review how the local identity/token database is stored, clear it between users or environments, and restrict filesystem access for shared machines. <br>
Risk: Sleep-rhythm anomaly output can be mistaken for a medical conclusion. <br>
Mitigation: Present results as visual activity and baseline-deviation signals only, and route concerning patterns to family, community staff, or clinicians for human follow-up. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-living-alone-rhythm-anomaly-analysis) <br>
- [API documentation](references/api_doc.md) <br>
- [SMYX analysis API documentation](skills/smyx_analysis/references/api_doc.md) <br>
- [Skill demo](https://lifeemergence.com/sample.html) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown or JSON-like structured analysis text with optional report links and saved output files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Can query historical report lists and can write the returned analysis text to a user-specified output path.] <br>

## Skill Version(s): <br>
1.0.4 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
