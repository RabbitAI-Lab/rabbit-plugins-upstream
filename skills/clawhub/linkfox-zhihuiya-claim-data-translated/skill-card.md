## Description:

Retrieves translated patent claim text from the Zhihuiya/PatSnap patent database in Chinese, English, or Japanese by patent ID or publication number.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and patent researchers use this skill to retrieve translated patent claim text for known patents in Chinese, English, or Japanese. It supports single or batch lookups by patent ID or publication number, with optional family-patent substitution when claims are unavailable.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends patent identifiers and request context to LinkFox/PatSnap services and uses credential-bearing network calls.

Mitigation: Use only for patent queries that may be shared with those services, and keep API keys limited to trusted environments.

Risk: Lookups consume paid credits and batch requests can multiply cost.

Mitigation: Confirm cost-sensitive requests with the user before running broad or repeated queries, and reuse cached results when appropriate.

Risk: Full API responses are persisted locally and may include confidential patent research.

Mitigation: Run from an appropriate workspace, review saved linkfox session data, and avoid using the skill where local persistence is unacceptable.

Risk: Authentication and billing flows may request phone/SMS login steps or payment actions.

Mitigation: Treat onboarding and payment steps as explicit user-driven actions and do not proceed without the user's informed approval.

Risk: Endpoint override environment variables can redirect credential-bearing requests.

Mitigation: Leave endpoint overrides unset unless the destination is trusted and intentionally configured.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/linkfox-ai/skills/linkfox-zhihuiya-claim-data-translated)
- [API Reference](references/api.md)
- [Authentication and Billing Onboarding](references/onboarding.md)
- [LinkFox Skills](https://skill.linkfox.com/)
- [LinkFox Agent Console](https://agent.linkfox.com/)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON API responses, shell command examples, and saved JSON result files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [API responses are saved under a local linkfox session directory; small responses may be printed in full, while large responses are summarized unless inline output is requested.]

## Skill Version(s):

1.0.7 (source: evidence.release.version)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
