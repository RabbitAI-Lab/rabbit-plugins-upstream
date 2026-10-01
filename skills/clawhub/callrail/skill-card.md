## Description:

Connects an agent to CallRail through Maton to review calls and analytics and manage tracking numbers, companies, and tags.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Agents and their users use an authorized CallRail connection to inspect call records and analytics, organize calls with tags, and manage tracking numbers or companies with approval for changes. Optional user-approved functions and triggers can automate CallRail actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Access to CallRail call records may expose sensitive business and personal data.

Mitigation: Use only the intended authorized account and return only the fields needed; avoid storing or logging raw responses.

Risk: Writes or new connections can change CallRail data or account access.

Mitigation: Confirm the exact account, resource, payload, and intended effect with the user before creating a connection or performing a write.

Risk: Hosted functions, triggers, and event destinations can run or forward data automatically after setup.

Mitigation: Require separate approval for automation and persistent destinations; review the handler, schedule or event source, destination host, and ongoing data flow.

## Reference(s):

- [CallRail skill release](https://clawhub.ai/byungkyu/skills/callrail)
- [Maton](https://maton.ai)
- [CallRail API documentation](https://apidocs.callrail.com/)
- [Maton documentation](https://docs.maton.ai)
- [Maton CLI manual](https://cli.maton.ai/manual)
- [Maton api-gateway skill for other apps](https://clawhub.ai/byungkyu/api-gateway)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Code, JSON]

**Output Format:** [Markdown guidance with CLI and code examples and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses an authorized CallRail connection; reads are the default, and changes or automation require user approval.]

## Skill Version(s):

1.2.6 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
