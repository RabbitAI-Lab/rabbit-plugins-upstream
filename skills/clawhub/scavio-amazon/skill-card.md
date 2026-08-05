## Description: <br>
Search Amazon, read full product details by ASIN, and list seller offers with buy-box status as normalized JSON including price, rating, review count, availability, shipping, and sellers across 22 marketplaces. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[scavio-ai](https://clawhub.ai/user/scavio-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent builders use this skill to fetch Amazon search results, ASIN detail, and seller-offer data from Scavio for product research, competitor monitoring, price checks, and marketplace comparison. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Product searches and ASIN lookups are sent to Scavio and most data endpoints bill API credits. <br>
Mitigation: Use the skill only when sharing shopping research with Scavio is acceptable, and warn users before deep pagination or bulk product lookups. <br>
Risk: Invalid marketplace codes can return plausible results from the wrong storefront. <br>
Mitigation: Validate country codes against the documented marketplace list or the free options endpoint before making paid data calls. <br>
Risk: Search result counts, review counts, prices, availability, and delivery estimates can be rounded or point-in-time. <br>
Mitigation: Report unavailable fields honestly, distinguish locally sorted pages from Amazon ranking, and avoid presenting search-derived or point-in-time values as stable facts. <br>


## Reference(s): <br>
- [Scavio Amazon API documentation](https://scavio.dev/docs/amazon-api) <br>
- [ClawHub skill page](https://clawhub.ai/scavio-ai/skills/scavio-amazon) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Code, JSON] <br>
**Output Format:** [Markdown guidance with bash and Python examples plus JSON API response shapes] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires SCAVIO_API_KEY; search, product, and offers calls generally consume one Scavio API credit each.] <br>

## Skill Version(s): <br>
3.0.1 (source: frontmatter and release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
