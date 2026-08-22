## Description:

Query the total number of Huawei Cloud services available through KooCLI offline metadata and return counts from the cached service catalog.

This skill is ready for commercial/non-commercial use.

## Publisher:

[erickeyhu-hug](https://clawhub.ai/user/erickeyhu-hug)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, cloud operators, and documentation authors use this skill to count Huawei Cloud services from the local KooCLI metadata cache for reporting, documentation, or service inventory awareness.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The release security summary reports unsafe setup and credential instructions involving KooCLI AK/SK credentials.

Mitigation: Install KooCLI through a verified method and avoid placing AK/SK secrets directly on the command line.

Risk: The skill may refresh and overwrite local KooCLI metadata for a simple count task.

Mitigation: Use the count-only path against an existing metadata cache unless the user explicitly wants to refresh metadata.

Risk: The security verdict is suspicious and recommends review before installation.

Mitigation: Review the skill and its commands before execution, with special attention to setup commands, credential handling, and metadata refresh behavior.

## Reference(s):

- [CLI Installation Guide](references/cli-installation-guide.md)
- [IAM Policies](references/iam-policies.md)
- [Verification Method](references/verification-method.md)
- [Data Flow Diagram](references/dataflow-diagram.md)
- [Acceptance Criteria](references/acceptance-criteria.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline bash and Python command snippets; runtime output is plain text service counts.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include commands that refresh KooCLI metadata and read the local services_en.json cache.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
