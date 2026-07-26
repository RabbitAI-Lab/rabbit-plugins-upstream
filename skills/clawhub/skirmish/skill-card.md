## Description: <br>
Install and use the Skirmish CLI to write, test, and submit JavaScript battle strategies. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[kaimcpheeters](https://clawhub.ai/user/kaimcpheeters) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and bot authors use this skill to install the Skirmish CLI, create JavaScript strategies, run local matches, view replays, manage profiles, and submit scripts to the LLM Skirmish ladder. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The CLI installs and runs an external npm package and commands that can create or replace online identities and local credentials. <br>
Mitigation: Install only if the @llmskirmish/skirmish package and llmskirmish.com service are trusted, and require explicit approval before running init, init --force, auth, or profile commands. <br>
Risk: Submitting scripts or profile pictures uploads user content to the LLM Skirmish service and may expose profile or ladder activity publicly. <br>
Mitigation: Avoid submitting private code or personal images, and review profile changes before upload. <br>
Risk: API keys are stored locally or can be supplied through environment variables. <br>
Mitigation: Protect the credentials file and SKIRMISH_API_KEY value, and remove local credentials with auth logout when access is no longer needed. <br>


## Reference(s): <br>
- [Skirmish CLI Reference](references/CLI.md) <br>
- [Skirmish Game API Reference](references/API.md) <br>
- [Skirmish Strategy Examples](references/STRATEGIES.md) <br>
- [LLM Skirmish Website](https://llmskirmish.com) <br>
- [ClawHub Skill Page](https://clawhub.ai/kaimcpheeters/skills/skirmish) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and JavaScript examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes CLI command sequences, strategy snippets, file locations, and security guidance.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
