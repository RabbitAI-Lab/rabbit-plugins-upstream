## Description: <br>
Analyzes litter-box area video or media URLs to estimate each cat's entry and exit events, daily usage frequency, visit duration, and behavior-based urinary-health alerts without providing a medical diagnosis. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Pet owners, catteries, boarding centers, and veterinary care teams can use this skill to analyze litter-box camera footage, summarize usage frequency and visit duration, and flag behavior changes that may warrant follow-up. The skill is intended for monitoring and triage support, not medical diagnosis. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill sends litter-box footage or media URLs to the LifeEmergence cloud service for analysis. <br>
Mitigation: Use only media that is appropriate to share with that service, and review organizational privacy requirements before installation or use. <br>
Risk: The security evidence reports silent local identity reuse or creation and locally stored service tokens. <br>
Mitigation: Install only in an isolated workspace where identity files, local databases, and tokens can be managed, rotated, and removed when no longer needed. <br>
Risk: Behavior-based urinary-health alerts may be mistaken for clinical diagnosis. <br>
Mitigation: Present alerts as monitoring signals and route concerning results to a qualified veterinarian for diagnosis and treatment decisions. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-litter-box-usage-monitor-analysis) <br>
- [Skill Demo](https://lifeemergence.com/sample.html) <br>
- [API Documentation](references/api_doc.md) <br>
- [Analysis API Documentation](skills/smyx_analysis/references/api_doc.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, JSON, shell commands, guidance] <br>
**Output Format:** [Markdown or JSON report content with report links and optional saved output file] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include structured monitoring results, frequency and duration summaries, alerts, recommendations, and cloud report links.] <br>

## Skill Version(s): <br>
1.0.5 (source: server release metadata; artifact frontmatter reports 1.0.7) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
