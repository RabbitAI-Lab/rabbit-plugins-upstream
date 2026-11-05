## Description:

Bridges Xiaomi XiaoAI speakers with an OpenClaw assistant by filtering speech transcripts, forwarding selected requests, and playing replies through text-to-speech.

This skill is ready for commercial/non-commercial use.

## Publisher:

[warm-winter](https://clawhub.ai/user/warm-winter)

### License/Terms of Use:

MIT-0

## Use Case:

Developers using OpenClaw with Xiaomi XiaoAI speakers can forward selected spoken requests to an assistant and play its replies through the speaker. The skill supports trigger filtering, duplicate suppression, and optional transcript-based forwarding decisions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: On Windows, cached account credentials may be accessible beyond the intended user because ACL access cannot be verified by the skill.

Mitigation: Independently restrict access to both credential configuration and cached sessions, and use a dedicated unprivileged account.

Risk: When JEV_API_KEY is configured, new speech transcripts are sent to Jev for forwarding decisions.

Mitigation: Leave JEV_API_KEY unset unless transcript sharing is acceptable; removing it returns routing to trigger-word filtering.

Risk: A downstream assistant may interpret forwarded speech as a consequential request.

Mitigation: Require separate confirmation before irreversible or otherwise consequential actions.

## Reference(s):

- [XiaoAI Bridge on ClawHub](https://clawhub.ai/warm-winter/skills/xiaoai-bridge)
- [MiGPT-Next API reference (bundled)](artifact/references/migpt-api.md)
- [TokenRhythm Jev service](https://tokenrhythm.studio)

## Skill Output:

**Output Type(s):** [JSON, Text, Audio]

**Output Format:** [JSON Lines containing selected speech transcripts, with replies played as text-to-speech audio]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Optional Jev routing sends speech transcripts for forwarding decisions when configured.]

## Skill Version(s):

1.3.1 (source: frontmatter, CHANGELOG, package.json, release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
