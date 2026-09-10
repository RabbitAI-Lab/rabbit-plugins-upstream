## Description:

Build modern Chrome and cross-browser extensions with WXT, TypeScript, and common UI frameworks such as React, Vue, Svelte, or Solid.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tenequm](https://clawhub.ai/user/tenequm)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to scaffold, configure, and package WXT-based Chrome or cross-browser extensions. It provides guidance for Manifest V3 entry points, browser APIs, React integration, storage, messaging, security practices, and build commands.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Examples include permissive or unsafe content security policy settings for extension pages.

Mitigation: Avoid copying unsafe-eval CSP patterns into production; use the narrowest CSP that supports the extension and document any exception.

Risk: Browser extension examples can involve powerful permissions, broad host scopes, cookies, history, or network traffic.

Mitigation: Use minimal and optional permissions, restrict host permissions, and require clear user consent before accessing sensitive browser data.

Risk: Package generator and dependency commands may resolve moving versions over time.

Mitigation: Pin npm generator and dependency versions where reproducibility or supply-chain review is required.

Risk: API keys or sensitive settings may be mishandled in browser storage.

Mitigation: Do not hardcode secrets or store API keys in synchronized browser storage; prefer explicit user configuration and local-only storage when needed.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/tenequm/skills/chrome-extension-wxt)
- [Clawdis Homepage](https://github.com/tenequm/skills/tree/main/skills/chrome-extension-wxt)
- [Chrome Extension Best Practices with WXT](references/best-practices.md)
- [Chrome 140+ Features](references/chrome-140-features.md)
- [Chrome Extension API Reference](references/chrome-api.md)
- [React Integration with WXT](references/react-integration.md)
- [WXT API Reference](references/wxt-api.md)
- [WXT Documentation](https://wxt.dev)
- [Chrome Extension Documentation](https://developer.chrome.com/docs/extensions)
- [Firefox Extension Documentation](https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with TypeScript, configuration, and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Documentation-only skill; generated advice should be reviewed before implementation in browser extensions.]

## Skill Version(s):

1.1.5 (source: SKILL.md frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
