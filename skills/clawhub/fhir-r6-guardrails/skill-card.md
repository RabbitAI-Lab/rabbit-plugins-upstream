## Description: <br>
HealthClaw Guardrails provides FHIR agent guardrails for clinical data access through MCP, including PHI redaction, audit trails, step-up authorization, tenant isolation, and support for stable FHIR R4 US Core v9 plus experimental FHIR R6 ballot3. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[aks129](https://clawhub.ai/user/aks129) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and healthcare AI teams use this skill to place a runtime guardrail layer between agents and FHIR data for controlled reads, searches, writes, statistics, access-control evaluation, and audit logging. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Upstream FHIR proxy mode can forward sensitive health query details to an external server. <br>
Mitigation: Use only trusted upstream FHIR servers, treat query parameters as potentially sensitive health data, and avoid real patient data unless privacy, consent, and contractual requirements are satisfied. <br>


## Reference(s): <br>
- [HealthClaw](https://healthclaw.io) <br>
- [ClawHub Skill Page](https://clawhub.ai/aks129/skills/fhir-r6-guardrails) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Configuration] <br>
**Output Format:** [Markdown with MCP tool names, tables, and bash code blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes setup variables, supported operations, write-confirmation flow, security guardrails, and known limitations.] <br>

## Skill Version(s): <br>
1.6.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
