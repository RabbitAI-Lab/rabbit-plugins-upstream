## Description: <br>
Connects AI agents to real FHIR servers through an MCP guardrail proxy that applies redaction, audit logging, step-up authorization, tenant isolation, disclaimers, and URL rewriting. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[aks129](https://clawhub.ai/user/aks129) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and healthcare platform teams use this skill to configure guarded proxy access from AI agents to HAPI FHIR, SMART Health IT, Epic sandbox, local HAPI, or authorized production EHR systems while preserving redaction, audit, step-up approval, and URL shielding controls. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill concerns access to sensitive healthcare systems and clinical records. <br>
Mitigation: Install only with authorization for the target FHIR server, use sandbox endpoints by default, and apply least-privilege credentials. <br>
Risk: Write operations could create, update, or delete clinical records if enabled against an upstream server. <br>
Mitigation: Require human approval before operations that modify clinical records, and keep audit trails enabled for both local and upstream activity. <br>
Risk: The proxy does not provide caching, cross-version translation, SMART-on-FHIR auth forwarding, or upstream tenant isolation. <br>
Mitigation: Confirm those controls are handled by the deployment environment or upstream server before production use. <br>


## Reference(s): <br>
- [HAPI FHIR R4](https://hapi.fhir.org/baseR4) <br>
- [SMART Health IT R4](https://r4.smarthealthit.org) <br>
- [HAPI FHIR R5](https://hapi.fhir.org/baseR5) <br>
- [Epic FHIR Sandbox](https://open.epic.com/Interface/FHIR) <br>
- [ClawHub Skill Page](https://clawhub.ai/aks129/skills/fhir-upstream-proxy) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Configuration] <br>
**Output Format:** [Markdown with inline bash code blocks and environment variable tables] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Non-executable guidance for configuring upstream FHIR proxy mode, including environment variables, supported upstream servers, limitations, and security posture.] <br>

## Skill Version(s): <br>
1.6.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
