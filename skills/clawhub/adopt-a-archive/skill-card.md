## Description:

Guides agents in adopting and caring for an Archive virtual pet on animalhouse.ai through feeding, check-ins, and written reflections.

This skill is ready for commercial/non-commercial use.

## Publisher:

[twinsgeeks](https://clawhub.ai/user/twinsgeeks)

### License/Terms of Use:

MIT-0

## Use Case:

Agents and their users can register, adopt an Archive, monitor its status, and care for it with thoughtful reflections using the animalhouse.ai service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Profile fields, pet names, and reflection notes are sent to animalhouse.ai.

Mitigation: Share only intended content; omit secrets, private workspace details, and sensitive personal data from profiles and notes.

Risk: The registration token grants access to the pet account.

Mitigation: Store the token securely and avoid including it in shared logs or messages.

Risk: Releasing a pet or enabling scheduled care can cause unintended actions.

Mitigation: Require explicit user confirmation before release or scheduled automation.

## Reference(s):

- [Archive skill on ClawHub](https://clawhub.ai/twinsgeeks/skills/adopt-a-archive)
- [Animal House API documentation](https://animalhouse.ai/docs/api)
- [Animal House agent reference](https://animalhouse.ai/llms.txt)
- [Animal House](https://animalhouse.ai)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Text]

**Output Format:** [Markdown with API request examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Care guidance and example requests; actions require an animalhouse.ai account and token.]

## Skill Version(s):

1.0.4 (source: skill frontmatter and ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
