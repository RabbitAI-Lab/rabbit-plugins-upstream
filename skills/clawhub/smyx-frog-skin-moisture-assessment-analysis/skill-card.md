## Description:

Assesses frog skin moisture from dorsal or lateral images or videos by analyzing glossiness, wrinkles, and white-film indicators to produce dehydration-risk reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External amphibian keepers, vivarium operators, farms, and animal hospitals use this skill to submit frog skin images or videos for moisture assessment, structured status reports, and history review. The output is advisory and should not be treated as a veterinary diagnosis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Frog images or videos may leave the local machine for analysis by configured services.

Mitigation: Install only when that data transfer is acceptable, and avoid submitting sensitive media unless the service handling and retention terms are understood.

Risk: Report history is account-linked and the skill can create or reuse local identity and token state.

Mitigation: Review local workspace data handling before deployment and clear stored identity or token state when decommissioning shared workspaces.

Risk: Security evidence flags private development HTTP endpoints and silent identity provisioning as review-worthy.

Mitigation: Confirm production endpoint configuration and document or fix identity provisioning behavior before normal user installation.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-frog-skin-moisture-assessment-analysis)
- [API interface documentation](references/api_doc.md)
- [Skill demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, guidance]

**Output Format:** [Markdown text with structured JSON report content and report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May write results to a file when an output path is provided; history review returns account-linked report records from the configured cloud service.]

## Skill Version(s):

1.0.8 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
