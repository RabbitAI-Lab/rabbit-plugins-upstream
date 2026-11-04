## Description:

Helps developers write, run, and debug web and mobile end-to-end tests, inspect live app flows, and explore applications or run bug bashes with e2e.

This skill is ready for commercial/non-commercial use.

## Publisher:

[e2e](https://clawhub.ai/user/e2e)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill to add, run, and debug end-to-end tests for web and mobile applications, inspect running app flows, and conduct structured QA explorations and bug bashes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Test flows that perform purchases or account changes could affect real users or services.

Mitigation: Use disposable accounts and sandbox payment services, and require explicit authorization before any real purchase or account change.

Risk: Screenshots, recordings, or model-provider interactions may expose application data.

Mitigation: Choose an approved model provider and inspect recordings before sharing them. Review dependency versions and generated MCP settings before use.

## Reference(s):

- [e2e homepage](https://e2e.com)
- [Setup guide](artifact/references/setup.md)
- [Writing tests guide](artifact/references/writing-tests.md)
- [Agent steps guide](artifact/references/agent.md)
- [MCP guide](artifact/references/mcp.md)
- [Running tests guide](artifact/references/running.md)
- [Debugging guide](artifact/references/debugging.md)
- [Explore guide](artifact/references/explore.md)
- [Bug bash guide](artifact/references/bug-bash.md)
- [AI SDK provider documentation](https://ai-sdk.dev/providers)
- [e2e decision models guide](https://e2e.tester.army/docs/decision-models)
- [e2e subscriptions guide](https://e2e.tester.army/docs/subscriptions#use-your-coding-agent)

## Skill Output:

**Output Type(s):** [Code, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown guidance with TypeScript test and configuration examples and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Project-specific examples and commands may vary by web, iOS, or Android target and test workflow.]

## Skill Version(s):

1.0.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
