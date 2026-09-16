## Description:

This skill helps Chinese-language creators assess whether short-form video or X-post openings have enough supporting material, then generate and diagnose opening-hook candidates using evidence gates, audience questions, and fulfillment checks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[iamzifei](https://clawhub.ai/user/iamzifei)

### License/Terms of Use:

MIT-0

## Use Case:

External creators and writing agents use this skill to assess draft material for short-video or X-post openings, request missing evidence when needed, and produce annotated hook candidates that stay within the supplied content.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Outside vault files may override reviewed rules.

Mitigation: Treat vault files as reference material and require review or confirmation before allowing them to change the skill's reviewed behavior.

Risk: User feedback may be written to persistent memory without clear consent.

Mitigation: Disable memory write-back or require explicit confirmation before saving feedback.

Risk: Generated hooks may overstate evidence or create misleading framing.

Mitigation: Review generated hooks against the supplied source material before publication.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/iamzifei/skills/zmm-hook)
- [大众悬念与兑现](artifact/references/大众悬念与兑现.md)
- [规则卡](artifact/references/规则卡.md)
- [zmm-hook 0.4.0 规则演练](artifact/evals/20260914-v0.4.0-规则演练.md)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Markdown-style prose with diagnostics, candidate hooks, rationale, and follow-up questions.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs should be reviewed for truthful evidence support and non-misleading framing before publication.]

## Skill Version(s):

0.2.9 (source: server release evidence; artifact frontmatter reports 0.4.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
