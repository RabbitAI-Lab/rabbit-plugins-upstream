## Description:

Helps sellers turn selected Douyin hot-search topics and their own still images into short talking hook clips.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Sellers use this skill to plan hooks from selected Douyin trends and create one short talking video per supplied still, with separate approval for paid generation steps.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Authorization grants a shared full-scope Beatra device token with broad media and task access.

Mitigation: Connect only if comfortable granting that scope; keep the token private and disconnect when access is no longer needed.

Risk: Paid trend lookup, voice, speech, and video operations can spend account credits.

Mitigation: Review the live quoted credit cost and requested work, then approve each paid step separately.

Risk: The bundled client can silently update local code by default.

Mitigation: Disable automatic updates before use if unapproved code changes are unacceptable.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/beatra-ai/skills/douyin-hot-to-hook-clip)
- [Douyin hot-search hook workflow](artifact/references/workflow.md)
- [Automatic updates and safety](artifact/references/automatic-updates-and-safety.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown plan and status reports with links to generated clips]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports selected topics, clip results, and actual credits charged; does not post or stitch clips.]

## Skill Version(s):

0.1.8 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
