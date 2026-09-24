## Description:

Reviews Kubernetes manifests and cluster exports for common configuration issues, including resource limits, probes, selector mismatches, image settings, network policies, and RBAC permissions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thcjp](https://clawhub.ai/user/thcjp)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and platform engineers use this skill to review Kubernetes YAML manifests or kubectl exports before deployment, during troubleshooting, or as part of security and configuration audits.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may request broad command execution or Kubernetes cluster-context access without clear limits.

Mitigation: Use it only with explicit scope, such as named manifests or read-only kubectl inspection for a specific context and namespace.

Risk: Suggested fixes or scripts could affect live cluster behavior if applied without review.

Mitigation: Review generated findings and remediation steps before applying changes to production resources.

Risk: The artifact mentions API key configuration without documenting a specific external service or token scope.

Mitigation: Do not provide API keys unless the publisher documents the exact service, required permissions, and storage expectations.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/thcjp/skills/k8s)
- [Kubernetes kubectl installation docs](https://kubernetes.io/docs/tasks/tools/)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with JSON examples, YAML snippets, and inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include prioritized findings, compliance scores, remediation suggestions, and kubectl inspection commands.]

## Skill Version(s):

1.0.0 (source: server release metadata; SKILL.md frontmatter says 1.0.1)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
