## Description: <br>
Kit (formerly ConvertKit) API integration with managed OAuth for managing email subscribers, forms, tags, sequences, broadcasts, and custom fields. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[byungkyu](https://clawhub.ai/user/byungkyu) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to operate Kit email marketing workflows through Maton-managed OAuth, including subscriber, tag, form, sequence, broadcast, custom field, purchase, email template, and webhook operations. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can access subscriber and customer data in the connected Kit account through Maton-managed OAuth. <br>
Mitigation: Install only when Maton and the connected Kit account are trusted, keep MATON_API_KEY private, and scope actions to the intended account. <br>
Risk: Write, delete, webhook, broadcast, or connection-management operations can modify email marketing resources. <br>
Mitigation: Confirm the target resource, account connection, and intended effect with the user before executing any modifying request. <br>
Risk: Multiple Kit connections can route requests to the wrong account if the connection is not specified. <br>
Mitigation: Use the Maton-Connection header when multiple Kit accounts exist. <br>


## Reference(s): <br>
- [Kit Skill on ClawHub](https://clawhub.ai/byungkyu/skills/kit) <br>
- [Kit API Overview](https://developers.kit.com/api-reference/overview) <br>
- [Kit API Subscribers](https://developers.kit.com/api-reference/subscribers/list-subscribers) <br>
- [Kit API Tags](https://developers.kit.com/api-reference/tags/list-tags) <br>
- [Kit API Forms](https://developers.kit.com/api-reference/forms/list-forms) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline API paths, JSON examples, and Python, JavaScript, or shell command snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires network access, MATON_API_KEY, and explicit user approval before write operations.] <br>

## Skill Version(s): <br>
1.0.3 (source: server release evidence; artifact frontmatter reports 1.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
