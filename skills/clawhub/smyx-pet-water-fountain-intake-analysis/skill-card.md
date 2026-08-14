## Description:

Analyzes pet water fountain area videos or URLs through provider-hosted APIs to estimate each pet's drinking frequency, session duration, daily intake, and changes against historical baselines.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to analyze pet drinking behavior from water fountain footage, produce structured intake summaries, and flag notable drops or spikes for health monitoring workflows. The results are health-reference signals and are not a veterinary diagnosis or treatment recommendation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends pet or household videos and URLs to configured lifeemergence.com services.

Mitigation: Use only footage appropriate for provider processing and confirm account, retention, and deletion practices before using sensitive home video.

Risk: The skill can create or reuse a local account identity, store tokens in a workspace SQLite database, and retrieve cloud history for that identity.

Mitigation: Run it in a controlled workspace, protect local token storage, and review cloud-history access expectations before deployment.

## Reference(s):

- [Skill API Documentation](references/api_doc.md)
- [Analysis API Documentation](skills/smyx_analysis/references/api_doc.md)
- [Skill Demo](https://lifeemergence.com/sample.html)
- [ClawHub Skill Page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-pet-water-fountain-intake-analysis)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown and JSON-style structured analysis reports with optional report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May query cloud history for the current provider-managed identity and may write analysis output to a user-specified file.]

## Skill Version(s):

1.0.5 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
