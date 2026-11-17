## Description:

Writes, runs, and debugs end-to-end tests for web and mobile apps with e2e, the agentic test runner, which mixes agent.act goals with exact locator assertions on a Playwright browser or an iOS or Android device. Also drives a project's running app live over the e2e MCP server to look at a screen, check a UI change, take a screenshot or record a video, and try a locator; and runs bug bashes, parallel e2e explore runs with each bug proven by a repro test.

This skill is ready for commercial/non-commercial use.

## Publisher:

[e2e](https://clawhub.ai/user/e2e)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and QA engineers use this skill to write, run, and debug end-to-end tests for web and mobile applications, inspect running app screens, and explore workflows or bug bash an app. It supports projects that use e2e or request browser, mobile, or agentic UI testing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Package installation instructions may use unpinned downloads, and scan coverage is partial.

Mitigation: Review installation commands before use, pin and verify exact package versions, and treat the scan as incomplete.

Risk: Test workflows could affect real accounts or expose application data through external services or uploaded test artifacts.

Mitigation: Use disposable or sandboxed app targets and billing integrations; review what application data, screenshots, traces, or repository information may be sent or uploaded.

## Reference(s):

- [e2e homepage](https://e2e.com)
- [Setup guide](artifact/references/setup.md)
- [MCP guide](artifact/references/mcp.md)
- [Writing tests guide](artifact/references/writing-tests.md)
- [Agent steps guide](artifact/references/agent.md)
- [Running tests guide](artifact/references/running.md)
- [Debugging guide](artifact/references/debugging.md)
- [Explore guide](artifact/references/explore.md)
- [Bug bash guide](artifact/references/bug-bash.md)
- [e2e examples](https://github.com/e2e-inc/e2e/tree/main/examples)

## Skill Output:

**Output Type(s):** [Code, Shell commands, Configuration instructions, Guidance, Screenshots and video]

**Output Format:** [TypeScript or JavaScript test code, configuration snippets, shell commands, and Markdown guidance; may also produce test traces, screenshots, or video artifacts.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs depend on the application, configured browser or mobile target, and available e2e tooling.]

## Skill Version(s):

1.0.4 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
