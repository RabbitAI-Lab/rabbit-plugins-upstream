## Description: <br>
Trades World Cup 2026 knockout-stage player fantasy-score markets on propSPACE by building a multimodal belief from FunctionSpace projections and optional sentiment enrichment, then selecting trades when belief diverges from consensus. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[bridgeaisocial](https://clawhub.ai/user/bridgeaisocial) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External developers and trading-agent operators use this skill to inspect propSPACE World Cup knockout player markets, rank one FWD, MID, and DEF by modeled edge, and optionally place play-money competition trades. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill logs in to propSPACE, can create or use an account, and stores a bearer token locally. <br>
Mitigation: Set a strong FS_PASSWORD, protect the local .auth token file, and delete it after use on shared systems. <br>
Risk: Passing --live places mutating propSPACE play-money competition trades. <br>
Mitigation: Run dry-run, list, and inspect modes first; use --live only after reviewing selected markets and collateral settings. <br>
Risk: The optional Brave enrichment path uses an API key and security guidance warns against shared logs until key-prefix printing is removed. <br>
Mitigation: Avoid running the enrichment script in shared logs and rotate any API key that may have been exposed. <br>
Risk: Trading outcomes depend on market mechanics, data freshness, and high-variance player fantasy scores. <br>
Mitigation: Refresh player data before each round, inspect representative markets, and treat modeled edges as uncertain. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/bridgeaisocial/skills/fs-worldcup-knockout) <br>
- [bridgeaisocial Publisher Profile](https://clawhub.ai/user/bridgeaisocial) <br>
- [propSPACE Campaign Site](https://propspace.fun) <br>
- [propSPACE App Signup](https://app.propspace.fun) <br>
- [FunctionSpace Competition Engine](https://fs-engine-api-mech-v0-4.onrender.com) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Terminal text and Markdown documentation with inline shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Dry-run output is non-mutating; live mode can place propSPACE play-money trades.] <br>

## Skill Version(s): <br>
0.1.5 (source: release evidence and skill frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
