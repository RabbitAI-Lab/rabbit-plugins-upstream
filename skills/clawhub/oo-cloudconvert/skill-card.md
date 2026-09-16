## Description:

CloudConvert lets agents operate CloudConvert through an OOMOL-connected account for file conversion jobs, task and job management, conversion type discovery, and current user or credit lookup.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use this skill to run CloudConvert conversion workflows through the oo CLI, inspect jobs and tasks, discover conversion types, and manage retries, cancellations, or deletions with confirmation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup guidance includes remote installer commands that execute downloaded code.

Mitigation: Prefer installing the oo CLI through a verified package or signed release, and review installer source before execution.

Risk: The granted oo CLI permission is broader than CloudConvert-only actions.

Mitigation: Review the skill before installing and restrict agent use to the documented cloudconvert connector actions.

Risk: Destructive CloudConvert actions can delete jobs, tasks, and related data.

Mitigation: Require explicit user approval for the exact target before running destructive actions.

## Reference(s):

- [CloudConvert homepage](https://cloudconvert.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [CloudConvert on ClawHub](https://clawhub.ai/oomol/skills/oo-cloudconvert)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON command responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Actions can read account data, create or retry conversion jobs, wait for task completion, cancel tasks, or delete jobs and tasks.]

## Skill Version(s):

1.0.3 (source: server release metadata and SKILL.md metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
