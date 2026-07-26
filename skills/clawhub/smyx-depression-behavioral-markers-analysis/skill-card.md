## Description: <br>
Analyzes long-duration bedroom and dining-area camera video to produce behavior-change reports about prolonged immobility, reduced eating activity, baseline comparison, alert level, and recommended follow-up, without presenting a medical diagnosis. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[18072937735](https://clawhub.ai/user/18072937735) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and care-platform operators use this skill to route consenting home-camera video or URLs to cloud analysis and return structured behavioral observation reports for family members or community doctors. It is intended as monitoring support for older adults or people living alone, not as a clinical diagnosis. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Sensitive home-camera footage and identity-linked monitoring data may be sent to external services and associated with locally stored tokens. <br>
Mitigation: Use only with knowing consent from users and monitored individuals; require clear upload and history-query confirmation, documented retention and deletion controls, and transparent account setup. <br>
Risk: Behavioral observations about immobility or appetite change may be mistaken for a depression diagnosis or treatment recommendation. <br>
Mitigation: Present outputs as visual behavior statistics and follow-up prompts only; require family, community doctor, or clinician review for medical interpretation. <br>
Risk: Cloud report-history lookup can expose prior sensitive health-monitoring records. <br>
Mitigation: Restrict history access to the intended account, protect local credentials, and make report-history retrieval an explicit user-visible action. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-depression-behavioral-markers-analysis) <br>
- [API interface reference](artifact/references/api_doc.md) <br>
- [Skill demo](https://lifeemergence.com/sample.html) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, JSON, shell commands, guidance] <br>
**Output Format:** [Markdown text with structured JSON report content and report links] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May write results to a user-specified output file; history queries return cloud report records.] <br>

## Skill Version(s): <br>
1.0.7 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
