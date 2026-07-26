## Description: <br>
Signalis helps agents retrieve global intelligence digests and AI-business narrative tracking through free discovery endpoints and paid x402 API calls. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[jcislo](https://clawhub.ai/user/jcislo) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and external agents use this skill to integrate Signalis API endpoints for current intelligence digests, historical digests, active AI-business narratives, and paid x402 request flows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Paid endpoints can spend USDC on Base through x402 when automated requests are enabled. <br>
Mitigation: Use a narrowly funded wallet, protect private keys in environment variables, and verify route prices before enabling unattended paid calls. <br>
Risk: The API returns public-data intelligence and LLM-synthesized narrative analysis that may be incomplete or stale. <br>
Mitigation: Check response createdAt provenance, use free sample and latest endpoints to inspect response shape and freshness, and treat outputs as informational rather than authoritative decisions. <br>


## Reference(s): <br>
- [ClawHub Signalis release](https://clawhub.ai/jcislo/skills/signalis) <br>
- [Signalis homepage](https://signalis.dev) <br>
- [Signalis API](https://api.signalis.dev) <br>
- [Signalis OpenAPI specification](https://api.signalis.dev/openapi.json) <br>
- [Signalis x402 payment manifest](https://api.signalis.dev/.well-known/x402) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, code, configuration] <br>
**Output Format:** [Markdown with endpoint tables, curl commands, and TypeScript examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Documents free and paid API routes, rate limits, x402 payment flow, Base Mainnet USDC settlement, and response-shape discovery links.] <br>

## Skill Version(s): <br>
1.0.0 (source: evidence.release.version and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
