## Description:

Answers stock research questions with compact, sourced market views and provides contracts and guidance for a local chat-and-canvas terminal when requested.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thesentitrader](https://clawhub.ai/user/thesentitrader)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use the skill to review dated market data and research signals, compare stocks, screen activity, and build a local chat-and-canvas terminal on request.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Market observations may be delayed, incomplete, or have unknown observation times.

Mitigation: Keep source dates visible and label data age as unavailable when no observation time is supplied.

Risk: Research queries go to SentiSense, and optional model-assisted app turns use the provider chosen by the user.

Mitigation: Use a dedicated API key through the host environment and keep broad aliases within financial conversations.

Risk: API quotas and rate limits can constrain the available research coverage.

Mitigation: Track request usage, honor rate limits, and avoid repeated retries when a request is limited.

## Reference(s):

- [SentiSense API reference](https://sentisense.ai/skill.md)
- [Get a SentiSense API key](https://app.sentisense.ai/get-api-key)
- [Commands and data](artifact/references/commands-and-data.md)
- [Build in an afternoon](artifact/references/build-in-an-afternoon.md)
- [Canvas grammar](artifact/references/canvas-grammar.md)
- [Runtime and stream](artifact/references/runtime-and-stream.md)
- [Blocks and rendering](artifact/references/blocks-and-rendering.md)
- [Verification guide](artifact/references/verification.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Configuration, XML, Guidance]

**Output Format:** [Compact sourced text or Markdown; requested builds may include application code, configuration, and XML canvas documents.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Research views include source dates and visible data gaps; app or artifact creation occurs only when requested.]

## Skill Version(s):

2.1.3 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
