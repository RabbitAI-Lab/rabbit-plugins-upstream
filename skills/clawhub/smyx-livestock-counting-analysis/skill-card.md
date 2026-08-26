## Description:

Automatically detects and counts livestock or poultry individuals from barn or passage camera images/videos, outputting total headcount with confidence for fast inventory.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

External users and farm operations teams use this skill to count livestock or poultry from barn and passage camera images or videos, producing inventory counts, confidence, and report links for faster stocktaking.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uploads livestock images, videos, or submitted URLs to the publisher's cloud service.

Mitigation: Use only footage appropriate for third-party cloud processing and review endpoint configuration before handling sensitive farm media.

Risk: The skill creates or reuses a persistent internal identity and stores local authentication tokens in the workspace data directory.

Mitigation: Run in an isolated workspace when needed and clear local skill data or credentials according to the deployment's retention policy.

Risk: Cloud history reports may be retrieved automatically for the active internal identity.

Mitigation: Confirm that report history access matches the intended user or tenant before using the skill in shared environments.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-livestock-counting-analysis)
- [API documentation](references/api_doc.md)
- [Shared analysis API documentation](skills/smyx_analysis/references/api_doc.md)
- [Skill demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, JSON, Files, Shell commands, Guidance]

**Output Format:** [Markdown reports or JSON-style structured analysis with optional saved output files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs can include total count, partition counts, confidence, analysis time, and report links.]

## Skill Version(s):

1.0.8 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
