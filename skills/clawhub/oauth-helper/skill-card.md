## Description: <br>
Automates OAuth login flows with Telegram-based user confirmation across Google, Apple, Microsoft, GitHub, Discord, WeChat, and QQ. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[helloliuyongsheng-bot](https://clawhub.ai/user/helloliuyongsheng-bot) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External users and developers use this skill to let an agent detect OAuth login options, request confirmation through Telegram, and complete provider-specific login or consent steps in a browser. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill automates login and OAuth consent pages while using Telegram for authentication-related confirmations. <br>
Mitigation: Use a dedicated browser profile or test accounts where possible, and avoid sensitive personal or business accounts unless Telegram exposure is acceptable. <br>
Risk: A mistaken confirmation can authorize an unintended relying party or scope request. <br>
Mitigation: Verify the relying party, OAuth provider, and requested scopes before approving any login or consent step. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/helloliuyongsheng-bot/skills/oauth-helper) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown instructions with browser-action examples and Telegram confirmation prompts] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes provider detection patterns, click sequences, one-time setup steps, and error-handling guidance.] <br>

## Skill Version(s): <br>
1.1.0 (source: ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
