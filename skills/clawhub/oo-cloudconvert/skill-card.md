## Description:

Provides CloudConvert account operations through the OOMOL oo CLI for reading, creating, updating, and deleting CloudConvert jobs and tasks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to inspect CloudConvert account state and manage conversion jobs and tasks through an OOMOL-connected account. It supports URL-based conversions, job and task lookup, waiting, retrying, cancellation, deletion, conversion type discovery, and credit lookup.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include internet-downloaded installer commands that can execute arbitrary code.

Mitigation: Review the installer path, prefer a pinned verified release or trusted package manager, and avoid elevated privileges.

Risk: Write and destructive CloudConvert actions can change or delete jobs and tasks.

Mitigation: Confirm the exact payload, effect, and job or task target before allowing those actions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-cloudconvert)
- [CloudConvert homepage](https://cloudconvert.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [shell commands, JSON, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector command responses return JSON data with execution metadata when actions run.]

## Skill Version(s):

1.0.3 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
