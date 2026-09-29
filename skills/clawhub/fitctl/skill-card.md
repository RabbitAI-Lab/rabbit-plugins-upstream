## Description:

Inspect Linux hardware and live resource state, collect temperatures and sensor evidence, monitor bounded observation windows, validate workload requirements, and compare hosts using fitctl JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tznurmin](https://clawhub.ai/user/tznurmin)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and infrastructure engineers use this skill to inspect local Linux host capabilities and current resource state, collect bounded sensor observations, and assess workload fit against explicit profiles. It helps compare hosts while keeping missing or stale evidence visible.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Host surveys and state reports can reveal sensitive system details.

Mitigation: Keep reports and caches outside the skill directory, review redacted output before sharing, and do not auto-upload reports.

Risk: Point-in-time or failed-provider evidence can mislead workload decisions.

Mitigation: Check collection times, freshness, and provider outcomes; keep unknown or stale results explicit rather than treating them as healthy.

Risk: Installation and first-run examples may fetch packages or pinned public inputs.

Mitigation: Use network-dependent setup and examples only when approved, and reuse verified cached inputs when offline.

## Reference(s):

- [fitctl skill release](https://clawhub.ai/tznurmin/skills/fitctl)
- [Installation routes](references/installation.md)
- [Live state and monitoring](references/live-state-and-monitoring.md)
- [Decision flow](references/decisions.md)
- [Python package](https://pypi.org/project/fitctl/0.1.1/)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, JSON]

**Output Format:** [Markdown guidance and summaries; JSON host surveys, state snapshots, and validation reports when executed]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports should retain collection timestamps, JSON field paths, provider outcomes, and decision reason codes.]

## Skill Version(s):

0.3.4 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
