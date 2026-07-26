## Description: <br>
Surveys connected health data sources and reports connection status, last activity, and record counts by type without exposing clinical values. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[aks129](https://clawhub.ai/user/aks129) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Patients or care-support agents use this skill to check which health data services are linked, whether records are available, and what next action to take without exposing record contents. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Source connection status, last activity, and record counts can reveal sensitive health information. <br>
Mitigation: Install only where HealthClaw/FHIR tools and STEP_UP_SECRET are trusted, and share outputs only in authorized patient workflows. <br>
Risk: Users may overread record counts as clinical detail or assume unavailable source connections exist. <br>
Mitigation: Report only values returned by sources_check; use audited record-search tools for clinical contents and state clearly when a source is not connected. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/aks129/skills/check-sources) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, API calls, guidance] <br>
**Output Format:** [Markdown or plain text summary of connected sources and record counts.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Protected tenants require step-up authorization; outputs source names, connection status, last activity, and counts only.] <br>

## Skill Version(s): <br>
1.6.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
