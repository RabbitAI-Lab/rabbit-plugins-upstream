## Description:

Guides developers in designing agent-native applications where agents act as the primary users.

This skill is ready for commercial/non-commercial use.

## Publisher:

[iliaal](https://clawhub.ai/user/iliaal)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and architects use this skill to design or review agent-native applications, including tool interfaces, agent execution loops, shared workspaces, and approval patterns.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Autonomous changes or external actions can occur without appropriate approval.

Mitigation: Require explicit approval before self-modification, commits, pushes, deployments, public posting, or prompt changes.

Risk: Unrestricted file access or exposed secrets in agent workflows.

Mitigation: Canonicalize and sandbox file access, and protect credentials and other secrets.

Risk: Synced, published, or cloud-processed content can expose private data.

Mitigation: Review privacy implications before enabling synchronization, publication, or cloud processing.

Risk: Architecture examples may be mistaken for production-ready security controls.

Mitigation: Treat examples as guidance and review security controls before deployment.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/iliaal/skills/compound-eng-agent-native-architecture)
- [Architecture review checklist](artifact/references/architecture-review-checklist.md)
- [Core principles](artifact/references/core-principles.md)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Code, Configuration instructions]

**Output Format:** [Markdown design guidance, checklists, and illustrative examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Recommendations depend on the application's requirements and must be reviewed before implementation.]

## Skill Version(s):

5.0.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
