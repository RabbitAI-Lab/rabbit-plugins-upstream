## Description:

This skill helps operators inventory and govern local LLMs, scan prompts for sensitive content, enforce model policies, and review usage and model drift.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use the skill to inspect single-endpoint local LLM deployments, detect unapproved models or digest changes, scan prompts, and apply model policy. It supports Ollama, llama.cpp, LM Studio, and single-node vLLM workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The installer metadata names a different software project, creating a risk of installing an unintended package.

Mitigation: Resolve and verify the installer package identity before installing this release.

Risk: Agent access does not enforce approval for model deletion or policy changes.

Mitigation: Start with read-only tools, require explicit approval for deletion and policy changes, and restrict writes at the API boundary.

Risk: Requests sent directly to a model runtime bypass the prompt guard.

Mitigation: Route prompts through the guarded calls when prompt scanning and policy checks are required.

Risk: Re-downloading a deleted model may return different weights.

Mitigation: Check the restored model against its pinned digest before relying on it.

## Reference(s):

- [AI Guardian release on ClawHub](https://clawhub.ai/zw008/skills/ai-guardian)
- [AI Guardian project homepage](https://github.com/AIops-tools/AI-Guardian)
- [Capabilities](artifact/references/capabilities.md)
- [Setup and security guide](artifact/references/setup-guide.md)
- [CLI reference](artifact/references/cli-reference.md)

## Skill Output:

**Output Type(s):** [Analysis, Guidance, Configuration, Shell commands]

**Output Format:** [Text and Markdown, including structured findings and configuration guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include model inventory, prompt risk findings, usage summaries, and policy or lifecycle recommendations.]

## Skill Version(s):

0.14.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
