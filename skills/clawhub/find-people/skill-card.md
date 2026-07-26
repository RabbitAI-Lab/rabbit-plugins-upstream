## Description: <br>
Find People (x402) helps agents run paid OSINT-style research on individuals for professional background, career timeline, due diligence, competitive intelligence, investor research, and credential-checking workflows. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[tzannetosgiannis](https://clawhub.ai/user/tzannetosgiannis) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers, analysts, recruiters, journalists, and business users can use this skill to request people-focused public-information research, including professional backgrounds, career timelines, credentials, leadership history, and due diligence context. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill asks for a wallet private key and passes it to external code fetched at runtime. <br>
Mitigation: Install only if the external npm package and research provider are trusted; use a dedicated low-balance wallet and avoid storing valuable private keys in project directories or shell history. <br>
Risk: Each lookup is a paid request that can spend USDC on the Base network. <br>
Mitigation: Confirm each paid lookup before execution and keep only the funds needed for expected requests in the configured wallet. <br>
Risk: People-search reports can contain incomplete, outdated, sensitive, or unverified personal data. <br>
Mitigation: Use the skill only for lawful and ethical purposes, verify important claims against primary sources, and do not use it for stalking, doxxing, discrimination, or consequential decisions based on unverified data. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/tzannetosgiannis/skills/find-people) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell commands and text research reports] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires a person query and a configured x402 wallet private key; each lookup costs $0.15 USDC on the Base network.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
