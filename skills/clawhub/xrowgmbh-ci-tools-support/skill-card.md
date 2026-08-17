## Description:

Triage and answer support requests for the xrow-public/ci-tools GitLab components catalog.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xrowgmbh](https://clawhub.ai/user/xrowgmbh)

### License/Terms of Use:

MIT-0

## Use Case:

Support engineers and agents use this skill to triage eligible GitLab CI Tools support issues or discussion threads and draft grounded, cited responses, follow-up questions, handoffs, or refusals.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Agents using the skill may be able to reply in GitLab threads or apply labels with permissions broader than the support workflow requires.

Mitigation: Install it only for agents with appropriately scoped GitLab permissions and review any thread replies or label changes according to the support process.

Risk: Support responses could expose private customer details if confidential logs, URLs, or internal project names are copied into public places.

Mitigation: Keep issues confidential when customer details are present, cite public sources, and avoid quoting private logs into public threads.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/xrowgmbh/skills/xrowgmbh-ci-tools-support)
- [Publisher profile](https://clawhub.ai/user/xrowgmbh)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Markdown or plain text support responses with cited public sources]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May ask one focused follow-up question, apply a concise handoff or refusal, or identify labels when a request is out of scope or unsafe.]

## Skill Version(s):

4.173.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
