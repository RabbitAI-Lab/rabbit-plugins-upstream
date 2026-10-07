## Description:

Guides agents to retrieve only the evidence needed for the next material decision, assess its sufficiency, and stop when further searching is unlikely to change the outcome.

This skill is ready for commercial/non-commercial use.

## Publisher:

[raguets](https://clawhub.ai/user/raguets)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and other agent users apply this skill when missing organization-specific, historical, or current knowledge could change a decision. It helps agents select authorized sources, retrieve narrowly, cite supporting evidence, and report unresolved gaps.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Agents may consult knowledge bases or prepare documents outside the user's authorized scope.

Mitigation: Expose only authorized sources and document-preparation tools; verify access before retrieval.

## Reference(s):

- [Know Enough on ClawHub](https://clawhub.ai/raguets/skills/know-enough)
- [Overpowered project (listed in skill metadata; import provenance unavailable)](https://github.com/raguets/overpowered)
- [Adaptive retrieval guidance](references/adaptive-retrieval.md)
- [Knowledge-source registry guidance](references/knowledge-source-registry.md)
- [Example knowledge-source registry](references/knowledge-sources.example.yaml)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown or plain text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Compact knowledge state with consulted sources, remaining uncertainty, and an ENOUGH or NOT ENOUGH sufficiency judgment.]

## Skill Version(s):

1.0.2 (source: ClawHub release evidence; skill metadata lists 0.1.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
