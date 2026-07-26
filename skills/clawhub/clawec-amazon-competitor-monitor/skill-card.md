## Description: <br>
Queries Amazon competitor data through the ClawEC API by marketplace, brand, seller, ASIN, or keyword, with optional AI interpretation. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[anyunzhong](https://clawhub.ai/user/anyunzhong) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Amazon sellers, ecommerce operators, and agent developers use this skill to submit competitor monitor searches, retrieve result logs and details, and optionally poll for AI-written analysis. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill sends Amazon research inputs and recent search-log lookups to ClawEC using a user-provided API key. <br>
Mitigation: Use a dedicated ClawEC API key, review account permissions and points or costs, and avoid submitting confidential product research unless ClawEC handling is acceptable. <br>
Risk: AI interpretation is asynchronous and may be incomplete, delayed, or unavailable while polling. <br>
Mitigation: Check the returned status, preserve raw competitor data when interpretation fails or times out, and retry later when needed. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/anyunzhong/skills/clawec-amazon-competitor-monitor) <br>
- [ClawEC API base](https://www.clawec.com/api) <br>
- [ClawEC API key page](https://www.clawec.com/api-key?source=q-clawhub) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, API calls, guidance] <br>
**Output Format:** [Markdown guidance with shell command examples and JSON API responses.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include competitor lists, BSR, sales, price, top brands, point usage, status codes, and optional AI analysis.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
