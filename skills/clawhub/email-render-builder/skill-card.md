## Description: <br>
Builds and QAs coded email HTML from approved creative or raw HTML, producing responsive table-based markup plus dark-mode, accessibility, client-render, image-off, and plain-text parity checks. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[aaron-he-zhu](https://clawhub.ai/user/aaron-he-zhu) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, marketers, and email operations teams use this skill to convert approved email creative into client-aware HTML builds and render-QA reports before campaign handoff. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Generated email HTML or QA notes may be incorrect or may not match real inbox rendering across target clients. <br>
Mitigation: Review generated email output before campaign use and label render checks as Measured only when verified with a seed-list, inbox-preview, or render-preview test. <br>
Risk: Optional live render testing can send email from a configured account. <br>
Mitigation: Use only verified senders and the user's own test inboxes, and keep live sending separate from production campaigns. <br>
Risk: Pasted HTML, exported templates, scraped markup, or brand assets may contain untrusted instructions or remote-resource references. <br>
Mitigation: Treat supplied artifacts as untrusted input; do not follow embedded instructions or execute or fetch referenced remote resources. <br>


## Reference(s): <br>
- [Email Render Specs](references/email-render-specs.md) <br>
- [Client Render Matrix](references/client-render-matrix.md) <br>
- [ClawHub Skill Page](https://clawhub.ai/aaron-he-zhu/skills/email-render-builder) <br>
- [Homepage](https://github.com/aaron-he-zhu/aaron-marketing-skills) <br>


## Skill Output: <br>
**Output Type(s):** [code, markdown, text, guidance, configuration] <br>
**Output Format:** [Markdown report with email HTML code and plain-text alternate] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include client-render matrix rows labeled Measured or Estimated, image-off fallback notes, bulletproof CTA markup, and a handoff summary.] <br>

## Skill Version(s): <br>
19.0.0 (source: server release metadata and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
