## Description:

Estimates concrete volumes and rebar ranges from structural drawings for material planning; it does not replace fabrication takeoff or settlement.

This skill is for research and development only.

## Publisher:

[lisong2003-lgtm](https://clawhub.ai/user/lisong2003-lgtm)

### License/Terms of Use:

CC BY-NC-SA 4.0

## Use Case:

Structural estimators and project teams use the skill to prepare preliminary concrete volume and rebar estimate bands by floor or pour zone for material planning, using drawing data supplied by the required CAD reader.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: ClawScan marks the skill suspicious for reported behavior beyond quantity estimation and questionable review outputs; five of 103 components were only partially inspected.

Mitigation: Review the source and generated reports, including behavior outside quantity estimation, before relying on the results.

Risk: The skill may automatically install its CAD reader base and related dependencies.

Mitigation: Manage setup explicitly with SKILL_NO_BASE=1 or disable base vendor auto-downloads with CAD_AUTO_SETUP=0, and confirm required local components are available.

Risk: Quantity outputs are estimates with stated error ranges and may omit or misread drawing details.

Mitigation: Check the source drawings and flagged omissions; use the results for planning only, not fabrication takeoff, settlement, or final measurement.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/lisong2003-lgtm/skills/tujian-suanliang)
- [Usage examples](references/usage-examples.md)
- [CAD reader contract](references/base-contract.md)
- [Runtime guide](docs/runtime.md)
- [Performance and indexing](docs/performance.md)

## Skill Output:

**Output Type(s):** [Analysis, JSON, CSV, Shell commands]

**Output Format:** [JSON and CSV quantity reports with human-readable command-line summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Preliminary quantity bands include review flags and source evidence; they are not final takeoff or settlement quantities.]

## Skill Version(s):

0.9.41 (source: ClawHub release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
