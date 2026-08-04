## Description: <br>
Bind and verify a public custom domain for an existing Volcengine TOS bucket, including DNS, certificate, and direct TOS custom-domain checks. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[tenshowinnovation](https://clawhub.ai/user/tenshowinnovation) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and cloud operators use this skill to diagnose and configure direct custom-domain access for Volcengine TOS buckets, including DNS CNAMEs, DV certificate validation, TOS domain binding, and HTTPS verification. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can propose DNS, certificate, and bucket-binding changes that affect public storage-domain availability. <br>
Mitigation: Review proposed DNS, certificate, and bucket-binding changes before approval, and use least-privilege Volcengine credentials where possible. <br>
Risk: Cloud credentials, private keys, and one-off validation secrets could be exposed if copied into shared output. <br>
Mitigation: Do not print or persist AK/SK values, private keys, certificate private keys, or one-off validation secrets in user-facing docs. <br>


## Reference(s): <br>
- [TOS Custom Storage Domain Runbook](references/tos-custom-domain-runbook.md) <br>
- [ClawHub skill page](https://clawhub.ai/tenshowinnovation/skills/volc-tos-storage-domain) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, code, configuration] <br>
**Output Format:** [Markdown with inline bash, JavaScript, JSON, and text examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces cloud-operation guidance that should be reviewed before applying DNS, certificate, or bucket-binding changes.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release metadata and skill metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
