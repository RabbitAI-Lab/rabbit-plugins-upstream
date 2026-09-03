## Description:

cmclaw connects an agent to YouCloud Creative Manager to analyze advertising creatives and return strategy reports or brainstorming output.

This skill is ready for commercial/non-commercial use.

## Publisher:

[youcloud](https://clawhub.ai/user/youcloud)

### License/Terms of Use:

MIT-0

## Use Case:

External users with paid YouCloud Creative Manager access use this skill to send ad strategy or creative analysis prompts to YouCloud and receive a complete markdown report or brainstorming response.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Ad strategy prompts, material-scope references, and account-linked user or team identifiers are sent to YouCloud and may appear in the web app conversation list.

Mitigation: Install only for intended YouCloud Creative Manager workflows and avoid submitting data that should not be processed by that service.

Risk: A broad YOUCLOUD_API_KEY or untrusted DAM_API_BASE could expose requests to the wrong account or host.

Mitigation: Scope YOUCLOUD_API_KEY to the intended account and keep DAM_API_BASE unset or pointed only at a trusted YouCloud endpoint.

Risk: The skill relies on long-running streamed responses and can produce incomplete output if interrupted early.

Mitigation: Wait for the stream to complete or return an error before treating the markdown response as final.

## Reference(s):

- [DamClaw Skill API](references/cm-claw-api.md)
- [YouCloud Creative Manager API base](https://console.dam.youcloud.com)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Markdown report or conversational analysis text with a conversation detail link.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Single complete response after the YouCloud stream ends; session_id may be retained for follow-up.]

## Skill Version(s):

1.0.1 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
