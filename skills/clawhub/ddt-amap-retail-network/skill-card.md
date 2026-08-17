## Description:

Analyzes published retail brand store snapshots for store scale, category structure, regional coverage, surroundings, comparisons, and candidate-site context using DDT retail APIs and optional Amap-copied address text.

This skill is ready for commercial/non-commercial use.

## Publisher:

[horacetu](https://clawhub.ai/user/horacetu)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to ask retail network questions about published brands, including store footprint, regional concentration, retail category mix, surrounding area signals, brand comparisons, and candidate-site screening. It is intended to keep conclusions tied to current DDT API responses and published data snapshots.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The DDT API service receives brand names and any user-provided coordinates or public store IDs needed for retail analysis.

Mitigation: Confirm that use of the DDT API service is acceptable for the workflow, and send only the inputs required for the requested analysis.

Risk: The skill requires an API key for live calls.

Mitigation: Store DDT_API_KEY in the local or controlled runtime environment, and do not paste real keys into chats, files, logs, or version control.

Risk: Retail conclusions can be incomplete when a brand is unpublished, API coverage is insufficient, or preview results are truncated.

Mitigation: Stop unsupported conclusions, report unavailable coverage or truncation, and base conclusions only on fields returned by the API.

## Reference(s):

- [DDT Claw API homepage](https://gotoshop-ai.com/ddtclaw/)
- [ClawHub skill page](https://clawhub.ai/horacetu/skills/ddt-amap-retail-network)
- [Publisher profile](https://clawhub.ai/user/horacetu)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, API calls, guidance]

**Output Format:** [Markdown responses with concise conclusions, key metrics, coverage and data-version notes, limited store details when requested, and occasional shell command examples for setup.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires DDT_API_KEY for live API calls; uses only published aggregate data and restricted store previews described by API responses.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
