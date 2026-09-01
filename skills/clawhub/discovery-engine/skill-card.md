## Description:

Discovery helps agents use Disco to upload tabular datasets, run statistically validated pattern discovery, and return structured findings with effect sizes, p-values, citations, novelty scores, and report links.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jessicarumbelow](https://clawhub.ai/user/jessicarumbelow)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, data scientists, and agent builders use this skill to analyze tabular datasets with Disco, choose target and excluded columns, estimate costs, run public or private analyses, and explain returned patterns.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Datasets can be uploaded to Disco/Leap Laboratories.

Mitigation: Use only data approved for that service, and use private visibility for confidential, personal, regulated, or proprietary data.

Risk: Public analyses publish results to a public gallery.

Mitigation: Confirm visibility with the user before analysis and choose private runs when results should not be public.

Risk: The skill can support payment, credit purchase, and subscription actions.

Mitigation: Require explicit human approval before attaching payment methods, buying credits, or changing plans.

Risk: Signed URLs and local file uploads may expose sensitive data.

Mitigation: Require explicit human approval before sharing signed URLs or uploading local files.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/jessicarumbelow/skills/discovery-engine)
- [Disco](https://disco.leap-labs.com)
- [Disco MCP Server](https://disco.leap-labs.com/mcp)
- [Python SDK Reference](docs/python-sdk.md)
- [OpenAPI Specification](docs/openapi.json)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON, Python, and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include structured pattern summaries, p-values, effect sizes, citations, novelty classifications, feature importance, cost estimates, and report links.]

## Skill Version(s):

0.2.168 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
