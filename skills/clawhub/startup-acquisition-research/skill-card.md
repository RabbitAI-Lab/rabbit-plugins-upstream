## Description:

Screen startups listed for sale using Crawlora's TrustMRR marketplace, stored company records, and daily metric history.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tonywangcn](https://clawhub.ai/user/tonywangcn)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to screen startup acquisition candidates, compare asking prices and revenue history, and turn evidence gaps into diligence questions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The bundled helper honors CRAWLORA_API_BASE, so an unsafe override could receive the user's Crawlora API key.

Mitigation: Run it only in a trusted environment, leave CRAWLORA_API_BASE unset for normal use, and verify the API base before sending credentials.

Risk: The helper is broader than the acquisition workflow and can send user-provided request bodies to Crawlora endpoints.

Mitigation: Use only the endpoints needed for the workflow and avoid including unrelated sensitive data in request bodies.

Risk: Revenue metrics, seller claims, AI summaries, and asking prices can be mistaken for audited financials or investment recommendations.

Mitigation: Separate each evidence type, label calculations explicitly, and present open diligence questions instead of acquisition advice.

## Reference(s):

- [Endpoint reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [TrustMRR FAQ](https://trustmrr.com/faq)
- [ClawHub skill page](https://clawhub.ai/tonywangcn/skills/startup-acquisition-research)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown candidate table with source links, dated metrics, labeled calculations, discrepancies, and diligence questions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include Crawlora REST helper commands; research output does not place offers or contact sellers.]

## Skill Version(s):

1.0.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
