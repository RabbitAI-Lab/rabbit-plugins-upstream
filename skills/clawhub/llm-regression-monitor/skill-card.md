## Description:

Monitors LLM behavior over time by capturing baselines, running scheduled behavioral checks, tracking drift trends, and sending configured alerts when outputs change unexpectedly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[swanand33](https://clawhub.ai/user/swanand33)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to set up behavioral regression monitoring for LLM applications, capture expected baselines, run scheduled checks, and receive alerts when outputs drift or assertions fail.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: LLM prompts, outputs, baselines, reports, trend logs, and alert logs may contain sensitive application or customer information.

Mitigation: Use non-sensitive test prompts and outputs where possible, add generated monitoring files to .gitignore, and install the skill only in projects where local storage of these artifacts is acceptable.

Risk: Failure summaries can be sent to configured WhatsApp, Slack, Discord, or email destinations.

Mitigation: Configure alert channels only for approved recipients and avoid including secrets or sensitive customer data in monitored prompts and outputs.

Risk: Unpinned Python dependencies can change behavior across installations.

Mitigation: Pin dependency versions before production use and review dependency updates before deployment.

## Reference(s):

- [LLM Regression Monitor Skill Page](https://clawhub.ai/swanand33/skills/llm-regression-monitor)
- [swanand33 Publisher Profile](https://clawhub.ai/user/swanand33)
- [Providers Setup Guide](references/providers.md)
- [test_suite.yaml Field Reference](references/test-suite-format.md)
- [Ollama](https://ollama.com)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration, JSON, Text]

**Output Format:** [Markdown guidance with YAML examples, shell commands, generated JSON reports, JSONL trend logs, and text alert summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Creates local baseline, report, trend, warning, and alert log files when the bundled scripts are run.]

## Skill Version(s):

1.1.0 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
