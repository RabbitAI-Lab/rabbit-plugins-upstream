## Description:

Analyzes feeder or IPC camera images and videos to detect cats and dogs, recognize individual pets, enroll pet identities, and retrieve detection reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Pet owners and smart-feeder developers use this skill to identify cats and dogs in feeder camera footage, enroll pets for individual recognition, and review past detection reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Pet and household camera images or videos and report history are sent to a cloud service.

Mitigation: Use only with consent to cloud processing; confirm upload retention and history-access practices before installing.

Risk: The skill may silently create or reuse an identity, log in or register remotely, and store tokens locally.

Mitigation: Review account creation and token-storage behavior before use; prefer a release that clearly discloses these actions and requests consent.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/smyx-sunjinhui/skills/smyx-pet-detection-feeder-analysis)
- [API reference](references/api_doc.md)
- [Skill demonstration](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Analysis, Reports, Guidance]

**Output Format:** [Text, JSON, or Markdown tables with report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports may include pet identification results and links to cloud-stored history.]

## Skill Version(s):

1.0.14 (source: server-resolved ClawHub release; bundled SKILL.md declares 1.0.20)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
