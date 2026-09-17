## Description:

Helps agents operate Alibaba Cloud ACK through OOMOL's oo CLI by inspecting connector schemas and running ACK connector actions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to inspect Alibaba Cloud ACK connector schemas, run ACK connector actions, and generate short-lived kubeconfig files through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can generate temporary ACK kubeconfig material that may grant access to Kubernetes clusters.

Mitigation: Use it only for expected ACK administration tasks, confirm the target cluster and requested action, and handle generated kubeconfig output as sensitive temporary credential material.

Risk: The setup guidance includes remote installer commands.

Mitigation: Install the oo CLI through a verified installation path and review installer contents before execution instead of blindly piping remote scripts to a shell.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-aliyun-ack)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [Alibaba Cloud ACK homepage](https://www.alibabacloud.com/product/kubernetes)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance, JSON]

**Output Format:** [Markdown with inline shell commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce short-lived ACK kubeconfig material through connector output when requested.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
