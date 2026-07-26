## Description: <br>
This skill helps an agent analyze consented enterprise office video or image inputs for anonymized employee emotion-fluctuation indicators, produce HR care-oriented reports, and query historical cloud reports. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
HR and authorized enterprise administrators use this skill to generate anonymized workplace emotion fluctuation reports and supportive care suggestions from fixed-camera office footage. The skill is intended for consented, access-controlled internal HR review and historical report lookup, not for diagnosis, performance evaluation, promotion, or termination decisions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Sensitive workplace emotion monitoring and cloud report access can affect employee privacy and workplace rights. <br>
Mitigation: Use only with legal and compliance approval, explicit employee notice, opt-out support, allowlisted enterprise camera sources, documented retention terms, and access limited to authorized HR administrators. <br>
Risk: The skill may create or reuse a persistent account identity and send identity-linked video or report requests to external services without a clear runtime consent gate. <br>
Mitigation: Require administrator-controlled authentication, document cloud processing and retention, and verify who can list or export historical reports before installation. <br>
Risk: Emotion fluctuation outputs could be misused as medical diagnoses or employment-decision evidence. <br>
Mitigation: Treat outputs as supportive HR care signals only; prohibit use for diagnosis, performance evaluation, promotion, or termination decisions. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-employee-emotion-fluctuation-hr-analysis) <br>
- [Publisher profile](https://clawhub.ai/user/smyx-sunjinhui) <br>
- [API interface documentation](references/api_doc.md) <br>
- [Skill demo](https://lifeemergence.com/sample.html) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, JSON, shell commands, configuration] <br>
**Output Format:** [Markdown report text with structured JSON analysis data, HR care suggestions, historical report listings, and report links.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May produce optional output files when requested; report queries and analysis are backed by cloud API calls.] <br>

## Skill Version(s): <br>
1.0.3 (source: server release metadata; artifact frontmatter reports 1.0.7) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
