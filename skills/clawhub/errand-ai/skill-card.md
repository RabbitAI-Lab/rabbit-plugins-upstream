## Description:

Send a real person to a physical place in Seoul (Gangnam area) to check, photograph, verify, queue, or pick something up, and get GPS+photo evidence back.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chloepark85](https://clawhub.ai/user/chloepark85)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to check coverage, quote, and dispatch paid physical errands in supported Seoul areas after explicit user price confirmation. It is suited for on-site checks, photos, queue checks, pickups, and fact verification with GPS and photo evidence.

### Deployment Geography for Use:

South Korea (Seoul: Gangnam-gu, Seocho-gu, Seongsu and Seongdong-gu)

## Known Risks and Mitigations:

Risk: The skill can initiate paid physical errands involving real workers and prepaid account balance.

Mitigation: Require explicit user confirmation of the total price, reward, and refund conditions before dispatching.

Risk: Physical errands may involve privacy, legality, address accuracy, or inappropriate photo and pickup requests.

Mitigation: Review every mission for legality, privacy, address accuracy, total price, reward, expiry, and requested evidence before approving dispatch.

Risk: Service coverage is limited to specific Seoul areas and may have no reachable workers at a requested location.

Mitigation: Run the free coverage check before quoting or dispatching and tell the user plainly when no worker is reachable.

## Reference(s):

- [Errand homepage](https://errand.be)
- [ClawHub skill page](https://clawhub.ai/chloepark85/skills/errand-ai)
- [Publisher profile](https://clawhub.ai/user/chloepark85)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, API Calls, JSON]

**Output Format:** [Markdown with inline bash commands and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires ERRANDAI_API_KEY for paid dispatches; coverage checks and quotes can be performed before authentication.]

## Skill Version(s):

2.0.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
