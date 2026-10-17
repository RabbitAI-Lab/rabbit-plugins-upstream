## Description:

Builds a sorted index of paths and methods from a user-provided OpenAPI JSON document.

This skill is ready for commercial/non-commercial use.

## Publisher:

[hmahmadcs](https://clawhub.ai/user/hmahmadcs)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and API reviewers use this skill to survey endpoints and prepare smoke-test checklists from a supplied OpenAPI 3 JSON document.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A supplied OpenAPI file may contain secrets or sensitive API details.

Mitigation: Provide only specs approved for local agent access; remove secrets before sharing.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/hmahmadcs/skills/openapi-endpoint-indexer)

## Skill Output:

**Output Type(s):** [Text]

**Output Format:** [Plain text METHOD /path lines with counts by method]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Sorted by path; excludes webhooks and callbacks.]

## Skill Version(s):

1.0.0 (source: ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
