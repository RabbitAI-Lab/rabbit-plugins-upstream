## Description: <br>
Evaluates agent actions for security risks, enforcing least-privilege policies with allow, deny, or confirmation decisions and secret redaction. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[bharathjanumpally](https://clawhub.ai/user/bharathjanumpally) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and agent builders use this skill to evaluate proposed HTTP, file, and command actions before execution so policies can allow, deny, request confirmation, redact secrets, and emit audit records. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Users may treat the evaluator as a complete security boundary instead of a policy decision helper. <br>
Mitigation: Use it as one layer in a broader control plane, configure policy.yaml for the deployment environment, and fail closed on evaluator errors or unexpected action types. <br>
Risk: Unsafe downstream execution can bypass the evaluator's redaction and deny decisions. <br>
Mitigation: Execute only sanitizedAction after an ALLOW decision and stop on DENY or unresolved NEED_CONFIRMATION decisions. <br>
Risk: Outdated dependencies or policy defaults can reduce coverage over time. <br>
Mitigation: Keep dependencies patched and review deny domains, file jail settings, command patterns, and secret redaction rules before deployment. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/bharathjanumpally/skills/claw-permission-firewall) <br>
- [README](artifact/README.md) <br>
- [Default policy](artifact/policy.yaml) <br>


## Skill Output: <br>
**Output Type(s):** [JSON, Guidance, Configuration] <br>
**Output Format:** [JSON decision object with reasons, sanitizedAction, confirmation details when needed, and audit metadata] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [CLI exits with 1 on DENY and 0 on ALLOW or NEED_CONFIRMATION.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata, package.json, CHANGELOG) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
