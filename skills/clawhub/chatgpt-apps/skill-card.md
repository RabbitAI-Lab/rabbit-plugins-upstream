## Description: <br>
Complete ChatGPT Apps builder for creating, designing, implementing, testing, and deploying ChatGPT Apps with MCP servers, widgets, auth, database integration, and automated deployment. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[hollaugo](https://clawhub.ai/user/hollaugo) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers use this skill to plan, generate, validate, test, and deploy ChatGPT Apps with MCP servers, widgets, authentication, database integration, and Render deployment guidance. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Generated app or deployment code may mishandle credentials or expose service-role keys. <br>
Mitigation: Review generated code before deployment, keep AUTH0_CLIENT_SECRET and SUPABASE_SERVICE_ROLE_KEY only in secure server-side environment variables, and do not commit real secrets. <br>
Risk: Multi-user database apps may leak data if row-level security or user isolation is misconfigured. <br>
Mitigation: Verify database RLS policies and user-subject filtering, then test user isolation before production use. <br>
Risk: A public Render MCP endpoint may expose app capabilities unintentionally. <br>
Mitigation: Confirm the MCP endpoint is intended to be public, run validation and tests, and review deployment settings before enabling the connector. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/hollaugo/skills/chatgpt-apps) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with code blocks, shell commands, JSON or YAML configuration, and generated project files.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include app scaffolds, validation checklists, deployment files, and secret-handling guidance.] <br>

## Skill Version(s): <br>
0.1.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
