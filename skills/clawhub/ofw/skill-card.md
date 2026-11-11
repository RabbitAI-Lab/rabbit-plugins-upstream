## Description:

This skill should be used when the user asks about OurFamilyWizard (OFW) co-parenting data. Triggers on phrases like "check OFW", "OurFamilyWizard inbox", "OFW messages", "OFW calendar", "OFW expenses", "what did my co-parent say", "log an expense in OFW", "OFW journal", or any request involving co-parenting messages, calendar events, shared expenses, or journal entries.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

People managing co-parenting through OurFamilyWizard use this skill to review messages, calendar events, expenses, and journal entries, and to prepare or carry out account actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Activation may extend to co-parenting requests without a clear OurFamilyWizard context.

Mitigation: Use the skill when the request clearly concerns OurFamilyWizard, and review its trigger scope.

Risk: The security assessment is partial because some local references could not be resolved.

Mitigation: Review the unresolved references and skill behavior before relying on it.

Risk: Reading an unread message can change its read state, and account writes can alter legal co-parenting records.

Mitigation: Explain read-state effects and get explicit approval before sending, deleting, or changing shared records.

## Reference(s):

- [ofw-mcp package](https://www.npmjs.com/package/ofw-mcp)

## Skill Output:

**Output Type(s):** [Text, Markdown, Configuration instructions, Files]

**Output Format:** [Markdown guidance and structured OurFamilyWizard results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Message and draft results may be cached; verify freshness and completeness before stating current status.]

## Skill Version(s):

2.28.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
