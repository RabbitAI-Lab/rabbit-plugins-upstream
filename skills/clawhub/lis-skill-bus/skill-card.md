## Description:

Connects local CAD skills so one drawing is parsed once and its evidence-backed contract is shared across downstream quantity skills. Runs locally without network and degrades safely when the bus is absent.

This skill is ready for commercial/non-commercial use.

## Publisher:

[lisong2003-lgtm](https://clawhub.ai/user/lisong2003-lgtm)

### License/Terms of Use:

MIT

## Use Case:

Developers using local CAD reading and quantity skills use the bus to share project state and evidence-backed drawing contracts across skills, allowing downstream work to reuse extracted data and resume by project, building, and floor.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A shared contract may be reused for a different drawing despite a content fingerprint mismatch.

Mitigation: Independently verify the drawing identity and fingerprint before relying on a shared contract; a supplied fingerprint alone is not sufficient.

Risk: Installation can change the MCP client configuration.

Mitigation: Review the configuration change and keep its backup; set SKIP_MCP_REG=1 when installing without MCP registration.

Risk: Uninstalling leaves cached drawing evidence on disk.

Mitigation: Inspect and remove cached state separately when it should not be retained.

## Reference(s):

- [CAD contract schema](schemas/cad-contract-v1.schema.json)
- [Pilot integration guide](example_pilot/pilot.md)

## Skill Output:

**Output Type(s):** [JSON, Text]

**Output Format:** [Structured JSON contract and state data, with plain-text CLI responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Local project state and CAD evidence contracts keyed by project, building, and floor.]

## Skill Version(s):

0.1.7 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
