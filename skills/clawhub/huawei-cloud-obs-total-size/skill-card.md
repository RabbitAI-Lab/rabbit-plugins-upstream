## Description: <br>
Queries Huawei Cloud OBS bucket storage totals in a read-only flow and returns a single size value for one bucket or all buckets, using KooCLI/obsutil with a Python SDK fallback. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[erickeyhu-hug](https://clawhub.ai/user/erickeyhu-hug) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, cloud operators, and storage administrators use this skill to answer capacity review, cost estimation, storage planning, and compliance audit questions about Huawei Cloud OBS bucket usage. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill uses local Huawei Cloud OBS credentials and can query storage metadata from the configured account. <br>
Mitigation: Install it only where Huawei OBS metadata queries are intended, use least-privilege OBS read-only credentials, and avoid sharing AK/SK values in agent conversations. <br>
Risk: A generic storage or capacity question could be answered against the wrong cloud context. <br>
Mitigation: Confirm that the request is for Huawei Cloud OBS and clarify whether the user wants one bucket or all buckets before running commands. <br>
Risk: All-buckets totals may be incomplete when individual buckets are inaccessible and skipped. <br>
Mitigation: Review warnings from the query run and verify bucket permissions when totals are used for audits, cost estimates, or compliance tracking. <br>


## Reference(s): <br>
- [CLI Installation Guide](references/cli-installation-guide.md) <br>
- [IAM Policies](references/iam-policies.md) <br>
- [Verification Method](references/verification-method.md) <br>
- [Data Flow Diagram](references/dataflow-diagram.md) <br>
- [Acceptance Criteria](references/acceptance-criteria.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, guidance] <br>
**Output Format:** [Plain text numeric value; markdown with shell commands when guiding setup or verification] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Returns bytes by default, with optional KB, MB, GB, or human-readable units.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
