## Description:

Comprehensive guidance for building, debugging, and publishing Chrome extensions with Manifest V3.

This skill is ready for commercial/non-commercial use.

## Publisher:

[samber](https://clawhub.ai/user/samber)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to plan and implement Manifest V3 Chrome extensions, including manifests, content scripts, service workers, extension UI surfaces, messaging, permissions, storage, network/CSP patterns, debugging, and Chrome Web Store publishing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill includes patterns for bypassing or removing website security protections in Chrome extension workflows.

Mitigation: Use only for authorized extension development; prefer narrow domain allowlists, runtime user consent, and avoiding CSP weakening unless there is a clearly justified defensive or enterprise need.

Risk: Generated extension code could request broad host permissions, inject page scripts, relay network requests, persist content scripts, or store tokens in unsafe ways.

Mitigation: Review generated code before installation or publication, minimize host permissions, validate relay endpoints, and handle credentials with storage and access patterns appropriate to the extension threat model.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/samber/skills/chrome-extension)
- [Project homepage](https://github.com/samber/cc-skills)
- [Content Scripts Reference](references/content-scripts.md)
- [Debugging and Common Mistakes Reference](references/debugging-mistakes.md)
- [Execution Contexts, Communication Flows, and Limits](references/execution-contexts.md)
- [Manifest V3 Complete Reference](references/manifest-v3.md)
- [Messaging and RPC Reference](references/messaging-rpc.md)
- [Network Requests and CSP Bypass Reference](references/network-csp.md)
- [Permissions Reference](references/permissions.md)
- [Chrome Web Store Publishing Reference](references/publishing.md)
- [Service Worker Reference](references/service-worker.md)
- [Storage Reference](references/storage.md)
- [TypeScript and Build Tooling Reference](references/typescript-build.md)
- [UI Surfaces Reference](references/ui-surfaces.md)
- [Web Accessible Resources Reference](references/web-accessible-resources.md)

## Skill Output:

**Output Type(s):** [guidance, markdown, code, shell commands, configuration]

**Output Format:** [Markdown with code blocks and configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires review before execution, especially for generated extension permissions, network relays, CSP changes, injected scripts, and token storage.]

## Skill Version(s):

1.1.0 (source: server release evidence and artifact metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
