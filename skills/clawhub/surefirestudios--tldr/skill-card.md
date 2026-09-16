## Description:

Compress output without losing it: lead with a three-line TL;DR, keep the full detail directly underneath, and compress agent-to-agent reports to a parseable block.

This skill is ready for commercial/non-commercial use.

## Publisher:

[surefirestudios](https://clawhub.ai/user/surefirestudios)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, operators, and agent users use this skill to make assistant responses easier to scan by placing a concise TL;DR first while preserving full detail below. It also standardizes agent-to-agent handoffs into a compact parseable block.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A summary-first response could mislead readers if important caveats are compressed too aggressively.

Mitigation: The skill requires full detail to remain below the TL;DR and names categories that must stay visible, including destructive actions, security findings, data loss, money and quota, legal, medical, and safety boundaries.

Risk: The session-wide style can remain active after the initial request.

Mitigation: Users can turn the behavior off with "stop tldr", "tldr off", "normal mode", or "/tldr full".

Risk: The Gemini adapter references an external context file path.

Mitigation: Check the adapter's context_file path before relying on the Gemini configuration.

## Reference(s):

- [tldr reference](reference.md)
- [GitHub homepage](https://github.com/SurefireStudios/tldr)
- [ClawHub skill page](https://clawhub.ai/surefirestudios/skills/tldr)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Markdown or plain text with a leading TL;DR and full detail below]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May use a parseable tldr code block for agent-to-agent reports.]

## Skill Version(s):

0.3.0 (source: release metadata and agents/openai.yaml)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
