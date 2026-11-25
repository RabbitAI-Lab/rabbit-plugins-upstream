## Description:

Helps developers write, run, and debug end-to-end tests for web and mobile apps, inspect live interfaces, and turn discovered bugs into reproducible tests.

This skill is ready for commercial/non-commercial use.

## Publisher:

[e2e](https://clawhub.ai/user/e2e)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use e2e to create and run browser and mobile end-to-end tests, investigate failures, and explore an app to find issues worth reproducing in tests.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Unpinned package commands may download changing dependencies.

Mitigation: Review package names and pin versions or use a committed lockfile before installing.

Risk: Test runs may share project data with model providers or incur charges.

Mitigation: Check provider data handling and expected costs, and keep credentials and sensitive test data out of prompts and outputs.

Risk: Uploaded screenshots, recordings, traces, or reports may expose sensitive app data.

Mitigation: Inspect generated artifacts and remove sensitive content before sharing or uploading them.

## Reference(s):

- [Setup guide](references/setup.md)
- [Writing tests guide](references/writing-tests.md)
- [Agent steps guide](references/agent.md)
- [Running tests guide](references/running.md)
- [MCP guide](references/mcp.md)
- [Debugging guide](references/debugging.md)
- [Explore guide](references/explore.md)
- [Bug bash guide](references/bug-bash.md)
- [e2e documentation](https://e2e.com)
- [AI SDK provider documentation](https://ai-sdk.dev/providers)
- [e2e decision models guide](https://e2e.com/docs/decision-models)
- [e2e coding agent subscriptions guide](https://e2e.com/docs/subscriptions#use-your-coding-agent)

## Skill Output:

**Output Type(s):** [Code, Shell commands, Configuration instructions, Guidance, Screenshots and video]

**Output Format:** [Markdown guidance, TypeScript test code, configuration examples, and optional screenshots or video]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Task-dependent; may include test reports, traces, screenshots, or video recordings.]

## Skill Version(s):

1.0.5 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
