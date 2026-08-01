## Description: <br>
Uses pet face images or videos to identify a pet, query linked vaccination records, compare the most recent vaccination date against the reminder cycle, and return due or overdue vaccination reminders without providing medical advice. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External pet hospital, boarding center, and insurance workflows use this skill to check whether a recognized pet's vaccination record is due or overdue. It returns database-comparison reminders and report links, not veterinary medical advice. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Pet images or videos, vaccination and report records, and account identifiers are sent to external LifeEmergence/SMYX services. <br>
Mitigation: Use the skill only when that backend is trusted, verify data retention and authorization controls, and avoid submitting sensitive or unapproved media. <br>
Risk: The skill silently creates or reuses identity state and caches tokens. <br>
Mitigation: Prefer a dedicated workspace or account, review local identity and token state before deployment, and avoid environments where silent account creation or token caching is unacceptable. <br>
Risk: Report and media requests rely on external services with limited user control. <br>
Mitigation: Review before installing, restrict use to approved workflows, and confirm that outbound service access is allowed in the deployment environment. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-vaccination-reminder-analysis) <br>
- [API documentation](references/api_doc.md) <br>
- [Analysis API documentation](skills/smyx_analysis/references/api_doc.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, JSON, shell commands] <br>
**Output Format:** [Structured text or JSON with optional Markdown report links] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include a vaccination reminder status, structured analysis content, historical report records, and exported report links.] <br>

## Skill Version(s): <br>
1.0.5 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
