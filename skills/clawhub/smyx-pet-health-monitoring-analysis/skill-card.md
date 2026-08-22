## Description:

Analyzes pet monitoring images or videos with computer vision to report feeding, drinking, excretion, mental-state, vomiting, and limping indicators and surface possible health anomalies.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External users and pet-care developers use this skill to submit pet monitoring video or image inputs and receive structured health monitoring reports, recommendations, report links, and report-history results from the configured cloud service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Pet media and report history are handled by the listed cloud services.

Mitigation: Install only if that data handling is acceptable, and avoid submitting pet media or report history that should not leave the local workspace.

Risk: The skill silently creates or reuses a local identity and stores session tokens in the workspace data directory.

Mitigation: Review or remove data/smyx-api-key.txt and the generated SQLite database when identity-linked reuse is not desired.

Risk: Health analysis reports may be used as medical guidance even though the artifact says results are for pet-health reference only.

Mitigation: Treat outputs as monitoring signals and seek professional veterinary diagnosis when the report surfaces abnormalities or health concerns.

## Reference(s):

- [API interface documentation](artifact/references/api_doc.md)
- [Skill demo](https://lifeemergence.com/sample.html)
- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-pet-health-monitoring-analysis)

## Skill Output:

**Output Type(s):** [text, markdown, json, files]

**Output Format:** [Structured health report text, Markdown tables for history lists, JSON detail output, and optional saved output file.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports local video files or video URLs, cat/dog pet type, monitor-day count, and basic/standard/json detail levels; local video validation limits files to supported formats and a 10 MB maximum.]

## Skill Version(s):

1.0.12 (source: server release evidence; artifact frontmatter reports 1.0.13)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
