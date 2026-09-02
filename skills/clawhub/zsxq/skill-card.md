## Description:

Guides agents using zsxq-cli to manage ZSXQ communities, content, members, notes, scheduled tasks, and Skill Pay payment flows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zsxq](https://clawhub.ai/user/zsxq)

### License/Terms of Use:

MIT-0

## Use Case:

External users and community operators use this skill to operate ZSXQ groups through zsxq-cli, including content publishing, moderation workflows, member review, reporting, media generation, and payment-related flows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can perform sensitive account, member, payment, and public-content actions.

Mitigation: Install only when agent access to the ZSXQ account is intended, use the least privileged account available, and confirm every write, delete, payment, or public publishing action before execution.

Risk: Member and profile data may be exposed through broad exports, reports, or shared logs.

Mitigation: Limit member exports to the task at hand and redact profile, member, and account data from logs or shared outputs.

Risk: The mandatory trigger scope is broad and may activate for many ZSXQ-related requests.

Mitigation: Review the agent's intended action path before state-changing operations and prefer read-only discovery until the user confirms the target resource and operation.

Risk: Notes and generated content can become public or externally shareable.

Mitigation: Avoid placing private, sensitive, or credential-like data in notes, posts, generated posters, videos, or share links.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zsxq/skills/zsxq)
- [SKILL.md](artifact/SKILL.md)
- [Authentication and error handling](artifact/references/auth-errors.md)
- [Group operations](artifact/references/group-list.md)
- [Topic creation](artifact/references/topic-create.md)
- [Topic editing](artifact/references/topic-edit.md)
- [Member review](artifact/references/group-members.md)
- [Skill Pay and WeChat order creation](artifact/references/wechat-order-create.md)
- [Daily patrol scenario](artifact/references/scenarios/daily-patrol.md)
- [Risk monitoring scenario](artifact/references/scenarios/monitor-risky-content.md)
- [Operations report scenario](artifact/references/scenarios/compose-operations-report.md)
- [Video generation scenario](artifact/references/scenarios/generate-video.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and structured operational steps]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May direct agents to call zsxq-cli and to create local media artifacts such as PNG posters or MP4 videos when the relevant scenario is used.]

## Skill Version(s):

2.2.0 (source: artifact frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
