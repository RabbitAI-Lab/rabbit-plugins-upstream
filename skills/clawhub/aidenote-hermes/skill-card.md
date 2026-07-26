## Description: <br>
Pairs AideNote with Hermes, installs the local connection suite, and lets the agent query real AideNote recordings, transcripts, summaries, todos, knowledge bases, account status, and mobile bridge health. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ajingmiao](https://clawhub.ai/user/ajingmiao) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Hermes users use this skill to connect AideNote on their computer and mobile app, then retrieve authenticated AideNote recording notes, transcripts, summaries, extracted action items, and knowledge-base contents through explicit commands. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can query sensitive AideNote recordings, transcripts, summaries, todos, knowledge bases, and account data on broad productivity prompts. <br>
Mitigation: Install only when the user intends Hermes or OpenClaw to access that AideNote data; require successful AideNote command results before answering data questions and do not treat failures as empty accounts. <br>
Risk: Authorized install or repair commands can configure persistent local services and bridge settings. <br>
Mitigation: Run install or repair commands only after explicit user consent, keep checksum verification intact, and use read-only status checks when consent is absent. <br>
Risk: AideNote credentials and local bridge tokens are sensitive secrets. <br>
Mitigation: Use the pairing flow or local recovery tooling instead of asking users to paste keys into chat, and do not print environment variables, authorization headers, access tokens, or configuration files. <br>


## Reference(s): <br>
- [AideNote API contract](references/api-contract.md) <br>
- [AideNote mobile WorkBuddy skill guide](https://www.aidenote.cn/mobile/workbuddy-skill-guide.html) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration guidance, JSON] <br>
**Output Format:** [Markdown guidance with inline bash commands and summarized JSON command results] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Commands emit JSON; the skill instructs the agent to summarize results and avoid exposing credentials unless raw JSON is explicitly requested.] <br>

## Skill Version(s): <br>
1.2.9 (source: evidence.release.version and metadata.hermes.version) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
