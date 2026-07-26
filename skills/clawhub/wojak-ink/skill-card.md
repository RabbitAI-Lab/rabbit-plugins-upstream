## Description: <br>
Browse, search, analyze, and track Wojak Farmers Plot NFTs, including floor prices, marketplace listings, rarity estimates, traits, price history, and deal opportunities. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[koba42corp](https://clawhub.ai/user/koba42corp) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
NFT collectors, marketplace participants, and agent users use this skill to answer questions about the Wojak Farmers Plot collection, inspect listings, compare character floors, estimate rarity, track market history, and identify underpriced listings. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill contacts public MintGarden, Dexie, and IPFS image gateway endpoints, so availability and returned market data depend on third-party services. <br>
Mitigation: Use the outputs as market browsing assistance and verify important NFT pricing or listing decisions against the source marketplace. <br>
Risk: The skill can retain local market-history JSON files for price and sales tracking. <br>
Mitigation: Delete the skill data directory when retained history is no longer wanted. <br>
Risk: The release is a third-party Node CLI package. <br>
Mitigation: Review npm dependencies and install only in environments where public marketplace API access and local history files are acceptable. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/koba42corp/skills/wojak-ink) <br>
- [ClawHub publisher profile](https://clawhub.ai/user/koba42corp) <br>
- [Wojak.ink collection site](https://wojak.ink) <br>
- [MintGarden API](https://api.mintgarden.io) <br>
- [Dexie API](https://api.dexie.space/v1) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, guidance] <br>
**Output Format:** [Plain text responses suitable for CLI and chat surfaces, with documentation examples shown as shell commands.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses public MintGarden, Dexie, and IPFS endpoints; caches listings briefly and can retain local JSON market-history files.] <br>

## Skill Version(s): <br>
1.0.0 (source: server-resolved release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
