## Description: <br>
Search Google Shopping for products, fetch a full product page, and page through every store selling a product as structured JSON, including price, seller, rating, and price or sale filters. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[scavio-ai](https://clawhub.ai/user/scavio-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External developers and agents use this skill to search Google Shopping, compare products across retailers, fetch product details, and page through store offers through Scavio's API. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Endpoint calls consume Scavio credits, and broad store pagination can increase usage. <br>
Mitigation: Confirm the user wants additional pagination before paging through many stores, and make credit use explicit. <br>
Risk: The skill requires a Scavio API key. <br>
Mitigation: Read the key from SCAVIO_API_KEY and do not print, log, or embed the secret in generated code or responses. <br>
Risk: Shopping results, prices, sellers, ratings, and availability may change or be incomplete. <br>
Mitigation: Return only data from the Scavio API, avoid fabricating product details, and preserve displayed price strings while using extracted_price only for numeric comparisons. <br>


## Reference(s): <br>
- [Scavio Google Shopping Documentation](https://scavio.dev/docs/google-shopping) <br>
- [Scavio Rate Limits](https://scavio.dev/docs/rate-limits) <br>
- [ClawHub Skill Page](https://clawhub.ai/scavio-ai/skills/scavio-google-shopping) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, markdown, code, shell commands, configuration, json] <br>
**Output Format:** [Markdown guidance with inline shell and Python examples plus structured JSON API responses] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires SCAVIO_API_KEY and consumes 1 Scavio credit per endpoint request.] <br>

## Skill Version(s): <br>
1.0.0 (source: frontmatter and release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
