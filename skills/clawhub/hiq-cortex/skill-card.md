## Description:

Look up LCA emission factors, product carbon footprint data, BOM accounting inputs, production-route comparisons, EPD peer data, and benchmark distributions from HiQ Cortex databases and published EPDs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kirbyingithub](https://clawhub.ai/user/kirbyingithub)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and LCA practitioners use this skill to query HiQ Cortex for dataset matches, GWP values, LCIA indicators, process hotspots, EPD search, and peer benchmarks. It is intended for carbon-footprint and life-cycle-assessment workflows that need database, version, system model, geography, and reference-unit basis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can send raw LCA queries, product descriptions, and BOM lines to the external HiQ Cortex service.

Mitigation: Use it only when external HiQ Cortex processing is intended, and redact confidential material lists or product details before querying.

Risk: Browser sign-in stores reusable credentials in ~/.hiq/credentials.json.

Mitigation: Use the logout command to remove local credentials when the session should no longer persist, and avoid shared host accounts for sensitive work.

## Reference(s):

- [HiQ Cortex skill page](https://clawhub.ai/kirbyingithub/skills/hiq-cortex)
- [HiQ-AI agent-skills repository](https://github.com/HiQ-AI/agent-skills)
- [HiQ LCA data service](https://www.hiqlcd.com/)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and optional JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include dataset keys, GWP or LCIA values with basis, entitlement notes, purchase URLs, credential setup guidance, and raw JSON when requested.]

## Skill Version(s):

1.8.2 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
