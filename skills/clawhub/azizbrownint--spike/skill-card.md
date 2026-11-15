## Description:

Run throwaway prototypes to validate feasibility, compare approaches, and report a verdict.

This skill is ready for commercial/non-commercial use.

## Publisher:

[azizbrownint](https://clawhub.ai/user/azizbrownint)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to run focused feasibility spikes before committing to a full implementation. It helps validate ideas, compare approaches, stress one key failure mode, and return an evidence-based verdict.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Spike prototypes and recommendations may be mistaken for production-ready implementation work.

Mitigation: Treat spike artifacts as disposable evidence and rewrite any validated approach using normal production engineering standards before merging.

Risk: The skill may create small throwaway files or run simple validation commands while testing feasibility.

Mitigation: Review proposed commands and keep prototype work in the default throwaway workspace unless a repo-local path is intentionally requested.

Risk: External dependencies evaluated during a spike may later be adopted without adequate review.

Mitigation: Check dependency health, documentation, license, release activity, and install friction before using the dependency in production.

## Reference(s):

- [Spike skill release page](https://clawhub.ai/azizbrownint/skills/spike)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Guidance]

**Output Format:** [Markdown verdicts with command output, measurements, recommendations, and small prototype artifacts when needed.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create throwaway files under .tmp/openclaw-spikes/<slug> or repo-local spikes/<NNN-slug>/ when the user asks for a tracked path.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
