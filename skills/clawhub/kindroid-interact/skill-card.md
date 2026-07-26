## Description: <br>
Interact with Kindroid companions via their official API. Send messages, handle chat breaks, and manage multi-bot conversations. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[lumenlemons](https://clawhub.ai/user/lumenlemons) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
External users and developers use this skill to let an agent send messages, initiate chat breaks, and check companion status for Kindroid AI companions through the official API. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill uses a Kindroid API key and can send messages or perform chat breaks on the user's Kindroid account. <br>
Mitigation: Use a revocable API key, keep the credentials file permission-restricted, and install only when account-level messaging actions are acceptable. <br>
Risk: Chat text may be sent to the Kindroid API. <br>
Mitigation: Avoid including secrets or sensitive data in messages sent through the skill. <br>
Risk: Incorrect command paths could cause the agent to run a different local package than intended. <br>
Mitigation: Verify package paths if commands do not run as documented. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/lumenlemons/skills/kindroid-interact) <br>
- [Kindroid homepage](https://kindroid.ai) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell commands and JSON configuration examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires curl and jq; uses a local Kindroid credentials file and HTTPS API calls.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata, SKILL.md frontmatter, package.json) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
