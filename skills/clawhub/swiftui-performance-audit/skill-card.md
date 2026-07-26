## Description: <br>
Audits SwiftUI runtime performance from code review, architecture review, and user-supplied profiling evidence to diagnose slow rendering, janky scrolling, high CPU or memory usage, excessive view updates, and layout thrash. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[steipete](https://clawhub.ai/user/steipete) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and engineers use this skill to review SwiftUI app code and profiling evidence, identify likely root causes of runtime performance issues, and propose targeted remediation and verification steps. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Performance recommendations may be wrong or incomplete if the user provides partial code, missing profiling evidence, or non-representative reproduction steps. <br>
Mitigation: Ask for the minimal relevant code, symptoms, reproduction steps, and Instruments screenshots or traces when code review is inconclusive; verify changes against baseline metrics. <br>
Risk: Code snippets, profiling traces, or screenshots may contain proprietary data, credentials, API keys, or sensitive implementation details. <br>
Mitigation: Share only the code and profiling material needed for the audit, and redact proprietary data, credentials, API keys, and sensitive trace details before use. <br>


## Reference(s): <br>
- [Optimizing SwiftUI Performance with Instruments](references/optimizing-swiftui-performance-instruments.md) <br>
- [Understanding and Improving SwiftUI Performance](references/understanding-improving-swiftui-performance.md) <br>
- [Understanding Hangs in Your App](references/understanding-hangs-in-your-app.md) <br>
- [Demystify SwiftUI Performance (WWDC23)](references/demystify-swiftui-performance-wwdc23.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Guidance] <br>
**Output Format:** [Markdown with issue summaries, metrics tables, code-level findings, proposed fixes, and profiling guidance.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May request user-provided SwiftUI code, trace exports, screenshots, device/OS/build context, and before/after metrics.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
