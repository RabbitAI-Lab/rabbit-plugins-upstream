## Description:

Converts an explicitly named Simplified Chinese article into a Traditional Chinese twin and keeps the pair synchronized.

This skill is ready for commercial/non-commercial use.

## Publisher:

[j3ffyang](https://clawhub.ai/user/j3ffyang)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and editors use this skill to create or update the Traditional Chinese twin of an explicitly named Simplified Chinese article. The Simplified article remains the source of truth.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill runs a local conversion script with file and shell capabilities, and scanner analysis could not resolve several referenced paths.

Mitigation: Review the source and generated twin, and confirm the host runtime's file and shell restrictions are acceptable before use.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/j3ffyang/skills/simplified-to-traditional)

## Skill Output:

**Output Type(s):** [Markdown, Files]

**Output Format:** [Traditional Chinese Markdown article and matching cross-links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [One explicitly named article pair; the zh-hans article remains the source of truth.]

## Skill Version(s):

1.0.10 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
