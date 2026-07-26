## Description: <br>
Fasten Connect guides agents through connecting patient-authorized EHR and TEFCA health records into HealthClaw Guardrails, covering widget setup, connection registration, export tracking, ingestion status, and post-import Curatr quality scans. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[aks129](https://clawhub.ai/user/aks129) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and healthcare integration engineers use this skill to connect patient-authorized EHR or TEFCA records through Fasten Connect into HealthClaw Guardrails and monitor ingestion and quality-scan workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Fasten private keys, webhook secrets, and healthcare credentials can expose sensitive access if copied into client code, logs, or insecure storage. <br>
Mitigation: Store private keys and webhook secrets in a real secrets manager, keep private credentials server-side, and review examples before adapting them to production. <br>
Risk: The workflow handles patient health information and webhook events that may include PHI. <br>
Mitigation: Use only authorized test or patient data, avoid logging raw webhook payloads, and apply the documented PHI redaction, audit, authorization, and tenant-isolation guardrails. <br>
Risk: TEFCA live mode can introduce additional fees and production identity-verification behavior. <br>
Mitigation: Test with synthetic patients first, confirm patient consent and cost implications, and keep test credentials out of production workflows. <br>


## Reference(s): <br>
- [Fasten Connect documentation](https://docs.connect.fastenhealth.com) <br>
- [Fasten Developer Portal](https://app.connect.fastenhealth.com) <br>
- [Fasten webhook debugging simulator](https://docs.connect.fastenhealth.com/guides/webhook-debugging-simulator.md) <br>
- [ClawHub skill page](https://clawhub.ai/aks129/skills/fasten-connect) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with HTML, JavaScript, bash, and API request examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes environment-variable names, API endpoints, webhook events, ingestion lifecycle states, and operational cautions.] <br>

## Skill Version(s): <br>
1.6.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
