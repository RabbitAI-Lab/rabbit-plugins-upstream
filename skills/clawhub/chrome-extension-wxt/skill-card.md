## Description:

Build Chrome and cross-browser extensions with WXT using TypeScript and React, Vue, Svelte, or Solid.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tenequm](https://clawhub.ai/user/tenequm)

### License/Terms of Use:

Apache 2.0

## Use Case:

Developers and engineers use this skill to create WXT-based browser extensions, configure entry points and manifests, integrate UI frameworks, and package builds for browser stores.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Extension examples may encourage broad host permissions or sensitive browser permissions.

Mitigation: Review requested permissions before reuse, prefer least-privilege host access, and use optional permissions where possible.

Risk: Content scripts and injected page code can affect untrusted web pages or expose extension behavior.

Mitigation: Keep injected code minimal and trusted, validate inputs, and review content security policy settings before deployment.

Risk: Examples involving extension storage may be adapted to store long-lived API keys or other secrets.

Mitigation: Avoid storing long-lived API keys in synced extension settings without a clear threat model and appropriate user controls.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/tenequm/skills/chrome-extension-wxt)
- [Metadata homepage](https://github.com/tenequm/skills/tree/main/skills/chrome-extension-wxt)
- [WXT Docs](https://wxt.dev)
- [Chrome Extensions Docs](https://developer.chrome.com/docs/extensions)
- [Firefox Add-ons Docs](https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons)
- [Chrome Extension Best Practices with WXT](references/best-practices.md)
- [Chrome 140+ Features](references/chrome-140-features.md)
- [Chrome Extension API Reference](references/chrome-api.md)
- [React Integration with WXT](references/react-integration.md)
- [WXT API Reference](references/wxt-api.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with TypeScript, HTML, and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Review generated extension permissions, injected scripts, and storage patterns before reuse.]

## Skill Version(s):

1.1.3 (source: SKILL.md frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
