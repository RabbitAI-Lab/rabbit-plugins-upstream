## Description: <br>
UI Master helps agents build, refine, and review production-grade React or Next.js interfaces using Tailwind CSS v4, shadcn/ui, design tokens, accessible layouts, and verification checklists. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[anjasta-tarigan](https://clawhub.ai/user/anjasta-tarigan) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and UI-focused agents use this skill to set up or improve Tailwind CSS v4 and shadcn/ui interfaces, including landing pages, dashboards, auth flows, app shells, chat UIs, and accessibility or responsiveness reviews. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may suggest package installs, Tailwind or shadcn/ui setup commands, and component file changes that mutate the target frontend project. <br>
Mitigation: Review dependency changes, generated component files, and diffs before accepting them in the target project. <br>
Risk: UI changes can introduce accessibility, responsiveness, motion, or performance regressions if examples are adapted without verification. <br>
Mitigation: Run the included accessibility and performance checklist, including keyboard focus, WCAG contrast, reduced-motion handling, responsive breakpoints, and loading, empty, and error states. <br>
Risk: Chat UI examples include markdown rendering patterns that could be misapplied to user-controlled content. <br>
Mitigation: Render user input as plain text and apply the project's normal markdown sanitization policy to assistant-rendered markdown. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/anjasta-tarigan/skills/ui-master) <br>
- [Tailwind CSS v4 Setup](references/tailwind-v4-setup.md) <br>
- [shadcn/ui Setup and Theming](references/shadcn-setup.md) <br>
- [Design Tokens for Production UI](references/design-tokens.md) <br>
- [Accessibility & Performance Production Floor](references/accessibility-performance-checklist.md) <br>
- [Modern Effects Catalogue](references/modern-effects.md) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Markdown, Code, Shell commands, Configuration] <br>
**Output Format:** [Markdown guidance with TypeScript/TSX, CSS, JSON, and shell command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May propose package installs and component file changes for the target frontend project.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
