## Description:

Audit Git repositories and worktrees, preserve findings, and monitor scheduled audit health without deleting work.

This skill is ready for commercial/non-commercial use.

## Publisher:

[glucksberg](https://clawhub.ai/user/glucksberg)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and repository operators use this skill to audit authorized Linux Git repositories and worktrees, preserve private findings, and monitor scheduled audit health. It reports evidence, incomplete checks, and requested human actions without performing cleanup, commits, pushes, or deployment.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can access configured repositories and optional scheduler or runtime details.

Mitigation: Configure only explicitly authorized repositories, start with a local dry run without --fetch, --github, or --persist, and keep private configuration outside repositories and indexed memory.

Risk: Opt-in fetch, GitHub, and persistence modes can change remote-tracking refs or write private audit state.

Mitigation: Enable network and persistence flags only after review, protect the configured state directory, and avoid publishing generated state or operational findings.

Risk: Scheduling and supervised organization workflows can affect operational processes if run under the wrong authority.

Mitigation: Enable scheduling or supervised actions only with explicit authorization for the run, verify owner and scheduler authority, and report blockers instead of creating duplicate or unauthorized jobs.

## Reference(s):

- [Configuration](references/configuration.md)
- [Findings and reports](references/findings.md)
- [Repository inventory example](references/repositories.example.json)
- [Scheduling](references/scheduling.md)
- [Supervised actions](references/supervised-actions.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown audit summaries, JSON reports and state, and inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Private state can include approved paths, commit IDs, counts, and timestamps; the skill instructs users not to publish it.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
