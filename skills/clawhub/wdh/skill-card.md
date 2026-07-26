## Description: <br>
Call WDH.sh paid-per-call CLI utilities for file transfer, URL shortening, chart rendering, hosted markdown pages, QR codes, feature requests, and support tickets using USDC payments on Base mainnet via x402. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[workingdevshero](https://clawhub.ai/user/workingdevshero) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to invoke WDH.sh CLI utilities that create public URLs, rendered images, hosted markdown pages, QR codes, and paid support or feature-request tickets. It is intended for users who have a funded EVM wallet and accept per-call USDC charges on Base mainnet. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Every CLI run signs an x402 payment and may spend USDC from the configured Base wallet. <br>
Mitigation: Use a dedicated low-balance wallet for agent use and review commands before execution. <br>
Risk: Uploads, hosted markdown pages, QR targets, and short links can expose content publicly; short links do not expire by default. <br>
Mitigation: Review content before publishing, set expirations where supported, and avoid uploading secrets or private data. <br>
Risk: Re-running feedback or support commands can create duplicate Linear issues and charge again. <br>
Mitigation: Confirm whether a request has already been submitted before retrying paid feedback or support commands. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/workingdevshero/skills/wdh) <br>
- [Publisher profile](https://clawhub.ai/user/workingdevshero) <br>
- [WDH.sh homepage](https://wdh.sh) <br>
- [WDH.sh service docs](https://wdh.sh/docs) <br>
- [WDH CLI on npm](https://www.npmjs.com/package/@wdhsh/cli) <br>
- [x402 protocol](https://x402.org) <br>
- [chartsplat docs](https://chartsplat.com/docs) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, configuration] <br>
**Output Format:** [Markdown with inline shell commands and command output expectations] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires WDH_WALLET_PRIVATE_KEY; WDH CLI calls may spend USDC and may return public URLs or raw image bytes.] <br>

## Skill Version(s): <br>
0.3.1 (source: SKILL.md frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
