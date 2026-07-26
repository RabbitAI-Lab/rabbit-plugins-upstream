## Description: <br>
Helps agents audit whether a product or strategy claim has real network effects, estimate critical mass, distinguish imposters such as scale economies and virality, and choose an amplification or defense strategy. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[deciqai](https://clawhub.ai/user/deciqai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Product strategists, founders, investors, and operators use this skill to test network-effect claims in marketplaces, social products, communication tools, platforms, and AI ecosystem moat analyses. It guides an agent through classification, critical-mass estimation, imposter checks, and strategic recommendations. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Real company examples, strategy claims, or failure patterns entered during use may contain sensitive business information. <br>
Mitigation: Avoid entering confidential details unless the agent runtime and storage environment are approved for that information. <br>
Risk: The skill can produce strategic diagnoses that may be wrong if the user supplies incomplete or biased market evidence. <br>
Mitigation: Review the audit against observed user behavior, marketplace liquidity data, and the skill's listed falsifier before relying on the recommendation. <br>


## Reference(s): <br>
- [ClawHub release page](https://clawhub.ai/deciqai/skills/network-effects) <br>
- [Network Effects public page](https://www.deciqai.com/c/network-effects) <br>
- [Network Effects machine-readable metadata](https://www.deciqai.com/s/network-effects.json) <br>
- [Sources](references/sources.md) <br>
- [Theodore Vail at AT&T, 1907-1913 - and Metcalfe's Law, 1980](examples/theodore-vail-at-att-1907-1913-and-metcalfes-law-1980.md) <br>
- [The VHS vs. Betamax Format War](examples/vhs-vs-betamax-format-war.md) <br>
- [Nvidia's CUDA moat and the AI ecosystem (2023-2026)](examples/nvidia-cuda-and-ai-ecosystem-2023-2026.md) <br>
- [Metcalfe's Law After 40 Years of Ethernet](https://doi.org/10.1109/MC.2013.374) <br>
- [Metcalfe's Law is Wrong](https://doi.org/10.1109/MSPEC.2006.1653003) <br>
- [The Network Effects Bible](https://www.nfx.com/post/network-effects-bible) <br>
- [NVIDIA Investor Relations](https://investor.nvidia.com) <br>
- [U.S. Bureau of Industry and Security](https://www.bis.gov) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance] <br>
**Output Format:** [Markdown audit with structured bullets and decision guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May pause for user input in coaching mode before completing the audit.] <br>

## Skill Version(s): <br>
1.0.4 (source: server evidence release.version) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
