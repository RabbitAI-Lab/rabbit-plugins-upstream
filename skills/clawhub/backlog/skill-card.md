## Description:

Unified backlog lifecycle management and task tracking across session TODOs, workspace checklists, and issue trackers.

This skill is ready for commercial/non-commercial use.

## Publisher:

[drumrobot](https://clawhub.ai/user/drumrobot)

### License/Terms of Use:

MIT

## Use Case:

Developers and engineering teams use this skill to triage, prioritize, synchronize, prune, create, and comment on backlog items across local markdown checklists and issue trackers.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can mutate Plane backlog data and issue records.

Mitigation: Use a dedicated low-privilege Plane token and review intended mutations before enabling normal use.

Risk: Fallback paths may use Kubernetes, SSH, or direct database writes.

Mitigation: Remove or disable the Django-shell fallback where possible, or use a tightly scoped kubeconfig when fallback access is intentionally retained.

Risk: Tracker API calls can expose credentials if transport and redirect handling are not constrained.

Mitigation: Require HTTPS-only API calls and no-redirect behavior before routine use.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/drumrobot/skills/backlog)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create or update backlog records through tracker APIs when configured.]

## Skill Version(s):

0.3.1 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
