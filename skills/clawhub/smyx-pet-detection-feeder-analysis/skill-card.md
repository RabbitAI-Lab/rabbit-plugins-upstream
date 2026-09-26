## Description:

Analyzes feeder or pet-camera images and videos to detect cats and dogs, recognize or enroll individual pets, and retrieve prior detection reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Pet owners and smart-feeder developers use this skill to identify cats and dogs from camera media, enroll pets for individual recognition, and review historical detection reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Pet-camera media, URLs, and report history are handled by a cloud service.

Mitigation: Use only with approved media and review cloud data handling before enabling analysis or report lookup.

Risk: The skill creates or reuses cloud account tokens in the workspace data directory.

Mitigation: Restrict access to that directory and remove tokens when they are no longer needed.

Risk: A hidden identity selector could be misused by untrusted callers.

Mitigation: Remove or strongly authenticate the hidden identity path before allowing untrusted access.

## Reference(s):

- [Skill listing](https://clawhub.ai/smyx-sunjinhui/skills/smyx-pet-detection-feeder-analysis)
- [API documentation](artifact/references/api_doc.md)
- [Skill demonstration](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON]

**Output Format:** [Structured pet detection reports, enrollment results, report lists, and links; optional JSON output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include a cloud-hosted report export link.]

## Skill Version(s):

1.0.12 (source: server-resolved ClawHub release; bundled SKILL.md states 1.0.18)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
