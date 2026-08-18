## Description:

Disciplined diagnosis workflow for hard bugs and performance regressions, guiding an agent through reproduction, minimization, hypothesis ranking, instrumentation, fixing, regression testing, cleanup, and post-mortem.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dennisrongo](https://clawhub.ai/user/dennisrongo)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineering agents use this skill when diagnosing bugs, failing tests, flaky behavior, crashes, hangs, leaks, incorrect output, or performance regressions. It helps structure debugging work around a reproducible feedback loop, falsifiable hypotheses, targeted probes, and regression verification.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may lead an agent to inspect code, run reproduction loops, create tests or harnesses, use sub-agents, or add temporary instrumentation while debugging.

Mitigation: Use isolated development or test environments for repro work when possible, review commands and edits in sensitive projects, and confirm that temporary debug instrumentation is removed during cleanup.

Risk: Debugging workflows can surface sensitive logs, traces, payloads, or source details while building a feedback loop.

Mitigation: Scope shared artifacts to the minimum needed for diagnosis and redact secrets or private data before providing logs, traces, recordings, or captured requests.

## Reference(s):


## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, guidance]

**Output Format:** [Markdown with hypotheses, file references, inline code, shell commands, and implementation guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include proposed tests, harnesses, debug instrumentation, cleanup steps, and post-mortem recommendations.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
