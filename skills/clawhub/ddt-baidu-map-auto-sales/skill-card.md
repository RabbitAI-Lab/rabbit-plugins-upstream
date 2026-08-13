## Description:

Uses Baidu Maps address text to help automotive aftermarket field sales teams screen target stores, prioritize visits, assess nearby competitors, and ground conclusions in published DDT store snapshots.

This skill is ready for commercial/non-commercial use.

## Publisher:

[horacetu](https://clawhub.ai/user/horacetu)

### License/Terms of Use:

MIT-0

## Use Case:

External automotive aftermarket sales teams use this skill to turn copied map addresses, brands, coordinates, or public store IDs into store targeting, visit-priority, coverage, and competitive-context analysis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Automotive store queries, pasted map addresses, and coordinates may be sent to the DDT/gotoshop-ai.com service.

Mitigation: Use the skill only when that data sharing is acceptable under the user's organization policies; avoid submitting sensitive or unnecessary location details.

Risk: The DDT_API_KEY could be exposed if pasted into chats, logs, repositories, or shared outputs.

Mitigation: Store the key only in the local or controlled runtime environment and omit it from prompts, logs, generated files, and examples.

Risk: Returned store previews, coverage fields, or unavailable metrics could be misread as complete market coverage.

Mitigation: Report truncation, coverage gaps, and unavailable fields explicitly, and avoid filling missing API response values with assumptions.

## Reference(s):

- [DDT ClawHub API homepage](https://gotoshop-ai.com/ddtclaw/)
- [ClawHub skill page](https://clawhub.ai/horacetu/skills/ddt-baidu-map-auto-sales)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown responses with concise analysis, key metrics, coverage notes, limited store previews, and optional bash API examples.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses bounded previews for nearby-store and site-screening results; does not expose API keys, storage IDs, supplier fields, or unsupported metrics.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
