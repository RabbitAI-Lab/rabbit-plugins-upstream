## Description: <br>
Agent Registry helps Claude Code discover, search, and load specialized agents on demand instead of loading every available agent into context up front. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[matrixy](https://clawhub.ai/user/matrixy) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and Claude Code users use this skill to maintain a searchable local registry of agents, migrate selected agents into that registry, and load relevant agent instructions only when a task calls for them. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The installed UserPromptSubmit hook locally checks prompts against the agent registry and may add matching-agent suggestions to context. <br>
Mitigation: Install the skill only when automatic local agent discovery is desired, and review hook behavior before deployment. <br>
Risk: Opt-in telemetry can send anonymous usage events when AGENT_REGISTRY_TELEMETRY is enabled. <br>
Mitigation: Leave AGENT_REGISTRY_TELEMETRY unset, or set DO_NOT_TRACK or AGENT_REGISTRY_NO_TELEMETRY, when telemetry is not wanted. <br>
Risk: Agent migration can relocate source agent files if the explicit --move option is used. <br>
Mitigation: Use the default copy migration first, and run --move only when source file relocation is intentional. <br>


## Reference(s): <br>
- [ClawHub Agent Registry skill page](https://clawhub.ai/matrixy/skills/agent-registry) <br>
- [Agent Registry README](README.md) <br>
- [Agent Registry v2.0.1 release notes](docs/releases/v2.0.1.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown and command-line text, with JSON additionalContext from the prompt hook when matches are found] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Search results include agent names, summaries, relevance scores, and optional full agent instructions loaded from the local registry.] <br>

## Skill Version(s): <br>
2.0.1 (source: SKILL.md frontmatter, package.json, docs/releases/v2.0.1.md, and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
