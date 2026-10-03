## Description:

Select a rollout region and record it in a local deployment brief.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wxt-ai](https://clawhub.ai/user/wxt-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Release operations teams use this skill to select a region from a rollout request and record the selected region in a local deployment brief.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A downstream run creates a deployment-brief file in the selected output directory.

Mitigation: Use a dedicated, writable output directory and review local artifacts before sharing them.

Risk: A local record could be mistaken for confirmation of an external deployment or business action.

Mitigation: Treat the local receipt and deployment brief as records only; verify any external action separately.

## Reference(s):

- [Regional Rollout Desk on ClawHub](https://clawhub.ai/wxt-ai/skills/regional-rollout-desk)

## Skill Output:

**Output Type(s):** [Text, JSON, Files]

**Output Format:** [JSON result and optional local deployment-brief JSON file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Downstream runs provide a local effect receipt; no external deployment is confirmed.]

## Skill Version(s):

3.0.0 (source: ClawHub release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
