## Description: <br>
Native macOS/iOS app performance profiling via xctrace/Time Profiler and CLI-only analysis of Instruments traces for hotspot analysis and optimization. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[steipete](https://clawhub.ai/user/steipete) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and engineers use this skill to profile macOS or iOS applications from the command line, collect Time Profiler traces, extract samples, symbolicate stacks, and identify top performance hotspots without opening Instruments UI. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Profiling artifacts may contain app symbols, timing data, memory-map details, and other local diagnostic information. <br>
Mitigation: Keep generated traces and exported samples within trusted projects, and review them before sharing outside the project. <br>
Risk: The workflow depends on Apple developer tooling and local profiling targets, so results can be misleading when the trace, binary, or runtime load address do not match. <br>
Mitigation: Confirm the target binary, capture the runtime __TEXT load address, and match symbols to the recorded trace before acting on hotspot findings. <br>


## Reference(s): <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Code, Configuration] <br>
**Output Format:** [Markdown with inline shell commands and script-oriented guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May produce profiling workflow steps, command invocations, and analysis guidance for Time Profiler trace artifacts.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
