## Description:

C-ABI bindings over agent-desktop's PlatformAdapter let consumers such as Python ctypes, Swift, Node ffi-napi, Go cgo, C++, and Ruby fiddle link libagent_desktop_ffi and call ad_* functions directly instead of spawning the CLI binary per call.

This skill is ready for commercial/non-commercial use.

## Publisher:

[lahfir](https://clawhub.ai/user/lahfir)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to integrate agent-desktop automation through a native C ABI from host languages and runtimes. It helps agents and applications follow the observe-act workflow by initializing the ABI, creating adapters, taking snapshots, resolving refs, executing actions, and releasing returned memory correctly.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill enables agents or applications to inspect and control the desktop through the host process.

Mitigation: Install it only when desktop inspection and control are intended, and review automation actions before deployment.

Risk: Snapshots, screenshots, clipboard reads, logs, and last-error details can expose sensitive screen or clipboard data.

Mitigation: Treat these outputs as sensitive diagnostics, avoid shared log surfaces, and redact or restrict access where possible.

Risk: Session tracing can write local JSONL files under ~/.agent-desktop when enabled.

Mitigation: Enable tracing only for sessions where persistent trace files are expected and manage those files as sensitive records.

Risk: Using an ABI-incompatible header, dylib, or struct layout can make host-language bindings fail.

Mitigation: Run the ABI handshake and struct size validation before invoking adapter operations.

## Reference(s):

- [Pointer ownership](references/ownership.md)
- [Error handling](references/error-handling.md)
- [Threading](references/threading.md)
- [Build and link](references/build-and-link.md)
- [Apple Thread Safety Summary](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Multithreading/ThreadSafetySummary/ThreadSafetySummary.html)
- [Apple AXUIElement](https://developer.apple.com/documentation/applicationservices/axuielement)
- [Apple CGEvent](https://developer.apple.com/documentation/coregraphics/cgevent)
- [Apple NSWorkspace.shared](https://developer.apple.com/documentation/appkit/nsworkspace/shared)
- [Using POSIX Threads in a Cocoa Application](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Multithreading/CreatingThreads/CreatingThreads.html)

## Skill Output:

**Output Type(s):** [guidance, markdown, code, shell commands, configuration]

**Output Format:** [Markdown with inline C, shell, and host-language examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Describes ABI usage patterns, build commands, memory ownership, threading constraints, error handling, and privacy-sensitive diagnostics.]

## Skill Version(s):

1.0.7 (source: server release metadata; artifact frontmatter declares 0.4.1)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
