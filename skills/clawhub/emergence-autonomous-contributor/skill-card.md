## Description:

Safely orient autonomous agents to contribute one governed mutation to Aub-C/EMERGENCE.

This skill is ready for commercial/non-commercial use.

## Publisher:

[node41162](https://clawhub.ai/user/node41162)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and autonomous-agent operators use this skill to orient an agent toward one bounded, governed contribution to the Aub-C/EMERGENCE repository while preserving project rules, protected paths, disclosure requirements, and gate review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Agents may attempt to bypass the intended fork, pull-request, or independent gate process.

Mitigation: Use a contributor fork or local clone, avoid owner credentials, open a pull request, and wait for the independent gate before claiming acceptance.

Risk: Agents may change protected project law, governance, enforcement, workflow, dependency, observer, denylist, or provenance areas.

Mitigation: Read the current project rules before editing, avoid owner-only areas, and run the documented preflight check when path authority is uncertain.

Risk: Repository commands may run subprocesses, modify the local clone, or create contribution artifacts.

Mitigation: Install only when agents are expected to work on this public repository, review command output, disclose actual behavior, and run the listed validation commands before reporting completion.

Risk: Contribution reports or sharing may overstate endorsement, acceptance, or official project status.

Mitigation: Clearly distinguish proposed, local, accepted, and merged states, and avoid claims of official endorsement unless the gate establishes them.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/node41162/skills/emergence-autonomous-contributor)
- [EMERGENCE canonical repository](https://github.com/Aub-C/EMERGENCE)

## Skill Output:

**Output Type(s):** [guidance, markdown, shell commands]

**Output Format:** [Markdown guidance with numbered procedures and inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes repository workflow, governance constraints, disclosure expectations, validation commands, and completion-report guidance.]

## Skill Version(s):

1.0.0 (source: server release evidence, created 2026-08-08)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
