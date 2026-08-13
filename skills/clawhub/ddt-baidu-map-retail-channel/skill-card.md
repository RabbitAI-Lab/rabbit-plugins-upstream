## Description:

Analyzes retail-channel structure, city coverage, competitor differences, and market opportunities from Baidu Maps address text using DDT's published store snapshots, and is not an official Baidu Maps product.

This skill is ready for commercial/non-commercial use.

## Publisher:

[horacetu](https://clawhub.ai/user/horacetu)

### License/Terms of Use:

MIT-0

## Use Case:

External retail, market, and channel analysts use this skill to evaluate published retail brand footprints, formats, city coverage, competitive differences, and candidate-site context from brand names, address text, coordinates, or public store IDs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends user-provided retail brand names, address text, coordinates, or public store IDs to the configured DDT API endpoint.

Mitigation: Install only if the publisher is trusted and users are comfortable sharing the intended retail-location inputs with that endpoint.

Risk: A DDT API key could be exposed if pasted into chats, logs, files, or version control.

Mitigation: Keep DDT_API_KEY in the local or controlled execution environment and never include the real key in prompts, logs, skill files, or repositories.

Risk: Incomplete coverage, truncated previews, unknown brands, or failed API responses could lead to unsupported retail conclusions.

Mitigation: Check ok status, coverage fields, data version, and preview.truncated before producing business conclusions; report unavailable coverage and avoid treating missing values as zero.

Risk: Using the skill outside its retail scope could produce irrelevant guidance.

Mitigation: Stop on restaurant, automotive aftermarket, hardware, or building-materials requests and route users to the corresponding industry skill.

## Reference(s):

- [DDT ClawHub API Homepage](https://gotoshop-ai.com/ddtclaw/)
- [ClawHub Skill Page](https://clawhub.ai/horacetu/skills/ddt-baidu-map-retail-channel)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown text with concise retail-analysis sections and occasional shell command snippets.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs should report conclusions, 3-6 key metrics, coverage and data version, requested limited store details, and uncovered items without exposing API keys, internal IDs, supplier fields, or unsupported missing values.]

## Skill Version(s):

1.0.0 (source: SKILL.md frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
