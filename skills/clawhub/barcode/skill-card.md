## Description:

Looks up product names, brands, specifications, and origin details from a barcode using JisuAPI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jisuapi](https://clawhub.ai/user/jisuapi)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to query product information from EAN8 or EAN13 barcodes and summarize product name, brand, specification, content or weight, and origin details.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Barcode values and the JISU_API_KEY are sent to JisuAPI during lookups.

Mitigation: Use the skill only when third-party sharing with JisuAPI is acceptable, and avoid sensitive private inventory or purchasing contexts unless that sharing has been approved.

Risk: The skill requires a JisuAPI key in the environment.

Mitigation: Store JISU_API_KEY as an environment secret and avoid embedding the key in prompts, command examples, shared logs, or committed files.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/jisuapi/skills/barcode)
- [JisuAPI Barcode2 API Documentation](https://www.jisuapi.com/api/barcode2/)
- [JisuAPI Website](https://www.jisuapi.com/)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, JSON]

**Output Format:** [Markdown guidance with shell commands and JSON command output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires python3 and JISU_API_KEY; barcode lookup requests are sent to JisuAPI.]

## Skill Version(s):

1.0.11 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
