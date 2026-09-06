## Description:

Use Alibaba Cloud ROS Agent through its StartChat API for remote infrastructure conversations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[sdk-team](https://clawhub.ai/user/sdk-team)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and cloud infrastructure engineers use this skill to route explicit Alibaba Cloud ROS Agent requests through StartChat for infrastructure conversations, candidate selection, permission handling, and cancellation. It is intended for ROS Agent workflows, not ordinary local Alibaba Cloud infrastructure operations or unrelated ROS API work.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can initiate high-impact Alibaba Cloud infrastructure workflows through ROS Agent using the selected Alibaba Cloud credentials.

Mitigation: Use least-privilege RAM permissions limited to ros:StartChat for conversations and ros:StopChat only when cancellation is required.

Risk: Optional remote CLI mode depends on externally managed host execution and environment forwarding.

Mitigation: Prefer the default code transport or a tightly administered local policy, and avoid remote CLI mode unless the forwarded environment names and executor behavior are understood.

Risk: Infrastructure proposals or deployment guidance may be incorrect, incomplete, or unsuitable for the target environment.

Mitigation: Review ROS Agent outputs, architecture diagrams, permission prompts, and generated artifacts before approving or executing changes.

## Reference(s):

- [RAM permissions](references/ram-policies.md)
- [Release manifest](references/manifest.json)
- [ClawHub skill page](https://clawhub.ai/sdk-team/skills/alibabacloud-ros-agent)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and bounded JSON bridge results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May surface ROS Agent final text, deployment summaries, Mermaid architecture diagrams, permission prompts, and artifact references; raw bridge identifiers and credentials should not be exposed.]

## Skill Version(s):

0.3.0 (source: server release evidence and references/manifest.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
