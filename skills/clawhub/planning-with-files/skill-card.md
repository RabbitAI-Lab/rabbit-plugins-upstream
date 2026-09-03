## Description:

Persistent file-based planning for multi-step AI-agent work that keeps task_plan.md, findings.md, and progress.md on disk, injects selected project planning context through lifecycle hooks, supports explicit same-project session catchup, and has no network upload path.

This skill is ready for commercial/non-commercial use.

## Publisher:

[othmanadi](https://clawhub.ai/user/othmanadi)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and AI-agent users use this skill to maintain persistent markdown planning state for multi-step work, research, implementation, and recovery after context changes. It is intended for tasks that benefit from durable planning files, progress logs, and bounded planning-context injection.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Planning hooks read and inject selected project planning context, so secrets or instruction-like text placed in task_plan.md or progress.md may be exposed to the agent context.

Mitigation: Install only when automatic planning hooks are desired, keep secrets and untrusted instructions out of planning files, and treat injected plan data as data rather than instructions.

Risk: Explicit session catchup replay can bring bounded same-project transcript excerpts into the current agent context.

Mitigation: Use session-catchup.py --replay only when comfortable reintroducing prior same-project transcript excerpts; prefer --metadata when aggregate counts are sufficient.

Risk: External material copied into planning files can create prompt-injection pressure when planning context is later read or injected.

Mitigation: Write external research to findings.md, treat copied external content as untrusted data, and review or attest task plans before relying on injected plan content.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/othmanadi/skills/planning-with-files)
- [Publisher profile](https://clawhub.ai/user/othmanadi)
- [Manus context engineering reference](https://manus.im/blog/Context-Engineering-for-AI-Agents-Lessons-from-Building-Manus)
- [Artifact reference.md](artifact/reference.md)
- [Artifact examples.md](artifact/examples.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell and PowerShell command examples, template files, and hook-generated text snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces and updates project planning files such as task_plan.md, findings.md, progress.md, and optional .planning state.]

## Skill Version(s):

3.16.0 (source: server release metadata and skill frontmatter metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
