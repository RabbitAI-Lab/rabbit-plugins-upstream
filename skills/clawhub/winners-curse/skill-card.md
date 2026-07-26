## Description: <br>
Guides agents in applying winner's curse reasoning to common-value auctions and competitive bids by classifying value, conditioning estimates on winning, and setting pre-committed walk-away ceilings. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[deciqai](https://clawhub.ai/user/deciqai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Employees, external users, and agents use this skill when evaluating auctions, acquisitions, competitive bids, ad auctions, or other common-value contests where winning can signal over-optimism. It helps produce a curse-corrected bid ceiling or bid floor, escalation checks, and concise decision-support guidance. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Users may treat bidding or auction guidance as professional financial or legal advice. <br>
Mitigation: Use outputs as decision support and verify major bids with the user's own data, advisors, and approval process. <br>
Risk: The winner's curse frame can be misapplied to private-value transactions, single-buyer negotiations, or cases where value is known with near-certainty. <br>
Mitigation: First classify whether the value is common and uncertain; if those conditions fail, do not apply a winner's-curse bid shade. <br>
Risk: Auction fever, sunk costs, or competitive pressure can override the recommended walk-away ceiling. <br>
Mitigation: Set the value-conditioned ceiling or floor before live bidding and reopen it only when new information changes the underlying value. <br>


## Reference(s): <br>
- [Winner's Curse sources](references/sources.md) <br>
- [Competitive Bidding in High-Risk Situations](https://onepetro.org/JPT/article/23/06/641/163651/Competitive-Bidding-in-High-Risk-Situations) <br>
- [Anomalies: The Winner's Curse](https://www.aeaweb.org/articles?id=10.1257/jep.2.1.191) <br>
- [Naturally Occurring Markets and Exogenous Laboratory Experiments: A Case Study of the Winner's Curse](https://ideas.repec.org/a/ecj/econjl/v118y2008i528p822-843.html) <br>
- [Common Value Auctions and the Winner's Curse](https://press.princeton.edu/books/ebook/9781400830138/common-value-auctions-and-the-winners-curse) <br>
- [A Theory of Auctions and Competitive Bidding](https://doi.org/10.2307/1911865) <br>
- [Winner's Curse ClawHub page](https://clawhub.ai/deciqai/skills/winners-curse) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Markdown, Text] <br>
**Output Format:** [Markdown coaching response or bid discipline card] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Decision-support output only; no executable behavior or hidden access requests.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
