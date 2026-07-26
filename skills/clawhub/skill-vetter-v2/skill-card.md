## Description: <br>
Verification-guided review workflow for inspecting skill packages before use or publication, classifying risk and flagging claims that exceed evidence without performing cryptographic verification, emitting receipts, or proving a skill is safe. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[nutstrut](https://clawhub.ai/user/nutstrut) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, engineers, and agent operators use this skill to inspect skill packages before installation, classify install-time and runtime risks, and produce structured vetting reports. It supports local review first, with optional verification only for the completed report. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The optional OpenClaw hook adds a persistent startup reminder to agent bootstrap. <br>
Mitigation: Enable the hook only when that reminder is desired, and review the hook behavior before installation. <br>
Risk: Optional verification could expose information if users submit more than the final report. <br>
Mitigation: Send only the final structured report and exclude secrets, credentials, personal data, and private repositories. <br>
Risk: The local scan helper reports pattern matches that may be incomplete or context-dependent. <br>
Mitigation: Treat scan output as review evidence, then make the final safety decision through local human or agent review. <br>


## Reference(s): <br>
- [ClawHub Skill Listing](https://clawhub.ai/nutstrut/skills/skill-vetter-v2) <br>
- [Examples](references/examples.md) <br>
- [OpenClaw Integration](references/openclaw-integration.md) <br>
- [Review Checklist](assets/REVIEW-CHECKLIST.md) <br>
- [Vetting Report Template](assets/REPORT-TEMPLATE.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, JSON, shell commands, guidance] <br>
**Output Format:** [Markdown guidance with JSON report structure and optional shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces local vetting reports with capability inventory, risk labels, warnings, recommendations, verdict, and optional verification metadata.] <br>

## Skill Version(s): <br>
0.0.6 (source: server release metadata and artifact _meta.json) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
