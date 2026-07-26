## Description: <br>
Provides read-only Twitter/X research through SELAT for profiles, recent tweets, mentions, followers, tweet details, replies, retweeters, topic search, and trends. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[selat](https://clawhub.ai/user/selat) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to answer focused Twitter/X research questions by selecting read-only SELAT endpoints, dry-running prices, and summarizing returned public data in plain language. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Paid Twitter/X reads can spend USDC from the user's Circle Agent Wallet. <br>
Mitigation: Run the free dry run first, show the live quoted prices, and get explicit user approval before wallet setup or any paid run. <br>
Risk: The skill depends on an external SELAT CLI, router, and payment flow. <br>
Mitigation: Proceed only if the user trusts the SELAT CLI and payment flow, and never ask for or handle private keys. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/selat/skills/twitter-research) <br>
- [SELAT twitter-research homepage](https://github.com/SELAT-AI/selat-skills/tree/main/skills/twitter-research) <br>
- [SELAT skills documentation](https://github.com/SELAT-AI/selat-skills) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, guidance] <br>
**Output Format:** [Markdown or plain text with inline shell commands and concise research summaries.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include SELAT-reported dollar cost; raw JSON and endpoint URLs should not be relayed.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
