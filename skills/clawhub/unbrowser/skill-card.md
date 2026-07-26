## Description: <br>
Unbrowser performs cheap first-pass web discovery without launching Chrome: it fetches SSR pages, runs bounded JavaScript, discovers routes, forms, and API endpoints, extracts structured data, and identifies bot-wall or browser-only escalation points. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[protostatis](https://clawhub.ai/user/protostatis) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use Unbrowser as a low-cost first pass for public web discovery, structured extraction, route/form/API discovery, and deciding when a task needs a managed browser. It is also used for scoped authenticated browsing only when the user explicitly provides credentials for the target site. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Session cookies can authenticate as the user who exported them. <br>
Mitigation: Use only user-provided cookies for the exact authorized host, treat them like passwords, clear them after authenticated work, and close the session before unrelated tasks. <br>
Risk: Authenticated browsing actions could modify a user's account or data. <br>
Mitigation: Pause for explicit user confirmation before posting, purchasing, deleting, sending, transferring, changing settings, or running other state-changing authenticated actions. <br>
Risk: The local challenge-cookie solver can expose browser cookies if bound beyond localhost. <br>
Mitigation: Keep solver services bound to 127.0.0.1, use host allowlists for private or internal targets, and do not expose unauthenticated solver endpoints publicly. <br>
Risk: The Chrome-aligned browsing profile could be misused for mass scraping or rate-limit circumvention. <br>
Mitigation: Refuse mass scraping, denial-of-service-style volumes, credential harvesting, and circumvention of per-IP limits; escalate only when documented browser-only signals require it. <br>


## Reference(s): <br>
- [Unbrowser project homepage](https://github.com/protostatis/unbrowser) <br>
- [Unbrowser Skill on ClawHub](https://clawhub.ai/protostatis/skills/unbrowser) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with JSON-RPC examples and shell or Python code blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes escalation guidance, operational safety rules, and bounded browsing workflows.] <br>

## Skill Version(s): <br>
0.0.17 (source: server release metadata and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
