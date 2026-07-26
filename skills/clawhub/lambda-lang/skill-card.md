## Description: <br>
Lambda Lang is a native agent-to-agent language for compact, machine-oriented messages covering general concepts, code, evolution, agent communication, emotions, and social domains. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[swaylq](https://clawhub.ai/user/swaylq) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and agent builders use Lambda Lang to parse, encode, and reference compact agent-to-agent messages, including A2A and evolution-domain signals, compact logs, and vocabulary lookups. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Lambda messages can be opaque to humans and may be unsuitable for user-facing communication or exact natural-language contexts. <br>
Mitigation: Keep user-facing output in normal language unless Lambda is requested, and log or translate Lambda messages before acting on them. <br>
Risk: Untrusted external vocabularies or Pilot Protocol messages could change meaning or lead an agent to act on misleading compact signals. <br>
Mitigation: Only accept external vocabularies and Pilot Protocol messages from trusted, reviewed sources. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/swaylq/skills/lambda-lang) <br>
- [Agent Quick Reference](artifact/SKILL.md) <br>
- [Lambda Lang README](artifact/README.md) <br>
- [Core Specification](artifact/spec/v0.1-core.md) <br>
- [Stable Specification](artifact/spec/v1.0-stable.md) <br>
- [Atoms Dictionary](artifact/src/atoms.json) <br>
- [Compression Experiments](artifact/docs/compression-experiments.md) <br>
- [Pilot Protocol Integration](artifact/docs/pilot-integration.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown, plain text translations, code snippets, shell commands, and JSON vocabulary data] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs should remain in normal language for user-facing responses unless Lambda is explicitly requested.] <br>

## Skill Version(s): <br>
2.0.0 (source: server release evidence, target metadata, README status, and atoms.json) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
