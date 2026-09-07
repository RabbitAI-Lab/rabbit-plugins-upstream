## Description:

module-tsx helps agents write browser pages that run TypeScript, TSX, and React directly in HTML without a build step.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yieldray](https://clawhub.ai/user/yieldray)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to create no-build browser prototypes or pages that run TypeScript, TSX, and React through module-tsx, including inline scripts, relative imports, CSS imports, and optional import maps.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated browser pages can fetch and execute third-party CDN code when dependencies are not pinned or self-hosted.

Mitigation: Pin exact dependency versions, review remote packages before use, and consider self-hosting or vendoring dependencies for production or sensitive pages.

Risk: Browser pages that execute remote packages may expose production or sensitive contexts to unnecessary supply-chain and runtime risk.

Mitigation: Apply a restrictive Content Security Policy and use the skill primarily in prototypes, demos, or controlled browser apps unless dependencies and hosting are reviewed.

Risk: Incorrect import-map ordering, unsupported defer usage, or duplicate React instances can cause runtime failures.

Mitigation: Place import maps before the module-tsx script, avoid defer on module-tsx script tags, and deduplicate peer dependencies with pinned CDN URLs or deps parameters.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/yieldray/skills/module-tsx)
- [module-tsx CDN package](https://esm.sh/module-tsx)
- [module-tsx development build](https://esm.sh/module-tsx/dev)

## Skill Output:

**Output Type(s):** [guidance, code, configuration]

**Output Format:** [Markdown guidance with HTML and TypeScript/TSX code snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include import-map configuration, script tags, and dependency-pinning guidance for browser execution.]

## Skill Version(s):

0.1.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
