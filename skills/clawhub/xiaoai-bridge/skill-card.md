## Description:

Bridges Xiaomi XiaoAI speaker voice messages to an AI assistant, filtering and deduplicating commands while supporting background listening and text-to-speech replies.

This skill is ready for commercial/non-commercial use.

## Publisher:

[warm-winter](https://clawhub.ai/user/warm-winter)

### License/Terms of Use:

MIT No Attribution

## Use Case:

Developers and smart-home users use the bridge to route Xiaomi XiaoAI voice commands to an AI assistant and receive spoken responses.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Session-cache protections can fail silently, potentially exposing Xiaomi account credentials to another local user.

Mitigation: Use a dedicated non-admin Xiaomi account and a verified private, user-owned XIAOAI_STATE_DIR outside shared temporary storage; protect transcript logs, confirm consequential voice-triggered actions, and treat passToken like a password. Deleting the cache does not revoke exposed credentials.

## Reference(s):

- [Xiaoai Bridge on ClawHub](https://clawhub.ai/warm-winter/skills/xiaoai-bridge)
- [MiGPT-Next API reference](references/migpt-api.md)
- [MiGPT-Next project](https://github.com/idootop/migpt-next)
- [passToken guidance](https://github.com/idootop/migpt-next/issues/4)

## Skill Output:

**Output Type(s):** [JSON, Text]

**Output Format:** [JSON Lines voice-message events and text for text-to-speech playback]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Voice transcripts may contain sensitive personal data.]

## Skill Version(s):

1.1.1 (source: SKILL.md, CHANGELOG.md)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
