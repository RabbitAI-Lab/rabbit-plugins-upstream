## Description:

Analyzes pet water fountain area videos or video URLs through provider APIs to report drinking frequency, session duration, estimated daily intake, historical-baseline changes, and early warning alerts for notable intake drops or spikes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to analyze pet water-fountain videos, produce structured intake-monitoring reports, and query cloud history for prior reports. The output is for pet health monitoring reference and is not a disease diagnosis or treatment recommendation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Pet-area videos or URLs, account identifiers, and analysis metadata are sent to the provider service.

Mitigation: Use only with footage approved for third-party processing, and review configured endpoints, authentication, and retention expectations before installation.

Risk: The skill can create or reuse local persistent identity and token state.

Mitigation: Run it in a controlled workspace, rotate identities deliberately, and clear the local smyx data/token store when changing users or uninstalling.

Risk: Cloud history commands can retrieve stored reports for the resolved identity without prompting for a separate user identifier.

Mitigation: Confirm the workspace identity context before using history queries and restrict access to workspaces that may contain account state.

Risk: Water-intake values are estimates and health alerts are monitoring signals rather than diagnoses.

Mitigation: Present results as reference guidance only and direct medical decisions to a veterinarian.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-pet-water-fountain-intake-analysis)
- [Skill demo](https://lifeemergence.com/sample.html)
- [Pet water fountain analysis API documentation](references/api_doc.md)
- [Common analysis API documentation](skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Guidance]

**Output Format:** [Markdown text with structured JSON analysis and report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May write results to a user-specified output file; historical report listings are returned as structured text.]

## Skill Version(s):

1.0.6 (source: server release metadata; artifact frontmatter reports 1.0.9)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
