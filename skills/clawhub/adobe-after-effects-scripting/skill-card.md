## Description:

Write and review ExtendScript scripts and expressions that run inside Adobe After Effects, including project automation, ScriptUI panels, and rendering.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jhauga](https://clawhub.ai/user/jhauga)

### License/Terms of Use:

MIT-0

## Use Case:

After Effects users and developers use the skill to create, troubleshoot, and review scripts and expressions that run within the application, including project and render automation. It helps them account for the installed After Effects version, execution context, and ExtendScript's ECMAScript 3 limits.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security scan reported no findings, but its analysis was partial because some local references were unresolved.

Mitigation: Review the unresolved local references and the skill before installation, taking the scan's partial-analysis limitation into account.

Risk: Scripts that read or write files outside the project or use network sockets require the relevant After Effects access preference.

Mitigation: Review file paths and network access in a script, and enable the preference only when that access is needed.

## Reference(s):

- [After Effects Scripting Guide](https://ae-scripting.docsforadobe.dev/)
- [After Effects Expression Reference](https://ae-expressions.docsforadobe.dev/)
- [JavaScript Tools Guide](https://extendscript.docsforadobe.dev/)
- [Adobe Media Encoder Scripting Guide](https://ame-scripting.docsforadobe.dev/)
- [Adobe Help: Automated rendering and network rendering](https://helpx.adobe.com/after-effects/using/automated-rendering-network-rendering.html)
- [ClawHub release page](https://clawhub.ai/jhauga/skills/adobe-after-effects-scripting)

## Skill Output:

**Output Type(s):** [Text, Code, Shell commands, Configuration instructions]

**Output Format:** [Markdown guidance with ExtendScript code, expressions, and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Code examples target ExtendScript's ECMAScript 3 environment; expression syntax depends on the selected After Effects expression engine.]

## Skill Version(s):

1.0.6 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
