## Description:

ArcGIS Online (arcgis.com) enables agents to search and read ArcGIS Online data through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to run ArcGIS Online geocoding, reverse-geocoding, and autocomplete requests through an OOMOL-connected account after inspecting the live connector schema.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup guidance includes pipe-to-shell installation commands for the oo CLI.

Mitigation: Verify the installer source independently or use a trusted installation path before running it.

Risk: ArcGIS queries, addresses, coordinates, and request data may be processed through OOMOL as well as ArcGIS.

Mitigation: Review the OOMOL trust boundary and avoid sending sensitive location data unless the account and service terms permit it.

Risk: The skill has a broad routing instruction for ArcGIS Online requests.

Mitigation: Confirm the request intent, inspect the live action schema, and review payloads before execution.

## Reference(s):

- [ArcGIS Online homepage](https://www.arcgis.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, API calls, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before building request payloads; CLI responses include data and meta.executionId.]

## Skill Version(s):

1.0.3 (source: server release metadata and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
