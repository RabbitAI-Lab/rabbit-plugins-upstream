## Description: <br>
Fetch onchain reputation profiles via BaseCred SDK across Ethos, Talent Protocol, and optional Farcaster/Neynar sources for a wallet address. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[callmedas69](https://clawhub.ai/user/callmedas69) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and agent users use BaseCred to check wallet reputation, builder score, creator score, Ethos credibility, and Farcaster account quality for a 0x address. The skill helps summarize multi-source reputation signals, score levels, and profile recency caveats. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The query script sends wallet lookup requests to Ethos, Talent Protocol, and optionally Neynar. <br>
Mitigation: Install only when external reputation lookups are acceptable for the workspace and disclose the queried wallet address to those services. <br>
Risk: The script loads API keys from a workspace .env file and imports basecred-sdk from local node_modules. <br>
Mitigation: Use a workspace .env containing only the needed keys, avoid running from directories with unrelated secrets, and review or pin basecred-sdk before use. <br>


## Reference(s): <br>
- [BaseCred output schema and level tables](references/output-schema.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, JSON, guidance] <br>
**Output Format:** [Markdown guidance with shell command examples and JSON reputation-profile output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires a wallet address, basecred-sdk in the workspace, TALENT_PROTOCOL_API_KEY, and optionally NEYNAR_API_KEY for Farcaster scoring.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
