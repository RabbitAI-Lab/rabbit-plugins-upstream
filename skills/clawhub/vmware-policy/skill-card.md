## Description:

Unified audit logging, policy enforcement, and input sanitization for the entire VMware MCP skill family.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT

## Use Case:

VMware administrators and skill developers use this library to query cross-skill audit activity, configure optional deny rules and maintenance windows, and add auditing and input sanitization around VMware MCP tool calls.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup requires installing a package, and security checks could not resolve several local references.

Mitigation: Review the setup and referenced local files before installation, and confirm the documented local audit and policy files fit your environment.

## Reference(s):

- [Project documentation](https://github.com/vmware-skills/VMware-Policy)
- [ClawHub skill page](https://clawhub.ai/zw008/skills/vmware-policy)

## Skill Output:

**Output Type(s):** [Text, JSON, Configuration]

**Output Format:** [CLI audit tables or JSON exports, with YAML policy rules and Python integration guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Audit records can include tool parameters and results; configured sensitive fields are redacted. Audit writes are best-effort.]

## Skill Version(s):

1.24.4 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
