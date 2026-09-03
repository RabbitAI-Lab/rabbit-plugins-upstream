## Description:

Uses Alibaba Cloud ROS Agent through its StartChat API for remote infrastructure conversations, including normal and Pipeline workflows, user questions, candidate selection, permission responses, and explicit StopChat cancellation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[sdk-team](https://clawhub.ai/user/sdk-team)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and cloud infrastructure engineers use this skill to run Alibaba Cloud ROS Agent conversations for remote ROS and IaC tasks while preserving session state, progress updates, user questions, candidate selection, permission decisions, and cancellation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill communicates with Alibaba Cloud ROS Agent using the operator's Alibaba Cloud credential context.

Mitigation: Install only for intended ROS Agent use and apply a least-privilege RAM policy limited to ros:StartChat plus ros:StopChat when cancellation is needed.

Risk: Local runtime setup can involve Python dependencies or an Alibaba Cloud ROS CLI plugin.

Mitigation: Review any local CLI plugin installation before allowing it and keep the pinned Python dependency set updated.

Risk: Infrastructure workflows may request permissions or deployment confirmation before making changes.

Mitigation: Require user-visible summaries, diagrams where applicable, and explicit permission or candidate-selection responses before continuing.

## Reference(s):

- [RAM permissions](references/ram-policies.md)
- [ClawHub skill page](https://clawhub.ai/sdk-team/skills/alibabacloud-ros-agent)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown text with code blocks, Mermaid diagrams when deployment confirmation is needed, and bounded bridge JSON for agent tool handling.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May surface ROS Agent final text, deployment summaries, permission prompts, progress updates, and generated infrastructure artifacts.]

## Skill Version(s):

0.2.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
