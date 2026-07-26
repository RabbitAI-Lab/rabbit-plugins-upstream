## Description: <br>
Embedded Solution recommends embedded hardware options for chip selection, BOM design, vendor comparison, and reference design matching across semiconductor vendors, using official-source verification for component specifications. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[wangp-gh](https://clawhub.ai/user/wangp-gh) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and hardware engineers use this skill to compare embedded parts, design BOMs, and match reference designs for connected devices, wearables, robots, sensors, and power systems. It is intended to return candidate recommendations with comparison tables, source citations, and explicit "not verified" labels when official evidence is missing. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Web or API lookups for datasheets, product pages, mirrors, pricing, or availability may expose hardware requirements to third-party services if those tools are configured. <br>
Mitigation: Use approved lookup tools and API keys only, avoid sending sensitive requirements to third-party services, and prefer bundled or official vendor sources when possible. <br>
Risk: Specs, pricing, stock, and regulatory claims can be stale, incomplete, or unavailable even when a recommendation is well structured. <br>
Mitigation: Independently verify production-critical specifications, pricing, availability, and compliance claims against official vendor or distributor sources before committing a design. <br>
Risk: Catalog entries and fetched pages may have varying verification levels, especially for placeholder, mirror, distributor-only, or marketing-level data. <br>
Mitigation: Treat low-confidence or placeholder fields as incomplete and require datasheet or official product-page cross-checks before using them as design facts. <br>


## Reference(s): <br>
- [Server-resolved GitHub provenance](https://github.com/wangp-gh/embedded-solution) <br>
- [ClawHub skill page](https://clawhub.ai/wangp-gh/skills/embedded-solution) <br>
- [README](README.md) <br>
- [Application Solutions Index](references/application-solution/INDEX.md) <br>
- [Verification Policy](VERIFICATION.md) <br>
- [Evaluation Rubric](references/testing/evaluation-rubric.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Guidance] <br>
**Output Format:** [Markdown with comparison tables, source citations, and verification labels] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include vendor URLs, part candidates, BOM trade-offs, and "not verified" markers for unsupported specifications.] <br>

## Skill Version(s): <br>
0.1.3 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
