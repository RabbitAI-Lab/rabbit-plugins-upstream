## Description:

A bilingual patent disclosure completion assistant for patent agencies, inventors, and R&D teams that packages a standalone customer-facing HTML guide, collects invention information through a structured 7-step workflow, supports AI-assisted completion of rough R&D notes, and generates a structured invention disclosure draft for patent attorney review.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yuanzhian-patsnap](https://clawhub.ai/user/yuanzhian-patsnap)

### License/Terms of Use:

MIT-0

## Use Case:

Patent agencies, inventors, and R&D teams use this skill to turn early invention notes, product descriptions, abstracts, or research conversations into a more complete patent disclosure draft. The generated draft is intended for review and refinement by patent professionals before use in patent work.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Sensitive invention details may be entered into the workflow or sent to external PatSnap MCP/API services if those services are configured.

Mitigation: Use the skill only with invention details you are authorized to process, avoid trade secrets unless the environment is approved by your organization, and configure only the PatSnap services that are actually needed.

Risk: The manifest does not declare MCP dependencies even though setup instructions direct users toward broad PatSnap MCP/API access.

Mitigation: Review the required PatSnap services before installation, confirm what data each service can receive, and document the approved services for the deployment environment.

Risk: AI-assisted disclosure completion can produce incomplete or inaccurate patent disclosure language.

Mitigation: Treat generated drafts as working material and require patent attorney or qualified professional review before relying on the content.

## Reference(s):

- [Disclosure Guide HTML](artifact/assets/disclosure-guide.html)
- [ClawHub Skill Page](https://clawhub.ai/yuanzhian-patsnap/skills/disclosure-completion-assistant)
- [PatSnap Open Platform](https://open.zhihuiya.com/)
- [PatSnap Authentication Guide](https://open.zhihuiya.com/devportal/guides/authentication)
- [PatSnap MCP Server Marketplace](https://open.zhihuiya.com/marketplace/mcp-servers)
- [PatSnap Developer Documentation](https://open.patsnap.com/devportal)

## Skill Output:

**Output Type(s):** [Text, Files, Guidance, Configuration instructions]

**Output Format:** [HTML page and structured text draft]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Bilingual zh-CN and en interface; missing disclosure fields are marked for follow-up.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
