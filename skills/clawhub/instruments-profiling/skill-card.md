## Description: <br>
Use when profiling native macOS or iOS apps with Instruments/xctrace. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[steipete](https://clawhub.ai/user/steipete) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and agents use this skill to profile native macOS or iOS apps with Apple Instruments and xctrace, select the correct app process or binary, capture traces, and export stack data for performance analysis. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Profiling the wrong app or process can capture unrelated or sensitive process activity. <br>
Mitigation: Confirm the app path or PID before recording, prefer direct binary paths for deterministic launches, and verify the process path before trusting a trace. <br>
Risk: Generated .trace and XML export files may contain sensitive local performance data. <br>
Mitigation: Store trace and export files in appropriate local locations, avoid sharing them broadly, and treat them as potentially sensitive artifacts. <br>
Risk: xctrace may require Developer Tools permission for the terminal or Xcode. <br>
Mitigation: Grant Developer Tools permission only when needed and only to trusted tooling used for the profiling session. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/steipete/skills/instruments-profiling) <br>
- [Publisher profile](https://clawhub.ai/user/steipete) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Guides use of Apple Instruments and xctrace; may produce local .trace and XML export files when the suggested commands are run.] <br>

## Skill Version(s): <br>
1.0.0 (source: server-resolved release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
