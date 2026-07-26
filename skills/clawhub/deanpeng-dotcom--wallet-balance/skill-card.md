## Description: <br>
Checks multi-chain wallet balances across EVM, supported non-EVM, and Bitcoin addresses, with address memory and language-matched replies. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[deanpeng-dotcom](https://clawhub.ai/user/deanpeng-dotcom) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and agents use this skill to look up wallet holdings, total USD value, and token-level balance tables for supported blockchain addresses. It can also reuse saved addresses for later balance checks when the user asks without providing a new address. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Saved wallet addresses may reveal sensitive financial relationships and can be listed, changed, or reused through unauthenticated local endpoints. <br>
Mitigation: Install only in environments where address memory is acceptable; bind the gateway to localhost or place it behind access controls, avoid shared hosts, review or clear memory regularly, and do not save sensitive addresses. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/deanpeng-dotcom/wallet-balance) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, guidance] <br>
**Output Format:** [Localized natural language with Markdown balance tables and concise command guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Redacts wallet addresses in user-visible replies and localizes prompts, totals, table headers, confirmations, and errors.] <br>

## Skill Version(s): <br>
1.4.1 (source: evidence release and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
