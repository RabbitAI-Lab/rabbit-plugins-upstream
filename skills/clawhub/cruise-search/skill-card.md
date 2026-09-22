## Description:

Cruise-search helps agents search and recommend cruise itineraries, retrieve Tuniu-backed product details, compare cabin options, and summarize ship facilities.

This skill is ready for commercial/non-commercial use.

## Publisher:

[travel-skills](https://clawhub.ai/user/travel-skills)

### License/Terms of Use:

MIT-0

## Use Case:

External travel users and agents use this skill to find cruise routes, compare prices and cabin details, review product policies, inspect ship amenities, and open Tuniu booking links.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Cruise search details, product IDs, and travel preferences are sent to the configured Tuniu proxy service.

Mitigation: Install and use the skill only when this data sharing is acceptable for the user and deployment context.

Risk: The proxy token is a secret used to authenticate requests.

Mitigation: Store PROXY_TOKEN as a secret, avoid exposing it in prompts or logs, and rotate it if disclosure is suspected.

Risk: Using an unintended proxy endpoint could send travel queries to the wrong service.

Mitigation: Verify PROXY_URL points to the intended Tencent SCF endpoint before use.

Risk: Cruise prices, availability, policies, and booking links may change after the skill returns results.

Mitigation: Confirm final price, cabin availability, cancellation terms, and booking details on Tuniu before purchase.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/travel-skills/skills/cruise-search)
- [Tuniu cruise booking pages](https://m.tuniu.com/cruise/)
- [Configured Tencent SCF proxy host](https://1439498936-0junm3maxj.ap-guangzhou.tencentscf.com)

## Skill Output:

**Output Type(s):** [Markdown, JSON, API Calls, Guidance]

**Output Format:** [Markdown summaries or JSON objects containing cruise search results, recommendations, product details, cabin data, ship information, errors, and booking links.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results depend on PROXY_URL and PROXY_TOKEN, call a Tuniu-backed proxy service, and may include live prices, images, satisfaction scores, policy excerpts, and external booking links.]

## Skill Version(s):

1.0.19 (source: server release metadata; artifact frontmatter reports 3.0.1)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
