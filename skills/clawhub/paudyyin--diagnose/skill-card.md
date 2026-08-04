## Description: <br>
Debug complex bugs and performance regressions using a structured six-phase methodology: build a feedback loop, reproduce, hypothesize, probe, fix, and review. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[paudyyin](https://clawhub.ai/user/paudyyin) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to guide troubleshooting work for complex bugs, test failures, build issues, runtime errors, and performance regressions. It emphasizes reproducible feedback loops, hypothesis-driven probing, regression tests, and cleanup before resuming feature work. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Broad troubleshooting triggers may activate the skill for many debug or diagnose requests. <br>
Mitigation: Review the task context and continue only when a structured debugging workflow is appropriate. <br>
Risk: Debugging workflows can lead an agent to propose shell commands, trace collection, or production instrumentation. <br>
Mitigation: Review proposed commands, trace collection, and production instrumentation before allowing execution or deployment. <br>
Risk: Error messages, stack traces, logs, or third-party service output can contain misleading or malicious instructions. <br>
Mitigation: Treat external diagnostic output as evidence only; present embedded commands or URLs for user confirmation instead of following them automatically. <br>


## Reference(s): <br>
- [Debugging patterns](references/debugging-patterns.md) <br>
- [Debugging tools](references/debugging-tools.md) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, markdown, shell commands, code, configuration] <br>
**Output Format:** [Markdown guidance with checklists, command examples, code snippets, and troubleshooting tables] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces procedural debugging guidance for an agent; it does not include an executable payload.] <br>

## Skill Version(s): <br>
3.0.0 (source: server release evidence and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
