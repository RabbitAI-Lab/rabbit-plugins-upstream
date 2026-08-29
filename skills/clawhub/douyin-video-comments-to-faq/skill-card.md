## Description:

Turns Douyin video comments into one FAQ still per selected seller-answered question.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External sellers and commerce operators use this skill to turn public Douyin comment questions and confirmed product facts into 4 to 8 listing FAQ stills. It can also guide paid Douyin comment lookup, image generation, image transformation, and local corrections through Beatra.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can use a shared Beatra device connection with wallet-spending authority for paid comment lookup and image generation.

Mitigation: Install only when that spending authority is acceptable; require the skill's separate six-field confirmation before each paid lookup, generate, transform, or edit stage.

Risk: The shared Beatra credential has broad account scope relative to the narrower FAQ-image workflow.

Mitigation: Keep the token only in the local Beatra credential store, never expose it in chat or command arguments, and revoke the device from the Beatra Console when access is no longer wanted.

Risk: Automatic updates are enabled by default and can change package files without a separate per-update approval.

Mitigation: Disable silent update checks with `python3 scripts/mcp_client.py update --auto off` when release control is required.

Risk: Generated FAQ stills could misstate product claims or render small text unclearly.

Mitigation: Use only seller-confirmed facts, do not invent comments or answers, and review each returned still for visible wording before treating it as usable listing content.

## Reference(s):

- [Douyin comment FAQ workflow](artifact/references/workflow.md)
- [Douyin comment lookup](artifact/references/comment-lookup.md)
- [Tasks and results](artifact/references/tasks-and-results.md)
- [Billing, errors, and recovery](artifact/references/billing-errors-and-recovery.md)
- [Installation and authentication](artifact/references/installation-and-auth.md)
- [MCP connection](artifact/references/mcp-connection.md)
- [Automatic updates and safety](artifact/references/automatic-updates-and-safety.md)
- [ClawHub skill page](https://clawhub.ai/beatra-ai/skills/douyin-video-comments-to-faq)
- [Beatra skill homepage](https://beatra.ai/skills/douyin-video-comments-to-faq)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance, image files]

**Output Format:** [Markdown slot lists and production cards, inline JSON tool arguments, shell command snippets, and Beatra-returned image artifacts.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The default workflow plans 4 to 8 FAQ stills, uses one paid request per lookup or image slot after confirmation, and reports returned task status, artifact metadata, and net charged credits.]

## Skill Version(s):

0.1.1 (source: server release evidence and artifact manifest)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
