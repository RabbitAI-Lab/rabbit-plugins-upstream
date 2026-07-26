## Description: <br>
Use the Pasteclaw.com API to create, update, group, and delete shared code or text snippets and return preview URLs. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[tairov](https://clawhub.ai/user/tairov) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and agents use PasteClaw to publish HTML/CSS/JS prototypes, markdown, JSON, YAML, or text snippets to Pasteclaw.com and share stable preview URLs. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill uploads content to a third-party service. <br>
Mitigation: Use it only for material intended for external sharing, and avoid secrets, private configuration, personal data, or proprietary content. <br>
Risk: The artifact examples use curl with weakened HTTPS certificate checks. <br>
Mitigation: Remove the -k flag from curl commands so HTTPS certificates are verified. <br>
Risk: Edit tokens and session keys can affect snippet updates, deletion, and grouping. <br>
Mitigation: Protect edit and session tokens, never put session keys in URLs, and confirm snippet IDs and tokens before update or delete actions. <br>
Risk: Optional metadata headers can disclose model, tool, source, task, or version details. <br>
Mitigation: Omit metadata headers unless traceability is needed. <br>


## Reference(s): <br>
- [Pasteclaw service](https://pasteclaw.com) <br>
- [Pasteclaw snippets API](https://pasteclaw.com/api/snippets) <br>
- [PasteClaw ClawHub listing](https://clawhub.ai/tairov/skills/pasteclaw) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Code, API calls] <br>
**Output Format:** [Markdown with curl commands, Python snippets, JSON response examples, and preview URLs] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include snippet IDs, preview URLs, edit tokens, and optional session keys returned by the Pasteclaw API.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
