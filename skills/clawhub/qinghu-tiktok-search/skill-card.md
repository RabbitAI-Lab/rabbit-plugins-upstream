## Description:

Searches TikTok for creators, products, shops, videos, and live streams, and helps identify TikTok category IDs through Qinghu AI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External users and commerce researchers can search TikTok for relevant creators, products, shops, videos, or live streams, and look up category IDs for their research.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Paid searches may consume Qinghu credits.

Mitigation: Estimate the charge and obtain user approval before making paid calls.

Risk: Automatic installation or upgrades can change local Node.js and npm tooling.

Mitigation: Review installation steps and install a trusted, pinned qhkit version yourself rather than allowing automatic setup.

Risk: Local API-token configuration can expose credentials.

Mitigation: Provide the token through a secure secret mechanism and avoid including it in shared commands or files.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/autoagc/skills/qinghu-tiktok-search)
- [Qinghu qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown summary of TikTok search results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Searches return at most 30 items per call; paid calls consume Qinghu credits.]

## Skill Version(s):

0.1.0 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
