## Description:

Exports JD.com product reviews from a logged-in Chrome session into local Markdown tables, with deduplication, partial-result handling, and JSON status metadata.

This skill is ready for commercial/non-commercial use.

## Publisher:

[fatmind](https://clawhub.ai/user/fatmind)

### License/Terms of Use:

MIT-0

## Use Case:

External users, ecommerce analysts, and product researchers use this skill to collect JD.com buyer reviews for local review analysis, product selection, and quality monitoring. It is intended for runs where the user supplies a JD.com product URL and has an authorized logged-in Chrome session available.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill operates through a logged-in Chrome session and may handle JD account context, browser identifiers, and page text.

Mitigation: Use only with trusted local Chrome Relay and local LLM services, avoid sensitive account contexts, and minimize or redact cookie and page text before broad use.

Risk: The security evidence reports unsafe output-file path handling.

Mitigation: Use simple output basenames and a trusted local output directory, preferably a temporary directory, until path handling is constrained or validated.

Risk: The security evidence flags an obfuscated LLM helper and recommends review before installation.

Mitigation: Review the helper before deployment and replace it with readable code that uses a fixed or allowlisted local endpoint.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/fatmind/skills/jd-review-export)

## Skill Output:

**Output Type(s):** [markdown, json, text]

**Output Format:** [Local Markdown tables, compact JSON metadata, and one-line JSON stdout]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Markdown output may be marked partial when fewer reviews are collected than requested; collection count is controlled by the input count parameter.]

## Skill Version(s):

1.0.3 (source: server release evidence and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
