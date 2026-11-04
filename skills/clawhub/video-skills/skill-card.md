## Description:

Finds task-specific skills and tutorials for AI video, image, voice, and music work, then presents visual options before generation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[vargai](https://clawhub.ai/user/vargai)

### License/Terms of Use:

MIT-0

## Use Case:

People choosing an approach for a video, image, voice, or music task can use this skill to find matching agent skills and tutorials, compare visual options, and get workflow guidance. It helps select and plan a workflow; it does not generate media itself.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Project setup guidance may upload project data to a GitHub account or repository without making the upload scope clear.

Mitigation: Approve the account, repository, and exact files or media to upload; keep confidential details out of searches.

Risk: Linked downstream instructions were not bundled or retrieved, so their safeguards and executable behavior are unverified.

Mitigation: Review added skills and downstream instructions before use.

Risk: Media generation can incur paid-model or rendering costs.

Mitigation: Set a spending cap and review cost estimates before paid calls or batches.

## Reference(s):

- [varg how-to](https://varg.ai/how-to)
- [varg MCP server](https://mcp.varg.ai/mcp)

## Skill Output:

**Output Type(s):** [Guidance, API calls, Shell commands]

**Output Format:** [Markdown guidance with links and example curl commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Skill recommendations and workflow guidance; no media generation.]

## Skill Version(s):

1.0.13 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
