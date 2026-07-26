## Description: <br>
Search Google Maps for local businesses and places, fetch full place details, and read place reviews as structured JSON. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[scavio-ai](https://clawhub.ai/user/scavio-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, developers, and agents use this skill to search for places, retrieve place details, and read reviews from Google Maps through Scavio. It is suited for local business discovery, lead list building, and enrichment workflows that need structured place data. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Map searches, precise coordinates, place IDs, and review requests are sent to Scavio using the user's API key. <br>
Mitigation: Avoid sending sensitive location intent unless the user is comfortable with Scavio handling it. <br>
Risk: Each Google Maps endpoint call consumes Scavio credits, and pagination can multiply usage. <br>
Mitigation: Tell the user before paginating through many pages and keep requests scoped to the needed places or reviews. <br>
Risk: Place names, ratings, addresses, coordinates, and reviews may be used in user-facing decisions. <br>
Mitigation: Return only API-provided data and do not fabricate missing map or review details. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/scavio-ai/skills/scavio-google-maps) <br>
- [Scavio Google Maps documentation](https://scavio.dev/docs/google-maps) <br>
- [Scavio rate limits](https://scavio.dev/docs/rate-limits) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, markdown, code, shell commands, configuration, JSON] <br>
**Output Format:** [Markdown guidance with inline shell commands, code examples, and structured JSON API responses] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires SCAVIO_API_KEY; each documented Google Maps request consumes 1 Scavio credit.] <br>

## Skill Version(s): <br>
1.0.0 (source: frontmatter and release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
