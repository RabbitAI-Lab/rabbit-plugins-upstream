## Description: <br>
Create and manage Privacy.com virtual cards, including single-use and merchant-locked cards, spending limits, card state changes, and transaction lookups via the Privacy.com API. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[johnielee](https://clawhub.ai/user/johnielee) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and operators use this skill to generate and manage Privacy.com virtual cards, set spending controls, pause or close cards, and inspect card transactions from an agent workflow. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill enables sensitive financial card actions, including creating cards, changing spend limits, and permanently closing cards. <br>
Mitigation: Review before installing, use the sandbox where possible, and require explicit confirmation before creating, updating, pausing, or closing cards. <br>
Risk: Card tokens, full card numbers, CVVs, expiry values, transaction details, and API keys may be exposed in chats, logs, terminal history, or shared files. <br>
Mitigation: Keep the API key least-privileged and avoid displaying or storing sensitive card data or credentials in shared agent output. <br>
Risk: A mistaken destructive operation can close the wrong card or close a card when reversible suspension would be sufficient. <br>
Mitigation: Verify the exact card token before destructive actions and prefer pausing over closing when temporary suspension meets the need. <br>


## Reference(s): <br>
- [Privacy.com API Reference](references/api.md) <br>
- [Privacy.com](https://privacy.com) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown with inline bash commands, tables, and JSON examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires a Privacy.com API key and supports production or sandbox API endpoints.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
