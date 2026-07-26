## Description: <br>
Read and trade on Manifold Markets (search markets, fetch probabilities, inspect users/bets, place bets/sell/comment). Never place a bet/sell/comment without explicit user confirmation. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[crotalus](https://clawhub.ai/user/crotalus) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and external users use this skill to search Manifold markets, inspect public market and user data, and prepare trades or comments. Write actions require an API key and explicit user confirmation before placing bets, selling shares, or posting comments. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Confirmed write actions can affect a Manifold account balance or public activity. <br>
Mitigation: Review every proposed bet, sale, or comment and proceed only after explicit confirmation. <br>
Risk: The MANIFOLD_API_KEY grants account access for write actions if exposed. <br>
Mitigation: Keep MANIFOLD_API_KEY private and provide it only in the intended execution environment. <br>


## Reference(s): <br>
- [Manifold Markets](https://manifold.markets) <br>
- [Manifold API documentation](https://docs.manifold.markets/api) <br>
- [ClawHub skill page](https://clawhub.ai/crotalus/skills/manifold) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown with curl commands and JSON payload examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires curl for API calls and MANIFOLD_API_KEY for write actions.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
