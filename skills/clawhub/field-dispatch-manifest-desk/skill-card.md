## Description:

Sequence stops for a field route and build a local dispatch manifest.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wxt-ai](https://clawhub.ai/user/wxt-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Field-service dispatchers and operations teams use this skill to order route stops from supplied locations and create a local manifest for handoff.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Route and stop locations may be sensitive.

Mitigation: Use only location data appropriate for the workflow and handle generated plans and manifests accordingly.

Risk: Downstream execution writes a local manifest in the selected output directory.

Mitigation: Choose a dedicated, writable output directory and review its contents before sharing.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/wxt-ai/skills/field-dispatch-manifest-desk)

## Skill Output:

**Output Type(s):** [JSON, Files]

**Output Format:** [JSON route plan or dispatch manifest; downstream also writes a local manifest JSON file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Downstream writes to a caller-selected output directory.]

## Skill Version(s):

3.0.0 (source: skill frontmatter and ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
