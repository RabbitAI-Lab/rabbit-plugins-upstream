## Description:

Self Reflection Loop helps an agent run a Reflexion-style generate, assess, and refine cycle with rubric scoring, tool-anchored checks, gap analysis, and learned lessons fed into later attempts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qq435912743](https://clawhub.ai/user/qq435912743)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, engineers, and agents use this skill to create rubrics, assess artifacts, run iterative refinement loops, and record recurring lessons for later use. It is suited to self-correction, code self-validation, quality gating, and structured improvement workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The refinement loop can run user-supplied shell commands.

Mitigation: Prefer init and assess workflows without --refine-cmd; review any refinement command manually before execution.

Risk: The learning module can retain local cross-run usage and preference history.

Mitigation: Periodically inspect or delete learned_patterns.json if retained history is not desired.

## Reference(s):


## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, configuration, guidance]

**Output Format:** [Markdown reports, JSON rubrics or logs, and shell command output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May update local learned_patterns.json usage and preference history when the learning script is used.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
