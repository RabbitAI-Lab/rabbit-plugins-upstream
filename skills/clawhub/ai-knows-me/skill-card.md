## Description:

通过轻松聊天帮用户生成专属AI文档，让AI智能体认识用户、配合用户，并持续进化。

This skill is ready for commercial/non-commercial use.

## Publisher:

[jeasonhaitao](https://clawhub.ai/user/jeasonhaitao)

### License/Terms of Use:

MIT-0

## Use Case:

External users use this skill to onboard an AI assistant through guided conversation, producing an AI-understands-me booklet and an AI enablement diagnosis with an action plan. Returning users can also use it to refresh the assistant's profile, memory, tool notes, secrets guidance, and behavior rules.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can create local profile, memory, and document files that contain personal information about the user.

Mitigation: Install only when comfortable with local personal-profile files, review generated documents before reuse, and delete them when no longer needed.

Risk: The skill references a plaintext secrets file pattern for sensitive information.

Mitigation: Do not put passwords, tokens, financial identifiers, medical details, or other secrets into SECRET.md or similar markdown files; use a real secret manager instead.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/jeasonhaitao/skills/ai-knows-me)

## Skill Output:

**Output Type(s):** [Text, Markdown, Files, Guidance]

**Output Format:** [Markdown documents and conversational guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces local profile, planning, memory, and behavior-rule documents based on user-provided information.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
