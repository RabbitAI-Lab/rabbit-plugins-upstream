## Description: <br>
Beatclaw helps an agent generate instrumental beats with a user-provided Suno API key, publish them on the BeatClaw marketplace, and optionally prepare WAV plus stems sales. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[youngpietro](https://clawhub.ai/user/youngpietro) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent operators use this skill to configure a BeatClaw seller agent, generate instrumental beats through supported Suno providers, manage marketplace listings, and handle optional stem processing. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill gives an agent authority over marketplace listings, API credentials, payment details, and credit-consuming music generation. <br>
Mitigation: Review the BeatClaw service and setup flow before installation; share Suno, MVSEP, PayPal, and owner-email details only when the user trusts BeatClaw to store and use them. <br>
Risk: Beat generation and some stem-processing paths can spend credits from a user-provided third-party API account. <br>
Mitigation: Require explicit user approval before calling generation or paid stem-processing endpoints, and stop on provider or credit errors instead of retrying automatically. <br>
Risk: The artifact describes an update flow that can overwrite the installed SKILL.md from a remote URL. <br>
Mitigation: Do not allow the skill to overwrite local instructions unless the user intentionally approves the update source and understands that the session must restart before the new instructions apply. <br>


## Reference(s): <br>
- [BeatClaw Skill Page](https://clawhub.ai/youngpietro/skills/beatclaw) <br>
- [BeatClaw](https://beatclaw.com) <br>
- [sunoapi.org](https://sunoapi.org) <br>
- [apiframe.pro](https://apiframe.pro) <br>
- [MVSEP User API](https://mvsep.com/user-api) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, API calls, guidance] <br>
**Output Format:** [Markdown guidance with JSON request examples, HTTP endpoint details, and shell command snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires human confirmation before spending third-party credits or deleting marketplace content.] <br>

## Skill Version(s): <br>
1.45.2 (source: server release metadata and artifact text) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
