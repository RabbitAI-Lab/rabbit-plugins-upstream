## Description:

Diagnoses suspected Alibaba Cloud Security Center cryptomining incidents by running a read-only six-step investigation for alerts, IOCs, affected assets, attack surface, risk, and remediation reporting.

This skill is ready for commercial/non-commercial use.

## Publisher:

[sdk-team](https://clawhub.ai/user/sdk-team)

### License/Terms of Use:

MIT-0

## Use Case:

Cloud security operators and incident responders use this skill to investigate suspected cryptomining activity in Alibaba Cloud Security Center, extract IOCs, scope affected assets, assess likely entry vectors, and produce prioritized remediation guidance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can automatically use local Alibaba Cloud credentials for broad account security reads.

Mitigation: Install and run it only with a dedicated read-only RAM role matching the documented permissions, and avoid broad default profiles.

Risk: A clean mining result may still read one unrelated alert detail for workflow completeness.

Mitigation: Run the skill only in the intended account, region, and profile, and treat non-mining alert details as investigation context rather than a mining finding.

Risk: Confirmed mining reports require operational containment, but the skill itself is read-only and does not isolate hosts or kill processes.

Mitigation: Route the report to the responsible incident-response workflow and perform containment, eradication, hardening, and verification through approved operations tools.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/sdk-team/skills/alibabacloud-mining-attack-diagnosis)
- [Detection Flow](references/detection_flow.md)
- [Mining Indicators Reference](references/mining_indicators.md)
- [Module 1: Mining Alert Detection](references/module1_alert_detection.md)
- [Module 2: Alert Detail & IOC Extraction](references/module2_alert_detail_ioc.md)
- [Module 3: Affected Asset Scope](references/module3_affected_assets.md)
- [Module 4: Attack Surface Detection](references/module4_attack_surface.md)
- [Module 5: Remediation Best Practices](references/module5_remediation_best_practices.md)
- [Module 6: Corroboration](references/module6_corroboration.md)
- [Module 7: Deep Entry-Vector Scan](references/module7_deep_scan.md)
- [RAM Policies](references/ram-policies.md)
- [Alibaba Cloud CLI documentation](https://help.aliyun.com/document_detail/121541.html)

## Skill Output:

**Output Type(s):** [text, markdown, json, shell commands, guidance]

**Output Format:** [Markdown or JSON incident report]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes masked account-scoped identifiers, preserved IOCs, API warning logs on errors, and prioritized manual remediation guidance.]

## Skill Version(s):

0.0.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
