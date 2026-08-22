## Description:

Identifies bird species in images or videos, supports recognition of at least 500 common species, and can use customized model training for ecological observation, garden birdwatching, and related scenarios.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to identify bird species from uploaded images, videos, or public URLs, retrieve structured analysis results, and list prior cloud reports for the associated account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Bird images, videos, URLs, generated identity values, and report history may be sent to the LifeEmergence cloud service.

Mitigation: Use the skill only with media and URLs appropriate for that service, avoid sensitive footage, and confirm consent and retention controls before deployment.

Risk: The skill can create or reuse persistent local identity and authentication token state.

Mitigation: Run it in a controlled workspace, review local data storage, and define token deletion or revocation steps before broad installation.

Risk: The authoritative security scan verdict is suspicious.

Mitigation: Review the skill, its network behavior, and publisher documentation before installation or production use.

## Reference(s):

- [Bird Recognition API documentation](references/api_doc.md)
- [Shared analysis API documentation](skills/smyx_analysis/references/api_doc.md)
- [Skill demo](https://lifeemergence.com/sample.html)
- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-bird-recognition-analysis)

## Skill Output:

**Output Type(s):** [text, markdown, json, shell commands, guidance]

**Output Format:** [Markdown and JSON text with report links; optional file output when --output is used]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May call LifeEmergence cloud APIs, upload media or submit URLs, poll for results, and query report history.]

## Skill Version(s):

1.0.17 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
