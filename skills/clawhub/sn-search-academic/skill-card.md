## Description:

Supports academic research by searching scholarly and encyclopedic sources, reading papers or sections, and tracing references and citations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[sensenova-skills](https://clawhub.ai/user/sensenova-skills)

### License/Terms of Use:

MIT-0

## Use Case:

Researchers, developers, and agents use this skill to gather papers and encyclopedia entries, inspect full text or named sections, and build citation context for academic literature reviews.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Crawler fallback can run a local Node dependency and expose environment variables to browser processes.

Mitigation: Use an isolated environment with no unrelated secrets, and use crawler fallback only when camoufox-js is installed from a trusted pinned source.

Risk: DeepXiv providers may register or use a token when no DEEPXIV_TOKEN is supplied.

Mitigation: Review DeepXiv token-registration behavior and provide approved credentials explicitly before enabling DeepXiv fallback.

Risk: Search queries, paper IDs, and retrieved content may be sent to external academic and encyclopedia services.

Mitigation: Avoid submitting confidential topics or sensitive identifiers, and restrict sources when a workflow should contact only specific services.

## Reference(s):

- [Search reference](references/search.md)
- [Paper reading reference](references/paper.md)
- [Reference tree reference](references/refTree.md)
- [ClawHub skill page](https://clawhub.ai/sensenova-skills/skills/sn-search-academic)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with JSON-producing Python script commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Large search, paper, and citation results can be written to files with --output.]

## Skill Version(s):

2026.9.11 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
