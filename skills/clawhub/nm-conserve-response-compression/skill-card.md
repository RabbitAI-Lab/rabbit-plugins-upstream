## Description:

Compresses verbose responses by removing filler and framing to save 200-400 tokens.

This skill is ready for commercial/non-commercial use.

## Publisher:

[athola](https://clawhub.ai/user/athola)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use this skill to make assistant responses shorter and more direct while preserving useful technical context and safety warnings.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Shortening responses can remove important uncertainty, caveats, or safety context.

Mitigation: Preserve factual uncertainty markers, critical warnings, and caveats for debugging, medical, legal, financial, safety-sensitive, or uncertain topics.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/athola/skills/nm-conserve-response-compression)
- [OpenClaw homepage metadata](https://github.com/athola/claude-night-market/tree/master/plugins/conserve)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Concise Markdown or plain text guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Optimized to reduce response length by removing filler, decorative framing, and unnecessary closings while preserving critical warnings.]

## Skill Version(s):

1.9.19 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
