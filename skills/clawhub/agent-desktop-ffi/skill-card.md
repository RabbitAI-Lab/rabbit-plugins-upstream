## Description: <br>
C-ABI bindings over agent-desktop's PlatformAdapter let consumers such as Python ctypes, Swift, Node ffi-napi, Go cgo, C++, and Ruby fiddle link libagent_desktop_ffi directly and run the observe-act workflow without spawning the CLI binary per call. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[lahfir](https://clawhub.ai/user/lahfir) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to build, link, and operate FFI integrations for desktop automation through agent-desktop's PlatformAdapter. It helps consuming runtimes manage ABI handshakes, adapter lifecycles, references, errors, threading, and memory ownership. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Consuming programs can drive desktop automation through this FFI. <br>
Mitigation: Install and use the skill only when that desktop automation capability is intended for the consuming host program. <br>
Risk: Snapshots, screenshots, clipboard data, trace files, and last-error details can contain sensitive user or application data. <br>
Mitigation: Treat these outputs as sensitive diagnostics and avoid routing them to shared logs or storage unless explicitly intended. <br>
Risk: Tracing and log callbacks can record or route diagnostic events. <br>
Mitigation: Enable tracing or log callbacks only when those diagnostics should be recorded or delivered to the caller's callback. <br>


## Reference(s): <br>
- [Build and link](references/build-and-link.md) <br>
- [Error handling](references/error-handling.md) <br>
- [Pointer ownership](references/ownership.md) <br>
- [Threading](references/threading.md) <br>
- [Apple Thread Safety Summary](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Multithreading/ThreadSafetySummary/ThreadSafetySummary.html) <br>
- [Apple AXUIElement](https://developer.apple.com/documentation/applicationservices/axuielement) <br>
- [Apple CGEvent](https://developer.apple.com/documentation/coregraphics/cgevent) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Code, Shell commands, Configuration] <br>
**Output Format:** [Markdown with inline shell, C, Python, and FFI guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes build commands, ABI validation guidance, lifecycle rules, and risk-aware diagnostic handling.] <br>

## Skill Version(s): <br>
1.0.6 (source: server release metadata; artifact frontmatter lists 0.4.1) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
