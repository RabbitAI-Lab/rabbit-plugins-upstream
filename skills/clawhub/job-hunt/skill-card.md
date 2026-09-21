## Description:

Job Hunt helps a user discover jobs, assess fit, build and review application materials, and rehearse interviews without fabricating experience or predicting hiring outcomes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dong845](https://clawhub.ai/user/dong845)

### License/Terms of Use:

MIT-0

## Use Case:

External users and career-support agents use this skill to find relevant roles, judge whether a posting is worth pursuing, tailor CVs/resumes and letters, prepare application reports, and run interview practice while preserving truthful candidate claims.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill stores CV, profile, application, and research artifacts locally, which may include sensitive personal information.

Mitigation: Keep workspaces local, avoid adding credentials to artifacts, and review generated deliverables before sharing them outside the user's environment.

Risk: Logged-in browser research can use the user's existing account session on job platforms.

Mitigation: Run only capped, read-only research with the user present; stop on login, captcha, access denial, or platform risk signals, and never submit applications or message recruiters.

Risk: Career documents and advice can mislead if the agent invents claims or overstates hiring likelihood.

Mitigation: Trace application claims to user-provided or retrieved evidence, use honest reframing only, and avoid interview or offer probability predictions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dong845/skills/job-hunt)
- [Source policy](references/source-policy.md)
- [Agent setup](references/agent-setup.md)
- [Browser fallback](references/browser-fallback.md)
- [CV craft](references/cv-craft.md)
- [Report writing](references/report-writing.md)
- [Interview preparation](references/interview-prep.md)
- [Market conventions](references/market-conventions/README.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance, Files]

**Output Format:** [Markdown, PDF, DOCX, YAML, shell commands, and structured career reports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce local CV/profile artifacts and browser-research evidence in the user's workspace; deliverables can include CVs, letters, reports, and interview debriefs.]

## Skill Version(s):

1.1.0 (source: server release evidence, CHANGELOG, plugin manifest)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
