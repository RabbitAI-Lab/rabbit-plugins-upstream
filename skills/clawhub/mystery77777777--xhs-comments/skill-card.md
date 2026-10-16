## Description:

Collects public Xiaohongshu note comments step by step, showing results after each paid collection step and allowing CSV export.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mystery77777777](https://clawhub.ai/user/mystery77777777)

### License/Terms of Use:

MIT-0

## Use Case:

Analysts and other users collect public note comments for sentiment monitoring and customer feedback, inspect replies on demand, and export collected comments to CSV.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The default HTTP service address can expose service tokens and collected comments in transit.

Mitigation: Review the configured service address and use a working HTTPS endpoint; avoid the default HTTP address on untrusted networks.

Risk: Collecting each page or expanding replies consumes credits.

Mitigation: Show the estimated scope and cost, and obtain user confirmation before every paid step.

Risk: Existing credentials and insecure settings from an older installation may be imported unexpectedly.

Mitigation: Check the configured service address, token, and insecure setting before use, especially when older credentials exist.

Risk: Exported comments may contain identifiable nicknames and IP locations.

Mitigation: Collect only public comments for authorized purposes and safeguard exported CSV files.

## Reference(s):

- [xhs-comments on ClawHub](https://clawhub.ai/mystery77777777/skills/xhs-comments)

## Skill Output:

**Output Type(s):** [Text, Files, Guidance]

**Output Format:** [JSON results and CSV export, with conversational summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Comment text, nicknames, like counts, IP locations, and reply counts; each collection step requires user confirmation and may consume credits.]

## Skill Version(s):

1.0.1 (source: ClawHub release metadata; bundled files state 2.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
