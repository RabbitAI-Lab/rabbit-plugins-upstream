## Description: <br>
Finds Amazon products that compete in the same Jiimore niche segments as a reference ASIN, with filters for conversion, clicks, sales, reviews, ratings, price, FBA fees, and gross margin. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[linkfox-ai](https://clawhub.ai/user/linkfox-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External Amazon sellers and ecommerce analysts use this skill to query LinkFox Jiimore data for same-niche competing ASINs in the US, JP, and DE marketplaces, then filter and compare products by conversion, traffic, sales, reviews, price, fees, and margin. <br>

### Deployment Geography for Use: <br>
Global; marketplace queries are limited to US, JP, and DE Amazon data. <br>

## Known Risks and Mitigations: <br>
Risk: ASIN query data, the LinkFox API key, and optional session metadata are sent to LinkFox services. <br>
Mitigation: Use a scoped API key, avoid submitting sensitive proprietary context, and review the request parameters before execution. <br>
Risk: LINKFOX_TOOL_GATEWAY can redirect API traffic if set. <br>
Mitigation: Keep LINKFOX_TOOL_GATEWAY unset unless the destination is controlled and trusted. <br>
Risk: Full API responses are saved locally under a linkfox directory that may be outside the current project when fallback paths are used. <br>
Mitigation: Run the skill from the intended writable workspace and handle saved result files as sensitive business data. <br>
Risk: Repeated or high-frequency calls consume LinkFox credits. <br>
Mitigation: Tell users about credit cost before repeated retrievals and rely on the built-in cache when repeating the same parameter set. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-jiimore-page-asins-by-asin) <br>
- [Jiimore ASIN product mining API reference](artifact/references/api.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with JSON request parameters, shell commands, and saved JSON response files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [The script writes full API responses under a local linkfox data directory, prints small responses inline, summarizes larger responses, and uses a 24-hour local cache by default.] <br>

## Skill Version(s): <br>
1.0.4 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
