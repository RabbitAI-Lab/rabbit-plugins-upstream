## Description: <br>
Use when building HTML email templates with React components, adding a visual email editor to an application using the React Email visual editor, rendering emails to HTML, or sending emails with Resend. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[christina-de-martinez](https://clawhub.ai/user/christina-de-martinez) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to create React Email templates, embed the React Email visual editor, render email content to HTML or plain text, and prepare email-sending integrations. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Email-sending examples could send unintended messages if run without review. <br>
Mitigation: Confirm recipients, sender domain, subject, and message content before executing sending examples. <br>
Risk: Email provider API keys could be exposed if embedded directly in generated code. <br>
Mitigation: Store API keys in environment variables or a secret manager and avoid committing secrets. <br>
Risk: Production email delivery can fail compliance or domain requirements if provider setup is incomplete. <br>
Mitigation: Use verified sender domains and review the selected email provider's data handling and compliance requirements. <br>


## Reference(s): <br>
- [React Email documentation](https://resend.com/docs/react-email-skill) <br>
- [React Email repository](https://github.com/resend/react-email) <br>
- [React Email homepage](https://react.email) <br>
- [React Email Components Reference](references/COMPONENTS.md) <br>
- [React Email Editor Reference](references/EDITOR.md) <br>
- [Internationalization (i18n) Guide](references/I18N.md) <br>
- [Common Email Patterns](references/PATTERNS.md) <br>
- [Sending Guide](references/SENDING.md) <br>
- [Styling Guide](references/STYLING.md) <br>
- [Email Client CSS Support](https://www.caniemail.com) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, code, shell commands, configuration] <br>
**Output Format:** [Markdown with inline TypeScript, JSON, and shell code blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include React Email component examples, CLI commands, package setup, rendering examples, and email-sending guidance.] <br>

## Skill Version(s): <br>
2.0.0 (source: server release metadata and artifact frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
