## Description:

Verify an LLM API endpoint for model authenticity, billing inflation, relay provenance, performance, and silent downgrades.

This skill is ready for commercial/non-commercial use.

## Publisher:

[asale-ai](https://clawhub.ai/user/asale-ai)

### License/Terms of Use:

Apache-2.0

## Use Case:

Developers, engineers, and AI tool users use this skill to check whether an LLM endpoint matches the claimed model, billing, relay or proxy path, latency behavior, and downgrade status before relying on it or using it as a CI gate.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Remote shell or PowerShell install commands can execute fetched code before review.

Mitigation: Install through ClawHub or inspect and verify the fetched installer source before running it.

Risk: The default installer can modify every detected AI coding tool.

Mitigation: Prefer a scoped or project-local install target when evaluating or deploying the skill.

Risk: Endpoint verification exercises the supplied API credential against the selected endpoint.

Mitigation: Use only the endpoint intended for testing and prefer a temporary or limited API key.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/asale-ai/skills/llm-verify)
- [README](README.md)
- [Skill Definition](SKILL.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration guidance]

**Output Format:** [Markdown guidance with shell commands, verdict summaries, and optional JSON or HTML report paths]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include exit-code interpretation and confidence caveats for probes that were skipped or inconclusive.]

## Skill Version(s):

0.2.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
