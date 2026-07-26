## Description: <br>
Scan Reddit for trending stocks and sentiment spikes using the ApeWisdom API (free). Use this to find "meme stocks", retail momentum, and sentiment shifts on r/wallstreetbets. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[stuhorsman](https://clawhub.ai/user/stuhorsman) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers, analysts, and market-monitoring users use this skill to fetch live ApeWisdom sentiment data and identify trending tickers, mention spikes, and subreddit-specific market chatter. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill contacts ApeWisdom to retrieve live market-sentiment data. <br>
Mitigation: Install and run it only in environments where outbound access to ApeWisdom is acceptable. <br>
Risk: Trending ticker and sentiment output can be mistaken for investment advice. <br>
Mitigation: Treat the results as informational sentiment data and verify decisions against independent financial analysis. <br>
Risk: The Python script requires the requests dependency. <br>
Mitigation: Confirm the Python environment includes requests before relying on the skill. <br>


## Reference(s): <br>
- [ApeWisdom API filter endpoint](https://apewisdom.io/api/v1.0/filter) <br>
- [ClawHub skill page](https://clawhub.ai/stuhorsman/skills/apewisdom) <br>


## Skill Output: <br>
**Output Type(s):** [text, JSON, shell commands, guidance] <br>
**Output Format:** [JSON printed by a Python command, with Markdown usage guidance in the skill instructions] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Results include rank, ticker, name, mentions, upvotes, previous 24-hour mentions, and calculated percentage change.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
