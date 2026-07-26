## Description: <br>
Recommends benchmark and top Douyin accounts for a supplied Douyin nickname or account ID, using RedFox API data to return account metrics, comparison tables, commonalities, differences, and optimization suggestions. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[redfox-data](https://clawhub.ai/user/redfox-data) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Douyin creators, content operators, MCN teams, and brand marketing teams use this skill to find comparable accounts, evaluate top accounts in a niche, and turn RedFox account metrics into growth, topic, and placement guidance. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Persistent API-key storage or readback can expose a RedFox API key beyond the current session. <br>
Mitigation: Use a scoped, revocable RedFox API key stored in a platform secret store or temporary session environment, and avoid writing the key to shell profile files. <br>
Risk: The account collection flow submits a Douyin account ID to RedFox for later processing. <br>
Mitigation: Run the sync flow only after the user explicitly approves submitting that account ID for collection. <br>
Risk: Subscription and push prompts can create follow-up notifications or service commitments without clear user intent. <br>
Mitigation: Treat subscription setup as a separate opt-in step and confirm frequency, timing, and cancellation expectations before enabling it. <br>
Risk: RedFox account data may be stale, incomplete, or unsuitable as the only basis for commercial decisions. <br>
Mitigation: Check the reported data timestamp and validate important placement or growth decisions against additional sources before acting. <br>


## Reference(s): <br>
- [Core workflow](artifact/references/core_workflow.md) <br>
- [RedFox API key settings](https://redfox.hk/settings/api-keys?source=clawhub) <br>
- [RedFox data platform](https://redfox.hk/) <br>
- [ClawHub skill page](https://clawhub.ai/redfox-data/skills/douyin-similar-account) <br>


## Skill Output: <br>
**Output Type(s):** [markdown, text, shell commands, guidance] <br>
**Output Format:** [Markdown report with account summaries, comparison tables, analysis notes, and operational prompts.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires a RedFox API key and may call RedFox endpoints for account lookup, account collection, and subscription-related flows.] <br>

## Skill Version(s): <br>
1.0.1 (source: release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
