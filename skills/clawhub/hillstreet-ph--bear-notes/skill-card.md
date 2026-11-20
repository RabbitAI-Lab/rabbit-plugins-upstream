## Description:

Create, search, and manage Bear notes via grizzly CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[hillstreet-ph](https://clawhub.ai/user/hillstreet-ph)

### License/Terms of Use:

MIT-0

## Use Case:

External users working with Bear on macOS can use this skill to create, open, append to, and search notes and tags through the grizzly CLI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The available security analysis is partial because a referenced local path could not be resolved, even though the scans reported no findings.

Mitigation: Review the unresolved reference and decide whether you trust it before installing; treat the scan result as limited to the available analysis.

Risk: Some Bear operations require an API token stored in a local file.

Mitigation: Keep the configured token file private and avoid copying the token into shared notes or logs.

## Reference(s):

- [Bear](https://bear.app)
- [Bear Notes on ClawHub](https://clawhub.ai/hillstreet-ph/skills/bear-notes)
- [grizzly CLI installation source](https://github.com/tylerwince/grizzly)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Configuration instructions, JSON]

**Output Format:** [Markdown guidance with inline shell commands; callback results can be JSON.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires macOS, Bear running, and grizzly; some operations also require a Bear API token.]

## Skill Version(s):

1.0.2 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
