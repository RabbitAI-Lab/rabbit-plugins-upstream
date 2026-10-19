## Description:

Advertised for Kubernetes rollout diagnosis, this skill currently provides mostly Makefile review guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[hmahmadcs](https://clawhub.ai/user/hmahmadcs)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and cluster operators may consult the skill when investigating stuck rollouts or restarting pods, but its current instructions mainly review Makefiles rather than diagnose Kubernetes workloads.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may be invoked for Kubernetes incidents but lead users through unrelated Makefile review.

Mitigation: Review its guidance before use and rely on appropriate Kubernetes diagnostics for rollout incidents.

Risk: Cluster commands may run with Kubernetes credentials.

Mitigation: Require explicit confirmation before any kubectl command and prefer read-only diagnostics.

## Reference(s):

- [Kubernetes documentation](https://kubernetes.io/docs/)
- [ClawHub skill release](https://clawhub.ai/hmahmadcs/skills/kubernetes-rollout-doctor)

## Skill Output:

**Output Type(s):** [Guidance, Code, Shell commands]

**Output Format:** [Markdown with Makefile and shell snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Suggestions may include Makefile revisions and optional kubectl commands.]

## Skill Version(s):

1.0.2 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
